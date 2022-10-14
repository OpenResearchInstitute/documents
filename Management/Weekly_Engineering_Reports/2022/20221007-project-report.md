# Project Reports

## Presentations

Ribbit was at DEFCON. Ribbit was at Ham Expo. 

Ribbit will now be at RATPAC!

If you could please save the date for 20 October 2022 at 6pm US Pacific, then Pierre et al will present and take Q&A in the emergency communications track Radio Amateur Training Planning and Activities Committee (RATPAC). 

This is an all-volunteer group that puts on two presentations a week about amateur radio. Wednesday nights are general interest, and Thursday nights are emergency communications. 

Find out more at https://sites.google.com/view/ratpac

Ribbit will also be featured as the program presentation at GARS on 14 March 2023. 

## FPGA 

### Downlink Transmitter

#### Default Digital Downlink (Triple-D) Chart

Example modulation and encoding combinations for Triple-D are below. 

- [ ] Review List

When no traffic is present, test patterns will be sent. The purpose of the test patterns will be to provide modulation and coding combinations for receiver testing and tuning. The test patterns will be sent in increasing order of bitrate, with the lowest bitrate test pattern sent every other slot. Alternating the easiest test pattern with all the others in order ensures that nearly any receiver has something to constantly listen to and tune towards. 

| Index | Modcod | Bitrate Mbps | TS Bitrate Mbps |
|---|--------|----------|--------|
|1| QPSK 1/4 | 3.6588 | 3.3718 |
|2| QPSK 1/3 | 4.9552 | 4.5666 |
|3| QPSK 2/5 | 5.9924 | 5.5224 |
|4| QPSK 3/5 | 9.1030 | 8.3898 |
|5| QPSK 2/3 | 10.1409 | 9.3455 |
|6| QPSK 3/4 |11.4373 | 10.5403 |
|7| QPSK 4/5 | 12.2152 | 11.2571 |
|8| QPSK 5/6 | 12.7338 | 11.735 |
|9| QPSK 8/9 | 13.598 | 12.5315 |
|10| 8PSK 3/5 | 13.6118 | 12.5442 |
|11| QPSK 9/10 | 13.7709 | 12.6908 | 
|12| 8PSK 2/3 | 15.1625 | 13.9732 | 
|13| 8PSK 3/4 | 17.1008 | 15.7596 |
|14| 8PSK 5/6 | 19.0392 | 17.5459 |
|15| 16APSK 2/3 | 20.1518 | 18.5713 |
|16| 8PSK 8/9 | 20.3315 | 18.7369 |
|17| 8PSK 9/10 | 20.5899 | 18.975 |
|18| 16APSK 3/4 | 22.728 | 20.9454 |
|19| 16APSK 4/5 | 24.2738 | 22.3699 |
|20| 16APSK 5/6 | 25.3043 | 23.3196 |
|21| 16APSK 8/9 | 27.0217 | 24.9024 |
|22| 16APSK 9/10 | 27.3652 | 25.219 |
|23| 32APSK 3/4 | 28.1395 | 25.9325 |
|24| 32APSK 4/5 | 30.0532 | 27.6961 |
|25| 32APSK 5/6 | 31.3291 | 28.8719 |
|26| 32APSK 8/9 | 33.4555 | 30.8315 | 
|27| 32APSK 9/10 | 33.8808 | 31.2235 |

One full cycle of the pattern sent (using the index) would be 1 2 1 3 1 4 1 5 1 6 1 7 1 8 1 9 1 10 1 11 1 12 1 13 1 14 1 15 1 16 1 17 1 18 1 19 1 20 1 21

A certificate of highest bitrate reception achieved could be designed. There are several ways to do this. However, first, we need to get successful transmission of the test patterns in order without any extra mechanism. 

Test patterns at the above bitrates were generated using simple video files from Adobe Premiere. 


### Uplink Receiver


## Haifuraiya

Article follow-up sent to JAMSAT Editor. 

### Power Bus

Power systems, power budget, and power dissipation determinations are in progress. Thank you to Thomas Parry, Michael KA2ZEV, and Samudra for ongoing contributions.

| Sources in Power Plant | 
| ---------------------- |
| Supercapacitors        | 
| Rechargeable Batteries | 
| Solar Panels           | 
| Power Controller       |

#### Supercapacitors

Kit donated, questions asked about role. 

#### Rechargeable Batteries

Battery packs from Nickel Metal Hydride cells will be created. These will be used as the initial battery packs for the engineering model. This work will complete the Cell Matching project. 

#### Solar Panels

Flexible panels from Northrup Grumman will be modeled and quoted.

#### Power Controller

Possible starting point is here https://gitlab.com/librespacefoundation/upsat/upsat-eps-hardware and https://gitlab.com/librespacefoundation/upsat/upsat-eps-software and Satellite Solar Power Budget tool here https://gitlab.com/librespacefoundation/satellite-solar-power-budget
