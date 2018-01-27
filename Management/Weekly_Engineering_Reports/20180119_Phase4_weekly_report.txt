https://youtu.be/eD5P4tHIb9w

Phase 4 Ground weekly report :+)

IEEE Radio and Wireless Week was held in Anaheim, California from 14 - 17 January 2017. RWW is an annual technical conference from IEEE, and is sponsored primarily by Microwave Theory and Techniques Society. It consists of five different co-located topical conferences. One of those conferences was the Topical Workshop on The Internet of Space or TWIoS, with two sessions. There was also a CubeSat workshop! 

This conference was great! Here's an overview of the speaker lineup for the workshops.  

The first workshop was about digital pre-distortion. Digital pre-distortion is a technique used to increase the efficiency of Power Amplifiers. By reducing the distortion created by running Power Amplifiers in their non-linear regions, Power Amplifiers can be made to be far more efficient. Radio power amplifiers tend to become more non-linear as their output power increases towards their maximum rated output. Pre-distortion is a way to get more usable power from the amplifier, without having to build a larger, less efficient and more expensive amplifier. You can do this in the analog domain, or the digital. This workshop was about digital pre-distortion techniques. We need to know about this because it will help us. I have all the papers and the workbook so if you're working on DPD get in touch for these resources.


Another workshop was Solid State Amplifiers for Space. Here's the lineup and I have the workbook, but it was at the same time as the digital pre-distortion, so I didn't attend in person. Same deal, I have papers and the workbook so get in touch if you want to work on this. 

The big workshop draw for me was the next day. The Microwave, CubeSats, and Small Satellites workshop. Here's the summary and the lineup. Microwave and mmWave CubeSats are the thing, so we're definitely on the right track. Being opportunistic and ready to deploy communications and scientific experiments in the rapidly growing CubeSat market are going to be vital for keeping in the mix going forward. 

Every slide that I saw for CubeSat launches has an almost exponential curve, with most of that curve taken up with commercial operations. The number of launches for educational and scientific missions is expected to be relatively flat. With more and more Universities and institutes putting together CubeSat programs, where does that leave amateur and educational efforts? Not all CubeSats are LEO, but most of them are. What it means to me is that things are about to get a lot more competitive, as the pressure on launch agencies to increase capacity and the competition for launches is expected to dramatically increase over the next two years. 

The introduction to the workshop was Challenges and Opportunities for the Internet of Space. The premise that Microwave CubeSats and Small Satellites need to meet the needs of the Internet of Things (Internet of Space) was a constant theme for the entire conference and for this workshop especially. There are a lot of questions about IoT, and 5G for that matter. Example one: Aircraft sensors, with data aggregation in the air and the results communicated via satcom, to make in-air decisions between gates for unscheduled maintenance decisions in order to keep aircraft continuously healthy and monitored. Example two: remote monitoring of industrial vehicles, where satellite makes sense. 

CubeSats with phased arrays, CubeSats that avoid data collisions, CubeSats that have enough power for desired payloads (like 10-20 watts), CubeSats that have attitude control, CubeSats that are reliable with COTS devices. Example: Iridium used COTS devices for large parts of the system. Lifetime requirements, use cases, sustainable business models, propulsion systems (nano-FEEP mission prepared for launch). Business case, capital expense, launch costs!

This workshop was all about the solutions for these challenges. 

Dr. Klaus Schilling spoke about a standardized electrical interface for CubeSat Bus Interfaces. Download PDF here: http://unisec-europe.eu/standards/bus/

"The success of the CubeSats was based on standardization of geometric dimensions, allowing joint use of launcher adaptors. An important next step in order to be able to exchange boards at subsystem level was a specification and standardization of the electrical interfaces, which is addressed in this contribution." The standard is pretty good, satellites have been successfully launched using this standard, and the advantage is no wiring harness, dramatically reduced assembly time, the ability to swap out failed parts at the last minute, increased reliability, and increased interoperability. 

Dr. Schilling heads up the University Wurtzburg Experimental satellites, or UWE, program. 

http://unisec-europe.eu/missions/uwe-3/

UWE-3 was launched in November of 2013. The main mission objectives of UWE-3 are to demonstrate the use of a real-time miniature attitude determination and control system on-board the satellite, using a variety of sensors, magnetic torques and one reaction wheel. To establish a robust base for a series of future satellites, UWE-3 additionally features an advanced modular and flexible architecture of the pico-satellite bus, in order to increase robustness, reduce mass and add reliability to the overall system. One example is the redundant On-Board Data Handling core module of UWE-3, which is tolerant to SEU’s, capable of repairing its own memory and therefore able to recover the satellite and ensure safe operations. It's still up there working, and handles SEUs and latchups and recovers. 

Only COTS parts were used, but fault detection, identification, and recovery by software and watch-dog timers have ensured a level of reliability. Their data handling methodology is achieved through redundancy with mutual supervision and recovery, redundant serial flash, high precision real time clock, and a quad-redundant power cycling unit. 

UWE-3 mission involved lots of amateur radio operators and Dr. Schilling is very familiar with AMSAT-DL and highly complimentary of amateur effort and assistance. 

The attitude determination and control system has worked well enough to where they feel ready to try some formations. Formations are when the satellites communicate with each other and adjust their attitudes in space to maintain distance and altitude without intervention from the ground. The range is up to 100km with a patch antenna on 10.475GHz. The mixer, IF filter, modem, reference clock, synthesizer, PA, LNA, RF filter, antenna etc. fit on a 40 by 20mm PCB.

