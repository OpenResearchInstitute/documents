# FutureGEO Workshop Memo

A FutureGEO Workshop was held 19 September 2025. The event was organized by AMSAT-DL with sponsorship and support from the European Space Agency (ESA). The workshop was immediately before AMSAT-DL’s Symposium and Membership Meeting, which was 20-21 September 2025. 

## Presentations

Peter Gülzow, President and Member of the Board of Directors of AMSAT-DL, opened the workshop, expressing hope for good results. 

Peter described the timeline and progression of payloads from SYNCART to QO-100 to FutureGEO. The QO-100 timeline from 2012 to 2018 was explained. QO-100 had some iteration along the way. In the end, AMSAT-DL provided the specification for custom hardware from Es’Hail. QO-100 is not a “detuned commercial transponder”, as some describe, but is composed of mostly custom circuits. There are some off the shelf components in the system. For example, the traveling wave transformers (TWT) are one of the backups for the commercial functions. 

Volunteer amateurs were unfortunately not involved in the building of the satellite. Peter explained that the entity that builds the host payload makes a tremendous difference in what the payload looks like, how much power is available, and what policies the hosted payload will be operated under. QO-100 was build by MELCO in Japan, and their decisions set the possibilities and the limitations for the QO-100 hosted payload.

For FutureGEO, multiple designs are expected, covering a range of options and systems design theories. 

The 47 degree West footprint shown in slides and online is “a wish”. No launch or orbital slot has yet been chosen. 

Presentations continued with Frank Zeppenfeldt PD0AP, from the European Space Agency Satellite Communications Group.

Frank explained that there is interest from ESA on a follow-up to QO-100. This lead to the formal solicitation as described in ESA ARTES Future Preparation 1A.126. The FutureGEO outreach and community building process started in 2023. Frank admitted that the communications from ESA have not been as frequent or consistent as desired over the past 18 months. Frank highlighted this workshop as demonstrating an improved FutureGEO community and consensus building state of activity.  

AMSAT-DL will help evaluate proposals and is responsible for completing tasks outlined in the ARTES solicitation. 

GEO opportunities are hard to get. It’s is hard to get a slot. As a way to move the process forward, ESA is providing 200,000 Euro through ARTES. This funding includes some amount of prototyping. 

Amateur built payloads are unlikely to fly. But, we must have a number of ideas documented and prototyped so that we are ready to fly something that we want as a community. For example, 18 months ago there was a missed opportunity in the 71-81 GHz band. Ideas need to be developed, and then there will be financing. 

Peter then explained about attempts to get EU launches. This was very difficult. Peter said that not everyone was welcoming of an amateur payload, and that there were complicated and challenging discussions. 

Peter reviewed the objective and scope of the ARTES Statement of Work, and then outlined the progress on Tasks 1 through 3. 

Task 1 was to identify parties and stakeholders in amateur radio that should be reached out to, and to provide basic storage for data from consultations. Also, to provide background and briefing material about FutureGEO. AMSAT-DL set up a GitLab instance for FutureGEO documents and has provided a chat server for participants.

Task 2 work products are an actively maintained discussion forum on the website, documentation of lessons learned with QO-100, documentation describing requirements formulated by amateur community, documentation describing and analyzing the initial payload proposals from the amateur community, including synergies with other amateur initiatives, and an actively updated stakeholder’s database. These parts of the task fall to AMSAT-DL. ESA support in this task will be providing additional contacts of individuals and industry active in the amateur satellite world, initial publicity using ESA’s communication channels, and technical support in assessing payload and ground segment options.

Task 3 is to analyze and consolidate 3-4 big/small HEO/GEO designs. The designs need to be interesting for a broad community and also address the need for developing younger engineers. Technologies considered may include software defined radio (SDR), communication theory, field programmable gate arrays (FPGA) and more. A report on the workshop discussions and conclusions is expected along with a report describing the consolidated satellite amateur missions.

Task 1 has been satisfied. This FutureGEO workshop was part of the process of completing Tasks 2 and 3. 

## Workshop Participants

