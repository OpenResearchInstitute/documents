Welcome to the Phase 4 Weekly Report for 9 March 2018!

Video report at: https://youtu.be/1GirCiB5XNg

An ASCENT Conference Call Part 2 on Careful COTS of a Powerful SDR is proposed for 14 March 2018.

Phase 4 Space organized and hosted an ASCENT conference call on 28 February 2018 with Nate Temple and Neel Pandeya from Ettus Research. The purpose of the meeting was to explore the idea of a careful COTS of the E310 and X310 Universal Software Radio Peripheral (USRP) devices. 

Nate and Neel described the USRP lineup, gave a brief history of Ettus Research, and expressed their enthusiasm for an effort in this direction. 

The most significant action item resulting from this meeting was to include additional Ettus Research personnel for business planning and engineering scoping. 

One engineering possibility discussed was to revisit and re-activate the Tritium line as a base design. Phase 4 Space is interested in a part at least as large as the 7045, and is interested in using the UNISEC electrical bus standard. The Tritium was not productized, and is not on the current Ettus Research product roadmap, but was demonstrated at GNU Radio Conference and other events. 

Since the initial conference call, several conversations have occurred within Ettus Research, and a conclusion has been reached. Ettus Research is unable to provide resources or support for Tritium. This design will not be released for a careful COTS redesign. It was never fully productized and has been retired (EOL'd). The code supporting it has bit-rotted badly and will not be released. 

However, Ettus Research can provide support for E310, E312, X300/X310, and the upcoming E320. The support is given enthusiastically as those are active current products. Support in this context means technical and engineering advice, primarily from Neel and Nate. 

It is not yet clear whether Ettus Research could provide either the Gerber files, or the full bill of materials (BoM), or both, for the E310/E312/X300/X310/E320. 

Given that re-layout is going to be required for thermal and size reasons, the Gerber files may not be necessary, and only the full BoM would be needed. A full BoM would be easier to release than Gerber.

An NDA would be required in order to use the BoM. 

So in between now and then, what can we do? Well, we can start a layout with what we know from the schematic. 

The question now is, which schematic?

E310, E312, X300/X310, or E320?

Zach Leffke wrote to the Phase 4 mailing list about his experience with the E310 at Virginia Tech. I'm going to read the whole thing because there's a lot of good stuff in here. You can skip ahead to <timecode> to pick up after the email. But, please enjoy these photos of kittens during this narration. 

"FYI, I've now put 3 E310 USRPs in Space aboard sounding rockets via the Rocksat-X project.  They survived 20+ Gs at Launch, so are plenty sturdy.  They were only 'in space' for about 5 minutes, in a sealed enclosure (so maintained pressure, temperatures were actually pretty warm from the launch friction) but performed excellently from an RF perspective.  No attempt to use the onboard GPS or IMU in the E310, the rocket made it to Mach 5, and went 100+ km in altitude, so we suspected the GPS would fail either do to the ITAR velocity/altitude restrictions on GPSs or would fail to lock up due to excessive speed and the fact that its in a metal tube all the way up until just before apogee, requiring a cold start when the skirt separates and the payloads 'go active' (would take to long to lockup to be useful information as the payloads were only 'on' for less than 5 minutes).  I've heard rumors from a source I can't cite that they perform miserably in high radiation environments though in their 'off the shelf' configuration.  Not sure what the actual failure was, but I suspect the power conditioning, not the Zynq.  Hence the desire for the lighter weight, radiation hardened AstroSDR from Rincon, which is essentially a singleboard E310 without all the extras that aren't needed for Space.  We also launched a Kuhne Electronics S-Band PA and it also performed surprisingly well in those extreme conditions.

Not sure if you are planning to launch an E310/E300 or just using it for development but either way watch out for the following gotcha:

There is a funky firmware bug in the microcontroller (as of about a year ago, might be fixed now) that controls the boot process.  Basically, the default mode is for the E3XX to boot when the power button is pushed.  You can override this in the OS with by setting a flag bit with a simple 'echo 1' type command that will cause it to boot when power is applied to the DC power port.  However this bug will rear its head every so often and somehow the microcontroller will overwrite that boot flag bit and revert back to booting only when the power button is pressed.  Not sure how an off chip microcontroller can affect a memory location accessible to the host OS in the Zynq and vice versa (shared memory location somewhere?).  VERY annoying when you have everything all buttoned up inside a payload and you have to figure out a way to snake an ethernet or USB cable in to reset the bit.  The number of power cycles before the 'revert' is random, but I've never seen it revert with only 10 power cycles or so (sometimes it takes 100 or more, sometimes 20 is enough, hence I call it 'random').  

Our fast solution, the day before the payload was delivered to NASA (we found it way late in the development cycle about a month before the payload was delivered) was to sit there and power cycle the payload over an over an over again until the revert happened.  We then buttoned everything up, did one more test (increment power cycle count by 1) and handed it over to the integration folks at Wallops.  The students doing the integration with the rocket kept careful track of how many power cycles the payload went through during integration (our last test, initial checkout at Wallops, GPS rollout, etc.).  That number (I think about 5 times, can't remember now, definitely less than 10) translated directly to our pucker factor on launch day, with lots of 'I hope it boots up' muttering.  We actually had two E310s in the 2017 payload, and both displayed the same behavior relative to the boot issue (with different number of power cycles between them before the revert).  In the end it worked.

I found one obscure post about the issue on a board somewhere (I'd have to dig out my notes for the link) that referenced the issue.  Someone from Ettus had a recommended microcontroller firmware hack to re-flash the microcontroller with a couple of changes to the code (commenting out an if statement somewhere I think) that would permanently disable the 'boot from button' mode and always cause boot when power was applied to the DC port.  We were too close to launch, and too unskilled with the microcontroller re-flash process to attempt the patch (didn't want to brick the payload in the weeks leading up to delivery).  I believe he said they acknowledged the bug and that they would try to incorporate a fix in the next firmware release, not sure if that happened or not.

-Zach, KJ4QLP"


GNU Radio Conference 2018 tickets are available:

https://www.gnuradio.org/grcon-2018/

The whole conference is packed with wonderful experiences and fun.

Come join Phase 4 Ground at our DVB-S2 and DVB-S2X workshop and hackfest on Friday! Presented by Open Research Institute, Inc. with a goal to produce an open source DVB-S2/X receiver in GNU Radio primarily for AMSAT. 

Please share with whoever you think would love to come! There will be a new user track as well as advanced content, workshops, vendors, demonstrations, and multiple social events. 



