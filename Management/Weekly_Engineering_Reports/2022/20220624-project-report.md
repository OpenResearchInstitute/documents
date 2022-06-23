# Project Report

## P4DX

Authentication and Authorization work in progress at https://github.com/phase4ground/documents/tree/master/Engineering/AAAAA

### FPGA

Tuesday's FPGA Stand-up meeting video is here: 

[https://youtu.be/yTXBU3sseh4](https://youtu.be/L7WIITfFbKI)

Uplink simulator work can be found here:

https://github.com/phase4ground/documents/tree/master/Engineering/Uplink%20Modem/Simulator

Nothing new added to that until we work through required changes to the demod codebase from mobilinkd to move from 3200 bps CODEC2 to 16 kbps OPUS. High bitrate voice mode is called Opulent Voice.

Here's the (updated) state diagram we start with in the demodulator:

https://drive.google.com/file/d/1L3DJ7vEKKnR4eT2ai8B-9Lv2nZOWfixM/view?usp=sharing

Here's a tracking document for Opulent Voice:

https://docs.google.com/document/d/1vmOwcjmGKwMgAqcdLQ-7zk8PMv6MAcV1hhGDVRyijsQ/edit?usp=sharing

Uplink voice and data streams will be received and multiplexed onto the downlink. 

Codebase is here: https://github.com/phase4ground/opv-cxx-demod

#### Encoder

Our encoder is integrated into the reference design from ADI, and is on the PLUTO in Remote Lab West (keroppi). 
Our encoder has been integrated into the reference design from ADI in Remote Lab UK. This design now builds successfully but the fixes need to be pulled in to the repo.
Our encoder is in the process of being integrated into the reference design from ADI in Remote Lab South. 

#### Decoder

Very exciting! Decoder work has begun. Base is Ahmet's repo. There will be improvements and a new revision. 

## Remote Lab South

Budget allocated; building has commenced. Some of the Lab equipment in storage in NorCal will arrive at Remote Lab South as soon as practical. Keith is here this week in San Diego for talks about ORI and the Lab. 

## Ribbit Updates

Rattlegram is *in the Android store*. You can download it for free and play with it. Poster session at DEFCON 30. 

## FCC TAC 

Weekly AI/ML working group assignment on Bandwidth metrics and how AI/ML will affect policies concerning Bandwith is proceeding with the assistance of our FCC liaison. Prototype with either CBRS or inexpensive ultrasonic transducers is what we're talking about in the working group. 

## Components Engineering

47 GHz transponder components engineering proceeding, and the first batch of components has been received. 

## Grants and Fundraising

SBIR/STTR grants are the focus. Two FDA grants look good and are under consideration. There's plenty more out there at grants.gov. 

A large grant application is proceeding with a potential project partner, and we look forward to announcing good news this year. 

Our dedicated fundraising portal (from Commit Change) is set up and will be used for several campaigns revolving around unique items. It's also available to any project that uses ORI as a fiscal sponsor. 

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
