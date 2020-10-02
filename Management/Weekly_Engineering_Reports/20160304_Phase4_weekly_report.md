Flex Report

Paul KB5MU, Bob N4HY, and myself (Michelle W5NYV) traveled to Austin, TX to meet with Steve and Gerald at FlexRadio Systems on 22-23 February 2016. A manufactured radio is one of the solutions that Phase 4 Ground will develop in support of Phase 4B payload, Phase 3E payload, Cube Quest Challenge, terrestrial Groundsats, and future payloads. FlexRadio, as a leading manufacturer of ham radio SDR equipment, approached AMSAT about the possibility of manufacturing Phase 4 Ground radios.

Steve and Gerald and many others at Flex were extremely generous with their time and advice. We talked about a variety of subjects relating to Phase 4 Ground. We introduced the project, showed block diagrams, discussed engineering philosophy and expectations, and shared context.

There were results.

Phase 4 Ground asked Flex to build a small quantity (25) of development boards, based on existing technology from Flex products. These boards will provide enough Flex-centric hardware in order for us to advance down the path of a manufactured solution for Phase 4 Ground. The build is pending the release of private funding. Efforts will be expended to align the Flex hardware builds with another larger order with another organization that requires nearly identical hardware. Coordination of this type greatly reduces risk and cost.

There will be some number of these boards available to Phase 4 Ground developers. We will have a document that will track interest in and possession of the boards, so that everyone can see who has them, and what they're doing with them. 

The meetings at Flex concluded with a resolution to support the Phase 5B Mars Mission. 

Single Antenna Efforts

One of the topics discussed during the Flex meetings was our dual-band feed effort. Having a single antenna was considered by Flex to be a very important requirement, especially for the emergency communication market. 

There are recognized difficulties with a dual-band feed for the frequencies and power levels under consideration. This is an area of active research in Phase 4 Ground, with the challenges being much better described and explained over the past week or so. Here’s an image that might serve to show more clearly what we are concerned about. 

The purple x is the downlink. The blue asterisk is the second harmonic of the uplink. The green triangles are the working limits of the receive LNB we expect to be using. You can see that the second harmonic of the uplink falls within the receive range of the LNB. You can see that selecting different local oscillators doesn’t really help. You can see that moving to a different 5GHz sub-band doesn’t really help, and would require some politicking. So, in order to achieve our goal of having a single antenna solution, we have to confront this signal, and we have to reduce it as much as possible. 

Why do we care so much about something like a dual-band feed? Because based on market research and professional feedback, we must do our best to provide a single dish solution. A dual-band feed is one way to achieve this. It’s not the only way, as Kent Britain WA5VJB is working on a patch plus dish design, and I think several of us are thinking about some expensive phased array techniques. If you have another idea, share it. 

Kent believes that 120dB of isolation would be required in order to declare success, and that a low pass filter at the uplink PA was an obvious part of the solution. Flex radio advised looking into a push-pull amplifier, as this would greatly reduce the second harmonic from the get-go. We have the uplink linear polarization orthogonal to the downlink linear polarization. There is some isolation from that. 

Bill Werner W3EAO proposes an uplink RF chain. He recommends a power amp by CREE CGH55015xxx, which produces 10 watts at 6cm (+40dbm) with the second harmonic expected to be down 20dB at +20dbm. This feeds a pair of Minicircuits LFCN722+ low pass filters, 1.5dB at 6 cm, 38dB at 3cm, 3cm now at -55dBm; 6cm at 5 watts (+37dBm). This goes to DirectiveSystems dual band feed (WB5LAU design) with 70dB isolation twixt 6cm and 3cm ports (at 6cm), and assume 30 dB (at 3cm). Second harmonic is now at -85dBm, 6cm now at -33 dBm. Then, use Minicircuits ZVBP-10R5G+ filter from feed to 3 cm pre-amp. The insertion loss is 0.24 dB and 6cm rejection of additional 52+dB which puts both 5.6GHz and its 2nd harmonic at -85 dBm into the 10GHz pre-amp. He judges this to be close enough. 

He writes, “This design, while not cheap, does give a 5 watt 5.6GHz transmitter (should be more than enough) using a single dish. The use of cross polarization should give about another 10 to 20 dB. Also, need to evaluate why 10GHz pre-amp has such limited dynamic range.”

