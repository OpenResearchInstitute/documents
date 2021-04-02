# 2 April 2021 Phase 4 Weekly Report
Open Research Institute
https://openresearch.institute

Greetings all! Here’s an engineering report about recent work within Open Research Institute.

Corrections and additions to ori@openresearch.institute

## Trello Board Roundup

Join Phase 4 Ground Trello board:
https://trello.com/invite/b/REasyYiZ/8de4c059e252c7c435a1dafa25f655a8/phase-4-ground

Join Phase 4 Space Trello board:
https://trello.com/invite/b/GRBWasqW/1336a1fa5b88b380c27ccf95d21fec79/phase-4-space

These are kanban boards that follow the “to do”, “doing”, and “done” workflow model. Find out more about kanban boards at https://en.wikipedia.org/wiki/Kanban_board

### Phase 4 Space To Do

The “To do” list at Phase 4 Space has emptied out, but the remaining items are deceptively simple.

1) Create Initial End-to-End Simulation Model
2) Create End-to-End Documentation

These items will be addressed in part this coming Saturday, at the FPGA planning meeting. That meeting is to determine next steps on the hardware description language work for DVB-S2/X transmission and reception. As many of you know, the transmitter work was completed for demonstration at the mid-March QSO Today Ham Expo Virtual Hamfest. The next step is the receiver. The simulation model and the documentation will dramatically increase the probability of success for integration, testing, and deployment. These two tasks will be broken down into many more tasks with a higher level of specification. 

For the Ham Expo transmitter demonstration, you can see the page with the high-level results here:

https://www.openresearch.institute/qso-today-ham-expo-technical-demonstrations/

### Doing

 Under “doing” for Phase 4 Space, there’s plenty going on. 

We have a task for 

### Publish the current resource reports from the FPGA work. 

This will, over time, become much more complicated. The transmitter utilization snapshot can be found here:

https://www.openresearch.institute/wp-content/uploads/2021/03/Screenshot_2021-03-12_21-28-10.png

### Second, Sequence Diagram for Authorization/Authentication.

Tilak and Paul KB5MU are working on this with weekly meetups. Most of those meetups have happened, and the reports are positive. The current working document is an introduction and a draft of the sequence diagram. The work produce will be a design ready for wider review. 

Here’s the draft introduction:

Assembly, Acquisition, Access, Authentication, and Authorization for a Multiplexed Digital Communications System for the Amateur Radio and Amateur Satellite Services
The Phase Four Ground (P4G) project has defined, and various compatible payload projects are adopting, a digital communications system based on many single-user FDMA channels of digital uplink data and a single DVB-S2/X downlink channel multiplexed on board the payload using Generic Stream Encapsulation (GSE). Ground stations and payloads comply with a common _Air Interface_ specification that defines all interactions between stations in enough detail to ensure compatibility. The Air Interface codifies many of the design decisions that tailor the system to meet the identified system goals. The intention is that ground station equipment can come from a variety of sources, including commercial manufacturers, kits of parts for individual builders, and even independent DIY construction projects built from scratch by more advanced amateurs. The hope is that commercial equipment manufactured in quantity will be very affordable and relatively easy to use, while extremely flexible experimenter-friendly equipment can still be used to advance the state of the art. For all this to be possible, it is necessary to specify the detailed behavior of the ground station in full detail.
Several decades of experience with satellite communications systems has revealed a variety of problems that can arise from the fact that any satellite, at any given time, is potentially accessible by many people spread over a large area. Some of those people are welcome users of the system, and these people need a way to cooperatively share the limited resources of the satellite. Others may be eligible to use the system, but for some innocent reason are causing problems with the satellite, say by transmitting with excessive uplink power on a linear transponder. Another group may be causing problems maliciously, say by intentionally interfering with specific transmissions. In a worst-case scenario, organized groups of unlicensed stations may take over part or all of the system for their own use. This has been seen on disused military systems such as FLTSATCOM. To my knowledge, we have not experienced any systematic “pirate” usage of amateur satellites, perhaps in part because of their limited orbits and signal strengths. An easy-to-use geosynchronous system, such as we want to build, could be far more attractive to pirate users.
On an analog satellite, there is little or nothing that can be done about these problem stations, short of continuously monitoring for abuse and turning off the satellite when abuse is detected. Features like AMSAT-DL’s LEILA have had some success in mitigating the problems caused by excessive uplink power, but can only do so much on an analog transponder, because it isn’t practical to distinguish wanted signals from unwanted ones in the spacecraft payload. With all-digital transmission and a relatively powerful computer on board, we can do much more.

