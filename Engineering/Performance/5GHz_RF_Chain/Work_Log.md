Notes for the Take This Job 5GHz RF Chain

16 October 2016

John Toscana lashed up a pair of the SkyWorks PA's in parallel with some
filtration. He asked NO5K to verify any increase in output power over
the less-than-expected results with a single PA.  
  
John working on a proposal to NO5K and K5TRA to build a PA mimicking the
SkyWorks design but with 4 devices instead of 2.  
  
Goal: closer to 7 watts than 1 watt.

Chuck AF8Z reports:

Here’s some thoughts of a “HiQ” PCB filter.

 

1.       Space out a quarter wave filter built on both sides of the PCB
so that the resonator rods are on both sides of the PCB and connected by
vias.  Add top and bottom covers hollowed out over the rods.

2.      Most of the field is in air so the dielectric losses are low.

3.      The precision metal work is on the PCB so the design is more
reproducible.

4.      Metal shields can be done at one of the maker shops

5.      Tuning can be added with a threaded tuning screw through one of
the covers.  Covers are identical and interchanable.

6.      High Q resonators are necessary.  Lower Q resonators work fine
in broader filters but the losses set a limit to how narrow the filter
can be.  I’m trying to think of a way to describe it so bear with me. 
The unloaded Q is set by the losses or Rp of a parallel tuned circuit. 
To get a wider bandwidth we transform the  up the load impedance to set
the new bandwidth.  As you go for a higher Q filter the transformer load
gets closer and closer to the unloaded Q or Rp.  Losses go up because a
higher proportion of the signal current goes through Rp than Rload. 
When Rload is higher than Rp the Q doesn’t go up.

 

I need to play with a model for a bit to see what I can do.

 

Failing that a half wave microstrip filter on RF material (for
consistency) or even a SIW (substrate integrated waveguide) filter are
alternatives.

 

Chuck AF8Z
