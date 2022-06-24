# Project Report

## P4DX

Authentication and Authorization work in progress at https://github.com/phase4ground/documents/tree/master/Engineering/AAAAA

SSL prototype work has been done and the repo has been updated. At some point, some of this work may need to involve ARRL's LoTW team, not only to make them aware of the work but also in the case that we need support from LoTW in order to achieve all the functionality envisioned by this part of the project. 

The default state of the transponder is permissive and not restrictive. Restrictions may be required for emergency communications support or to restrict bad actors. Having a working and tested authentication and authorization system within a digital transponder increases the utility of the work beyond amateur radio. This respects the requests for authentication and authroization from the multiple potential amateur radio satellite operators we've spoken with about this over the past three years. 

### FPGA

Tuesday's FPGA Stand-up meeting video is here: 

[https://youtu.be/yTXBU3sseh4](https://youtu.be/L7WIITfFbKI)

Uplink simulator work can be found here:

https://github.com/phase4ground/documents/tree/master/Engineering/Uplink%20Modem/Simulator

Nothing new will be added to this until we work through required changes to the demod codebase from mobilinkd to move from 3200 bps CODEC2 to 16 kbps OPUS. High bitrate voice mode is called Opulent Voice.

Here's the (updated) state diagram we start with in the demodulator:

https://drive.google.com/file/d/1L3DJ7vEKKnR4eT2ai8B-9Lv2nZOWfixM/view?usp=sharing

Here's the protocol tracking document for Opulent Voice:

https://docs.google.com/document/d/1vmOwcjmGKwMgAqcdLQ-7zk8PMv6MAcV1hhGDVRyijsQ/edit?usp=sharing

Uplink voice and data streams will be received and multiplexed onto the downlink. 

Codebase is here: https://github.com/phase4ground/opv-cxx-demod

#### Encoder

Our encoder is integrated into the reference design from ADI, and is on the PLUTO in Remote Lab West (keroppi). 
Our encoder has been integrated into the reference design from ADI in Remote Lab UK. This design now builds successfully but the fixes need to be pulled in to the repo. 
Our encoder is in the process of being integrated into the reference design from ADI in Remote Lab South, but this is delayed due to physical plant upgrades necessary to expan the lab for biomedical work. 

#### Decoder

Very exciting area of progress is the DVB-S2/X HDL decoder. Decoder work has begun. Base is Ahmet's repo. There will be improvements and a new revision donated back to the repository. 

## Remote Lab South

Budget allocated; building has commenced. Some of the Lab equipment in storage in NorCal will arrive at Remote Lab South as soon as practical. Keith Wheeler was here this week in San Diego for business, and spent time after work in talks about ORI and the Lab. Thank you to Keith and the rest of the board for all the support, interest, and expertise to stand up an open source lab in an underserved community (central Arkansas, USA). 

## OpenRTX

OpenRTX (and M17 Project) are at Friedrichshafen Ham Radio show this weekend. If you're there please drop by and support them. ORI funded the travel for participation in this event from the M17 ARDC grant. 

## Ribbit Updates

Rattlegram is *in the Android store*. You can download it for free and play with it. There will be a poster session at DEFCON 30 in the RF Village. 

## FCC TAC 

Weekly AI/ML working group assignment on Bandwidth metrics and how AI/ML will affect policies concerning Bandwith is proceeding with the assistance of our FCC liaison. Prototype with either CBRS or inexpensive ultrasonic transducers is what we're talking about in the working group. 

## Components Engineering

47 GHz transponder components engineering proceeding, and the first batch of components has been received. 

## Grants and Fundraising

SBIR/STTR grants are the focus. Two FDA grants look good and are under consideration. There's plenty more out there at grants.gov. 

A large grant application is proceeding with a potential project partner, and we look forward to announcing good news this year. 

Our dedicated fundraising portal (from Commit Change) is set up and will be used for several campaigns revolving around unique items. It's also available to any project that uses ORI as a fiscal sponsor. Here is our first campaign! Please help spread the word. 

https://us.commitchange.com/ca/san-diego/open-research-institute/campaigns/where-will-we-go-next

## Event Planning

### Friedrichshafen 24-26 June 2022

M17, OpenRTX, and Evariste's work on FGPA encoder designs for P4DX will all be at the show this year. See https://www.hamradio-friedrichshafen.com/ for more details.

### DEFCON will be August 11-13, 2022

In-person demonstrations of everything we have working, plus we discussed whatever doesn't, and why. Excellent support from DEFCON over the past week - thank you to all helping out here. 

### Ham Expo will be September 17-18, 2022

Virtual event with booth and multiple speaking track. Has been a very successful event for ORI. Should we have our next quarterly TAC at Ham Expo? 

### ORI will be the November 2022 program for San Bernardino Microwave Society. 

Update about ORI's work and in-person demonstrations. 

### HamCation 2023?

Anshul and Art are interested in going. We'll need more people to commit in order to be a formal part of the show. 

### IMS2023 

Time to start submitting for inclusion on the floor and in the ham social demo area.
