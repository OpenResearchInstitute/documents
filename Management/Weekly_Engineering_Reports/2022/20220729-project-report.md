Greetings all!

Here is a summary of Open Research Institute (ORI) work as of summer 2022. 

## Draft Project Report

Thank you to everyone that contributed to this report. If you see something that was missed or needs to be corrected, please send it in via email or file a pull request to this document in github. 

### AmbaSat Inspired Sensors

AmbaSat Inspired Sensors is currently referred to as AmbaSat 70cm Re-Spin and Sounding Rocket Project. As you know, the 915 MHz AmbaSat board was redesigned for 70 cm. A very small number were able to be built (5) and they are in the hands of developers. Developers were solicited through open community outreach. 

We now have an opportunity to be on a sounding rocket, have purchased the right 70 cm antenna for the sounding rocket, and are working towards useful experiments for the upcoming flight. 

Original budget: $4200.00
Current balance: $2841.27

Capabilities:
1) New design submitted as a pull request back to AmbaSat. A 70 cm version is much more useful to the amateur satellite community than a 915 MHz version. 
2) Improvements in power supply and noise performance were also made and a pull request made back to the original AmbaSat repo. 
3) 10 GHz beacon (the community-chosen sensor) design and presentation was made at QSO Today Ham Expo. 
4) Students under the supervision of Dan White were able to use the hardware in a university lab environment to learn about LoRa, digital communications, and space communications. 
5) Sounding rocket opportunity, coordinated by Jay Francis, will result in useful data and additional published designs. 

The design will be exploited until the budget is exhausted. 

### P4DX 

GEO/HEO Transponder Communications is the goal of P4DX, which stands for Phase 4 Digital Multiplexing Transponder. 

P4DX is a frequency division multiple access (FDMA) uplink, which is received, demodulated, and decoded in the spacecraft. Processing makes decisions based on the information streams, which use the Opulent Voice open source protocol. The downlink streams use Generic Stream Encapsulation over Digital Video Broadcast Satellite version 2 and extension, or DVB-S2/X. This is a time-division multiplexing standard. Ground station design is included in this project. 

Original budget: $50,000 for Phase 1, $450,000 for Phase 2
Current balance: $458,700.95

Thank you to everyone that has helped backfill the budget to keep this project fully funded and supported. 

Capabilities:
1) Open Source DVB-S2/X encoder in FPGA. See the video presentation from Andre Suoto for a deep dive on the mathematics required to produce this work. 
2) Three Remote Labs established. Remote Labs West, Remote Labs South (formerly East), and Remote Labs UK. We took the original budget and increased the number and capability of the Remote Labs for the original budgeted amount. Remote Labs allow a developer full access a zc706 (with ADRV9371 attached), a zcu106, a PLUTO SDR, fully licensed MATLAB with all toolboxes (through March 2023), and a floating license of Vivado and Vitis. Remote Labs are fully described at this link. Labs are open for all open source FPGA and SDR work and will remain open as long as ORI can maintain them. 
3) Open source electric motor synchronization for integrated digital communications. We have obtained permission to develop a patent from George Washington University in this area and will prototype an application of the patent. Ion and electric engines provide a serious challenge for digital communications in terms of noise. Better synchronization of engines for spacecraft is desired in and of its own right, but enhanced communications are a particularly attractive benefit. There is a fundraiser for this part of the project going on right now. Find it at the following link. 
4) Opulent Voice open source digital protocol. This is the native digital uplink for P4DX. Loosely based on the M17 protocol, Opulent Voice increases the bit rate from 3200 bps CODEC2 to 16 kbps (or higher) OPUS. It drops puncturing, updates the randomizer, updates the interleaver, drops the Link Status Frame (LSF) simplifies the state machine, allows for flexible codec rates, and adds standard data networking layers in order to allow voice and data to use the same protocol, and to allow for simple integration of authorization and authentication. While Opulent Voice is intended for use at 5 GHz, it seemed a shame to not deploy this protocol terrestrially for more to enjoy. Therefore, a 1.2 GHz portable point-to-point version is currently in progress and has a late-summer demonstration target.
5) Multimedia beacons. Demonstrated at the end of 2021, these multimedia beacons are actually a subset of our downlink. Sending out either camera views or pre-recorded video with test signals, the beacons are getting a big boost from San Bernardino Microwave Society, which has made them a priority in mountaintop deployment. Five are planned and fundraising is in progress. 
6) Polyphase channelizer implementation in FPGA. Leveraged from Theseus Cores, it’s a big step forward to have a working open source polyphase channelizer. Most examples right now are limited by desktop general purpose processing performance, or are proprietary.  
7) Electric/Ion engine synchronization work to reduce interference to microwave-band digital communications on spacecraft. We have obtained the royalty free use of a well-defended patent and are producing an open source application of the patent. 

