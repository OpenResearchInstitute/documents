This report focuses on advancements made in deciding the air interface. We're looking at DVB-S2X to receive, and OQPSK to transmit. 

Repository for documents and software can be found: https://github.com/phase4ground

We have nearly 50 volunteers on the mailing list and activity across the country. We're working hard to make a wonderful radio for AMSAT and terrestrial microwave, and we appreciate your support, feedback, comments, and critique. 

DVB-S2 stands for Digital Video Broadcasting - Satellite - Second Generation. There is a recent extension to this standard, called DVB-S2X, that has very low SNR capabilities and a lot of other goodies. The geo project, ascent, and eventually the high earth orbit project, are expected to transmit using DVB-S2X. This is the foundation of our common air interface. 

DVB-S2X specifies the modulation and coding for our received signal. There are five major landmarks. 

One, an input stream adapter. Input streams can be packetized or continuous, from single or multiple sources. This is helpful! 

Two, forward error correction. Our type is low density parity check codes concatenated with BCH codes. What does this mean? 

A concatenated code is one that combines two different coding schemes. In coding theory, there's a fundamental problem in that finding a really great code that has very low probability of error usually means that the block length has to go up, and the decoding is more and more complex. When you use two codes together that each have particular strengths, they balance each other out. You can get exponentially decreasing error probabilities, but you only have to pay a polynomially increasing cost in terms of code block length. This may seem complicated, but just remember concatenation is codes doing teamwork, and the standard that we're using is bad ass. 

Our inner low density parity check code can achieve extremely low error rates near channel capacity. This means, it's about as good as you can get. The outer BCH codes are used to correct sporadic errors made by the LDPC decoder, and to trick it out so that we don't have enormous block lengths and stuff like that. 

Three, we have a wide range of code rates. The code rate is expressed as a fraction. The top number is how many uncoded bits go in. The bottom number is how many coded bits come out. We have four constellations. This is the the type of transformation from bits to symbols. We have great choices here, and DVB-S2X provides additional choices.

Four, there is a variety of spectral shaping available to us in DVB-S2. This is a really neat thing. You can change the pulse shape of a transmitted waveform in order to make it better suited for the radio environment it's expecting to be traveling through. Usually this means making it fit into a bandwidth better. You don't get something for nothing, though, so being too aggressive with the pulse shaping shows up in other aspects. Our particular shaping is different levels of raised-cosign filtering. DVB-S2X provides additional levels of shaping. 

Five, this standard lets us learn and develop with something very much like cognitive radio. As you can see, there are a lot of choices for coding and modulation. We can specify a fixed coding and modulation. This is called CCM for constant coding and modulation. In the past, people like us looked at a link, designed for the worst case solution, and used coding and modulation that would cover almost all the bases. DVB-S2 has CCM, but it also specifies something called variable coding and modulation, or VCM. The coding and modulation can be changed on a frame-by-frame basis in response to different station types or changes in the channel. In addition to that, there is something called adaptive coding and modulation, or ACM, where modulation and coding automagically adapts. This can happen on a frame by frame basis. 

DVB-S2 has things called annexes. In annex M, there's a specification for something we've already talked about wanting to do. We want to map the transmitted services or station streams into time slices and then recover information without having to demodulate the entire signal.

DVB-S2 follows the usual flow of having input data coded up to remove unnecessary redundancy, which is called source coding, and then it is put into one of two different stream types. Because DVB-S2 is designed for MPEG streams, it has a lot of mechanisms for MPEG data types, and I believe that this is the transport stream path in the drawing. We aren't going to use MPEG, so we fall into the generic stream category.

The functional blocks of DVB-S2 include these things in trapezoids. Mode adaptation, which starts to build up the data frames by constructing the right header to go with the data. Stream adaptation, which adds in the right amount of padding and scrambling. Forward error correction, which produces coded frames that are of one of two sizes. Mapping to constellations, which is the modulation. Finally, there is physical layer framing. An open question is how minimal of a station can be supported? Driving it down as low as possible is going to be fun and challenging. 

What we are anticipating is that the space teams will obtain an implementation of a DVB-S2X transmitter. Talks are already underway for this. Phase 4 ground is going to engineer the various DVB-S2X receivers. Standards documents are already in the repository and work is beginning. Get off the bench and hit the books!

So let's talk a bit about some changes in the uplink for phase 4 radios. We were MSK, or minimum shift keying, but we are now OQPSK, or offset quadrature phase shift keying. That is what the payload team is currently designing for. 

Like MSK, Offset QPSK has no more than a 90 degree phase shift at a time. This is good. In order to create this, you begin with a QPSK signal, where you take two data bits at a time. These two binary data bits make four distinct values. Each of these values are mapped onto four transmit phase shifts. 

For offset QPSK, the odd and even bits coming into the modulator have a timing offset, of one bit period. Hence the name. That means the in-phase and quadrature signals, the I and the Q, never change at the same time. 

The power spectral density of QPSK and Offset QPSK is the same. The shift in time doesn't effect that. 

Uplink experiments are beginning. We started putting together Team HackRF, which will investigate the use of HackRF SDRs as one of the phase 4 radio recipes. Lots of other experiments to work out other recipes for amateurs to experiment need to happen too. If you have a set of hardware and you want to work in parallel, then speak up. The USRPs will get into the act ASAP, some people have BladeRFs, and so on.

