Greetings all!

First, there is a dual-band feed design update from Paul Wade W1GHZ.

He reports that what he’s come up with looks like it would work pretty well for an offset dish like the DSS dishes, with good efficiency at both bands. Simulation says the isolation from 5.8 GHz to the 10 GHz port is about 80 dB.

Performance plots are attached. He is going to work up a sketch for 3D printing.

He recommends a filter (like the ones in his QEX articles) that can easily provide 60 dB of second harmonic rejection. He believes that the second harmonic from any decent amplifier is 20 or 30 dB down, so that's at least 80 dB down. Unless the signal is actually inband, a signal that far down won't hurt.

He added that as for push-pull amps, we may be underestimating the difficulty of keeping them balanced at microwaves. Using a push-pull amplifier as part of the dual-band solution may not provide the performance we need.

Second, there's plenty of action in the transmitter RF chain with results from measurements at the VHF super conference. Thank you to Eric Nichols, Mike W4UOO, John Petrich, W7FU, John Toscano, Mike Seguin and several others for stepping up to volunteer on this part of the project. We'll be increasing our use of google forms to coordinate parts of the project,  maintaining a list of all the forms on github, and possibly setting up a webpage to increase project findability. 

Third, San Diego Microwave Group demonstrated the results of a project that Drew and Kerry Banke have been working on these last couple of weeks. It is the combination of a $4.24 Arduino processor board with a $29 ADF4350 PLL board to provide a programmable fixed  LO in the 137-4400 MHz range. Once programmed, this set of off-the-shelf boards comes up on frequency at power up. The programming software utilizes the Analog Devices ADF4350 evaluation software to calculate the PLL  data. This is entered by hand in to an Arduino program(sketch) written by Drew. This then is uploaded to the Arduino and that's it. Kerry reports that the software is easy to use and free. Check out this video report from Paul KB5MU.

-Michelle W5NYV