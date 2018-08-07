Welcome to the engineering report for Phase 4 Ground!
27 July 2018

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Ubuntu Snaps for SDR

Snaps are containerized software packages for Ubuntu. They are designed to be simple to create, install, run, and update on all major Linux systems without modification. 

Steve Conklin, our platform lead, believes that Ubuntu Snaps are a great solution for some of our SDR work. He will be looking to work with Phil Karn's SDR package. What needs to happen next is getting the Karn SDR package updated with any recent work, and getting it to reliably build. If you can help with this, then contact Steve Conklin (steve@conklinhouse.com) and proceed. 

The current SDR code is here: https://github.com/phase4ground/ka9q-sdr

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

IP Multicast Engineering Adventures

Phil Karn found what he thought were two annoying Linux kernel bugs last week. 

The first was indeed an ipv4 multicast routing bug. The second was in the ALSA sound driver, and turned out to be a hardware-specific driver setting problem.

First, the ipv4 bug. An arbitrary hard-coded limit of 10 pending entries in the multicast routing table caused multicast traffic to never start on a network with lots of multicast traffic (e.g., at University of California at San Diego UCSD) when the stream you want had low activity.

Phil could usually (but not always) get audio to flow when the receiver was tuned to NOAA Weather Radio (continuous), but often not when tuned to APRS (intermittent). And he could never get decoded AX.25 frames (every 5-10 sec or so).

These things worked well in other networks, but not at UCSD.

Phil filed a bug report with the Linux kernel developers who confirmed it was a problem and proposed a patch. Phil reported that it only took a few hours to get a response. 

Open source for the win!

Of course, as Phil notes, open source only works when enough people use a functionality or protocol to create enough test cases that cover enough of the potential search space to where you will get the weird results that turn out to be subtle bugs. 

When Phil dug into the sound driver bug, it turned out to be a glitch in the Intel HDA timing system in his particular Dell laptop. There's a lot of this glitchery in this particular chip, and there are pages and pages of notes on various driver options to set to work around it. He found a discussion of what sounded like his problem, tried the suggested options on the kernel module, and the problem cleared up.

The problem was that with the default settings, an interrupt didn't get registered in the Linux kernel. He doesn't understand why it worked at all, but it's working now, and seems limited to particular laptop hardware. The symptom was that callbacks from the portaudio library stop coming, and the thread that calls them is stuck in a poll() that never returned. 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Multicore Programming Notes

Threading is powerful but also full of pitfalls. Phil relies heavily on pthreads. With even embedded processors often having two to four cores, anything worth coding really needs to take multiple cores into account and use them as effectively as possible. However, not only do you have to be concerned about race conditions, but also memory fencing, store fending, and load fencing. 

Race conditions are somewhat self-explanatory. One set of instructions starts before input data is available or calculated in time. That means stale or missing data is used instead of expected timely results. Race conditions can be managed in several ways, including the use of flags or semaphores or guaranteed delays. 

Memory fencing is when you ensure that memory operations occur in the correct order. If you have a single linear set of operations, this is inherent in the code. If you have concurrent lines of code, then enforcing proper shared memory access (both loads and stores) becomes critical. 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

PlusUltra!

Ultra96 work is proceeding. This effort is focused on getting Charles Brain's LDPC decode into an FPGA (among other functions). The Ultra96 is the leading contender for a development platform.

We've build bootable SD cards for the Ultra96 in a variety of ways. Methods include the PetaLinux toolchain as well as utilities from Brennan Ashton (https://gitlab.com/btashton/ultra96-notes/tree/master). 

Jan Schiefer has updated his instructions on building an SD card that includes GNU Radio for the Ultra96: https://github.com/phase4ground/PlusUltra

This rewires the console port to come out of the console connector, adds drivers for some popular Realtek-based USB Ethernet dongles (so you can use Ethernet, or even TFTP-boot!), and adds gnuradio (version 3.7.13.4), including UHD.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Trans-Ionospheric Badge

100 production badges arrived today (Friday 27 July) and another 100 will arrive next week. These hackable conference badges are amateur radio themed and are planned to interact with Phase 4 Ground radios as a wearable extension of the user interface. 

Proceeds directly benefit Phase 4 Ground radio development board efforts. Our major sales event for Trans-Ionospheric badges will be at DEFCON, which is coming right up. 

The good news here is that we have a cooperative vendor in the DEFCON vendor room that has agreed to sell the boards at his booth. We are greatly appreciative of this opportunity. It's a huge help to funding Phase 4 Ground and spreading the fun of #badgelife. 

Phase 4 Ground, Open Research Institute, and Ettus Research will be part of WiFi Village this year. Come visit us and have fun with SDRs and GNU Radio!

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Linux in the Ham Shack 

Tune in to the Linux in the Ham Shack podcast episode 238 to hear Michelle W5NYV and Steve Conklin interviewed about Phase 4 Ground, Ubuntu Hams, Open Research Institute, and a few other things. Thank you to everyone at Linux in the Ham Shack for the opportunity to spread the news about open source efforts in amateur radio! http://lhspodcast.info/ 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Block Party at GNU Radio Conference

The hardest part of Phase 4 Ground radios is on the receiver side. Having complete DVB-S2 and DVB-S2X receiver blocks in GNU Radio, preferably leveraging RFNoC, is a major (and ambitious) goal. We are making progress, but we have a lot to do. We have organized a summit at GNU Radio Conference in September 2018. It's called a Block Party, because we want to make some blocks, and because we want it to be fun. 

We will have a dedicated room for the week and volunteers ready to help advise. We are bringing as much lab equipment as we can, a white board, and plenty of enthusiasm. The goal is to produce blocks (or substantial progress on blocks) for GNU Radio. We'll have some swag and quite possibly some Trans-Ionospheric badges and other items available. 

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Space Policy Participation

Open Research Institute will be at Goddard Space Center to participate in the Interplanetary CubeSat Workshop in August. We'll also be at the Open Source CubeSat Workshop in Madrid, Spain in September. 

The goal of participating and presenting at events such as these is to advance open source hardware and software in the amateur radio satellite service. There is a lot of work to be done here and we have a lot to learn. Our views are distinct from, add to, and interact with, those of AMSAT, ARRL, and others. We advocate a strong, committed open source approach and are actively developing and refining our policy views in order to make open source work easy and accessible and effective for anyone wanting to contribute to the amateur radio satellite service. 

Join our mailing list and find out more about Phase 4 Ground and other Open Research Institute projects at https://openresearch.institute/



