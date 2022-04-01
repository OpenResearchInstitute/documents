## Project Report

### Goals for the week

- [x] 1) MATLAB HDL Coder training definition. We have 40 hours of training credit through the Startup Plan from MathWorks (MATLAB). This is long term and speculative work to produce open source HDL from MATLAB scrips. There are no license issues. There are a lot of learning curve issues.

- [ ] 2) End-to-End transponder demonstration. Is it working over the air in Remote Lab West?

- [x] 3) ProFlix DVB-S2/X gear installed in Remote Labs West. Needs to happen to confirm what we’re transmitting can be received by commercial gear.

- [x] 4) Cubesat Developer’s Workshop - we need a human resource to commit to the show, or else we need to cancel the poster session.

- [ ] 5) HamCation 2023? If you want to see it happen, then get in touch and speak up. We need a team, today, to start organizing an effort. 

- [x] 6) Bringing data modes to the M17 Protocol: needs to happen. We need some woodshedding on this very soon.

- [x] 7) AI/ML at FCC TAC: are propagation models the right path forward? Lots of discussion with Leonard Diguez this past week about the meeting on 23 March. Also - We need to get our guest speakers introduced to the chair ASAP. 

### Reports

#### MATLAB HDL Coder
A MATLAB HDL Coder example was worked through and presented at the FPGA standup on 29 March. There was a hitch with hw_server and the PLUTO already being assigned, or attached. HDL Coder targets the zcu106. 

We've learned (during the meeting discussed below) that the hardware support package for ADRV9371 did not work because we didn't have access to HDL Coder when we tried to use it. Even if you do not need to generate HDL, the HSP for ADRV9371 will not work without license access to it. This is a very big impediment to doing simple things like playing IQ files through the ADRV9371 in MATLAB. We can now go back and try to run the radio card using MATLAB, but this isn't a sustainable solution given the cost of the toolboxes. 

Meeting 1 April with training specialists at MATLAB. 
Met with TJ Moore, Brian Evans, and Radu David in a video conference. 

Training from MATLAB is 50% for us. There is zc706/Zedboard training, Simulink training, and SoM and SoC training of various types. 

Customized training is available, that can address specific needs of ORI and the community. Minimus are $750 per day per person with a minimum of 5 people. 2-6 days, 4 to 8 hours a day, depending on various factors such as time zones and instructor availability. $7500 (2 days, 5 people) to $22,500 (6 days, 5 people) would be the minimum for 2-6 days of customized training. This would be a significant fraction of the training budget, which is also currently being considered for re-allocation to Remote Lab South physical plant. 

6 week lead time. Algorithm development and "DSP for FPGAs" is curriculum available to us; not just how to use the tools. MATLAB has sent outlines and information and the entire set has been forwarded to the board for review. 

#### P4DX FPGA Work
Phase 4 digital multiplexing transponder (P4DX) Field Programmable Gate Array work was summarized in the FGPA Standup on 29 March 2022. Here's the video link to the meeting recording:
https://youtu.be/8Q-8SGUbnvo

#### Cubesat Developer's Workshop
Jay Francis inquired about whether it was in-person or virtual. It is in-person.
Poster was constructed and a copy can be found here: https://github.com/phase4ground/documents/blob/master/Papers_Articles_Presentations/Posters/ITAR-EAR-poster-2022.pdf

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

