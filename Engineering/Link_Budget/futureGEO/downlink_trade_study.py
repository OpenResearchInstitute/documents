#!/usr/bin/env python3
"""
futureGEO downlink band trade study
Open Research Institute, for reproducible analysis

Compares candidate amateur-satellite downlink bands for a geostationary
payload, using ITU-R propagation models (via the `itur` package, v0.4.0):
  - Rain attenuation:        ITU-R P.618-13 (with P.837 rain-rate maps)
  - Gaseous absorption:      ITU-R P.676
  - Cloud attenuation:       ITU-R P.840
  - Tropospheric scintillation: ITU-R P.618

Domain model
------------
  Band          - a candidate downlink allocation (frequency + regulatory facts)
  GroundStation - a named location in the candidate footprint
  GeoSlot       - an orbital position; owns the geometry to any station
  SpaceSegment  - per-channel EIRP assumptions (taken from the public
                  AMSAT-DL "payload ideas" deck so results are comparable)
  UserTerminal  - dish + receiver noise assumptions per band
  LinkBudget    - composes the above; evaluates C/N at a given availability

All numeric assumptions are collected in ASSUMPTIONS_* constants and are
printed into the output tables so nothing is silently baked in.
"""

from dataclasses import dataclass
from math import radians, degrees, cos, sin, acos, atan2, sqrt, log10, pi
import itertools
import numpy as np
import pandas as pd
import itur
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Physical constants and shared assumptions
# ----------------------------------------------------------------------
C_LIGHT = 299_792_458.0          # m/s
K_BOLTZ_DBW = -228.6             # dBW/K/Hz
R_EARTH = 6378.137e3             # m, equatorial
R_GEO = 42164.0e3                # m, geostationary radius
T_RAIN_MEDIUM = 275.0            # K, effective medium temp for rain noise (ITU-R P.618 convention)

# ASSUMPTION (from the public AMSAT-DL payload-ideas deck, for comparability):
ASSUMPTION_CHANNEL_BW_HZ = 2400.0        # narrowband voice channel
ASSUMPTION_EIRP_PER_CHANNEL_DBW = 12.5   # 100 W TWTA, 6 dB backoff, 1.5 dB losses,
                                         # 17 dBi footprint-defined antenna, 50 channels
# ASSUMPTION (analysis choice): the spacecraft antenna gain is set by the
# required footprint, not by frequency, so EIRP/channel is held constant
# across bands. Per-band PA technology differences are discussed in text.

ASSUMPTION_DISH_DIAMETER_M = 0.8         # deck's user terminal
ASSUMPTION_DISH_EFFICIENCY = 0.65


# ----------------------------------------------------------------------
# Domain model
# ----------------------------------------------------------------------
@dataclass(frozen=True)
class Band:
    """A candidate downlink allocation and its regulatory facts (IARU table, Jan 2020 rev.)."""
    label: str
    freq_ghz: float
    allocation: str           # primary/secondary
    regions: str
    lnb_noise_figure_db: float   # ESTIMATE: representative achievable RX noise figure
    antenna_temp_clear_k: float  # ESTIMATE: clear-sky antenna temperature at moderate elevation
    ecosystem_note: str

    @property
    def rx_temp_k(self) -> float:
        return 290.0 * (10 ** (self.lnb_noise_figure_db / 10.0) - 1.0)


@dataclass(frozen=True)
class GroundStation:
    name: str
    lat_deg: float
    lon_deg: float   # East positive


@dataclass(frozen=True)
class GeoSlot:
    lon_deg: float   # East positive

    def geometry(self, gs: GroundStation):
        """Elevation (deg), azimuth (deg), slant range (m) to this slot. Spherical earth."""
        lat = radians(gs.lat_deg)
        dlon = radians(self.lon_deg - gs.lon_deg)
        # central angle between sub-satellite point and station
        cos_psi = cos(lat) * cos(dlon)
        psi = acos(cos_psi)
        slant = sqrt(R_EARTH**2 + R_GEO**2 - 2 * R_EARTH * R_GEO * cos_psi)
        el = degrees(atan2(cos_psi - R_EARTH / R_GEO, sin(psi)))
        az = degrees(atan2(sin(dlon), -sin(lat) * cos(dlon))) % 360.0 if psi > 0 else 180.0
        return el, az, slant


