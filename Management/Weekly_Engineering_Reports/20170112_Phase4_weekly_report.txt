https://www.youtube.com/watch?v=pxxBg3oSmaQ

Phase 4 Ground weekly report :+)

An intro to #badgelife, update on progress on our badge efforts, human radio interface proposal, and a demo of the first version bound for JOCO. 

Rectangular printed conferences badges of paper or laminated plastic are a familiar sight at conventions and meetings of all sizes. Printed and usually worn with a clip or lanyard, conference badges often serve as an event ticket. 

By 2009, several large technical conferences offered hackable electronic badges as part of registration, like these from DEFCON.

Ranging from extremely simple LED blinky badges all the way up to fully functional cameras, radios, game systems, and more, badge engineering, or #badgelife, is another way to get involved in DIY and maker movement electronics. 

Not all recent badges are electronic. One of these is a white vinyl 45 record. The audio track was an encoded message that was part of a puzzle participants could solve at the conference. 

This is a badge from the car hacking village at DEFCON. This badge plugs into the OBD-II port and talks to your car.  https://github.com/lanrat/CHVBadge_16 

This is a prototype badge for development of the JOCO version of the badge we are working on. Board by Steve Conklin. 

Kits for the simplest electronic badge, the blinky badge. It's just LEDs and batteries.

The badge from the 2017 Hackaday Superconference was an expandable working digital camera. Details: https://hackaday.com/2017/10/11/building-the-hackaday-superconference-badge/

Here's the Layer One conference badge with the game controller that came with it. Details: https://hackaday.io/project/13262-layerone-2017

Some badges are more art than electronic. This skull themed badge had a Intel Quark D2000, eight switches, and 5 LEDs. It put out some clues on the serial port and lit up with the Konami Code, but to make it do anything else you need to reprogram it, and the Quark was then discontinued by Intel. 

The first and second Bender Badges can be seen here details at https://hackaday.io/project/19121-andxor-dc25-badge this open source badge is what our badges are based upon, and we cannot say thank you enough to the AND!XOR team. 

Here's set of badges from the r00tz conference, which is for kids. It's held at DEFCON. These badges are packed with features. Details: https://github.com/HelloTechie/r00tzbadge

Check out this working prototype of the first version of our ongoing badge effort! JOCO pirate monkey theme. 

Here's an example of an entry in a hackable badge contest. This is our DEFCON17 badge turned into a geiger counter, where detected radiation was used for a one-time pad cryptographic link over ZigBee. A demo https://www.youtube.com/watch?v=2_gEeffx8t8 and writeup at http://bigideatrouble.com/dc17badgehack.pdf

Here's another badge hack with the DEFCON18 badge. The modified badge is on the left and the stock badge is on the right. 

So what's the point of doing a badge? Having fun and learning how to work together, outreach and DIY maker awareness and encouragement, and also because a badge can be a radio accessory and part of the Human Radio Interface. 

One of the functions of the Trans-Ionospheric is to show channel acquisition health and status. Here's where we are today with this concept. 

Your radio listens for a list of channel assignments that are transmitted from the Groundsat in order to know which uplink channels are free and can be accessed. A lot has to go right to get a channel assignment. Knowing how far the radio is getting into the process gives you better visibility and control. 

These are proposals. What we are talking about can also work for an HTML skin, a physical radio layout, and other UI expressions. As always, comment and critique welcomed and encouraged. 

If you see the first LED lit, that means you have symbol timing. The second LED means you have frame timing. The third LED means you have successfully received and demodulated the physical layer header. This means that a lot has already happened. You've got symbol timing and frame timing and you've demodulated the pi/2 BPSK header and now you know how to decode the rest of the payload, and you know where to look for the next physical layer header. 

Now we select an unused channel and transmit our request to use the downlink, which includes a signal to noise report. How well we can hear the downlink is used by the payload to determine how much forward error correction coding you need. 

At this time, we might be identifying ourselves to the payload and asking to use it. I say might be, because one can always just listen. When you want to transmit you need to get a downlink channel. The choice of how long to reserve an unused channel is a good one. Should this process be done for every uplink frame? Or should there be sessions that time out? 

The registration process can range from everyone automatically gets access through the transmitter to full authentication and authorization with list management, where only pre-approved operators can use it. 

The particular policy is up to the operator of the Groundsat or payload. Perhaps the first LED would be request transmitted , the second would be successful authentication, and the third successful authorization. Once you hear yourself in the downlink channel assignment list, then you are good to go and can transmit. 

The payload is using the downlink signal to noise value that you report assign you modulation and coding, so the LEDs along the top can give you an indication of how good you're doing, if you have any messages, what mode we're in, room requests, and more. 

We need to make a software prototype of this type of user interface. Can you do it in python? In HTML5? In Erlang? No I'm not kidding. Sign up, submit it, and let's show it off! The user interface is the product, so let's see if this idea works for us. 

Updates from Firmwarez and Steve Conklin follow! 



AMSAT Phase 4 Ground home page https://phase4ground.github.io/

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


