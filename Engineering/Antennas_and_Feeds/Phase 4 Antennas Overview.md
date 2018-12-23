-   [Dual Antenna](#dual-antenna)
    -   [Two dishes](#two-dishes)
    -   [Patch antenna plus dish](#patch-antenna-plus-dish)
-   [Single Main Antenna with Two Single-band
    Feeds](#single-main-antenna-with-two-single-band-feeds)
-   [Single Antenna with Dual Band
    Feed](#single-antenna-with-dual-band-feed)
    -   [An Introductory Example](#an-introductory-example)
    -   [Coaxial Feed](#coaxial-feed)
    -   [Waveguide Based Advantage](#waveguide-based-advantage)

Phase 4 anticipates a 10MHz uplink within 5650-5660 MHz and a 10MHz
downlink within the range of 10450 - 10460 MHz.

A figure of merit for the investigation of simultaneous feeds in two
bands is the dual-band ratio. This is a ratio of the center frequency of
the high band to the center frequency of the low band. For values within
the range of 0.5 to 5, dual-band feeds are considered to be possible.
For a dual-band ratio close to 1, single broadband antennas and feeds
can often be used.

For Phase 4, the ratio is 1.85. A case study of a design for a dual-band
system for a dual-band ratio of 2.15, as a reference, can be read here:

https://www.ll.mit.edu/publications/journal/pdf/vol04\_no1/4.1.4.EHFdualbandfeed.pdf

As the article from MIT describes, there are at least three design
patterns for dealing with dual band systems. The three approaches, and
relevant Phase 4 details, are outlined below.

Dual Antenna
============

Two dishes
----------

This approach uses two entirely separate antennas, one for transmit and
one for receive. Each antenna is a single-band antenna. This is the
baseline approach for Phase 4. Parabolic dish side lobes are on the
order of 17dB (first sidelobe) to 30dB (fourth sidelobe) down. Isolation
from one dish to another is good, but not infinite.

Patch antenna plus dish
-----------------------

An approach actively being investigated involves using a patch array for
5GHz and a dish and feed horn for 10GHz. Kent Britain WA5VJB is
“Designing 2 patch arrays for use as 5.7 GHz ground station TX antennas.
One in the 16-17 dBi range that would be set and forget. And one in the
18-20 dBi range that would probably would need to be moved twice a day.”

Single Main Antenna with Two Single-band Feeds
==============================================

This approach is best used in the case where the bands are sufficiently
far enough apart to where the smaller feed, at the higher frequency,
does not substantially interfere with the larger lower frequency feed.

For Phase 4, it may be possible to put two feeds on the dish with one
above or beside the other. With this configuration one beam is squinting
to the left, and one to the right.  With careful placement you can still
have both beams illuminate the satellite with usable results.   This
takes advantage of 5.7 GHz beam being much wider than the 10.4 GHz.

Single Antenna with Dual Band Feed
==================================

This approach uses a single antenna and one dual-band feed. This reduces
the pointing effort at the cost of some loss in the duality of the feed.
A proposed PLL LNB already has a horn feed as part of the LNB. Exploring
a dual-band feed would mean developing separate PCB designs with their
own connectors.

An Introductory Example
-----------------------

A successful 5GHz/10GHz dual-band feed for terrestrial use in the
coaxial style can be found here:

<http://www.ntms.org/files/Dual_Band_2_3_and_5_10GHz.pdf>

The isolation from 5700MHz to 10000MHz is -70dB. The isolation from
10000MHz to 5700MHz is -30dB. Tuning the feed requires care, as each
tuning screw affects both bands. The feed, as designed, has the same
polarization on both bands. Linear cross-polarization could increase
isolation by approximately 20dB. Modifying and testing this type of feed
is a proposed experiment for Phase 4.

Coaxial Feed
------------

For a common dual-band feed, the signal is duplex on the same coax.
According to Kent WA5VJB , this requires two filters with about 40-50 dB
rejection of the other frequency. This situation is similar to repeater
duplexer cavities.     

Waveguide Based Advantage
-------------------------

Paul Wade W1GHZ writes, “The dual-band feed can work.  If the two
frequencies are cross-polarized, then the tuning gets much easier, since
the two frequencies no longer interact. Isolation at 10 GHz is free,
waveguide beyond cutoff, but 5 GHz needs a low-pass filter. This is much
easier than repeater cavities.”
