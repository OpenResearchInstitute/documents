#!/usr/bin/env python3
"""
futureGEO architecture trade addendum:
bent-pipe NB SSB vs regenerative Opulent Voice uplink / DVB-S2 downlink.

Imports the domain model from downlink_trade_study.py and adds:
  1. Downlink: single-carrier DVB-S2 capacity per band/station, exploiting
     single-carrier TWTA operation (output backoff ~1 dB vs 6 dB multicarrier).
  2. Uplink: required user C/N0 and EIRP, Opulent Voice MSK vs 2400 Hz SSB.

ALL Opulent-Voice air-interface constants below marked ESTIMATE must be
checked against the published OPV specification before publication.
"""
from math import log10, sqrt, pi
import numpy as np
import pandas as pd
import itur
from downlink_trade_study import (BANDS, STATIONS, SLOT, UserTerminal,
                                  C_LIGHT, K_BOLTZ_DBW)

# ---------------- Opulent Voice / channelizer scheme ----------------
OPV_CHANNELS = 64                     # stated: 10 MHz / 64-channel polyphase scheme
OPV_UPLINK_BW_HZ = 10e6
OPV_CHANNEL_SPACING_HZ = OPV_UPLINK_BW_HZ / OPV_CHANNELS   # 156.25 kHz
OPV_INFO_RATE_BPS = 27_100.0          # ESTIMATE - CHECK AGAINST PUBLISHED OPV SPEC
OPV_FEC_RATE = 0.5                    # K=7 convolutional, r=1/2 (Voyager 171/133)
OPV_EBN0_REQ_DB = 4.5                 # K=7 r=1/2 Viterbi @ BER 1e-5 (textbook value)
OPV_IMPL_MARGIN_DB = 1.0              # ASSUMPTION: implementation margin

SSB_BW_HZ = 2400.0
SSB_CN_REQ_DB = 10.0                  # ASSUMPTION: usable analog SSB voice convention

UPLINK_FREQ_GHZ = 2.410               # deck's main uplink (13 cm)
SPACECRAFT_G_OVER_T = -13.0           # ESTIMATE dB/K: 17 dBi RX horn (deck), ~1000 K system

# ---------------- DVB-S2 (ETSI EN 302 307) ----------------
# (modcod, Es/N0 threshold dB, spectral efficiency bit/symbol)
DVBS2_MODCODS = [
    ("QPSK 1/4", -2.35, 0.490), ("QPSK 1/3", -1.24, 0.656),
    ("QPSK 2/5", -0.30, 0.789), ("QPSK 1/2",  1.00, 0.989),
    ("QPSK 3/5",  2.23, 1.188), ("QPSK 2/3",  3.10, 1.322),
    ("QPSK 3/4",  4.03, 1.487), ("QPSK 5/6",  5.18, 1.655),
    ("8PSK 3/5",  5.50, 1.780), ("8PSK 2/3",  6.62, 1.981),
    ("8PSK 3/4",  7.91, 2.228),
]
DVBS2_SYMBOL_RATE = 8.0e6             # 10 MHz slot, 20% roll-off -> 9.6 MHz occupied
DVBS2_MODCOD_MARGIN_DB = 1.0          # ASSUMPTION

# Single-carrier space segment (same 100 W TWTA & 17 dBi antenna as the deck):
EIRP_SINGLE_CARRIER_DBW = 20.0 - 1.0 - 1.5 + 17.0   # 1 dB OBO (ASSUMPTION: typical
# single-carrier operation) vs the deck's 6 dB multicarrier backoff -> 34.5 dBW
EIRP_MULTICARRIER_TOTAL_DBW = 29.5    # deck value, for comparison

PER_CHANNEL_NET_RATE_BPS = 32_000.0   # ESTIMATE: OPV voice+headers net downlink share


