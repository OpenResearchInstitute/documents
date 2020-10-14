# Engineering Report for 16 October 2020



The NASA Ames Small Satellite Webinar
13 October 2020
1300 - 1500 US Eastern Time

These were lightning talk format and TTP aimed. 

Ames is a heart of smallest information and has a virtual resource center with a lot of information. 

technology.nasa.gov
smallsat-institute

Presenter 1 Paul Wercinski
ADEPT project
Transformable heat shield umbrella style with a diameter greater than the launch vehicle. Prototyping and ground testing photos were shown. 1 meter diameter target size. The technology key is the performance of the carbon fabric. Intended for entry vehicles for planetary problems. 

Here we see another GoPro in Space, like we have been seeing consistently from NASA for many projects. 

Drag skirt to orbit. 1 meter to 23 meters is envisions. 20 ton payload to Mars envisioned. This is described as a "push" technology and is JPL-related. Cost vs. performance? This fills a niche. Higher cost vs traditional rigid heat shields, but it can be used in situations where the rigid heat shield is not available. 

Presenter 2 Don Soloway
EM Monitoring and Control of a Plurality of Nanosats
Relative motion control of a cluster of nanosats using electromagnets for control actuation. 

Patented. 

Magnetometer for relative position determination "designed and built not fully tested yet" therefore fails the Klein Gilhousen test, but obviously is far enough along to get into a webinar at Ames. 

Now, why is this really neat? It's non-propellant based. Solar panels can be the source. No reaction wheel. No moving parts. Something about single dipoles. No costly position determination systems. Magnetometer for relative position determination. It's mm accurate. 

Tumbling => detumbling => separation of combined nanosats into individual nanosats => individual pointing

For example, multipoint earth observation nano sat cluster constellations. 

3 DOF simulation developed. Hardware for that demo was shown. 

Maximum separation with demo hardware is 1 meter. The software for the simulation was MATLAB.

Power requirements? Speaker dissembled somewhat. 

Alternate commands to mitigate field effects. First one pole, then the other, then back again, etc. 

Speaker 3 Rick Alena
Heterogenous Spacecraft Networks (HSN)
NASA/ESA/JAXA 
"Open Spacecraft Network"

But we immediately started talking about Patents. Granted in February 2018. 

Open Operation Architecture (open but patented)

Simultaneous and complementary data collection and distribution. No details. "distributed virtual operations centers"

Why is this cool? Because you can:
Fly your own coordinated satellites in this cluster. 

NASA TechEdSat is the demo satellite series. 

ISS orbit used Iridium to communicate back and forth to do telemetry (802.15.4)

Q: Can this work with Starlink?
A: What we're finding is adequate link margin and views with these commercial protocols. Globalstar, Starlink, we look at their characteristics, decide if they can support cubesat missions. Emerging forms might provide support to cubesat missions. There exist regulatory issues that must be addressed in the spacecraft license. But everyone has to do this, so the speaker thinks that's ok. 
Looking at protocols, long-range LoRa is next.

Terrestrial protocols are designed to co-exist or adapt. 

This is why we use DVB-S2/X/T2. 

Q: um, cybersecurity?
A: Security is totally ok! What could possibly go wrong? (yeah, well, they don't think it's an issue)

Q: Mobile ad-hoc networks?
A: DTN and other similar networks are already self-managing. What could go wrong?

Uses cFS and arduino and Linux. 


Speaker 4 Red Chirayath

Fluidcam
MIDAR

Next generation technology for ocean mapping. 

2 patents. Patents again. 

Motivation? Only 6% of the ocean floor is mapped. Wow!

100 meters is all you get penetrating the ocean with visible light. 

Red applies astronomy techniques to the ocean. Distortion is cruel with water. But there are techniques to mitigate. 

3 meter resolution is about as good as it currently gets. But, we can do better, and we can use these techniques from space. 

Hence, Fluidcam!

