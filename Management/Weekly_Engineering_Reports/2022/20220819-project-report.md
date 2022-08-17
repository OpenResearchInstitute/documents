# Project Reports

## DEFCON 30 Report

Open Research Institute's amateur radio open source showcase at the annual hacker convention DEFCON was located in RF Village (RF Hackers Sanctuary) in The Flamingo Hotel. A volunteer crew of seven people from three US states staffed the exhibit that ran from Friday 12 August to Sunday 14 August 2022. 

RF Village hosts a very popular wireless Capture the Flag (CTF) event. It is a top tier contest at DEFCON and the winners are recognized at closing ceremonies. RF Village also has a peer-reviewed speaking track. See previous talks in the YouTube playlists here: https://www.youtube.com/c/RFHackersSanctuary

RF Village generously offers space for exhibits from the community. For 2022, the exhibits included Open Research Institute, Kent Britain PCB Antennas, Alexander Zakharov (ALFTEL Systems Ltd.), and Starlink (SpaceX). Starlink brought two stations and allowed visitors to experiment with network and physical security. 

Total attendance at DEFCON 30 was estimated at 27,000. Conference events were held in the new Caesar's Forum + Flamingo, Harrah's, and Linq convention centers.

Open Research Institute's exhibit had multiple parts. The entry to the exhibit was a poster session. Posters presented were ITAR/EAR Regulatory Relief for Amateur Satellite Service, Libre Space Foundation's Manifesto, Authentication and Authorization Protocol for Amateur Satellites, and the Ribbit Project Introduction and Architecture. 

All posters were enthusiastically well-received. Specific technical feedback was received on the Authorization protocol that will improve the design. There will be a presentation about the Authorization and Authentication protocol at the September 2022 QSO Today Ham Expo. 

Visitors understood the purpose and potential of Ribbit and could download the free open source Android app from a QR code on the poster. The code was also on the Ribbit stickers handed out at the booth. All 300 of the Ribbit stickers were handed out by Sunday morning. Ribbit allows an amateur operator to type in SMS messages on an Android app. Each SMS message is converted to digital audio tones. The tones are played out the phone's speaker into the microphone of an amateur radio handheld or mobile rig. This can turn any analog HT into part of a digital messaging network. The app can do point-to-point communications and also has a repeater mode. 

Find the Ribbit "Rattlegram" application here: https://play.google.com/store/apps/details?id=com.aicodix.rattlegram

There will be a Ribbit presentation at the September 2022 QSO Today Ham Expo. 

The ITAR/EAR Open Source amateur satellite regulatory relief poster garnered a lot of attention. A very large fraction of DEFCON attendees are familiar with ITAR/EAR, which are a set of regulations that govern the way we design communications satellites in the USA. People that read the poster at DEFCON understood and appreciated the value of the work, which provides long-awaited regulatory relief for the amateur satellite service. The poster presentation lead to an invitation to Policy Village Sunday afternoon for a panel session hosted by the Office of the National Cyber Director. Summary of that session can be found in ORI's 19 August 2022 project report. The ITAR/EAR poster will be part of the projects display at the September 2022 QSO Today Ham Expo. 

Foot traffic flowed past the posters and into the live demonstrations.

The first live demonstration visitors encountered was from OpenRTX (https://openrtx.org). This demonstration used a tablet computer running OpenWebRX to display modified MD-380 transmissions. Visitors could use headphones to hear live transmitted signals. Posters at the table explained the modifications required to implement the M17 protocol on the MD-380 and also described the motivation and value of the work, with an emphasis on the use of the free and open CODEC2 voice codec. The use of CODEC2 in M17 replaces the proprietary AMBE codec found every other digital voice protocol for VHF/UHF ham radio. There was strong interest in both the M17 and the DMR work from OpenRTX, broad understanding of why proprietary codecs are not ideal, and consistently positive feedback. 500 OpenRTX business cards were printed with QR codes for the OpenRTX website and nearly all of them were handed out. 

The second demonstration was Opulent Voice. This is a high bitrate open source voice and data protocol. It's designed as the uplink protocol for ORI's amateur satellite program. The Authentication and Authorization fields are built in and sending data does not require a separate packet mode. The baseline voice codec for Opulent Voice is OPUS at 16 kbps. Higher bitrates are a build-time option. For the DEFCON demonstration, Opulent Voice was transmitted from an Analog Devices PLUTO SDR and received on an RTL-SDR/Raspberry Pi. Visitors could use headphones to listen to the received audio. The modulator and demodulator code can be found at https://github.com/phase4ground/opv-cxx-demod. 300 custom art stickers for Opulent Voice were ordered and all were handed out. 

The two demonstrations compared and contrasted voice quality (3.2 kbps vs 16+ kbps), regulatory limitations (VHF/UHF vs. microwave), and approach to framing (P25 style vs. COBS/UDP/RTP).


The next station had stickers, buttons, patches, ORI's Tiny CTF, Haifuraiya proposal printouts, and a Trans-Ionospheric badge display. See https://www.openresearch.institute/badge 

ORI's "Tiny CTF" was a hidden web server, accessible from the wifi access point located at the OpenRTX demonstration. The access point allowed people to view the OpenWebRX display directly on their connected devices. Participants that found the hidden web server and then blinked the LEDs on a certain piece of equipment at the booth received a prize.

Haifuraiya (High Flyer) is an open source highly elliptical orbit communications satellite proposal. Microwave amateur band digital communications at 5, 10, and 24 GHz are proposed. Transmissions are frequency division multiple access Opulent Voice up, and DVB-S2/X time division multiplexed down. A presentation about this proposal will be at the September 2022 QSO Today Ham Expo.

Based on the feedback about the Trans-Ionospheric, ORI will update and build another round of these badges. Round one of the Trans-Ionospheric badge was a very successful fundraiser. The badges have been enduringly popular in the community, and they can serve as radio peripherals that display link and payload health over bluetooth. The artistic design of the badge is based on the front panel of the Zenith Trans-Oceanic radio. 

There were very high levels of interest, enthusiasm, and positive feedback throughout the weekend. Friends from Ham Radio Village and Aerospace Village visited the booth and shared their experiences, the organizational support from RF Village leads was excellent, and ORI will return to DEFCON in 2023 with another round of open source digital radio work to share. 