Attitude control systems on UWE-3 included multiple magnetic field sensors, redundant gyroscopes, and interfaces with high precision sun-sensors. The attitude is estimated using an isotropic Kalman filter while magnetic torquers are used for efficient board pointing. This is also available in combination with reaction wheels. The board interfaces directly via the UniSec CubeSat standard and is fully updatable in orbit. There's a scripting tool embedded in a sandbox environment on board, so that you can test the algorithms and maneuvers at low risk and effort. It can do detumbling, pointing, and spin stabilization, even at 1U. This is so cool. 

UniSec has been extended past the electrical standard. There is also a Satellite Development Board that can serve as an electrical ground support equipment after launch. Standardized testing came up as well. UniSec standard satellites can be assembled in about an hour, which reduces the cleanroom time and makes it easy to upgrade or produce larger quantities. 

So all of this was really exciting to me, because it means that the tasks of attitude control, power distribution, and communications are all successfully being done and we can do it too. If we become familiar with this University project, and others like it, and build on it, then we can be way further ahead on amateur spacecraft design than we thought we were at the GOLF meeting at Symposium. 

Upcoming event:
https://sites.google.com/site/naass2018/

That was just the first talk. The next one was about super awesome umbrella folding microwave reflector mesh antennas that pop out from the cubesat and give you real gain. In between that and attitude control, you can do Ka-band in a CubeSat with 42dBi. It needs 1.5U of space. This is intended for like 6U CubeSats. 

But wait, there's more. He talked about the ReflectArray which is on the InSight mission that is delivering MarCo CubeSats to Mars for communications relays. Imagine all the benefits of a parabolic dish, but with the convenient packaging of a a flat patch array. Check out more at this link:
https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=3180&context=smallsat

Next was Dr. Mark Bachman CTO of Integra Devices and UC Irvine professor. He talked about how to make structures for mmWave and microwave applications using techniques more often found in the component packaging industry. This was pretty rad. They think it's the right technology for space and they were pretty darn convincing. 

After that was William Deal from some company called Northrup and their demonstration of a 666GHz crosslink for inter satellite communications. 9.5Gbps! They showed off their demo of this data link and wow that's really high up there isn't it?

Steven Riesling From Colorado State University talked about remote sensing systems for earth and atmospheric sciences using small satellites, with a focus on TEMPEST, or Temporal Experiment for Storms and Tropical Systems. These are five identical 6U CubeSats that do repeat-pass mmWave radiometry. They fill in a gap in the knowledge of cloud dynamics between formation and precipitation. It started up for real in 2015 and is supposed to launch in May 2018. They're scanning five frequencies between 89 and 182 GHz. 

The last talk in the workshop was Dr. Ivo Vertat and ground station communications during shared launches. Amateur radio played a big part in this effort because the ground stations operated in the UHF amateur radio band, and hams helped sort things out and provided a lot of support. 


That evening I got to set up a booth in the main hall as an amateur radio demonstration along with two other volunteer demonstration stations from the San Bernardino Microwave Society. I'm a member of that club too, and they are great. If you're near Corona, CA then you have one of the best microwave clubs in the country nearby. Brian Thorson AF6NA and Rein W6SZ were my fellow demonstrators. Jeffrey Pawlan WA6KBL got us in the door with IEEE and supported us the whole way. We showed off microwave band amateur radio to engineers from Italy, Poland, Germany, Austria, Spain, Canada, India and the U.S. all evening. The food was great, the drinks were free, and I showed off the amateur satellite service, AMSAT, 3D printed 122GHz cassegrain antenna prototypes, dual band feeds for Phase 4 Ground, 10GHz elliptical taper 3D printed horns, and told plenty of tall tales. Huge success. Lots of student interest and plenty of awareness raised. 




Phase 4 Ground home page https://phase4ground.github.io/

We are Phase 4 Ground and our mission is to implement an open source version of the DVB-S2 and DVB-S2X and Generic Stream Encapsulation (GSE) protocols for amateur radio, for both space and ground. The project includes the radios and a central server, or Groundsat. It's named Groundsat because it's a satellite simulator on the ground, providing the same functions a broadband microwave payload would in order to create a network. 

All the Digital Video Broadcasting protocols that we are working with can be found for free at https://www.dvb.org/ and from links on our homepage.

Note that GSE allows any digital data to be transmitted. We are not implementing a system limited to MPEG video. 

DVB world conference is coming up! Anyone near Warsaw? That's where it's at for 2018.

Our reference design is in GNU Radio and we have some of the blocks done. We need plenty more and upcoming videos will go into detail for each one. 

Learn all about GNU Radio here: https://www.gnuradio.org/

Engineering for Phase 4 Ground is done primarily on our email list and Slack accounts. 

We have a YouTube playlist at https://www.youtube.com/playlist?list=PLavdGnjBLuiX97DAKk32NJ1bCF1a0cv01 that includes our video reports and videos that are of use or interest to Phase 4 Ground. Please subscribe and let us know what you'd like to hear about most. 





Phase 4 Space home page https://phase4space.github.io/

Phase 4 Space is an open source public domain project for broadband microwave amateur radio satellites because we want a lot of payloads to talk to! We'll be using two wonderful open source resources to start. AO-10 blueprints and UPSat, the open source satellite currently operational, from Libre Space Foundation. 

To volunteer directly for either, visit the AMSAT volunteer landing page https://www.amsat.org/volunteer-for-amsat/ or send an email w5nyv@arrl.net to get started!


