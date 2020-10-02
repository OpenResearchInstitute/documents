Greetings!

Today we're talking about correlators. 

Correlators help us find patterns in data streams. This is a very common function in digital communications. Why? 

When we send a stream of digital data over a wireless link, we have no way of knowing in advance when the snapshots of digital data were made, what phase of the carrier we're dealing with, what the exact frequency is of the carrier, the path delay, and where in the frame we are. That sort of thing. 

This is why receivers are more complicated and more difficult to design than transmitters. An entire class of circuits and solutions for what's called the synchronization problem exists because we have to figure out the best time to take our snapshot of the received signal symbol in order to get the bits. You want to sample when the received signal is definitely 1 or definitely 0, not when it's crossing over to the other value or off peak by enough to where you're not sampling anywhere close to the point where the value was set. We then have to maintain that symbol timing throughout reception. Once we know we have good symbols, then we have to figure out the edges of the frames or packets or whatever other structure the protocol has.

Essentially, once we get received symbols we need to figure out where in the data stream we are. Looking for known patterns that are periodically sent in the signal is a common way to solve this problem. 

Our desired correlator is a block or circuit that looks for the known pattern of symbols that occurs at the start of every DVB-S2 frame. This pattern is called the Start of Frame. It is defined in the standard for DVB-S2. The start of frame is 18D2E82 in hex. For DVB-S2, the modulation for the PLHEADER is pi/2 BPSK. 

It looks like that we need our own correlator block. 

So how is correlation usually done? Your correlator looks at the incoming received symbols. You have a pattern you are looking for. You take the dot product of some number of those symbols with the pattern and integrate. If the result is above a threshold value that you have set, then you declare victory. 

This could be a fixed threshold. Or, the threshold could be dynamically chosen based on the noise in multiple samples surrounding the peak. For low SNR and wide band modes, this dynamic adaptive method offers better performance. The desired signal with the Start of Frame is like 2 dB below the noise, and our signal is wideband. Low signal to noise ratios and wideband signals mean a dynamic or adaptive threshold approach is probably what we should be doing.

The current correlation estimation block in GNU Radio implements a dynamic logarithmic approach. It uses a constant false alarm rate approach, where the probability of false alarm is negative log times the quantity of 1 minus a threshold. A detection happens when the magnitude is greater than 4 times the probability of false alarm times the average of the magnitude of the noise in the surrounding samples. Source code for this implementation can be found here https://github.com/gnuradio/gnuradio/blob/master/gr-digital/lib/corr_est_cc_impl.cc

From discussion on GNU Radio github, there are some unresolved concerns with this block for the following reasons.

Lack of documentation, the factor of 4 seems arbitrary, the averaging time constant may not work as intended, and if you get a value of threshold equal to or greater than one, then your negative log produces some problematic numbers.