def atmos(gs, f_ghz, el, p, diam):
    Ag, Ac, Ar, As, _ = itur.atmospheric_attenuation_slant_path(
        gs.lat_deg, gs.lon_deg, f_ghz * itur.u.GHz, el, p, diam,
        return_contributions=True)
    Ag, Ac, Ar, As = [float(x.value) for x in (Ag, Ac, Ar, As)]
    return Ag + sqrt((Ar + Ac) ** 2 + As ** 2), Ag + Ar + Ac


def main():
    term = UserTerminal()
    rows = []
    for band in BANDS:
        for gs in STATIONS:
            el, _, slant = SLOT.geometry(gs)
            if el < 5.0:
                continue
            f = band.freq_ghz
            fspl = 20 * log10(4 * pi * slant * f * 1e9 / C_LIGHT)
            A, A_abs = atmos(gs, f, el, 0.5, term.diameter_m)
            t_sys = band.antenna_temp_clear_k + band.rx_temp_k \
                + 275.0 * (1 - 10 ** (-A_abs / 10))
            gt = term.gain_dbi(f) - 10 * log10(t_sys)
            cn0 = EIRP_SINGLE_CARRIER_DBW - fspl - A + gt - K_BOLTZ_DBW
            esn0 = cn0 - 10 * log10(DVBS2_SYMBOL_RATE)
            usable = [(m, th, eff) for m, th, eff in DVBS2_MODCODS
                      if esn0 >= th + DVBS2_MODCOD_MARGIN_DB]
            if usable:
                m, th, eff = usable[-1]
                rate = eff * DVBS2_SYMBOL_RATE
                nch = int(rate // PER_CHANNEL_NET_RATE_BPS)
            else:
                m, rate, nch = "none - link does not close", 0.0, 0
            rows.append(dict(band=band.label, station=gs.name,
                             esn0_db=round(esn0, 1), modcod=m,
                             mbps=round(rate / 1e6, 2), opv_channels=min(nch, 9999)))
    dl = pd.DataFrame(rows)
    dl.to_csv("dvbs2_downlink_capacity.csv", index=False)
    print(dl.to_string(index=False))

    # ---------------- Uplink: OPV vs SSB ----------------
    cn0_ssb = SSB_CN_REQ_DB + 10 * log10(SSB_BW_HZ)
    cn0_opv = OPV_EBN0_REQ_DB + OPV_IMPL_MARGIN_DB + 10 * log10(OPV_INFO_RATE_BPS)
    print(f"\nRequired uplink C/N0: SSB {cn0_ssb:.1f} dBHz, "
          f"OPV {cn0_opv:.1f} dBHz, delta {cn0_opv - cn0_ssb:.1f} dB "
          f"(delta is independent of spacecraft G/T)")

    up_rows = []
    for gs in STATIONS:
        el, _, slant = SLOT.geometry(gs)
        if el < 5.0:
            continue
        fspl = 20 * log10(4 * pi * slant * UPLINK_FREQ_GHZ * 1e9 / C_LIGHT)
        A, _ = atmos(gs, UPLINK_FREQ_GHZ, el, 0.5, 1.2)
        eirp_ssb = cn0_ssb - SPACECRAFT_G_OVER_T + fspl + A + K_BOLTZ_DBW
        eirp_opv = cn0_opv - SPACECRAFT_G_OVER_T + fspl + A + K_BOLTZ_DBW
        up_rows.append(dict(station=gs.name, elevation=round(el, 1),
                            eirp_ssb_dbw=round(eirp_ssb, 1),
                            eirp_opv_dbw=round(eirp_opv, 1)))
    ul = pd.DataFrame(up_rows)
    ul.to_csv("uplink_opv_vs_ssb.csv", index=False)
    print("\nRequired user uplink EIRP (dBW) at 13 cm, G/T assumption "
          f"{SPACECRAFT_G_OVER_T} dB/K:")
    print(ul.to_string(index=False))


if __name__ == "__main__":
    main()
