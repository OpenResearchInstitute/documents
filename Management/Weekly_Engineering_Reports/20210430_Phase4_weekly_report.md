# Project Report for Open Research Institute 
30 April 2021

We welcomed several new volunteers this week. We look forward to the resumption of in-person events when it is safe and practical. The next set of technology demonstrations is scheduled for August 2021. 

## Trello Boards

Join Phase 4 Ground Trello board:
https://trello.com/invite/b/REasyYiZ/8de4c059e252c7c435a1dafa25f655a8/phase-4-ground

Join Phase 4 Space Trello board:
https://trello.com/invite/b/GRBWasqW/1336a1fa5b88b380c27ccf95d21fec79/phase-4-space



The following areas reported progress for this reporting period. 

## FPGA Work

Hardware prototype:

https://github.com/phase4space/p4xdmt_hw_protoype

Receiver development:

https://github.com/phase4space/receiver-development


## CHONC - San Diego Remote Labs PC

Lab PC parts delivered, PC assembled, booted, Unraid installed, and drive and parity drive built. CHONC is Cubical Heavy Open Number Center. 

It's important that participants and potential users know what we have at Remote Lab. The same computer is also at Florida Remote Lab and will be configured when that lab is rebuilt. The building was damaged by a fire in late December 2020 and is in the final stages of repair. No lab equipment was lost in the fire. 

Here are the components for the lab PC. 

G.SKILL Ripjaws V Series 256GB (8 x 32GB) 288-Pin DDR4 SDRAM DDR4 3600 (PC4 28800) Intel XMP 2.0 Desktop Memory Model F4-3600C18Q2-256GVK

This is sufficient memory for demanding applications.

Geforce RTX 3080 GPU

There is a lot of work that can be done on the GPU alone. This is a system unto itself, and we do have interest here in leveraging GPU work in LDPC and machine learning for amateur communications of all types.

EVGA SuperNOVA 1600 G2 120-G2-1600-X1 80+ GOLD 1600W

This is a power supply sufficient for anything that goes into this case.

The case is a View 71 Tempered Glass Thermaltake. 

Seagate SkyHawk AI 16TB 3.5" SATA 256MB 7200RPM Hard Drive ST16000VE000

We plan to have four of these. Two are currently installed. Two are currently suspected dead. Kegen is working on returns/replacements.

Next steps: memory test, host OS installed (Windows 10 Pro as per Wally's request), and configure for remote access. Wireguard comes with Unraid, so that part of the access may be more easily possible. 

Role for this equipment: 

1) Host the DVB-S2/X modulator and demodulator for testing and validation.
2) Host signals and systems machine learning projects.

The DVB-S2 lab gear that goes into CHONC is as follows.

First, a DekTec DTA-2115B-SP VHF/UHF/L-band modulator for PCIe - DTA-2115B-SP

This supports all constellations and modulation modes for each supported standard in VHF, UHF and L-band. Direct digital synthesis of the RF output signal and an on-board ultra-low phase-noise oscillator. Flexible architecture is capable of ATSC 3.0, DVB-S2X, multi-segment ISDB Tmm, and 64 MHz DVB-C2 channel bonding.

Why have this?

Because we want a high-end general-purpose test modulator for developing and qualifying DTV equipment for amateur radio, and for experimentation with new RF modulations. 

You can play-back arbitrary I/Q sample files that are recorded or generated by MATLAB, with a bandwidth up to 72 MHz.

This has the DekTec DTC-383-S2X option, to enable DVB-S2X.

Second, is the DekTec DTA-2132-SX High-end satellite receiver with StreamXpert. 

Professional satellite receiver card with high-quality RF measurements and monitoring, modulator testing and high-speed data distribution. The card comes with full decoding and analysis of DVB Carrier ID. 

This is an FPGA-based DVB-S2/S2X demodulator. The CPU is not involved.  There are calibrated channel-power and MER measurements available. 

Supports VCM, ACM, multiple input streams), GS (generic stream) with access to baseband frames (BBFRAMEs) in L.3 format. This is good.

Hardware demodulator can be bypassed to obtain I/Q samples for recording or SDR. You don't have to work through all the other stuff we're talking about. You can get the samples directly.

What does this mean? 

1) A monitoring and measurement solution for DVB-S2 and DVB-S2X for the open source amateur satellite community. 

2) Decoding and analysis of single or multiple DVB-CID signals, even when the satellite carrier interferes with other carriers.

3) Validation of DVB-S2/S2X/CID modulators is possible with this gear.

There's plenty to learn, and it will all be openly shared. 


## Dual-band Feeds

