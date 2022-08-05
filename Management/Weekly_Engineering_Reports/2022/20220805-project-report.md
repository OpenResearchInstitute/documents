# Project Report

Additions and corrections? Submit a pull request or send them in via email. 

## FPGA

### DMA read/write problem with the Encoder solved

FPGA meetup video recording can be found here: https://youtu.be/r2Mbz-XQCCc

We have been battling a problem with our DVB-S2 encoder block. 

The repository that integrates the reference design from ADI and our encoder can be found here:

https://github.com/phase4ground/adi_adrv9371_zc706

The hdl-as-submodule branch has re-arranged the repository as a set of submodules instead of static directories.

Reads and writes from the Zynq processor were not happening correctly. The team pulled together and didn't give up and the problem is now solved. The root cause was with the memory map. Thank you to Evariste, Anshul, Suoto, Leonard, and Ken for taking the time to fix this. We now know how to add the next custom block in a way that will avoid this issue. We also now know how to better use the integrated logic analyzer. We've also documented the process of going from HDL git clone to processor-side application. 

https://github.com/phase4ground/documents/blob/master/Remote_Labs/Working-With-FPGAs.md

`check out the zc706-petalinux-Vitis branch to see the documentation`

A pull request for this branch of the documentation has been made, so it should show up as "mainline" instructions shortly.

### Transmit with Encoder

MQTT, as pioneered by Evariste on his implementation on the PLUTO, looks like a great way to go. Anshul is taking this on and we'll back him up in Remote Lab West. 

In order to use the ADRV9371, we generate sample code from the Transceiver Evaluation Software from ADI. This provides configuration settings for a particular frequency and bandwidth for the transceiver, in either C or Python. From this starting point, we will write the transmit application code. We have already run TES successfully, but integrating the large number of settings produced and making sure the transceiver is behaving properly is a non-trivial milestone. If you have experience here please review our work. 

### Downlink Receiver

Codebase updates in progress. Ahmet Ihnan is the lead. 

## Haifuraiya

We will propose an open source amateur radio HEO satellite project to JAMSAT. We are grateful for the opportunity and look forward to their review. 

Successful project kickoff, slide deck review, and the publishing of an annotated video recording of the work session all happened this past week. 

https://youtu.be/wMaDHsPUhLw

## Uplink

Demonstration of our uplink protocol Opulent Voice working over the air can be seen here: https://youtu.be/i7k-jKtU_n8

## Aqua-Phage

Letter requesting permission to submit a grant proposal to the FDA (required as per their process) was sent this week. The funding opportunity sought is for a conference on bacteriophage in aquaculture, specifically fish farming. 

## DEFCON - Imminent!

### DEFCON Demonstrations and Presentations by Open Research Institute at RF Village

#### Opulent Voice

Opulent Voice is an open source high bitrate digital voice (and data) protocol. It's intended to be useful for both space and terrestrial deployments. We’re getting nice clear 16kbps OPUS audio out of the demodulator. See and hear a demonstration at the ORI exhibit in RF Village.  

We’ll be using COBS protocol within Opulent Voice. If you’re unfamiliar with COBS, please read about it here: 

https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing

Authentication and authorization is built in and optional. There is no separate “packet mode”. Things are designed to “just work” and get out of your way whether or not you’re sending voice or data. 

Based on Mobilinkd codebase that implemented M17, the Opulent Voice development implementation can be found here:

https://github.com/phase4ground/opv-cxx-demod

Authentication and Authorization functions will be summarized in a poster presentation. Find out more about this work here:

https://github.com/phase4ground/documents/tree/master/Engineering/AAAAA

#### Ribbit

Ribbit is an open source SMS data mode that leverages smart phone hardware. The free Android app produces digital audio that you transmit over your HT or any other audio coupled device. There will be poster explaining the architecture and you can pick up a Ribbit sticker with QR code for the free Android app at ORI's exhibit in RF Village. 

#### Regulatory

Interested in being able to do more with open source satellites? We have some landmark regulatory results that solve a big problem for those of us in the US that have wanted to do open source satellite work without fear. See our poster in RF Village and find out more at the following link:

https://github.com/phase4ground/documents/tree/master/Regulatory

#### OpenRTX

OpenRTX is a team based in Italy that specializes in open source firmware for a variety of platforms in the VHF/UHF digital voice world. They work on DMR and M17 implementations for the MD-380, and more. Pick up a business card and see a demonstration of OpenRTX's work at ORI's exhibit in RF Village. 

#### Tiny CTF

We'll have the World's Smallest Wireless CTF! Come and find it and get a mission patch if you're successful. 

#### More!

There's plenty more. If you see a Volcano and friendly people, you've found the right place. 