Kerry Banke N6IZW shared some progress on the dual-band feed effort. He also is working on recruiting an additional person that has expertise in this particular area. If successful, then that would bring the number of people working on the several solutions for single-dish design to five, with Paul Wade W1GHZ also working on a dual-band feed design of his own. Not bad, but there’s still room for more. Paul Wade says to hang in there he’s working on it and will report back soon. 

Kerry Banke writes,
“I ran a test using your LNB to see at what input level in the 11350 MHz range the 10450 MHz starts being affected.

It looks like we need to have the PA second harmonic less than about -70 dBm at the LNB input. I'm thinking I'll build one of Al Ward's dual band feeds to get some first hand experience with the isolation subject. My general leaning at this point is to see if a circular waveguide bandpass filter can be built into the rear section (tube) of the 10 GHz portion of the feed and then  cut the horn  off an  LNB and  directly directly attach the circular LNB guide to the filter output of the feed. I'll also look at a low pass filter for the Tx PA to reduce the 2nd harmonic. I will need to dig through my stuff to see how much power I can generate at 5 GHz. I suspect 5GHz TWT amps can be had for testing.”

He is thinking maybe a low pass filter for the PA and low loss band pass waveguide  filter at the LNB input. 

One of his thoughts is to see if a waveguide post bandpass filter for 10450 MHz can be designed for 3/4" ID copper pipe as part of the dual band feed to reject the 11440 MHz Tx harmonic.

There is always the baseline design of two dishes with two separate feeds. Think of two dishes as the stacked HF monobander approach. You can always do this. 

John Klingelhoeffer, Howie DeFelice, Bill Werner, and several others provided substantial feedback on this mid-week. They raised the possibility of gating the transmitter off during receive, and discussed some numbers to back up this approach. The system is defined as full duplex, but this strategy needs to be kept in mind if we cannot achieve our goals any other way.  

If you have another solution that you don’t see mentioned here, or any feedback at all about any of this, then we are very interested in it! We welcome experimentation, comment, and critique. 


Codec Quality

John WB4LNM brought up something that a lot of us very strongly agree with. Digital systems, not just amateur ones, but commercial ones as well, have been plagued with really crappy codecs. Voice compression allows more money to be made, therefore compressing to the point of pain is worth doing. We do not want crappy voice quality. John interviewed the two codecs we're most interested in using on Phase 4 and provided valuable feedback on what he thought was acceptable quality. 


Air Interface

Discussion continued and expanded on how to achieve adaptive coding and modulation for Phase 4 Ground radios. There are a lot of questions to consider, progress made, and content being collected for revising the air interface document. There are some ideas that have endured for months, and some that are shifting. 

A worthy goal in this area is to reduce the required state in the satellite to zero, whenever possible. In other words, the preference is that no user state is stored the satellite. This reduces the complexity of the satellite code. This is highly desirable. This also means the satellite functions are much more scaleable. This makes the radios on the ground much simpler as well, because they do not have to deal with a complicated satellite. 

So, where do you pay for all this simplicity? You pay in two ways. Each frame must be able to fully explain itself. There is increased overhead in every transmission. 

This overhead is what would otherwise be stored in a “connection object”, or memory bank, or register or whatever, in the satellite. When you say you don’t want to do that, then you, as a frame or packet, have to always be ready to present proper state, or allow that state to be calculated, at any time. In other words, system complexity is reduced because we purchase the simplicity with additional overhead, and quite possibly a more complex protocol. 

Another very large factor in our protocol is that our hardware is not fixed. The protocol must be adapted to intelligently handle any reasonable combination of uplink and downlink capability, and it must be able to do this without burdening the satellite hardware. If the hardware was fixed, then some of what we are talking about doing would not be necessary because one could make assumptions about the ground. Providing this adaptive capability is a challenge, but it is definitely achievable. 

RFNoC Feedback

John Petrich W7FU had some questions and comments for RFNoC. He asks, "Just what part or parts of the Phase 4 (and maybe other phase programs) communications system are you considering using the RFNoC technology?"

Any part that seems like it can be moved to the FPGA from the general purpose processor would be up for grabs as an RFNoC implementation.

