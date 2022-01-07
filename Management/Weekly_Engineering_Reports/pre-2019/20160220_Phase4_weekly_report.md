Hi, I'm Paul, KB5MU, in San Diego.

...and THIS is a HackRF One SDR board. Antenna on one side,  USB on the other side. 1 MHz to 6 GHz at up to 20 megasamples per second, transmit and receive. There's an ARM processor, and a Xilinx CPLD. It doesn't have the fancy FPGA like the USRP has, but it does work fine with GNU Radio flowgraphs, and it's  just three hundred bucks.

This week, "Team HackRF" has made some progress in establishing a development environment for this board, getting github to cooperate with us, and so on, getting on the air. Our mission is to evaluate, develop, and document the HackRF for use as one of a number of possible solutions for a Phase 4 Ground radio. 

On Thursday the 18th of February, two of us had a preliminary, relationship-building meeting with representatives of A-H-A Products Group. They have an FPGA design -- what they call an "IP core" in the industry -- that can transmit the DVB-S2X standard, which is what we've decided on for the downlink.  We think their IP core would be very useful in the spacecraft. Certainly for Phase 4B, probably for Phase 3E as well. And, the Cube Quest Challenge spacecraft would make great use of the low SNR modes added to the standard in the S2X Extensions. For ground station development, we hope to get a time-limited evaluation version of the transmitting side to use against our receiver implementation in the lab.

Millennium Space Systems has been working for a while on an "accommodation study", which determines whether our payload is compatible with their spacecraft, the primary mission. On Friday the 19th of February, MSS presented the results of this study to AMSAT, and everything looks good. "No impact" to the primary mission! That is really good news, and in light of that, we think the Air Force will very soon grant approval for our mission. Big milestone!

Next week, some of us from the Ground and Space teams will meet with Flex Radio for discussions about the possibility of manufacturing a version of the ground station radio, when it's ready. Other manufacturers and organizations are also being approached about this.

DVB-S2X has dozens of modes, combinations of modulation and coding. These are  in the standard, of course, which you can downloade from DVB.ORG, and read it, if you dare. But in order to keep track of all the modes and make it easier to do some calculations on each mode, we're preparing a spreadsheet, which has each mode on a separate line. Look for that to appear in the repository soon.

And now, some video and photos from the lab efforts to try to get a DVB-T signal transmitted and received on a HackRF, here in the lab.