### Third, Thermal Desktop Remote Access through our FlexLM License Server.

The essential task of obtaining and installing the license file in our FlexLM License Server appeared to have worked, but two software dependencies are holding up the use of this powerful package. 

One dependency is AutoCad, which is now subscription-based, out of budget, and has no non-profit discount. Another dependency is Intel Parallel Studio XE. 

There are at least two areas of thermal modeling that we need to do. One, whether or not the architecture we envision can work at GEO the way we assume. Given the link budget, and given the amount of power required for communications and spacecraft functions, and given the equipment available and the solar panels assumed, how much thermal margin do we have within 6U?

This task was proposed to Virginia Tech as a student project in August 2020. A set of slides, an experienced volunteer advisor, funding, and software tools were part of the support package. 

This proposal got good initial reviews from Virginia Tech. There were two teleconferences discussing the work. Volunteers were introduced to faculty and resources committed. 

### Working With Universities

We now know that this proposal was part of a “showcase” of projects presented to students. We assume it was not selected and then not assigned because we did not hear back from Virginia Tech. 

A failure to “begin work” as expected also happened with AmbaSat Inspired Sensors at Vanderbilt University. ORI is the financial sponsor for this project, which was awarded a grant from ARDC. The money was received in late summer 2020. However, no students “selected” the work - through two semester cycles. Work that we hoped would commence in December 2020 did not start until March 2021, when a community volunteer agreed to take on the challenge of creating amateur microwave beacons on the AmbaSat platform. It’s highly positive that the work is beginning. This work will have impact on open source amateur radio with lightweight miniature beacon designs freely shared with the community.  

At many Universities, there are “showcases” or “selection days” where students choose from a menu of projects. There are more projects than students. This was not explained or understood when ORI was putting together proposals for student work at Virginia Tech. If it’s a competition where ORI work is pitched in to fill out a line-up for students, then ORI cannot afford to put critical path work into these proposals. 

As a result of these experiences, over the past week we began a review of ORI’s approach to Universities. Part of this review was stating the perceived problem, and soliciting feedback, on the mailing list. 

These examples are not the only University work proposals that ORI made that 1) got strong positive reviews and 2) where funding was provided by ORI and then 3) work didn’t start. These are the most useful examples for us to study. 

The board of directors has an open session. The feedback and discussion about this will be taken to heart, and changes will be made. 

Advice so far tends towards taking a much more active role in creating opportunities for people to do the work. In summary, the advice from a variety of sources is to 1) provide our own internships and 2) halt proposals to Universities that have “showcases” and 3) stop trying to fight commercial competition for student work.

Commercial interests often can, and do, internally fund faculty and staff. ORI really cannot compete with this type of internal corporate funding that Universities secure. It doesn’t mean our work isn’t excellent and worth doing. It’s simply an outcome of our current economy, commercial dominance, and the way Universities and students are funded. We can and will adapt. 

It’s not the fault of University faculty and staff. They are telling the truth when they like our work and they honestly want things to move forward. There is a mismatch in that we really need the work to happen and it hurts when an expected project doesn’t start, but the University feels absolutely nothing one way or another. The engineering departments we’ve been involved with and talked to will keep doing what they have been doing, whether we stepped on their train, or we got left at the station. Since not being selected costs us a lot more than it does them, we have to figure out how to equalize this out and make any necessary adjustments. We should have no expectation that Universities will make any changes, at all, about anything they do. It’s up to us to bring the probability of success up from today’s “zero” to whatever we believe is an acceptable number. 

If you have experience and advice here and haven’t weighed in on the thread on the mailing list, then please do. Or, write me or the board directly. Thank you to everyone that has already shared some very useful and helpful advice and insight. It is making a difference!

### Back to Thermal Desktop Remote Access through our FlexLM License Server.

The second area of thermal modeling is the FPGA. The FPGA will be the source of a lot of heat. Efforts to reduce power consumption, and reduce the thermal load, will be required. The ability to model this work is necessary. There is not a lot of open source work in this area, at all. Anything that we publish will be significant. 