**Name and Affiliation**
* Thomas Telkamp PA8Z Amateur Operator
* Danny Orban ON4AOD Amateur Operator
* Colleague of Danny Orban (need name)
* Nicole Sehrig Bochum Observatory
* Frank Zeppenfeldt PD0AP ESA
* Ken Easton Open Research Institute
* Michelle Thompson W5NYV Open Research Institute
* Brian Jacobs ZS6YZ South African Radio League
* Hans van de Groenendaal ZS6AKV South African Radio League
* Hennie Rheeder ZS6ALN South African Radio League
* Peter Gülzow DB2OS AMSAT-DL
* Matthias Bopp DD1US AMSAT-DL
* Félix Páez EA4GQS AMSAT-EA
* Eduardo Alonso EA3GHS AMSAT-EA
* Nicolas Nolhier F5MDY AMSAT-F
* Thomas Boutéraon F4IWP AMSAT-F
* Michael Lipp HB9WDF AMSAT-HB
* Martin Klaper HB9ARK AMSAT-HB
* Graham Shirville G3VZV AMSAT-UK
* David Bowman G0MRF AMSAT-UK
* Andrew Glasbrenner K04MA AMSAT-USA

With audio-visual and logistics support from Jens Schoon DH6BB.

With moderation from Joachim Hecker, a highly-regarded science journalist and electrical engineer. 

## Brainstorming Session

Workshop participants then focused on answering questions in a moderated session about the satellite system design of a future amateur radio GEO spacecraft. Specific questions were posed at four stations. Workshop participants divided into four groups. Each group spent 20 minutes at each station. All groups visited each station, in turn. The content generated by the participants at the four stations was then assembled on boards. Participants clustered the responses into sensical categories. Then, all participants weighted the clusters in importance with stickers. 

### Board 1: Mission Services & Overall Architecture

"Your idea for the mission with regards to services offered and overall architecture."

From on-site discussions:

Multiple antennas with beamforming. 

Downlink (analog) all antennas? Beamform on the ground.


Physics experiment: measure temp, radiation, etc. Magnetometer. 

Downlink in beacon. 

For schools.

Something like Astro Pi, coding in space (put data in beacon). 

Beacons are very important for reference for microwave. Beacons are good! 24GHz and higher, 10 GHz too. 

GEO-LEO multi-orbit communications. In the drawing, communications from LEO to GEO and then from GEO to ground are indicated with arrows. 

Doppler and ranging experiments.

Bent pipe and regenerative capability. 

Store and forward capability? 

Sensor fusion from earth observation, cameras, and data collection.

Multiple bands in and out, VHF to 122 GHz or above. 

Inter-satellite links: GEO to GEO, GEO to MEO, GEO to LEO

Education: Still images of Earth, data sent twice in 2-10 minute period. High resolution? 

Propagation: greater than or equal to 24 GHz. 

Handheld very low data rate text service.

Asymmetric low data rate uplink, traditional downlink.

“Aggregate and broadcast”. 

Cannot be blocked by local authority. 

Use Adaptive Coding and Modulation (ACM) to serve many sizes of stations. Measure SNR, then assign codes and modulations. 

Flexible band plan, do not fix entire band, leave room for experimentation. 

From online whiteboard: 

One sticky note was unreadable in the photograph. 

Educational easy experiments requiring receive only equipment. 

Same frequency bands as QO-100 to re-use the equipment. 

Have a wideband camera as part of the beacon. 

Maybe allow nonlinear modulation schemes. 

Keep in mind “Straight to Graveyard” as an orbit option. Look not just for GEO but also MEO or “above GEO” drift orbit. 

Look at lower frequency bands (VHF, UHF, L-band). 

Make the community more digital. 

We should have a linear bent-pipe transponder. 

Enable Echolink type operations.

For emergency communications it would be useful to be able to pass text-based messages including pictures. Having more bandwidth helps for faster speeds. 

We need telemetry, especially for working with students. 

Power limitation? 

Clustered topics:

Beacons

Coding (like Astro Pi)

Intersatellite links

Telemetry/Sensors

Text and image facilities for emergencies

Near-GEO options for orbits

Adaptive coding and modulation

Bands: transmit 5 GHz 24 GHz and receive 10 GHz 24 GHz 47 GHz 76 GHz 142 GHz

Ranging experiments

Bent pipe or regenerative (including mode changes input to output)

### Board 2: Payload & Antenna Subsystem Platform

"Your idea for the payload and antenna subsystem, and their platform accommodation requirements."

From on site discussions:

Phased Arrays: 

Simple, fixed, e.g. horn array

Electronically steerable

Switchable

User base:

Large user base at launch with 2.4 GHz uplink 10 GHz downlink.

Good user base at launch with experiments. 


Use the frame of the solar cells for HF receive. 

Distributed power amplifiers on transmit antennas. 

Array of Vivaldi antennas allows multiple frequencies with same array.

Camera at Earth “still” 1 image every 2 to 5 minutes. Camera at satellite for “selfie sat” images. AMSAT-UK coll 2012? 

5 GHz uplink and 10 GHz downlink at the same time as 24 GHz uplink and 10 GHz downlink. 76 GHz 47 GHz beacon or switched drive from FPGA core (transponder). 

