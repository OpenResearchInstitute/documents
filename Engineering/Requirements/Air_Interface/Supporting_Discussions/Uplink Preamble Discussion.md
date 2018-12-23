Initial draft KB5MU, KA9Q, W5NYV

The Phase 4 FDMA uplink channel is currently assumed to be 10MHz wide,
consisting of one hundred 100kHz channels.

There are certain things we need from our uplink signal. We need a
constant envelope signal. We need reliable signal acquisition at the
satellite. We want to reduce adjacent channel interference. We do not
want to spend more power than necessary.

We believe that reliable signal acquisition at the satellite can be
enabled with a preamble on uplink transmissions. The purpose of the
preamble is for the satellite to identify a Phase 4 signal from the
earth, obtain symbol timing, obtain frame timing, and then set the
modulation, coding, and data rate for the transmission that follows.

Since a user terminal can hear itself on the downlink, it will not have
to resynchronize as long as its own signal is being received. If it
loses its own signal, then the preamble is resent. For cases where there
are uplink-only stations, such as emergency operations, automated
operations, or equipment failure, another mechanism must be required
that forces resynchronization.

Below are the major components of the preamble in time order.

A fixed-sized header is then sent at the lowest modulation rate. This
header describes the packet. The contents of the header are as follows.

The next header field contains the following information. The
modulation, coding, and data rate combinations may be encoded in order
to make them as compact as possible.
