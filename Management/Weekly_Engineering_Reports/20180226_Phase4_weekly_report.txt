Welcome to the Phase 4 Weekly Report for 26 February 2018.

Correlator Update and on-ramping!

Our goal is to implement an open source version of the DVB-S2 and DVB-S2X protocol for amateur radio terrestrial and space use. 

The DVB-S2 header starts out with a fixed pattern of symbols. This is called "Start of Frame" or SOF for short. The correlation looks for this pattern to find the edges of the frame.

Knowing where the frame starts is vital. Otherwise it's really hard to get your payload off the "train" of transmitted frames. Correlation also helps us locate our pilot tones. Pilot tones improve our receive process.