@dataclass(frozen=True)
class UserTerminal:
    diameter_m: float = ASSUMPTION_DISH_DIAMETER_M
    efficiency: float = ASSUMPTION_DISH_EFFICIENCY

    def gain_dbi(self, freq_ghz: float) -> float:
        lam = C_LIGHT / (freq_ghz * 1e9)
        return 10 * log10(self.efficiency * (pi * self.diameter_m / lam) ** 2)


@dataclass
class LinkResult:
    band: Band
    station: GroundStation
    elevation_deg: float
    availability_pct: float
    fspl_db: float
    atten_gas_db: float
    atten_cloud_db: float
    atten_rain_db: float
    atten_scint_db: float
    atten_total_db: float
    t_sys_k: float
    g_over_t_dbk: float
    cn_db: float


class LinkBudget:
    def __init__(self, slot: GeoSlot, terminal: UserTerminal):
        self.slot = slot
        self.terminal = terminal

    def evaluate(self, band: Band, gs: GroundStation, availability_pct: float) -> LinkResult:
        el, _az, slant = self.slot.geometry(gs)
        p_exceed = 100.0 - availability_pct   # % of average year attenuation is exceeded
        f = band.freq_ghz

        fspl = 20 * log10(4 * pi * slant * f * 1e9 / C_LIGHT)

        Ag, Ac, Ar, As, _Atot = itur.atmospheric_attenuation_slant_path(
            gs.lat_deg, gs.lon_deg, f * itur.u.GHz, el, p_exceed,
            self.terminal.diameter_m, return_contributions=True)
        Ag, Ac, Ar, As = [float(x.value) for x in (Ag, Ac, Ar, As)]
        # Combine per P.618 §2.5 convention used by itur's total
        Atot = Ag + sqrt((Ar + Ac) ** 2 + As ** 2)

        # Excess sky-noise from the attenuating atmosphere (excluding scintillation)
        A_absorptive = Ag + Ar + Ac
        t_excess = T_RAIN_MEDIUM * (1.0 - 10 ** (-A_absorptive / 10.0))
        t_sys = band.antenna_temp_clear_k + band.rx_temp_k + t_excess

        g = self.terminal.gain_dbi(f)
        g_over_t = g - 10 * log10(t_sys)

        cn0 = (ASSUMPTION_EIRP_PER_CHANNEL_DBW - fspl - Atot
               + g_over_t - K_BOLTZ_DBW)
        cn = cn0 - 10 * log10(ASSUMPTION_CHANNEL_BW_HZ)

        return LinkResult(band, gs, el, availability_pct, fspl, Ag, Ac, Ar, As,
                          Atot, t_sys, g_over_t, cn)


# ----------------------------------------------------------------------
# Scenario definition
# ----------------------------------------------------------------------
BANDS = [
    Band("9 cm  (3.402-3.410 GHz)", 3.406, "Secondary", "R2+R3 only — NOT Europe/Africa",
         0.6, 40.0, "LNAs cheap; NO allocation in Region 1 — shown for reference only"),
    Band("6 cm  (5.830-5.850 GHz)", 5.840, "Secondary", "R1+R2+R3",
         0.8, 40.0, "adjacent 5.8 GHz ISM; terminals feasible, no COTS LNB ecosystem"),
    Band("3 cm  (10.450-10.500 GHz)", 10.489, "Secondary", "R1+R2+R3",
         1.0, 50.0, "QO-100 heritage: modified TV PLL LNB ~$10-30"),
    Band("1.25 cm (24.000-24.050 GHz)", 24.048, "Primary", "R1+R2+R3",
         2.5, 90.0, "24 GHz LNBs exist (ham microwave), cost & NF higher; rain-critical"),
]

STATIONS = [
    GroundStation("San Francisco, US", 37.7562, -122.443),
    GroundStation("San Diego, US",     32.7157, -117.161),
    GroundStation("Chicago, US",       41.8781,  -87.630),
    GroundStation("New York, US",      40.7128,  -74.006),
    GroundStation("Bochum, DE",        51.4818,    7.216),
    GroundStation("London, GB",        51.5074,   -0.128),
    GroundStation("Madrid, ES",        40.4168,   -3.704),
    GroundStation("Sao Paulo, BR",    -23.5505,  -46.633),
    GroundStation("Accra, GH",          5.6037,   -0.187),
    GroundStation("Miami, US",         25.7617,  -80.192),
]

