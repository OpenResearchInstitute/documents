## Project Report

### Goals for the week

1) MATLAB HDL Coder training definition. We have 40 hours of training credit through the Startup Plan from MathWorks (MATLAB). This is long term and speculative work to produce open source HDL from MATLAB scrips. There are no license issues. There are a lot of learning curve issues.

2) End-to-End transponder demonstration. Is it working over the air in Remote Lab West?

- [x] 3) ProFlix DVB-S2/X gear installed in Remote Labs West. Needs to happen to confirm what we’re transmitting can be received by commercial gear.

4) Cubesat Developer’s Workshop - we need a human resource to commit to the show, or else we need to cancel the poster session.

5) HamCation 2023? If you want to see it happen, then get in touch and speak up. We need a team, today, to start organizing an effort. 

- [x] 6) Bringing data modes to the M17 Protocol: needs to happen. We need some woodshedding on this very soon.

- [x] 7) AI/ML at FCC TAC: are propagation models the right path forward? Lots of discussion with Leonard Diguez this past week about the meeting on 23 March. Also - We need to get our guest speakers introduced to the chair ASAP. 

### Reports

#### MATLAB HDL Coder
Meeting 1 April with training specialists at MATLAB. <notes here!>

A MATLAB HDL Coder example was worked through and presented at the FPGA standup on 29 March. There was a hitch with hw_server and the PLUTO already being assigned, or attached. HDL Coder targets the zcu106. 

#### P4DX FPGA Work
Phase 4 digital multiplexing transponder (P4DX) Field Programmable Gate Array work was summarized in the FGPA Standup on 29 March 2022. Here's the video link to the meeting recording:
https://youtu.be/8Q-8SGUbnvo

#### Cubesat Developer's Workshop
Jay Francis inquired about whether it was in-person or virtual. It is in-person.
Poster was constructed and a copy can be found AI: insert link here

#### IP over M17
"Office Hours" on 30 March 2022 5pm US Pacific to talk about data modes and microwave. 
Link to the meeting on our public calendar can be found here: https://calendar.google.com/event?action=TEMPLATE&tmeid=MDhvb2k0b3RzMzViNDF1dHUwZW9sMTFzZmUgZ3N1aXRlQG9wZW5yZXNlYXJjaC5pbnN0aXR1dGU&tmsrc=gsuite%40openresearch.institute

Video is here: https://youtu.be/Am8gl3GxIqY

Consensus on:
1) Validity of use case for higher bitrate M17 for P4DX uplink.
2) IP over M17 could use an example (as could all the types in this field), but the type field indicating IPv4 is sufficient for carrying IPv4 within M17. M17 packet is small enough to where IP fragmentation will probably occur. 
3) M17 over IP is defined in the appendix, it works as implemented in the reflector network, and did not appear to need any additional work.
4) P4DX could provide a spigot of M17 uplinks over IP, using the protocol in the appendix, as a Groundsat feature. This would not affect the air interface.
5) We discussed the XOR with random data aspect (covert SPARROW channel here? Yes/maybe if there’s a known message)
6) Discussed asking for a P4 Type Field Indicator. Smart receivers won’t need this, but it would allow people to move between 9600 bps M17 and higher bitrate M17.

#### AI/ML at FCC TAC

ORI's remarks for 30 March 2022:

"Without open data sets, and open source algorithms, there is no way to deliver equitable results for the general public. 

The identification of the data sets, and not the ML techniques, should be the regulatory priority. 

We cannot get involved with implementation of ML. We must define what it means to have a successful ML algorithm within the context of telecommunications. 

We have not discussed that yet. 

In other words, we define the objective functions, not the parameters. 

What is the regulatory outcome that  we must deliver in order to satisfy the mission of the FCC? If that can be stated within this group, then we have some real traction on the problem."

We are serving as the co-chair for the Safe Uses of AI/ML sub-working group of the FCC Technological Advisory Committee for 2022. 

We have submitted OSI and IEEE CAI individuals as guest speakers.

Sub-working-group "Safe Uses of AI/ML" had a kickoff session on Thursday 1200 US Pacific. 

#### ProFlix DVB-S2/X gear installed in Remote Labs

1) DekTec DTA-2132 (receiver) installed in Remote Labs West CHONC. Will be attached to the Windows VM, which also has direct access to the RTX 3080 GPU. StreamXpert license is ready to go on Chonc-Win10.

2) DekTec DTA-2115 (transmitter) installed in Remote Labs West Hello KitTI PC

3) DekTec DTA-2115 (transmitter) previously installed in Remote Labs South CHUBB in November 2021.  

