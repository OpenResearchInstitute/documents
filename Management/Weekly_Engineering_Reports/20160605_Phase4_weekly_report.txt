Those of us that went to Wireless@VT have returned and are back to work! There were keynotes, tutorials, networking, tours, food, awards, a DARPA contest, a myriad of introductions, and large swaths of uninterrupted time with project participants. All of these things produced results and advanced the cause. This report summarizes the actions taken as a result of the work done at the conference.

The conference will not be the same next year. It's most likely going to be in a different location, and like all of us, it continues to evolve and change for a variety of reasons. 

There's some significant RFNoC news. First the was OpSec. Then there was DevOps. And before anyone could figure out the actual definition for DevOps, we have come to the precipice of OpNoc!

As you recall, RFNoC is the process of writing GNU radio blocks that more fully utilize the FPGAs in powerful SDRs. Any function where improvement can be gained from doing more in the FPGA is a candidate for RFNoC.

Therefore we are planning a variety of operations to advance RFNoC and use it our satellites and radios. 

From the payload perspective, very successful discussions at Virginia Tech resulted in the decision to draft an MOU in order to enable some focused on-site effort at AHA. The plan is to implement existing DVB-S2X intellectual property in RFNoC. If all goes well with agreements and funding, then there will be a delegation to AHA's site in northern Idaho. This is a multi organizational effort between AHA, Virginia Tech, and others. This is not an open source effort. 

How does this help the ground effort? Well, having a known good working payload helps us develop our receiver. If the payload effort is successful, then our groundsat can be implemented using this code, giving some advantage in terms of schedule. Schedule? We will work as quickly as possible to test an implementation of AHA's firmware in USRP with a goal of having RFNoC on FEC by GRCon2016. GNU Radio Con is 12-16 of September.

Details about this conference at the link in the notes. 

http://gnuradio.org/grcon-2016/

This effort doesn't directly help get Phase 4 Ground *radios* completed, but it dramatically helps the payload and therefore the entire project. The receiver design in the ground terminals is up to us. The specifications of the blocks has begun.

A tutorial exists for getting started with RFNoC. The link is in the notes. 

https://github.com/EttusResearch/uhd/wiki/RFNoC:-Getting-Started

I'm going to walk through this tutorial and make a video about it. This is separate from the weekly reports. After the tutorial, we're going to specify some blocks to start working on. These will be open source versions. These will also be described in as much detail as we can possibly provide, in order to make it easy to understand how these building blocks are constructed and what each of them do. 

The most obvious place to start is with those blocks that we know we need that already exist. We need QPSK, BPSK, and 8PSk demodulators. Those blocks exist in GNU radio but they may require some modification to make them match the constellations in DVB.

We need an LDPC-BCH decoder. There's one in GNU radio. It's described as being a soft-decision decoder that uses belief propagation (also known as message passing)

Belief propagation is described at the following link:

www.cs.toronto.edu/~radford/ftp/LDPC-2012-02-11/decoding.html

The documentation says it's "Designed for a memoryless AWGN channel, it assumes a noise variance of the value specified for sigma." Ok all of that is great, but when I moved the block into a gnu radio flow graph, it's listed as a definition block. I'm not sure how to use it yet, but when I do figure it out, I'm going to explain it. If you are way ahead of me here, then please speak up. 

I think we could use some blocks to handle generic stream de-encapsulation. We need some blocks to handle adaptive coding and modulation decision making. Those things are on us so we need to better figure out how we're going to attempt to handle them. 

This means that we're going to have to have a tutorial session on generic stream encapsulation and another one on adaptive coding and modulation. We can achieve these things. It's just going to take some thinking and doing. 

So what's our schedule for this? Here's one pivot. We've applied to present at DEFCON 24, 3-7 August. If accepted, we will get a slot at the wireless village and will demonstrate everything we have completed on protocol, authentication, authorization, and client layer at that point. 

I'd like to release at least some software at DEFCON, perhaps the Dymanic QSL, perhaps more. If we aren't accepted, then that's ok, we'll bring everything and demonstrate informally at wireless village, hardware hacking village, or wherever there's space and interest. 

Details about DEFCON at the link in the notes. https://defcon.org/

Payload team is deciding next steps after their preliminary design review has concluded. The PDR was May 27th. A sanitized version of the PDR slides is under construction and may be available soon. 

We need Southern California hams to help with the Dixon Palomar experiments. Outreach to get the Dixon site installed continues this week. We're going to have to go with solar power for Dixon. 

Please send your input, questions, and content in to Phase 4 Ground. Join ARRL, AMSAT, TAPR if you haven't already. Pick one or more. Their support is vital for the success of this project. 