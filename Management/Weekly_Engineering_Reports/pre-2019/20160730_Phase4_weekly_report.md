DVB Receive Chip - Under NDA but we're investigating one!

Steve Hicks and I talked about next steps in the adventure of building development and production hardware at Flex Radio. He's in the process of finding out out how much it would cost to get some small number of development boards, and my job is to figure out how big of an FPGA we really need. As mentioned last week, when we can get a better handle on the size required for a DVB-S2X/DVB-T2 design then we can start seriously selecting and pricing FPGAs. FPGAs are expensive and the pricing is weird. 

Over the past week there has been some good progress in finding a DVB receive chip. If we do our FDM trunked uplink the way we've been talking about, and if we're able to handle all the data with GSE the way we've been talking about, then this chip may do everything we need to receive a big DVB signal. We are now trying to find out if there's development hardware that we can use to confirm the behavior we need. In order to do this, we need GSE working on transmit. This isn't finished yet, but steady progress is being made on a python implementation. If you can help make this happen faster, then get in touch with me as soon as possible. 


Phase 4 Payload NDA with AHA Signed!

The NDA between AMSAT and AHA has been signed, and that means that AMSAT volunteers can work on the proprietary implementations of DVB-S2X that AHA has developed in order to get them onto our payloads. The agreement with AHA is really good news and will help AMSAT achieve remarkable things. 

The goal of this work is to implement forward error correcting codes from DVB-S2X into RFNoC blocks. As previously described, GNU radio blocks generally favor the general purpose processor, leaving the FPGA in many SDRs underutilized. RFNoC, or RF network on chip, is a way to partition the processing problem between GPP and FGPA in a way that makes the entire radio system much more efficient. We are super proud to be a part of this initiative and we hope to benefit from it for a long time in many different ways. 

AlasKit wants to Build!

Another contender for building all or some hardware for phase 4 is on the team. Besides being an award-winning writer and member of Phase 4 Ground, Eric Nichols KL7AJ also runs a company devoted to educational and scientific resources. He writes, 

-=-=-=-=-=-=-=-=-=-=-=-=-
AlasKit Educational and Scientific ResourcesEric P. Nichols, KL7AJ	It has been my longtime desire to see the expansion of manufacturing in Interior Alaska.  AlasKit Educational and Scientific Resources was created in order to facilitate the development of easy-to-manufacture and assemble technology products on a small scale, using the tried and true concept of youth apprenticeship.  	We are currently developing a number of low cost amateur radio accessories, assembled by middle school and high school students on a part time basis.   I believe a low cost 5 or 10GHz terrestrial radio would be a great project for our fledgling enterprise, and may be the first exposure a lot of students may experience in the manufacturing process.  Once a final form for the AMSAT terrestrial radio is “locked in” we would like to investigate the possibility of producing these radios here in Alaska.	The State of Alaska has some very attractive grants available for this kind of enterprise, and federal apprenticeship grant programs exist as well; we are currently pursuing this channel for some expansion funding.	Another product we can provide is top quality documentation, both for individual devices and for AMSAT in general, with over thirty-five years of experience in technical writing, both for commercial and amateur publication.	I am excited to see what role AlasKit can play in AMSAT Phase 4 and beyond.  I believe we can have a mutually beneficial professional relationship.Sincerely,Eric P. Nichols, KL7AJProprietor, AlasKit Educational and Scientific ResourcesNorth Pole, Alaska-=-=-=-=-=-=-=-=-=-=-=-=-


Phase 4 Ground at DEFCON!

DEFCON Wireless Village has accepted our proposal to speak at DEFCON. The conference is the first week of August. We speak Saturday from 2:30 until 2:50 in The Wireless Village. Come support us! It's a quick slot so we're going to talk fast. We are going to release software (if all goes well), reveal some tricks, and go over the architecture and how we have approached engineering and management challenges. 15,000 people are expected at DEFCON this year. While we won't reach them all, we will reach as many as we can, and learn as much as possible while we're there. 



Lots of repository updates. Here's the updates from last week. 

1) Calculated phase noise numbers from Kerry Banke N6IZW are in the repository. 

These are what is expected to be the phase noise for an LO based on the ADF4350. The ADF4350 is a wideband synthesizer with an integrated VCO. Check out the data sheet here:

http://www.analog.com/en/products/rf-microwave/pll-synth/adf4350.html

Kerry will take measurements as soon as possible and these measurements will be added to the document in the Performance folder in the github repository. As always, the repo is here:

https://github.com/phase4ground

2) We remain in a place where we need volunteers to write GNU radio DVB-S2, S2X, and T2 receiver blocks. 

We cannot provide the sort of recipes that we want to provide to the community without a GNU radio flow graph. Figuring out whether and how to modify the existing demodulation and decoding blocks in GNU radio is good first step. 

3) On the GNU radio transmitter side, there's some good news. DVB-S2X transmitter updates have been checked into the GNU radio project by Ron Economos aka Dr. MPEG. 

He is the author of the content in the DTV GNU radio module. He explains that the Physical Layer Framer block will need to be significantly updated to complete the VL-SNR transmitter. He also helped update the Phase 4 modulation and encoding spreadsheet. 

4) On the HDL side, there's an open source receiver board project that needs some review to see if we can use it to bootstrap our receiver. Links in the notes.

http://www.netup.tv/fr-FR/documentation/articles/universal-open-source-dvb-card
https://github.com/aospan/NetUP_Dual_Universal_CI-fpga

5) Our efforts to implement Generic Stream Encapsulation will pay off here because GSE would need to be grafted in to this codebase. Anyway, check it out and weigh in on the list. 






If you are a member of AMSAT, then you have received your AMSAT Journal, and you might have noticed a lot about Phase 4 and Dayton in that issue! 

Dr. MPEG wrote "After seeing the K3IO, N4HY and KM4KAL article in the latest AMSAT Journal, I've created a DVB-S2 with SSB flow graph that's a lot more functional. You can download it from my website. http://www.w6rz.net/dvbs2_ssb.grc"

The test video stream is in the notes. for 3.072 Msym/s 5/6 8psk is here. http://www.w6rz.net/drinky8psk.ts 

Oh yeah, you have to build and install his Controlled Envelope SSB (CESSB) out-of-tree module. Link in the notes.

https://github.com/drmpeg/gr-cessb 

He says "With the center frequency at 52 MHz, the SSB ends up on 50.125 MHz. You can just start to hear the 8psk waveform at around 50.160 MHz. I'm using an Icom IC-7300 as the receiver with a 30 dB attenuator. Both the SSB and DVB-S2 signal are around S-9." I believe Kent asked about something along these lines a couple years ago, so help us spread the word. 

Speaking of AMSAT, please join! 

If you want to contribute to Phase 4 Ground then join the mailing list by applying at the following link:
http://www.amsat.org/?page_id=1121.So, I found out how to get a terrain profile in google earth. Here is a set of them between some of the places we want to use for prototyping equipment. The Palomar mountain end of the control link, using Ubiquity hardware, is up and running. This is a great utility that happens to be free in google earth. However, it turns out that there is a free online tool that does profiling that does something that Google Earth does not. Google Earth does not account for the curvature of the earth. This site here does:

http://www.heywhatsthat.com/

This site was suggested by Mike Seguin. He writes: "In our microwave experimentation, we use "Hey What's That" to do profiles which can be set to specfically use curved earth. The "optical" feature of Hey What's That is what we use primarily for LOS paths on 24GHz and up."

These profiles of San Diego Phase 4 project locations are made by him using this site. Thank you Mike! 

More soon! Gotta catch 'em all!