Non-GEO attitude control? GEO 17 degree beamwidth. 

ISAC integrated sensing and communications. For example, 24 GHz communications gives free environmental and weather information. 

Keep in mind different accommodation models/opportunities. 16U, almost-GEO, MEO, very small GEO. 

Optical beacon laser LED.

PSK telemetry. 

Spot beam global USA + EU?

Uplink 10 GHz

Downlink 24 GHz, 47 GHz, 76 GHz

132 GHz and 142 GHz? 

From online whiteboard:

If we need spotbeams especially at the higher frequencies we should have multiple and/or be flexible. 

24 GHz uplink meanwhile is no more than expensive (homebuilt) transverter 2W, 3dB noise figure, approximately 400 Euros, ICOM is meanwhile supporting also 10 GHz and 24 GHz. 

Beacons for synchronizing

Cameras: maybe one covering the Earth and one pointing to the stars (for education). Attitude calculation as a star tracker. Space weather on payload. Radiation dose or SEU?

On a GEO satellite we should not only have 12 cm band but for instance also the 6 cm band (WiFi) close by makes the parts cheap. For example, 90 watt for about 400 Euros. 

We should have as back at AO40 we should have a matrix. For example, multiple uplink bands at the same time combined in one downlink. 

Maybe get back to ZRO type tests. 

Inter satellite link would be nice.

Higher frequency bands: use them or lose them. 

Linking via ground stations makes sense for Africa being probably in the middle of GEO footprints. 

One note was unreadable in the photo, but it starts out “beacon on the higher frequency bands would be interesting as a reference signal for people”

Clustered topics:

Phased arrays.

Large user base at launch from 2.4 GHz uplink and 10 GHz downlink. Good user base at launch from experiments. 

Use frame of the solar cells for HF receive. 

Keep in mind different accommodation models/opportunities. 16U, almost-GEO, MEO, very small GEO. 

Camera for education

Education at lower level such as middle school (12-14 years old). 

ISAC: Integrated sensing and communications, for example 24 GHz communications gives free environmental and weather information. 

Transponders and frequencies. 

### Board 3: Ground Segment Operations & Control

"Your idea for the ground segment for operations and control of the payload, and the ground segment for the user traffic."

From on-site discussions: 

For hosted payloads, you have less control. For payloads without propulsion, there is less to control. Payloads with propulsion you have to concern yourself with control of the radios and the station position and disposal. There is a balance between being free to do what you want with the spacecraft and the ownership of control operations. This is a keen challenge. Someone has to own the control operations. 

If you are non-GEO, then 3 or more command stations are required. Payload modes are on/off, limited by logic to prevent exceeding power budgets. Control ground station receives data (for example, images) and sends them to a web server for global access. This expands interest. 

GEO operations may need fewer control operators. HEO (constellation or single) may need more. 

Redundancy: multiple stations with the same capabilities. 

Clock: stable and traceable (logging). For example, multi band GPSDO with measurement or White Rabbit to a pi maser?

Distribute clock over transponder and/or lock transponder to clock. 

Open SDR concept, that the user can also use: 

Maybe a Web SDR uplink

Scalable

Remote testing mode for users

Payload clock synchronized via uplink - on board clock disciplined to uplink beacon or GPS. Payload telemetry openly visible to users. Encryption of payload commands?

From online whiteboard:

Allow also an APRS type uplink for tracking, telemetry, maybe pictures, maybe hand-held text based two-way communications, etc. Which suggests low-gain omni-directional antennas. 

Ground control for a GEO especially with respect to attitude will most likely be run 24/7 and thus hard for radio amateurs. 

If we are using a GEO hosted payload then ground control of the satellite would be provided by the commercial operator. 

If we want to have full control on the the payload such as the beacons: on QO-100 on the wide-band transponder we are limited as the uplink is from the commercial provider. 

We should have some transponders with easy access (low requirements on the user ground segment) but it is ok to have higher demands on this on some others (like the higher GHz bands). 

We will need multi band feeds for parabolic dishes. 

Clustered Topics:

We want telemetry!

We should have some transponders with easy access (low requirements on the user ground segment) but it is ok to have higher demands on this on some others (like the higher GHz bands). 

We will need multi band feeds for parabolic dishes. 

Ownership and planning of payload control.

Redundancy: multiple stations with the same capabilities. 

Clock: stable and traceable (logging). For example, multi band GPSDO with measurement or White Rabbit to a pi maser?

Distribute clock over transponder and/or lock transponder to clock. 

Open SDR concept, that the user can also use: 

Maybe a Web SDR uplink