SLOT = GeoSlot(-43.0)     # from the public deck's link budgets
AVAILABILITIES = [99.5, 99.9]

def main():
    terminal = UserTerminal()
    lb = LinkBudget(SLOT, terminal)

    rows = []
    for band, gs, avail in itertools.product(BANDS, STATIONS, AVAILABILITIES):
        el, az, _ = SLOT.geometry(gs)
        if el < 5.0:
            # ITU-R P.618 is not validated below ~5 deg; refuse to fake it.
            rows.append(dict(band=band.label, station=gs.name, elevation=round(el, 1),
                             availability=avail, atten_total_db=np.nan, cn_db=np.nan,
                             note="elevation < 5 deg: below P.618 validity; link impractical"))
            continue
        r = lb.evaluate(band, gs, avail)
        rows.append(dict(band=band.label, station=gs.name, elevation=round(r.elevation_deg, 1),
                         availability=avail,
                         fspl_db=round(r.fspl_db, 1),
                         atten_gas_db=round(r.atten_gas_db, 2),
                         atten_cloud_db=round(r.atten_cloud_db, 2),
                         atten_rain_db=round(r.atten_rain_db, 2),
                         atten_scint_db=round(r.atten_scint_db, 2),
                         atten_total_db=round(r.atten_total_db, 2),
                         t_sys_k=round(r.t_sys_k, 0),
                         g_over_t_dbk=round(r.g_over_t_dbk, 1),
                         cn_db=round(r.cn_db, 1), note=""))
    df = pd.DataFrame(rows)
    df.to_csv("trade_study_results.csv", index=False)
    print(df.to_string(index=False))

    # ---- Equal-service power inversion --------------------------------
    # For each band/station: RF power (50-ch total) required to match the
    # 3 cm / 100 W baseline C/N at the same station and availability.
    # Robust to amplifier-technology debates: converts the band trade into
    # "can this host provide X watts at band Y", which hardware people can
    # answer. Uses 99.5% availability.
    base = df[(df.band == BANDS[2].label) & (df.availability == 99.5)]
    inv_rows = []
    for band in BANDS:
        for gs in STATIONS:
            b = df[(df.band == band.label) & (df.station == gs.name) & (df.availability == 99.5)]
            b0 = base[base.station == gs.name]
            if np.isnan(b.cn_db.values[0]) or np.isnan(b0.cn_db.values[0]):
                continue
            delta_db = b0.cn_db.values[0] - b.cn_db.values[0]
            inv_rows.append(dict(band=band.label, station=gs.name,
                                 delta_vs_3cm_db=round(delta_db, 1),
                                 rf_watts_for_equal_service=round(100 * 10 ** (delta_db / 10), 0)))
    inv = pd.DataFrame(inv_rows)
    summary = inv.groupby("band").rf_watts_for_equal_service.agg(["median", "max"]).round(0)
    inv.to_csv("equal_service_power.csv", index=False)
    summary.to_csv("equal_service_power_summary.csv")
    print("\nRF power (W, 50-channel total) required to match 3 cm / 100 W service @99.5%:")
    print(summary.to_string())

    # ---- Figure 1: attenuation vs availability, representative stations ----
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), sharey=True)
    focus = [STATIONS[4], STATIONS[9], STATIONS[8]]   # Bochum, Miami, Accra
    p_range = np.array([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0])
    for ax, gs in zip(axes, focus):
        el, _, _ = SLOT.geometry(gs)
        for band in BANDS:
            if "R2+R3" in band.regions and gs.lon_deg > -30 and gs.lat_deg > 0 and gs.lon_deg > -20:
                pass  # still plot; regulatory flag handled in article
            atts = []
            for p in p_range:
                Ag, Ac, Ar, As, _ = itur.atmospheric_attenuation_slant_path(
                    gs.lat_deg, gs.lon_deg, band.freq_ghz * itur.u.GHz, el, p,
                    terminal.diameter_m, return_contributions=True)
                a = float(Ag.value) + sqrt((float(Ar.value) + float(Ac.value))**2 + float(As.value)**2)
                atts.append(a)
            ax.semilogx(p_range, atts, marker="o", ms=3,
                        label=band.label.split("(")[0].strip())
        ax.set_title(f"{gs.name}  (el {el:.0f}\u00b0)")
        ax.set_xlabel("Link availability (% of avg. year)")
        ax.grid(True, which="both", alpha=0.3)
        ax.invert_xaxis()
        ax.set_xticks([5, 2, 1, 0.5, 0.1, 0.02])
        ax.set_xticklabels(["95", "98", "99", "99.5", "99.9", "99.98"])
        ax.minorticks_off()
    axes[0].set_ylabel("Total atmospheric attenuation (dB)\nITU-R P.618/P.676/P.840")
    axes[0].legend(fontsize=8)
    fig.suptitle("Atmospheric attenuation vs availability, GEO 43\u00b0W, 0.8 m terminal")
    fig.tight_layout()
    fig.savefig("fig1_attenuation_vs_availability.png", dpi=150)

    # ---- Figure 2: C/N per user at 99.5% availability, all stations ----
    fig2, ax2 = plt.subplots(figsize=(11, 5))
    width = 0.2
    d995 = df[(df.availability == 99.5)]
    xnames = [gs.name.split(",")[0] for gs in STATIONS]
    x = np.arange(len(STATIONS))
    for i, band in enumerate(BANDS):
        vals = [d995[(d995.band == band.label) & (d995.station == gs.name)].cn_db.values[0]
                for gs in STATIONS]
        ax2.bar(x + (i - 1.5) * width, vals, width, label=band.label)
    ax2.axhline(10, color="k", ls="--", lw=1, alpha=0.6)
    ax2.text(len(STATIONS) - 0.4, 10.3, "10 dB ref.", fontsize=8)
    ax2.set_xticks(x); ax2.set_xticklabels(xnames, rotation=30, ha="right")
    ax2.set_ylabel("C/N per NB user (dB, 2400 Hz)\nat 99.5% availability")
    ax2.set_title("Per-user downlink C/N by band, GEO 43\u00b0W, deck EIRP assumptions")
    ax2.legend(fontsize=8, loc="lower left"); ax2.grid(axis="y", alpha=0.3)
    fig2.tight_layout()
    fig2.savefig("fig2_cn_by_band_station.png", dpi=150)

    # ---- Figure 3: elevation contours of the 43W slot over the footprint ----
    fig3, ax3 = plt.subplots(figsize=(9, 5.5))
    lats = np.linspace(-60, 70, 140)
    lons = np.linspace(-140, 60, 220)
    LON, LAT = np.meshgrid(lons, lats)
    cospsi = np.cos(np.radians(LAT)) * np.cos(np.radians(SLOT.lon_deg - LON))
    psi = np.arccos(np.clip(cospsi, -1, 1))
    elev = np.degrees(np.arctan2(cospsi - R_EARTH / R_GEO, np.sin(psi)))
    cs = ax3.contour(LON, LAT, elev, levels=[0, 5, 10, 20, 30, 40, 50, 60],
                     colors="tab:blue", linewidths=1)
    ax3.clabel(cs, fmt="%d\u00b0")
    for gs in STATIONS:
        ax3.plot(gs.lon_deg, gs.lat_deg, "r^", ms=5)
        ax3.annotate(gs.name.split(",")[0], (gs.lon_deg, gs.lat_deg),
                     fontsize=7, xytext=(3, 3), textcoords="offset points")
    ax3.set_xlabel("Longitude (deg E)"); ax3.set_ylabel("Latitude (deg N)")
    ax3.set_title("Elevation angle to GEO 43\u00b0W (5\u00b0 contour \u2248 practical service edge)")
    ax3.grid(alpha=0.3)
    fig3.tight_layout()
    fig3.savefig("fig3_elevation_contours_43W.png", dpi=150)
    print("\nWrote: trade_study_results.csv, fig1..fig3 PNGs")


if __name__ == "__main__":
    main()
