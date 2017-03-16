It came from outer space!

Actually, it came from Slack. 

This is Julian KF4MOT with a proposal for 5GHz RF. Link to his proposal is in the show notes.

https://phase4ground.slack.com/files/julian_kf4mot/F4HU975AT/5cm_1w_r0.zip

Julian's intent here is to take the output of any SDR, ranging from the -10 dBm HackRF to the +10 dBm Ettus B200, run it through an appropriate attenuator network for levelisation, and create a filtered and amplified output at the 20 dBm level to further drive another board to 40 dBm. He suspects choosing a correct attenuator value will be important since overdriving the amp will create harmonics, and that second harmonic is the one we really need to avoid.

The signal path is SMA input > amp > filter > amp > filter > amp > SMA output

Substrate is 62 mil FR4. The wildly varying dielectric constant <horrors!> shouldn't matter since both filters are tunable and the estimated 0.5 dB/inch lost in the substrate should be more than made up for with all the gain on this board. None of the other elements on this board are critical.

He has some ideas for filter tuning to make it easy for those without fancy test equipment, and he considers that critical to the success of the project. The SDR could be used either as a signal source or as a receiver with appropriate attenuators.

He wants to test this out before publishing a recommended method, but he plans to try a cheap 8 GHz power meter and a noise source in combination with the SDR as either a signal source or spectrum analyzer to see if he can come up with a good consistent method.

A simple power out indicator was included on the board. It just lights the LED when the output hits the roughly 20 dBm level. It could be made more complex/informative in a future board revision if testing and use deems it a useful thing.

Board dimensions are roughly 2x4 inches. It wasn't made to fit any particular enclosure, but instead sized to fit the limitations of a low cost board house. Julian's intent is that this board could be mounted close to the SDR, while the big PA could be mounted close to the feedhorn to minimize feedline losses. That's not set in stone though. Probably most any combination of positioning should work so long as feedline losses are accounted for. 

He'd like to take a couple more days to compare the schematic to the gerbers since according to Julian, Upverter allowed him to make some pretty serious mistakes without any errors or warnings. After that process, and any feedback you have for him, if there are no comments, complaints, or suggestions then he'll place the order. Probably a qty. of 20 since the price won't be any lower for a lesser volume. Should take a couple weeks to get them.

You can't see the 3/4" pipe cap filters soldered to the bottom layer, but Julian promises they're there!

Anybody have recommendations for a board house that does RF substrates? Julian has been planning to send an email to my normal board house (eteknet) but he hasn't got around to it as of this recording. He is leaning to Rogers 4350 but I'm open to others. Really, any substrate with consistent Er that doesn't cost an arm and a leg. 

So please review the design, give feedback on the filter tuning, dimensions, assumptions, board house recommendations, and anything else you see that would improve this part of the project.

And beware the Ides of March!