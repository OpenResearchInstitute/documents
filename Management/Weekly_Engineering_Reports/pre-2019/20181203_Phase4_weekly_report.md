Testing 10GHz antenna structures for terrestrial, balloon, and satellite applications is part of what we do! 

Both existing and new 10GHz antenna designs are in progress for  use on a high altitude balloon. 

The goal is to transmit DVB-S2/X live video from a high altitude balloon. This tests transmitter, antenna, processing, and sensing. Next steps would be two-way communications on 10GHz.  

High altitude balloon antennas have uncontrolled yaw. The current requirements are inexpensive enough to lose,  hemispherical coverage, optimal gain at 70 degrees, some gain at 0 degrees (directly beneath the balloon). Circular polarization would be ideal. Otherwise, polarization tracking at the ground is required.

Four different quadrifilar helix structures were simulated that gave a reasonable pattern. The problem so far is that these are easily realizable at GPS or 23cm frequencies, but the dimensions will be unreasonably small at 10.45GHz.

Another new design is a patch array model. Most accessible papers at or near 10GHz for circular polarized patch arrays seem to be a record of capturing results of trial and error. This gives shapes that can be (in most cases) duplicated, but does not give a model that can be manipulated and edited to better match the requirements. 

Another aspect of the published work is the heavy influence of industrial and commercial requirements on antenna design. Very broadband designs that allow 2-3 or more bands are the goal. The pattern doesn't have to be great and the gain isn't that critical. When the device is held near, say, a body, then the pattern is messed up from the get go, so optimizing (and adding expense) is not generally pursued.

So, that's where we come in. We don't have the same motivations or requirements as a commercial antenna deployment. We do need this antenna to be inexpensive enough to lose. Balloon payloads (and satellites, and even terrestrial gear) are lost in accidents and failures.

Kent Britain's Vivaldi antenna is an existing inexpensive design scheduled to be integrated and tested with the payload.

You might be saying "Wait, Vivaldis are only linear polarized" and yes you would be right. A single Vivaldi as the downlink antenna would give the right pattern but linear polarization, meaning polarization losses on the ground. Mitigations would be a challenge. 

However, Vivaldi antennas can be made to be circularly polarized in combination.

To achieve this, two Vivaldi antennas are orthogonally placed. They are driven by a specially designed feeding network that creates an input signal with two-way signals that have equal magnitude and orthogonal phase. This can be done with PCB techniques. 

Next steps? Antenna simulation, building, testing, and flying!

Comment and critique welcome and encouraged. 

Volunteers of any level accepted and supported. 