This requires us to define the division of labor between the host, or general purpose processor, and the FPGA. We're making progress in this direction, but until we get a flow graph that at least sort of works, we won't know exactly what should be done by RFNoC.  

John explained that his attitude toward RFNoC and similar attempts by amateurs tends to be negative.  He is concerned that committing too much of the program to advanced FPGA technology is a losing proposition when there is a launch deadline pending. He had the following reasons:

1)      Ettus is struggling to get RFNoC going smoothly.  The Discuss USRP Digest is dominated by X310 RFNoC questions. 
2)      SDRstick people affiliated with TAPR:  http://sdrstick.com/  have a product and plan to implement an FPGA product.  Their SDRstick Digest is totally consumed by the struggles to get the SDR ‘front end’ connected to the FPGA module up and running.  Also, they were faced with an 18 month delay at delivery of the promised FPGA that they had committed to using.
3)      I wonder, without any information, how much of the long delay that Flex Radio experienced at releasing their new 6000 series SDRs was because of FPGA “issues”: product delivery delays, programming challenges, etc.

These reasons are very compelling. When we talk about RFNoC, and say that it's developmental, and that people are literally circling the watering hole waiting for fresh meat to dive in and take the first and biggest risks, then you should get the idea that RFNoC really is kind of out there. 

If you weren't already all full up of risk just by working on a space project, then adding in RFNoC would certainly fully subscribe you to the same category of people that jump out of perfectly good airplanes. We will keep talking about this and I will keep talking to people involved with RFNoC. If it becomes obvious that it's worth the risk, learning curve, and processing and efficiency gains, or if our project gets somehow chosen as a test case and fully supported, then it might be worth going all in. For now, this qualifies as something for our R&D and long-range planning departments. 

John also ran into difficulty using the GNUradio DVB-S flow graph on a USRP B100. The USB2 data link will not support the 10 MSPS in the DVB-S transmitter flow graph.  The DVB-S flow graph runs perfectly on USRPs with either USB3 (like the X310) or Ethernet data links, but on a B100 USRP, which is pretty much the same as the HackRF interface, it produces massive Overruns and freezes up in short order, causing a “Force Quit” error. So heads up Team HackRF. Let us know if this concern is real. 

Equipment Deployed on Palomar

Over the weekend, Paul KB5MU and I set up a 2.4GHz and 5GHz end of the link to do demonstrations between Lake Dixon and Palomar Mountain.  The prototype site provides a much smaller off-mountain window, even with some chainsawing. This photo is for Steve. This map is for Steve. Check out those squiggles. We confirmed being able to remote into the Raspberry Pi running the show, and we can reach the Ubiquity bullets through this connection as well. We now need equipment on the other end to go live. The equipment is pointed sort of kind of towards Dixon, but will be moved to the better site as soon as we can. The site at Palomar Amateur Radio Club provides azimuth of 200 to 245 degrees. We determined exactly where we want to put the antennas and the equipment box over the weekend at the Palomar Club site. We are going to bring this to the board meeting this Wednesday and ask permission to go ahead and install. 

Management

We added many new volunteers this week possessing a diverse array of skills and experiences. It's been suggested that we develop a directory for the project volunteers. AMSAT does not publish a list of volunteers, but does publish a directory of the points of contact for major areas of activity. 

It seems like it would obviously help people to better find each other if we published a directory, but as an open source and open process project, volunteer contact information really must be opt-in. 

I believe that one can log in to their mailman account page for phase4@amsat.org and get a list of fellow subscribers, but a list of email addresses does not provide the sort of introduction that makes it easy to start working with each other. If you have ideas or suggestions for improvement in this area, then please share them. Making this an easy, enjoyable, and supported experience is my goal. 

We also need a formal process for delegating technical work. Up until this week it's been mostly possible to do through email. However, we are ramping up, and we need processes that support you all being able to better participate in the work. This means something like a google form, or a spreadsheet in github, or something else. I need some suggestions here on how to best delegate work to the team and also make it easy to report back and document. Again, ideas and suggestions are needed here. These are not easy problems to solve, as I'm sure each of you already fully know. I will do my best to make it easy and enjoyable to be a technical volunteer for AMSAT, and finding out what work needs to be done is almost the most important thing in making forward progress.  

