## Phase 4 Weekly Report for 11 December 2020

#### Architecture 9 December 2020

Progress this week on detailed architecture for the exciter. The short term goal is to be able to write base-band frames (BBFRAMES) to the buffer and send them out. BBFRAMES are connected to ethernet on the A53 side. This will achieve our original Phase I goals. Wally Ritchie leading efforts on the modulator and the interfaces so we can integrate the existing FEC code. 

#### Remote Labs 9 December 2020

Video report from Remote Lab West available here:

Video shows unpacking and deployment of the logic analyzer accessory for the mixed-signal oscilloscope. Device under test is an RC2014 and the signal inspected was RS232. Some concern here because we can get single characters and short bursts perfectly, but longer bursts of RS232 are not successfully decoded. Nick and others have given advice and it will be followed up on.

Signal generator for Remote Lab West expected Friday 11 December 2020. Remote Lab East has their signal generator with the upgraded clock already.

Trenz gear delayed, date TBD. 

#### 9 December 2020 Meeting Notes - Open Lunar Foundation Use of ORI Radio Designs

Participated in a working meeting on how to use ORI's transponder work in the NASA grant ecosystem. Answered questions, shared documents, and took some action items from Open Lunar Foundation. 

#### 8 December 2020 Meeting Notes - Open Lunar Foundation Donor Summit

Attended a donor summit held by Open Lunar Foundation. Answered questions about ORI, P4XT, open source licensing, and how best to use the ORI transponder and ground equipment as a base design for Open Lunar Foundation's efforts to provide solutions for LunaNet and beyond.

Learn more about Open Lunar Foundation at: 

https://www.openlunar.org/

#### 8 December 2020 Meeting Notes - Debris Mitigation, GMAT, and Orbits

Wally Ritchie
Anshul Makkar
Michelle Thompson

**AI:** = Action Items

GMAT stands for General Mission Analysis Tool. This is an open source framework from NASA that allows high-fidelity mission planning. Find more information about this tool here:

https://opensource.gsfc.nasa.gov/projects/GMAT/index.php

Our LEO-to-GEO GMAT models by Achim Vollhardt can be found here:

https://github.com/phase4space/p4xt/wiki/General-Mission-Analysis-Tool-%28GMAT%29-Scripts-and-Explanations

The LEO-to-GEO GMAT models shows what we need to do to get to GEO on our own. They allow us to do a trade study between motoring to GEO from LEO vs. paying for a launch to GEO. In both cases, we need to model the GEO-to-disposal orbit, which is one of the things Anshul Makkar is working on. 

There are multiple variables to consider when comparing LEO-to-GEO  against straight-to-GEO, including:

1) debris mitigation concerns because spiraling up through what may be very large LEO constellation may raise objections, where straight-to-GEO does not, at increased launch expense.

2) the capability cost to LEO-to-GEO due to the larger amount of space required for fuel. 

3) increased radiation exposure of a LEO-to-GEO spiral, which drives up cost and potentially capability. 

Anshul is creating a GMAT mission to model desired orbits for P4XT. He had some questions about Debris Mitigation, GMAT, and the impact on orbits. Here is a summary of the discussion and the resulting action items and goals. 

Anshul has been working through some examples to learn GMAT and has had success. He came to the point where he needed to know more about the parameters.

For Anshul's initial round of work, we will model from GEO delivery to disposal orbit. 

We currently refer to this as "Straight to Graveyard". 

The disposal orbits are 250 km above and below GEO. 

The upper stage of the launches we expect to be able to take advantage of deliver payloads 50 km above or below GEO. The final maneuvering is typically done by the primary payload after separation from the final stage. This orbit, 50 km out, is called the "maneuvering zone". 

While we would like an equatorial disposal orbit, we can handle inclinations.

**AI:** Wally to provide Anshul a paper about some stable orbits available in disposal.

**AI:** Wally to send Anshul an edition of a good book resource on orbital mechanics. 