Scalable

Remote testing mode for users

### Board 4: User Segment

"Your idea for the user segment."

From on-site discussions:

Entry-level phased array. 

Look at usage patterns of QO-100 for what we should learn or do. 

Capability to upload TLM to a central database. 
The user segment should allow us to start teaching things like OFDM, OTFS, etc. 

Easy access to parts at 2.4 GHz, 5 GHz, 10 GHz, 24 GHz. 

Broadband RX (HF, VHF, UHF) for experiments

LEO satellite relay service VHF/UHF

Single users: existing equipment makes it easy to get started. Low complexity. Linear.

Multiple access: 

Code Division Multiple Access (CDMA), spread spectrum, Software Defined Radio + Personal Computer etc.

Orthogonal Frequency Division Multiplex (OFDM), with narrow digital channels. 

Cost per user

Experimental millimeter wave

Something simple, linked to a smartphone, “Amateur device to device (D2D)” or beacon receive.

School-level user station in other words, something larger. 

Entry-level off the shelf commercial transceivers. 

Advanced uses publish complex open source SDR setups. 

Extreme low power access: large antenna on satellite? ISM band? (Educational and school access)? “IoT” demodulator service

A fully digital regenerating multiplexed spacecraft: Frequency division multiple access uplink to a multi-rate polyphase receiver bank. If you cannot hear yourself in the downlink, then you are not assigned a channel. Downlink is single carrier (DVB-S2). 

Mixing weather stations and uplink (like weather APRS). 

Dual band feeds exist for 5/10 GHz and 10/24 GHz. We are primary on 47 GHz. Why not a 47/47 GHz system.

Keep costs down as much as possible. 

From online whiteboard:

Linear transponder for analog voice most important but we should also allow digital modes for voice and data in reserved segments of the transponder. 

Multiple uplinks combined in a joint downlink (as AO13 and AO40). 

Experimental days. 

Tuning aid for single sideband (SSB) audio. 

Segment to facilitate echolink type operation using satellite in place of internet. 

Allow low-power portable operations. 

Allow experimental operations. For example, on very high frequencies. 

Store and forward voice QSOs using a ground-based repeater and frequencies as MAILBOX (codec2 or clear voice + CTSS). 

A codec2 at 700 bps/FSK could permit to reuse UHF radios using the microphone input and a laptop. We are exploring this using LEOs. 

Depending on the available power we may want to allow non-linear modulation schemes. 

We should support emergency operations. 

Depending on the platform, we may want to rotate operational modes. 

Clustered topics:

Simple (ready made) stations: off the shelf designs and 2.4 GHz 5.0 GHz 10 GHz 24 GHz 47 GHz

Sandbox for experiments and testing new modulations and operations. Just have to meet spectral requirements. 

## Workshop Retrospective:

A workshop retrospective round-table was held. QO-100 experiences were shared, with participants emphasizing the realized potential for sparking interest in both microwave theory and practice. 

The satellite enabled smaller stations and smaller antennas. It is unfortunate that people building it were limited in speaking about the satellite performance due to non-disclosure agreements. QO-100 has enabled significant open source digital radio components, such as open source DVB-S2 encoders that are now in wide use. Educational outreach and low barriers to entry are very important. $2000 Euro stations are too expensive. The opportunity for individuals to learn about microwave design, beacons, and weather effects is a widely appreciated educational success. 10 GHz at first seemed “impossible” but now it’s “achievable”. QO-100 had a clear effect on the number of PLUTO SDRs ordered from Analog Devices, with the company expressing curiosity about who was ordering all these radios. GPSDO technology cost and complexity of integration has come down over time. Over time, we have seen continuous improvements in Doppler and timing accuracy. Building it vs. Buying it is a core question moving forward. A high level of technical skills are required in order to make successful modern spacecraft. Operators clearly benefited from QO-100, but we missed out on being able to build the hardware. Builder skills were not advanced as much due to the way things worked out. “What a shame we didn’t build it”. No telemetry on QO-100 is a loss. Design cycle was too short to get telemetry in the payload, and there were privacy concerns as well. Building QO-100 was an expensive and long process. Mitsubishi took this workload from us. Moving forward, we should strive to show people that they have agency over the communications equipment that they use. We are living in a time where people take communications for granted. There is great potential for returning a feeling of ownership to ordinary citizens, when it comes to being able to communicate on the amateur bands. 

## High-level Schedule and Goals:

Documentation of the workshop and “Lessons Learned from QO-100” will be done starting now through the end of 2025. Prototypes are expected to be demonstrated in 2026.

_Edited by Michelle Thompson W5NYV_
