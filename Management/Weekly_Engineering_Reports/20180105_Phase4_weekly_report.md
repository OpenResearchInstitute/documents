Phase 4 Ground home page https://phase4ground.github.io/

Welcome to our weekly report! We're back after a great holiday break!

We are Phase 4 Ground and our mission is to implement an open source version of the DVB-S2 and DVB-S2X and Generic Stream Encapsulation (GSE) protocols for amateur radio, for both space and ground. The project includes the radios and a central server, or Groundsat. It's named Groundsat because it's a satellite simulator on the ground, providing the same functions a broadband microwave payload would in order to create a network. 

All the Digital Video Broadcasting protocols that we are working with can be found for free at https://www.dvb.org/ and from links on our homepage.

Note that GSE allows any digital data to be transmitted. We are not implementing a system limited to MPEG video. 

DVB world conference is coming up! Anyone near Warsaw? That's where it's at for 2018.

Our reference design is in GNU Radio and we have some of the blocks done. We need plenty more and upcoming videos will go into detail for each one. 

Learn all about GNU Radio here: https://www.gnuradio.org/

Engineering for Phase 4 Ground is done primarily on our email list and Slack accounts. 

We have a YouTube playlist at https://www.youtube.com/playlist?list=PLavdGnjBLuiX97DAKk32NJ1bCF1a0cv01 that includes our video reports and videos that are of use or interest to Phase 4 Ground. Please subscribe and let us know what you'd like to hear about most. 





Phase 4 Space home page https://phase4space.github.io/

Phase 4 Space is a very new open source public domain project for broadband microwave amateur radio satellites because we want a lot of payloads to talk to! We'll be using two wonderful open source resources to start. AO-10 blueprints and UPSat, the open source satellite currently operational, from Libre Space Foundation. 

To volunteer directly for either, visit https://www.amsat.org/volunteer-for-amsat/ or send an email w5nyv@arrl.net to get started!





Please welcome Pierros Papadeas to Phase 4. 

He is a program manager at Libre Space Foundation. This is a non-profit organization developing open source space technologies. They were founded in 2014 in Greece, but run global operations right now.

Some of their headline projects:

SatNOGS, a global open source ground station network. Non-profit, open by design (APIs etc), run by a global volunteer community. Active development, extensive stack of multiple technologies. 30+ active ground stations around the world right now with more than 10.000.000 packets gathered from 200+ satellites.

UPSat, the first open source software and hardware satellite. Developed as part of the QB50 constellation, with all submodules designed from scratch and coded as open source projects. Satellite is currently in orbit and operational. This is a wonderful design for us to start working from to create a microwave broadband satellite design. https://upsat.gr/

Libre Space Foundation is also active in various other areas. They have invested into PocketQube reference designs (expected to be delivered 2018Q1) and are assisting many satellite teams with TC&C and delivery. 

Libre Space Foundation also has rocketry and educational outreach activities as well, mainly in Greece. 

SATNOGS repository here! https://gitlab.com/librespacefoundation/satnogs/gr-satnogs




Ham Radio Workbench podcast interviewed us on 29 December, and recorded our recent IEEE talk about open source satellites in San Jose, CA in mid-December. Both recordings can be found at http://hamradio360.com/index.php/2018/01/01/ham-radio-workbench-amsat-phase-4b-ground-station-design/ 

A big thank you to George and all the volunteers for the Ham Radio Workbench podcast. If you don't subscribe, then please consider doing so. They are supportive, positive, and friendly and present technical topics in an accessible way. 




We've been invited to participate as an amateur radio exhibit at IEEE Radio Wireless Week 14-17 January in Anaheim, CA. https://radiowirelessweek.org/ I signed up for the cubesat workshop as well, and will give a full report about that! 



We spent some time putting together some proposals for AMSAT that address new challenges that the ITAR payload projects are facing. New data security regulations have gone into effect, and there need to be some changes to the way documents and email are handled within AMSAT engineering. 

Here is a link to a proposal for SVN server replacement with GitHub Enterprise: 
https://github.com/phase4ground/documents/blob/master/Papers_Articles_Presentations/Slide_Presentations/20171208_GitHubEnterpriseProposal.pdf

This GitHub Enterprise proposal has links to documents that explain the new regulations. Here they are for quicker reference:

Additional regulations went into effect at the end of December 2017      https://www.law.cornell.edu/cfr/text/48/252.204-7012
Information security standards and guidelines can be found here      http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171.pdf

Controlled Unclassified Information (CUI) compliance is the minimum standard. 

Web conferencing software and email servers need to be brought into compliance as well. There are some options here and the discussion is ongoing. If you have experience and can give input on CUI compliance, then AMSAT engineering can get back to engineering much faster and more fun can be had by everyone!






For the new year, we have a lot of major milestones. We also have a schedule. I'm committed full-time through January 2020. At that time, I hope we are clearly done or almost so. If not, we will take stock, thoroughly document, and then decide what to do. The goal is to finish an open source implementation of DVB-S2 and S2X for the amateur satellite service and terrestrial operations. We have a lot to do and everyone is welcome to join. 






Phase 4 Ground has a badge project. An early version, with a very fun gamer-oriented form factor, will be available for sale very soon. These badges are based on the Bender Badge framework. 

https://hackaday.io/project/19121-andxor-dc25-badge

The first version is scheduled for the JoCo Cruise in February. 

https://jococruise.com/

The radio-themed version, called the Trans-Ionospheric, is scheduled for Dayton. The retro styling is based on the Zenith Trans-Oceanic and it will have custom games and surprises. In the future, these badges can show Phase 4 Ground radio status, such as channel health and acquisition status, through a bluetooth connection, and are customizable and hackable. The badge effort is a very fun part of the project, but it also serves a purpose. It's given us an opportunity for many of us to work together on an electronic and software design for the first time, iron out toolchains, develop style and creative expressions, improve communications and get experience managing bills of material and build schedules. 






Some of us are putting together SATNOGs stations and seeing what needs to be done in order to get them working for Phase 4 Ground. The baseline receiver is an RTL-SDR, but the relatively small bandwidth of that device means it will only work for lower symbol rate deployments of Phase 4 radios. For the full 10MHz, you'll need more RF bandwidth. Fortunately there's a lot of choices and we'll be setting up our stations to test them out. The baseline controller is a Raspberry Pi, and that may not have enough horsepower to decode our forward error correction, but we are making progress on that as well. Being part of and supporting the SATNOGs network sounds like a step forward, and because all of this is open source, we have the opportunity to adapt an existing, working, quality design to our needs. 




Not a bad report for what we did over winter vacation! 

Have a great weekend and see you on Monday. 