With this GMAT mission creation, we will have three line elements (TLEs) that will enable ground station tracking modeling in currently available software. 

**AI:** GMAT animations will be created to show a train of 4 payloads for global coverage. 

The advantages to Straight to Graveyard are significant.

1) With a GEO-to-dispoal, we do not have to have the estimated 2 lbs of Iodine thruster fuel for a LEO to GEO orbit, modeled previously by Achim. 

2) We do not suffer the wear and tear a LEO to GEO mission incurs. 

3) We can use the saved space for more and better batteries, which increases mission life. 

Given the reduced stationkeeping requirements of disposal orbits, we may be able to use open source thruster technology such as AIS work to maintain attitude.

The disposal orbit does require some tracking. However, it is slow. It also provides additional DX opportunities for operators. Path loss will vary more. Anything below 20 to 15 degrees elevation is challenging. 

**AI:** Anshul to use existing GEO orbits and modify this mission with a burn to disposal to achieve the simplest Straight to Graveyard mission presentation.

**AI:** Anshul to present his work.

debris_mitigation Slack channel created for discussion, and relevant foundational documents have been shared there. 


#### Virginia Tech Industrial Advisory Board Meeting Report
Open Research Institute attended our first Virginia Tech Industrial Advisory Board Meeting on 20 November 2020. The meeting was attended by over 40 representatives from industrial, academic, amateur, and open source communities. The goal of the Industrial Advisory Board is to improve Virginia Tech's ability to educate students for roles in space exploration, science, technology, regulation, and management. 

**Action items:** prepare 2-3 slides about ORI and our mission on the Industrial Advisory Board. Open source regulatory advancements, positive effect on commerce when used appropriately, and the improvement in educational outcomes are the communications goals for the slide deck. 

#### High-Level Discussion on Thermal and Radiation 

Action Item closed: Thermal Desktop license successfully installed on a FlexLM server donated to the cause by the power of KN6NK. 

Current status: having trouble getting the license from the server to the local installation. 

**New Action Item:** Tutorials completed using this software. 

Mike Murphree requested a mission plan and expectations on the radiation environment as soon as possible.

Mike Murpree requested resource utilization of the Xilinx parts in order to compare against other potentially more radiation tolerant families of parts. 

Michelle to provide documentation on the block diagrams and architecture documentation. 

#### Trello Boards up and running
We are using Trello for task management. Plenty going on! 

Join Phase 4 Ground Trello board:
https://trello.com/invite/b/REasyYiZ/8de4c059e252c7c435a1dafa25f655a8/phase-4-ground

Join Phase 4 Space Trello board:
https://trello.com/invite/b/GRBWasqW/1336a1fa5b88b380c27ccf95d21fec79/phase-4-space

#### AmbaSat Inspired Sensors

Account at Wells Fargo set up and dedicated funds from ARDC deposited.  


#### Ham Expo 2021 Participation
ORI will present at and be part of an exhibit at the Ham Expo 2021. Details about the event here: https://www.qsotodayhamexpo.com/ 
**We will be using this event as a deadline for transponder work.** We will demonstrate functionality complete by March 2021 at the show. 

#### HamCation 2021 Participation
We will participate in HamCation 2021. This is a virtual event. We have 45 minutes available for presentations. HamCation wants unique, fun, engaging, interactive events. This is a wonderful opportunity for us. Message from organizers after we committed: "We don't have a schedule yet. Plan on 45 minutes for the webinar with a 15 minute break between. Please provide a topic for the presentation with short description that will be posted. Thank you for offering."

Topics for presentation and short descriptions need to be drawn up. We could do a competition, quiz bowl, live demo, technical presentation, contest, or anything of the sort. 

#### Regulatory Presentation
The report is called "Minimum Viable Product" and the Debris Mitigation activities fold into this presentation. Version 1.2 received from Jan King on 7 December 2020. 

