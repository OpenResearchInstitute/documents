This is the Phase 4 Ground weekly report for the week ending September 11th 2016.

Some of us are going to be at GNU Radio Conference all of next week and TAPR DCC next weekend. There will be very good opportunities to meet up at both events. Check in with Mike Sprenger W4UOO at TAPR. He's holding down the fort at DCC. Like base in a game of tag. 

If you are at GRC or DCC, please feel free to post whatever seems relevant and interesting to Phase 4 on the gnu_radio_con_2016 and tapr_dcc_2016 channels in Slack. That's what I'll be doing. I will do my best to summarize at the end of the day on the email list in a single post.

First up: LimeSDR unboxing and call for developers. Steve Conklin applied for and won one of two LimeSDRs. The description of Phase 4 Ground was compelling enough and the LimeSDR shipped out to Steve last week. Here's a video!

Steve is willing to coordinate and advise a team to figure out how to make the LimeSDR work for us. Now, the LimeSDR has a maximum frequency range of 3.8Ghz. However, there is an upcoming LMS8001 add-on module which will extended LimeSDR coverage all the way up to 12GHz. With an RF bandwidth of 61 MHz, 12 bit sampling depth, and a 61MHz sampling rate, two transmitters and two receivers, full duplex, USB 3.0, and 40,000 gates of programmable logic, excellent oscillator precision, it looks highly promising. You can see from this chart that the LimeSDR is very much a contender with all the other SDRs we've been using and talking about. 

There's SiLabs EVM progress. Dr. MPEG, also known as Ron Economos W6RZ generously agreed to test an evaluation module, or EVM, for a SiLabs DVB chip. The chip in question is the Si2169. Links to SiLabs web pages about it in the notes. 

https://www.silabs.com/products/video/demodulator/Pages/Si2169.aspx

http://www.silabs.com/Support%20Documents/TechnicalDocs/Si2169-D60-short.pdf

The EVM is big and beautiful. 

Here's the setup. Transport Stream file at correct bit-rate -> GNU Radio flow graph running the DVB-S2(X) transmitter -> B210 SDR -> coax cable with 30 dB attenuator -> Silicon Labs EVM -> USB to old laptop -> Silicon Labs GUI -> UDP to 127.0.0.1 -> VLC just copying UDP to 10.0.1.190 (Linux workstation) -> decode with VLC on Linux workstation.

Ron was able to confirm the correct operation of the DVB-S2X portion of the GNU Radio DVB-S2(X) transmitter. Up till now it was untested (only the DVB-S2 portion had been tested). This is a step forward for GNU Radio and therefore a big step forward for us.

He was also able to record video content from the IEEE1394 port of his cable TV box. He has a Transport Stream multiplexer that can redo the stream to the exact required bit-rate for a specific symbol rate/constellation.

This TS mux is work-related, so it is not open source. A key quote is "It's too bad, because it's way better than anything out there (like FFmpeg or VLC)." Opportunities!

The only thing that remains untested is the VL-SNR portion of the DVB-S2(X) transmitter, which as you recall Ron added a couple of weeks ago to the GNU radio project. 

Ron also did some DVB-T2 testing with the EVM. It seems a little buggy in DVB-T2 mode. Some profiles he knows that work were confusing it. His evaluation is just because the EVM acts weird with DVB-T2 doesn't necessarily mean that there's a silicon issue. More likely it's just the EVM software. 

Steve Hicks N5AC was instrumental in getting the loan of this EVM board to Phase 4. He handled the NDAs and communications with SiLabs. 

SiLabs does not usually deal with smaller projects like us. The ability to evaluate a chip for our radio like this is a an opportunity that we intend to fully take advantage of. 

If you have the skills and equipment to test this EVM for Phase 4 then this is a very nice board that you can try out. As a result of the evaluations, we will come to a decision about whether a chip like this, which is an ASIC specifically designed for DVB transceive, is a fully qualified alternative to using an FPGA. 

The ASIC vs. FPGA decision is important. One option would be to put both part footprints on the board. We'd then have a stuff option so that we can do either board — a lower cost unit without (for example) VL-SNR (using the ASIC) and a higher cost more full-featured version with an FPGA. 

There's Mr. Brain's DVB-S2X demodulator coding progress. There's a lot of very good technical updates located at the link in the notes. http://g4guo.blogspot.co.uk/ Go to his blog and subscribe to the updates and follow it, you won't be disappointed. His code will be in gitlab until it's working, and then will be released to his github, which is located here. https://github.com/G4GUO

There's 10GHz PA possibilities that I need help reviewing and deciding about. 

I'm looking for updates on the 5GHz RF chain? Schematic and BOM? Let me know!

I'm looking for people that are standing around waiting to do something? Let me know! 

If you haven't joined AMSAT, TAPR, or ARRL then please do. These organizations make our project possible. Want to join Phase 4 Ground? 