We have Ultrascale devices that will have thermal sheet. We will have some devices with thermal goo. We will publish results here. We will be looking to dial down the power consumption over time. Simulations with Thermal Desktop are going to be of great value here, but not unless we can get the dependencies sorted out and the software working and volunteers fully trained and fully engaged. There’s been a delay here due to multiple factors. The path needs to be cleared. 

### Default Digital Downlink

There’s significant conceptual progress here. With the transmitter HDL largely complete, this can be implemented. The goal is to use dummy frames in DVB-S2/X as test or beacon signals. In the case where the frames are not needed for communications, they will cycle through all the mod-cods and will carry recognizable default data of some type. This provides an “always on” method to test receiver capability without adding a nonstandard type of signal or breaking DVB-S2/X. 

The deadline for the requirements and specifications was 1 April 2021, but this is going to have to be extended!

### Open Lunar Foundation Support Action Items

There are two outstanding items from the list. 1) Do we need to include large frame size for LunaNet? And 2) read the CCSDS DVB-S2 documents.

Some of have read the CCSDS DVB-S2 documents, where it’s described how DVB-S2 and LunaNet are compatible. We’re not at a point where we are confident about some of the systems engineering challenges, but it is clear that LunaNet links can be done with DVB-S2 based equipment. 

Action Item: We need a meeting with Open Lunar Foundation to close these out. 

### Lab Bench PC Configuration Update

The San Diego lab bench PC has yet to be delivered. It was planned to be build alongside the Florida Lab PC and then shipped to San Diego. There have been multiple delays due a fire at the Florida site, COVID, health issues, and broken parts. All working parts have been requested to be shipped as of 31 March 2021 and the PC will be built in San Diego.

### “Minimum Viable Product” Presentation for Regulators on Amateur Radio Satellite Service and Debris Mitigation

This is proceeding well. The final drafts is in progress, additional reviewers have been obtained, and scheduling can be done for the meeting with about a week’s notice. April 2021 is the target month for the meeting. 

### UBA5-44 Battery Analysis

Batteries obtained, host computer obtained, and schedule has cleared up post-Ham Expo. Initial reports will be published in April 2021. 

### Write an Open Research Institute Remote Labs paper (for IEEE?)

Not started yet, but the Ham Expo Remote Labs presentation from Paul KB5MU will provide the baseline for this paper. 

### GMAT Direct-to-Graveyard mission plan

Completed and presented at Ham Expo by Anshul Makkar. Until 16 April 2021, please visit https://www.qsotodayhamexpo.com/ with the email address you used to register for the event, and log in and view the presentation. After 16 April, all presentations will be publicly available for free. 

### Write “Hardware in the Loop” Paper

Paper needs to be written and reviewed. In a practical sense, this is on hold until Wally Ritchie returns to work. 

### Review Link Budgets

On hold until Wally Ritchie returns to work. 


### Phase 4 Ground To Do

All of these items are “To Do” with small amounts of progress or preliminary work. 

#### HTML5 Draft of radio user interface.

#### Uplink amplifier for 5 GHz. 

#### Dual band feed electronics creation. Take LNB and our 5/10 feed design, combine, and test. 

### Dual Band Feed Characterization

Successful 10/24 GHz provisional results from Mike Parker and David Chan is here: https://github.com/phase4ground/documents/tree/master/Engineering/Antennas_and_Feeds/W1GHZ_10-24GHz_dual_band_feed

More work expected! These results will help extend the work from 5/10 GHz to 10/24 GHz. Thank you to Mike and David. 

ORI has a supply of these feeds. If you can test them or will get them on the air and in use and report back, then get in touch and we will send you one. 

### AXM0F243 Uplink Prototype

Initial results in GNU Radio achieved. Next, demodulate/decode/design 4-ary MSK in GNU Radio. Was delayed until after Ham Expo. 

Sprint deadline date adjusted. Looking for more help here. ORI has a second development board available. 

Action Item: It might be possible to remote this. 

## FPGA Next Steps

Planning meeting scheduled for Saturday 3 April 2021 at 8am Pacific. Next steps for FPGA work will be discussed. Multiplexing functions, receiver functions, and polyphase filter bank are all functions with some progress. Prioritization and preliminary scheduling, roles and responsibilities, and identification of roadblocks and necessary resources. Full report after the meeting. 
