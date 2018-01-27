
5GHz RF Update and the second part of the IEEE Radio and Wireless Week report from Phase 4 Ground.

Video at https://youtu.be/gY0IQsppSI4

TWIoS Session 1! The theme was Next Generation Concepts for Space and was chaired by Charlie Jackson from Northrup Grumman and Thomas Ussmueller from the University of Innsbruck. If you've been hanging out with us for a while then you know we already attended an entire class about commercial airline backhauls, so we skipped this one and had a civilized breakfast instead. This application is entirely commercial and locked down, and follows the design pattern of the subscriber or receiver being the entity that's very carefully controlled. We're already doing everything right in this implementation that we can be doing. As you know, in amateur radio, the receiver isn't the thing we are controlling. It's the transmitter. Anyone can receive, but we have only licensed transmitters. This reversal of some of the assumptions makes working through and adapting communications protocols so rewarding. 

TWIoS Session 1 talk 2 was a compelling and meaningful application of satellite communications link supporting a vital infrastructure project to a very marginalized and overlooked community in the Himalayans. The remote monitoring is for a small hydroelectric plant. The lessons learned here are very relevant. Maintenance and ease of use, pay as you go, sustainable and durable design, listening to the community and understanding what they really need? This came through loud and clear. The satellite technology in this case was a very small part of the presentation. The point of this talk was to show how satellite communications can provide remote monitoring and internet of things support. 

TWIoS Session 1 talk 3 was very relevant to Phase 4 Space. "Design Challenges of a Highly Integrated SDR Platform for Multi-Band Spacecraft Applications in Radiation Environments", by J. Budroweit and his team from Brandenburg University of Technology. Guess what they did? They took the AD9361, which is the same RFIC used in the Ettus USRP 300 series, and they zapped the snot out of it with radiation. They also got results for the voltage regulators. Voltage regulators are a hard part. As radiation goes up, voltage goes up, things stop working. So, quote, "At a total ionizing dose of 7.5kRad, the regulator outputvoltage in these tests increased continuously until the voltage level reaches the maximum specified input voltage of the following powered devices. Other sub-voltage-regulators in the system show a similar ionization effects behavior and has been classified as medium-critical for further development activities.

Everyone in our circle pretty much knows that the 7000 series Zync processors are going to work out as radiation tolerant devices, but characterizing the RFIC was something on our radar and Brandenburg University delivered. The result? For the RFIC, at a dose of 17.5kRad, the test-setup was modified with shielding-blocks for continuous irradiation only for the RF transceiver part. The AD9361 showed good robustness against this ionizing dose. No degradations were observed. How cool is that? Oh, and then? Then they amped it up to 25kRad and it still didn't care. 

The goal of this team is to put a highly integrated general SDR platform for multi band RF applications in space, using a state of the art transceiver. In orbit verification is expected on the S2TEP launch in 2019, with testing in 2020. This is a 35kg MicroSat. This is right up our Careful COTS alley on Phase 4 Space. Want to help? Write me and let's use these results to get a design together!


TWIoS Session 2 in the afternoon was Radiation Considerations for Space, chaired by chaired by Thomas Ussmueller from the University of Innsbruck and Charlie Jackson from Northrup Grumman. 

TWIoS Session 2 talk 1 was a circuit design for a radiation tolerant 2.4 GHz Synthesizer Based on COTS Components. Motivation is the move away from large bulky satellites to commercial commodity smaller satellites, like CubeSats, has increased the use of WiFi. Commercial wireless technology in space needs a good synthesizer that is radiation tolerant, and the design discussed here is a more durable synthesizer built up from discrete carefully chosen COTS components. 

There's a lot of Careful COTS discussed at this conference. If you're not familiar with that term, it means that you construct your circuit from radiation tolerant commercial off the shelf components that were not specifically designed from space, and then you test your design at the system level, possibly putting in redundancy and other mechanisms to recover from radiation induced events.

Careful COTS is in contrast to the much more rigorous and expensive "designed for space from the beginning heavily integrated solution" that we call radiation hardened. 

This synthesizer isn't terribly high performance, but it works. 

TWIoS Session 2 talk 2 was about JICG MOS Transistors for Reduction of Radiation Effects in CMOS. This is manipulating things at silicon level, so not exactly in our ballpark. Yet. 

TWIoS Session 2 talk 3 was Reflectionless Filters for miniaturized space applications. This is a class of filters that are very small, therefore possibly of use in CubeSats. Inductors don't obey Moore's law, it turns out, so some circuits can be miniaturized much more easily than others. 


I went to a 3d printed antenna track and a six port structure track and found out a lot of really good information on 122GHz RF. If you're into any of those things, let me know and we'll talk more. 


So, wow, that was a lot of satellite stuff! We made a lot of contacts and have solid offers of collaboration that I'm going to do my very best to take full advantage of. Check out the UWE-3 papers in the research papers repository at Phase 4 Space, and the AD9361 results. We had a great time at the ham demo and promoted AMSAT and amateur radio and made lots of friends. Well worth doing, and I think we'll see plenty of results. 

Next year, Radio and Wireless Week will be in Orlando, Florida, so if you are in that area and can help demonstrate amateur radio and amateur satellite, the chair of the event wants you to come! There's a very large amount of enthusiasm and support for amateur radio at this and other IEEE MTT-S events, so think about it and let's start planning now!



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