Updated lab testing results received for the 10/24 GHz dual band feeds from W1GHZ. 
David Chan, Engineer/Scientist 1 at Rincon Research Corporation writes, 

"Hi Michelle attached are 4 plots for the dual band feed antenna (E/H Plane cuts at 10 GHz and 24 GHz) along with a frequency sweep of the isolation between the 10 GHz and 24 GHz ports.

There are also VSWR plots to show that each of the ports are matched correctly. Let me know if you want to make any other measurements."

We would like to recognize and thank Rincon Research for the use of their anechoic chamber. This valuable resource makes it much easier to use this design. 

See data at https://github.com/phase4ground/documents/tree/master/Engineering/Antennas_and_Feeds/W1GHZ_10-24GHz_dual_band_feed


## Microsoft 365 Free for Non-profits

If you need or want a license for Microsoft 365 (free for non-profits) for ORI work, then we have 8 available. 

Mail ori@openresearch.institute to ask for a license. 


## M17 Project Update

Open Research Institute is a fiscal sponsor of M17 Project. ARDC has awarded a grant to the M17 Project. This is extremely good news!

Please visit https://m17project.org/ to find out more about the M17 Project.

See https://www.openresearch.institute/ to learn about ORI. 

ARDC stands for Amateur Radio Digital Communications, and has a very large fund for open source work in amateur radio. Find out more at https://www.ampr.org/

With the full support of Open Research Institute, M17 signals were successfully transmitted through the QO-100 satellite. 

https://twitter.com/amsatdl/status/1378043637129482240

While M17 Project is primarily terrestrial, the protocol is an excellent candidate for use in the amateur radio satellite service. 

M17 protocol will be included as an ORI transponder uplink protocol. 

Learn more about ORI's transponder work at https://www.openresearch.institute/getting-started/ and find out about all of the projects we support at https://www.openresearch.institute/projects/

Do you know of a project that would fit in at ORI? Let us know, because we want to help them succeed.

Derek Kozel has an early work in progress that will make a big difference. He's repackaged the C++ M17 de(modulator) as a library and is working on GNU Radio blocks.

https://github.com/dkozel/m17-cxx-demod/tree/cmake-refactor

https://github.com/dkozel/gr-m17

This work will more easily allow a transponder transmitter demo with live signals at an upcoming event. We're tentatively scheduling DEFCON and Ham Expo August 2021 for technical demonstrations. There may be changes based on the response to COVID-19. 

Please see https://www.defcon.org/ for the latest about DEFCON. We are looking at either Aerospace Village or Ham Radio Village for in-person technical demos. 

Please see https://www.qsotodayhamexpo.com/ for the most up-to-date information about Ham Expo. This event will be virtual with a strong interactive component. 

These two events are close together on the calendar. Therefore, the demonstration content presented at both will be the same. However, the demographics of attendees of the two events are very different. By presenting at both, the widest possible amateur radio audience will be reached. 

The comment from AMSAT-DL about a hope that the "efficiency of the physical modem layer to the satellite channel with minimum C/No requirements" can be improved from the QO-100 experiment can be addressed by using a different physical layer design. In the case of ORI's transponder, the uplink modulation is 4-ary MSK and there will be a large improvement in efficiency.

The GNU Radio blocks, along with the polyphase channelizer, GSE, QoS work, and the DVB-S2 transmitter, are expected to figure prominently in the next demonstration.

Thank you for all your support and encouragement. The future of amateur radio digital is very bright, and there's a whole lot going on in the satellite world.


## AmbaSat Inspired Sensors

Open Research Institute is a fiscal sponsor of AmbaSat Inspired Sensors. This work is funded by ARDC. 

Volunteers and advisors met on 28 April 2021. Basic operation and reporting through The Things Network has been confirmed and demonstrated. Component selection for "Sensor for 10 GHz CW Beacon" begun. We discussed beacons and balloon missions, one of which will be this coming Monday and will include an AmbaSat as a payload, plus GPS sensor. 

Parts and component research going on including but not limited to:

https://www.minicircuits.com/  

https://www.markimicrowave.com/home/

https://www.analog.com/en/index.html

Here's the website and repos for the work that Libre Space is organizing to try and get an inexpensive small radio up and running in hardware and software, to provide more open options for potential main board modifications. 

https://opensatcom.org/

https://gitlab.com/scrobotics/lsf-opensatcom-fw

https://gitlab.com/scrobotics/lsf-opensatcom-hw


## Debris Mitigation Minimum Viable Product

"We're in the "drafting slides" part of the process. The paper is complete but the review is not. The regulatory meeting will happen in the very near future."


Additions, corrections, updates to ori@openresearch.institute 