The Problem is Pointing

Large powerful telescopes with small field of view can be hard to point
at any particular star. The way astronomers have overcome this challenge
is to use a spotting scope. The spotting scope has less magnification
and light gathering ability but a wider field of view. It allows one to
see more of the sky, become oriented to the area being observed, and if
the spotting scope is aligned well enough with the primary scope, then
the primary scope can be accurately pointed based on the assist from the
spotting scope. Of course, this depends on the existence of bright stars
in the vicinity of the object to be observed.

Phase 4 radios can be used with a variety of antennas. We’re assuming
that a common use case is that they will be used with a DirecTV dish on
the order of 60cm in diameter. The beamwidth of this class of dish at
10GHz is 3.3 degrees. Pointing a Phase 4 radio dish at the satellite
with a 3.3 degree beam width can be challenging. It’s a task roughly
equivalent to pointing a DirecTV dish at a DirecTV satellite. The Phase
4 ground team would like to minimize the difficulty of antenna pointing.

One way to make pointing less difficult is to use the equivalent of a
spotting scope: an antenna with a broader beam (and thus lower gain).
There are several ways to achieve this. One can defocus the main dish by
moving the feed. One can also make the dish effectively smaller
(under-illuminated) by using a feed with narrower coverage. Or, one can
literally emulate the concept of a spotting scope by using a smaller
antenna, like a patch antenna, mounted at the side of the main dish.

The baseline design for the Phase 4 downlink is a single
time-multiplexed signal 10 MHz wide at a certain power level. The ground
station needs a 60cm class dish in order to receive and demodulate such
a downlink signal. It cannot be received with a much lower-gain antenna.
We only need to detect it, not receive it, but with a simple broadband
data modulation there’s no obvious trick to detect it with the spotting
antenna.

However, we can make a simple modification to the downlink signal to
make detection extremely easy. If we allocate a small percentage of the
downlink time to emitting an unmodulated carrier instead of the 10 MHz
wide data signal, it becomes quite detectable with a very low-gain
antenna. With, say, an antenna with only 6 dB of gain, the operator
could easily eyeball the correct pointing within a 90-degree sector. The
operator would then use a simple signal-strength indicator to peak up
the signal to get fairly accurate pointing. With some experimentation a
suitable antenna design could be developed that is able to detect the
carrier signal without much pointing and also able to peak up with
signal within 3 degrees or so, close enough that the main dish can
detect the signal.

Once we have allocated a chunk of the downlink time to this acquisition
beacon signal, can we do anything else useful with it? A quick
inspection of the link budget suggests that we can modulate the beacon
signal with low rate data without significantly impairing its function
as a pointing aid. For the sake of argument, let’s say we can put 1000
bits per second of data onto the acquisition beacon. That’s not a lot of
data, but it could still be useful.

One possible use for the beacon data would be to provide the ground
terminal with information it needs before it can receive the main
downlink data. This might include information about what mode the main
downlink is currently in, if there are ever multiple modes. It could
include time of day and orbital parameters for the spacecraft, in case
the ground station finds it convenient to compute the precise pointing
angles rather than search them out. It could include a unique identifier
for the spacecraft, against the day when we have a whole fleet of Phase
4 spacecraft. Probably none of this information is really required for
the baseline design.

The details of spacecraft access control have yet to be worked out, but
a basic requirement is that access to the spacecraft be limited to
authorized stations, at least in a special emergency mode. It might be
useful to initialize the authorization procedure with some sort of
cryptographic challenge in the broadcast data.

It can also serve as a broadcast channel for textual data. This could
include satellite operational bulletins, like notifications of emergency
situations that restrict access to the satellite. It could include
routine AMSAT News Service bulletins, or anything else of general
interest. These bulletins can and should be carried on a data channel in
the main data stream as well.

As a side effect, this modification means that stations that are not
able to deploy a 60cm dish can still get some good out of the satellite.
A much smaller, more portable, less expensive station could at least
receive the beacon. For an amateur radio service mission, this is much
more valuable than it might seem. It gives an easy way to get involved,
and could serve to generate a lot of extra excitement in the amateur
community.

Now, what can we do to make that smaller station even more useful? What
if there was also a low-rate uplink channel? Adding stuff like this to
the mission makes it harder to implement and harder to explain, but it
might be worth it. We think it’s worth investigating further.
