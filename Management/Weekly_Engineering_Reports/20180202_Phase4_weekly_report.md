
Phase 4 Ground Weekly Engineering Report! #dvb-receiver update, Snickerdoodle unbox and setup, and some Slack Analytics. 

Video at https://youtu.be/W13e0ds9HCA


DVB-RECEIVER

So let's look at some technical work going on in the #dvb-receiver channel on the Phase 4 Ground Slack.

Implementing an open source version of DVB-S2 and DVB-S2X receive is a very ambitious goal, and Charles Brain G4GUO has been particularly active here, with Jan Schiefer AC7TD, Ron Economos W6RZ, Wally Ritchie WU1Y, and many others helping and participating. 

Charles' implementation uses a GPU -- or graphical processing unit -- to handle the heavy computation. His successful implementation of LDPC forward error correction decoding was demonstrated at the AMSAT Space Symposium in October 2017.

GPUs get their computational horsepower from massive parallelism, and this has some interesting implications for radio performance. In order to take full advantage of the parallel processors, Charles has it configured to process a batch of up to 128 frames at once. All the frames have to have the same "MODCOD" -- modulation and coding.

Our air interface calls for the use of "adaptive coding and modulation," ACM, so that we can accommodate a very wide variety of ground station types and capabilities and take full advantage of higher-performance ground stations. With ACM, the downlink contains a mix of frames with different modulations and coding formats. This means that the GPU version -- or any radio with parallel processing -- may need some extra accommodations. 

If you want to read more about adaptive coding and modulation for Phase 4 Ground, here's a link to our paper on GitHub: 

https://github.com/phase4ground/documents/blob/master/Papers_Articles_Presentations/Papers/Adaptive%20Coding%20and%20Modulation%20for%20Phase%204%20Ground.pdf

// So what extra accommodations for the GPU are we talking about?

With this kind of receiver, there's a fundamental tradeoff between GPU utilization efficiency -- how many of the CPU cores we keep busy -- and latency -- how much extra delay is caused by holding back frames until we have a full batch. If our goal is to keep the GPUs busy to maximize the compute speed, then we have to wait until 128 frames *of the same MODCOD* have arrived before we can start to process any of them. All 128 frames then come out of the receiver in a burst. The 128th frame is only delayed by the necessary minimum processing time, but the first frame has been delayed by an additional 127 frame times, *or more* if some of the intervening frames had a different MODCOD.

The first question is, do we *need* to keep all the GPU cores busy? Probably not. It depends on just how fast the GPU cores can process frames, compared to the frame rate on the downlink. Maybe we only need to keep a fraction of the GPUs busy in order to keep up with the downlink, so maybe the magic number isn't really 128, but something smaller. The only way we'll find out for sure is to complete the GPU-based receiver implementation and benchmark it.

The second question is, just how bad is the extra delay? If we stick with 128 frames to a batch, how much delay is that? Our air interface calls for using so-called "short frames," as recommended for near-space communications by CCSDS, the Consultative Committee for Space Data Systems. Short frames in DVB-S2 and DVB-S2X are 16,200 bits long. To turn that into a duration, we need to know the effective bit rate of the channel.

We've chosen a baseline bandwidth of 10 MHz and a 20% rolloff, which results in a fixed channel symbol rate of 8.333... megasymbols per second. The formula is:

bandwidth in Hz = 1.2 * carrier symbol rate in Hz

where the .2 in 1.2 comes from the 20% rolloff. By the way, 20% rolloff is a good middle-of-the-road number. Industry groups say that DVB-S2 carriers below 10 Msps really need a guard band of at least 10% rolloff. The older DVB-S standard specified a fixed rolloff of 35%. The newer DVB-S2X goes all the way down to 5% rolloff.

So, we have our fixed symbol rate. With adaptive coding and modulation, the code rate and the modulation order change. That means the data rate changes depending on how much extra help your receiver needs to successfully decode a frame. We have chosen six MODCODs for our initial implementation of ACM. If you work out the math, the nominal data rates for these MODCODs at our baseline symbol rate range from 4.054 Mbps to 21.067 Mbps. There's a table in the notes.

QPSK 4/15   4.054  Mbps
QPSK 2/5    6.205  Mbps
QPSK 2/3   10.506  Mbps
QPSK 4/5   12.298  Mbps
8PSK 5/6   19.459  Mbps
8PSK 8/9   21.067  Mbps

The delay is longest at the lowest data rate, 4.054 Mbps. 128 frames of 16,200 bits is 2,073,600 bits, or about half a second. That's assuming we transmit nothing but the slowest MODCOD. The delay could be much longer if ACM inserts lots of frames of other types.

On the other end, 128 short frames at the highest data rate takes just a tenth of a second, but again that's a lower bound if we allow ACM to insert other frames.

These delays are on top of all the other delays in the system. For a Phase 4 satellite in GEO, there's already a quarter of a second just in propagation delay. Adding a tenth of a second to that might not be a big deal. Adding half a second might be. It would depend on the application. For lower orbits or terrestrial systems, the calculation is different, of course.

We can't improve these lower bounds, except by decreasing the number of frames we process in parallel. And we can only do that by making the processing faster, either by even more clever coding or by waiting for GPU hardware to get faster. We can't improve latency by just arbitrarily reducing parallelism. If we go below the magic number needed to keep up with the channel rate, we will *still* end up paying the latency price for all those frames we had to skip to keep up. 

On the other hand, we can try to avoid making the latency problem worse than it has to be. The simplest way to do that would be to fall back from ACM to CCM, constant coding and modulation. That is, transmit all frames with the same MODCOD. Unfortunately, by doing that we'd give up some very desirable flexibility in ground station designs.

Another simple approach would be to just accept that the parallel GPU-based implementation is only suitable for applications that aren't sensitive to latency. Applications like file transfer care more about the overall data rate than about latency.

There's room here for us to invent a more complicated solution to take these tradeoffs into account. Some sort of dynamic scheduling algorithm that takes the latency requirements of each data stream into account could by devised to suit our needs. That's called QoS, Quality of Service, and it's a can of worms.

Join the discussion on the #dvb-receiver channel on phase 4 ground slack!


SNICKERDOODLE

Finally, here's an unboxing and setup of another option for learning and programming FPGAs. This is a Snickerdoodle Black with a breakout board. It has a Xilinx Zynq 7020 and lot of interfaces and plenty of GPIOs exposed.




SLACKALYTICS

We use Slack for engineering discussion and planning. It's been a success. Here's some analytics on all our channels and an engineering update from #dvb-receiver. 

This graph is messages sent since we established the account. 40,912 
There are spikes and a trend up since early January. 

On top is where people are reading. The purple is public channels. The red is direct messages between members. The black represents a private channel. This private channel is for the badge build process. We're keeping it private as to not reveal the puzzles and surprises. 

The bottom graph is where messages are sent. Notice the difference? There are a lot of people following along in the public channels. 

On the top is messages sent over the past 30 days.
On the bottom is where people are reading over the past 30 days.

On the top is the messages sent in public channels and direct messages.
On the bottom is the one private channel, broken out. 

A lot of talking is going on in the private channel and we are very much looking forward to everyone seeing the results very soon. 




WHO WE ARE

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


