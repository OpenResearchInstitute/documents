This report focuses on some very high-level decisions about radio technology called RFNoC. For source material, see the links in the notes. 

Overview talk at https://www.youtube.com/watch?v=UwBZ8xkiTPA

Tutorial PDF at http://static1.squarespace.com/static/543ae9afe4b0c3b808d72acd/t/55f85bc2e4b067b8c2af4eaf/1442339778410/3-pendlum_jonathon-rfnoc_tutorial_fpga.pdf

Slide presentation at http://static1.squarespace.com/static/543ae9afe4b0c3b808d72acd/t/55ddc6d6e4b09069ee81e20c/1440597718379/3.+braun_pendlum--rfnoc+2015-08-26.pdf

What is RFNoC? RF network on a chip. It's an implementation of radio stuff in FPGA hardware. 

What is FPGA? Field programmable gate array. An FPGA is made up of what's called  logic fabric. This fabric can be programmed by software that turns it into reconfigurable circuits that do specific tasks. Just like sewing, you start out with 8 yards of satin and with skill and experience you end up with a wedding dress. If you don't know how to sew, it's a steep learning curve. Just like sewing, there's lots of different types of skills and techniques ranging from beginner to highly advanced. 

RFNoC is for FPGAs what GNUradio is for general purpose processors. RFNoC is the GNUradio of FPGAs.

Why RFNoC? Why isn't GNU radio enough? Well, GNU radio might indeed be enough for us, but we owe it to ourselves to figure out whether or not RFNoC is a huge win for us.

Here's why RFNoC is such a big deal right now. Take something simple in theory. in the talk referenced above, the example given was something like a 200MHz real-time Welch's Algorithm implementation. While it might seem straightforward to implement this in an optimal manner, in practice there are several stumbling blocks. Operations that are crying out to be done in parallel and operations that can be done in basic math are ideal to shift to an FPGA. But, the FPGA is underutilized. Transport between blocks is overloaded. It's not optimized, like, at all. 

Even with a high-end computer, the host just can't keep up with demanding radio applications that the x310 should indeed be able to do. RFNoC has great potential to eradicate this shortcoming. 

The goals here are several. Heterogenous Processing, where you have choices of composable and modular designs using general purpose processors, FPGAs, and beyond. Maintain ease of use, and have tight integration with GNU Radio. Push the boundary between GPP and FPGA processing to the optimal place for whatever design you're implementing. Make FPGA acceleration easier. The entire hardware stack is treated like a reprogrammable ASIC. Features are used as-is.

The basic premise is GNU radio flexibility should extend onto the FPGA all the way up to the ADC/DAC. 

RFNoC + GNU radio is a perfect match. Ideal way to use and test RFNoC is with GNU Radio. Seamlessly interconnects (with some caveats). One of the first caveats is something that many of us on the Phase 4 Ground already know. 

GNU radio has a steep learning curve and RFNoC is very developmental. Things may change out from under you. A lot of groups, companies, and organizations are dabbling in RFNoC. People are eyeing each other from the shoreline, just waiting for the first few intrepid explorers to dive in. 

The building blocks are all there for this. GNU radio is free. USRPs are available online, x310 contains big and expensive FPGA, seems like everything is there to move flow graphs onto the FPGA.

Why hasn't this already been done? Because it's difficult. Takes a lot of time, requires digital design expertise, and needs transparent integration into software. 

This is a situation where you need a lot of radio domain exports and a lot of FPGA experts, and traditionally there isn't a lot of overlap between the two groups. FPGA development is not really a requirement of communications engineering curriculum. FPGA designers generally don't have a communications background. And, the math is hard, and that affects everyone.

RFNoC architecture. The user application is GNU Radio. USRP source block ==becomes==> an RFNoC Source. This new source controls the radio core. 

There's a USRP hardware driver, which is on the host PC. On the USRP FPGA, there is an Ingress/Egress interface, and a crossbar. Below that there is a Radio Core, plus Custom RFNoC blocks. 

RFNoC provides the communication infrastructure. The crossbar knows what to do with the data it's getting. RFNoC provides space for user logic. 

e.g. Implement FFT as an RFNoC block in FPGA. You have an RFNoC shell. Put whatever you want into the shell. 

There's a big sticking point here with the tools available to us. FPGA tools are notoriously closed and expensive. RFNoC is all open source. Everything is available but it's hard work and a steep learning curve. 

Finally, there are implications for dropping in something proprietary that you might have purchased, like Xilinx IP cores. Doing this for your own use is ok, but then if you are selling it, say, to a customer, then you have to check with Xilinx or whoever you got the IP core from. Since we're doing an open source radio, this aspect doesn't affect us as much, but it is something that a lot of companies have to consider as they move into this space. 

So, should Phase 4 Ground radio be an RFNoC project? Should we bite off more than we can chew? Is it more than we can chew? This is what we need to be thinking about now, so that we can deliver a world-class radio that fits into the changing landscape of open source software defined radio. Comment and critique welcomed and encouraged. 

