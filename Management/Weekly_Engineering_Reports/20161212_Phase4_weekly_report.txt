Greetings all! This is the Phase 4 Ground weekly report for the weekend of December 9th 2016. Paul KB5MU sitting in for Michelle.

Generic stream encapsulation for DVB, or GSE for short, is now working in GNU Radio with ping packets! Low latency, high efficiency, and it's available as an out of tree module right now at the following link. 

https://github.com/drmpeg/gr-dvbgse

Thank you Dr. MPEG (Ron w6rz)

Why is GSE important? It's the data link layer protocol we've chosen, and therefore binds the universe together. It's efficient and low latency. It allows us to carry packet protocols like IP, ethernet, or whatever through our system. There are several addressing modes and it enables adapative coding and modulation. You can do hardware filtering with it and you can add other link protocols by extension. There are no built-in integrity checks in GSE. That's left up to the physical layer to do. We are confident that the physical layer is up to the job. 

GSE is also used in the terrestrial version of the protocol, DVB-T2. You've heard less about this but it's what we're going to use for terrestrial radio modes. Sharing GSE function between all modes makes for a more consistent design and a bit less work. 

The testing continues with GSE using the Ayecka SR1 and SR1 Pro. These are DVB-S2 receivers that claim to do GSE. Three of us purchased the SR1 in anticipation that it would do GSE out of the box and be either a good test equipment choice or possibly one of the many recipes for a Phase 4 Ground radio or both. However, GSE is, if you hunt hard enough, listed as an option that requires another $220 to unlock. And, Ayecka wants to upgrade your receiver remotely, which could be a problem in some IT situations.

Dr. MPEG's early results seem to indicate that there are some bugs in Ayecka's SR1 GSE implementation. That's just further evidence of our early adopter status. Yay us!

We were of course disappointed to find out that GSE was an extra cost option, and nobody like to run into bugs, but kudos to the Ayecka folks for being very responsive with fixes for the GSE issues we've reported.

"Just say no to HLS" 

We are soliciting opinions about HLS from Xilinx. This is High-Level Synthesis and is part of the Vivado design environment. It allows C, C++ and System C specifications to be directly targeted into Xilinx All Programmable devices without the need to manually create RTL. Sounds like magic, doesn't it?

Is it something that you have experience with? Is it something you have an opinion about? Xilinx wants to know. Get in touch with me with your feedback.

==
Michelle W5NYV has negotiated an educational discount for Phase 4 Ground team members who wish to purchase a Red Pitaya board. Today (Friday December 9th) is the deadline to get your request in to Michelle. Note that these discounts are for the version with 10-bit I/O channels. If you want 14-bit I/O, you'll have to pay the regular price.


More soon! 