There is a separate fundraiser for the electric engine synchronization work that can be found here:

https://us.commitchange.com/ca/san-diego/open-research-institute/campaigns/where-will-we-go-next

The design will be exploited and shared until the budget is exhausted. 

### Ribbit

Acoustically coupled open source project that transmits SMS messages over amateur bands using an Android cellular phone and a free application. Lead by Pierre W4CKX and Ahmet Inan (xdsopl). This project will have a poster and demonstration at DEFCON 2022.  

### Versatune

A software project supporting a major revision of an open source product in the DATV space. Demonstration expected in February 2023 at HamCation. Contact Anshul Makkar to get involved. 

### Skylark

This open source satellite project has asked ORI to be the fiscal sponsor and we have agreed. Proposed project budget for Phase 1 is $50,000. Currently unfunded, but that will change. Design and engineering work has commenced and critical regulatory paperwork has been completed. 

### ITAR/EAR Regulatory Work

While the ITAR part of the regulatory relief effort (see poster about this work linked here: ) was funded by ARDC, a reimbursement request for the EAR classification and the advisory opinion work was rejected. An application has been made to YASME Foundation to reimburse the individuals that funded the successful legal work.

An article describing the successful completion of this work was censored from the final version of the October 2021 AMSAT Journal. However, it can be found here:  

https://www.openresearch.institute/2021/09/13/itar-ear-regulatory-work-background-and-summary

This is significant legal work that will have lasting positive impact well outside of open source amateur radio satellites. 

Poster here:

https://www.openresearch.institute/2022/04/02/poster-presentation-itar-ear/

Capabilities:
1) If you publish, it must be free.
2) You can do open source satellite work. If you publish as you create, your work is free of ITAR and EAR. 

Work continues to support those using the regulatory results. 

Original Budget: $15,262.50
Current Negative Balance: ($14,425) 

### Sounding Rocket with University of Puerto Rico

Our proposal to collaboration with UPR for their entry to RockSat has been accepted. We will provide hardware and software for their student team to integrate Opulent Voice as the communications link for the scientific payload. Design and engineering is leveraged directly from P4DX, but will provide a different integration and test experience than a terrestrial side deployment. 

Budget handled through the university. If the University is selected, and if the project is completed as scheduled, then travel expenses will need to be discussed.  

Capabilities:
1) Students educated.
2) Sounding rocket integration for Opulent Voice.
3) Useful information concerning protocol performance obtained from the flight. 

Work is in progress, and if the project is selected by NASA, it will launch in August 2023. 

### Sponsorships, Affiliations, and Collaborations:

#### Villages at DEFCON 

We are sponsoring the Retail Hacking Village at DEFCON 2022. Please visit this Village if you get the chance. 

We are part of Radio Frequency Village at DEFCON 2022, as part of an Open Source Showcase. Please visit if you get the chance. An in-person ORI board meeting will occur at DEFCON 2022, so if you have items for the agenda, please send them to a board member. 

#### Libre Space Foundation

We support the work and mission of Libre Space Foundation. We are a signatory to the Libre Space Manifesto and actively support technical and regulatory work of value to Libre Space Foundation. 

#### IEEE

IEEE remains a productive and affirming partner, with multiple opportunities throughout the year for our work to be represented to the largest engineering organization in the world. IEEE LEO Sats has reviewed our work and provided appreciated advice and support. We thank the Communications Society, the Information Theory Society, and the Signals and System Society in particular for being gracious, accommodating, and welcoming to our speakers. 

#### United States Federal Communications Commission TAC

Membership in the Federal Communications Commission Technological Advisory Committee. Our working group is AI/ML and we co-chair the AI/ML “Safe Uses” Sub-working group. Membership concludes with the production of written work products late in 2022. Working group meets on Wednesday and the sub-working group meets on Thursday. We represent open source, open process, and open access to science to the FCC. These are deeply important topics to AI/ML regulation and the future of all radio services, as AI/ML becomes an increasingly important part of the radio and networking landscape. 