Swimming pool example in the webinar. Wave dynamics and reversing the functions. 

Cubesats limit the light-gathering capacity of the cameras, but we can get a lot done with Fluidcam. The demos was in tropical clear water and I think we were trying to measure coral growth and depth. 

MIDAR is multispectral imaging. Examples were 7 channels. Main advantage? Electrical efficiency using LEDs and such is very good.

So, I did a color detector in college with 8 LEDs and a photo-diode connected to an 8051. I lit up each LED and measured the result under a dome to make the sample otherwise dark. This is essentially the exact same thing, done from a cubesat.

Processing is a big deal. Doing more on board is desired. Ved said that it could get up to 10 GB per second of data generated, and the processing ran at a 1:10 ratio of data:time.

The previous MIDAR were on aircraft, and aircraft can carry big computers, so offline processing wasn't that big of a deal. Just take out the hard drive and set it aside for later. Cubesats cannot really do this easily. 

This is an area where I didn't quite follow if any details on "how" were revealed, but it sounds like they are doing a lot more number crunching on station, or need to do a lot more number crunching.

Questions ranged from "can this be used for human tissue to catch cancer" to "can you find wrecked ships". 


Speaker 5 Stevan Spremo

First Part:
Low Cost Star Tracker Overview

Software costs reduced by an order of magnitude. Works great in the lab. LEO tuned. 

Restrictions because export controlled.

10 arc second precise with an 8 degree field of view. Commercial versions of star trackers cost several hundred thousand dollars. 

This demo was done with a Lumenaera LW230 monochrome machine vision camera with FujimonHF355A-1 35mm lens. 

LEO low cost, assumed 6 month missions. Quaternion solutions. 

Patented.

Second Part:
Cost optimized test of spacecraft Avionics and tech (COTSAT)

Spacecraft software architecture overview.
Pressurized environment for your circuits to snuggle in! This is supposed to drop the cost. Again, export controlled. 

Software and hardware are scaleable. 

Q: What about proprietary components hooked up to your software bus?
A: Um, yeah, about that, there will have to be retail transactions and contracts and customization. 

Q: Testing? Ruggedization?
A: audience pointed to a podcast from www.techbriefs.com for more information. 

Speaker 6 Arwen Dave

Affordable Vehicle Avionics (AVA) Overview.

Credit to team.

COTSAT sparked project. People have trouble finding rides. So, how about reducing the cost of avionics? Sounds like a good idea. 

This is a set of hardware, software, and methods that go together. It requires a lot of participation from the point of view of the "customer". 

COTS sensors, but they use a common filter to guide launch vehicles. 

Mass reduction of the avionics achieved was 5kg to less than 1kg over time. 

Cost of avionics reduced from $500,000 to $6,000 for components.
Cost of avionics reduced from $1,000,000 to $42,000 for software.

Method/user driven. 

Nanosats can ride to LEO as primary payloads. 

2 flights to test 2018 with ADEPT (see earlier) and 2019. Spin stabilized, took over from default, controlled the flight, then handed control back. 

Licensees will be taking on a lot of risk to finish this project's next steps out. 

Tailored to a specific vehicle. 


Speaker 7 Peter Goorjian

Space Opticals for LEO and Low Lunar Orbit (LLO). 

Lens arrays + VECSEL/photodetectors. 

Optical multiple access wavelength division multiplexing.

Discussed LunaNet and LLO 100km LunaNet. Computer sims have been done. 

There was a lot of very very very long reading of slides.

Dr. Govind Agrawal mentioned.

980 nm and 850 nm are the current areas of study and development. Previous work used 1550 nm. 

Cluster or array draws 150mW of power. 


Speaker 8 Shak Ghassemich

Nanosat Launch Adapter System (NLAS) 

Can handle up to 24U. Compatible with P-POD, stackable, and has an advanced and capable sequencer. Internally powered with very accurate timing, which apparently is super important. 


