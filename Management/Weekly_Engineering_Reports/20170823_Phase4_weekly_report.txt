Greetings!

Today we're talking about correlators. 

Correlators help us find patterns in data streams. This is a very common function in digital communications. Why? 

When we send a stream of digital data over a wireless link, we have no way of knowing in advance when the snapshots of digital data were made, what phase of the carrier we're dealing with, what the exact frequency is of the carrier, the path delay, and where in the frame we are. That sort of thing. 

This is why receivers are more complicated and more difficult to design than transmitters. An entire class of circuits and solutions for what's called the synchronization problem exists because we have to figure out the best time to take our snapshot of the received signal symbol in order to get the bits. You want to sample when the received signal is definitely 1 or definitely 0, not when it's crossing over to the other value or off peak by enough to where you're not sampling anywhere close to the point where the value was set. We then have to maintain that symbol timing throughout reception. Once we know we have good symbols, then we have to figure out the edges of the frames or packets or whatever other structure the protocol has.

Essentially, once we get received symbols we need to figure out where in the data stream we are. Looking for known patterns that are periodically sent in the signal is a common way to solve this problem. 

Our desired correlator is a block or circuit that looks for the known pattern of symbols that occurs at the start of every DVB-S2 frame. This pattern is called the Start of Frame. It is defined in the standard for DVB-S2. The start of frame is 18D2E82 in hex. For DVB-S2, the modulation for the PLHEADER is pi/2 BPSK. 

It looks like that we need our own correlator block. 

Why? We have a very specific case of correlation, the existing correlation estimator block in GNU Radio could change out from under us again, and we have a general idea about how challenging synchronization will be, and we have to receive pi/2 BPSK. 

There's a rule in the DVB-S2 spec that describes what this modulation looks like. 

So how is correlation usually done? Your correlator looks at the incoming received symbols. You have a pattern you are looking for. You take the dot product of some number of those symbols with the pattern and integrate. If the result is above a threshold value that you have set, then you declare victory. 

This could be a fixed threshold. Or, the threshold could be dynamically chosen based on the noise in multiple samples surrounding the peak. For low SNR and wide band modes, this dynamic adaptive method offers better performance. The desired signal with the Start of Frame is like 2 dB below the noise, and our signal is wideband. Low signal to noise ratios and wideband signals mean a dynamic or adaptive threshold approach is probably what we should be doing.

The current correlation estimation block in GNU Radio implements a dynamic logarithmic approach. It uses a constant false alarm rate approach, where the probability of false alarm is negative log times the quantity of 1 minus a threshold. A detection happens when the magnitude is greater than 4 times the probability of false alarm times the average of the magnitude of the noise in the surrounding samples. Source code for this implementation can be found here https://github.com/gnuradio/gnuradio/blob/master/gr-digital/lib/corr_est_cc_impl.cc

From discussion on GNU Radio github, there are some unresolved concerns with this block for the following reasons.

Lack of documentation, the factor of 4 seems arbitrary, the averaging time constant may not work as intended, and if you get a value of threshold equal to or greater than one, then your negative log produces some problematic numbers.

Given that we need a block, we learned how to make one. 

There is a very useful GNU Radio Block Coding Style Guide https://wiki.gnuradio.org/index.php/BlocksCodingGuide

There is a very helpful set of guided tutorials from the GNU Radio website. https://wiki.gnuradio.org/index.php/Guided_Tutorials

There's a tool called gr-modtool that sets up a module and adds blocks to that module. In GNU Radio a module is the category and the blocks that belong to that category are in the module. Blocks do specific DSP functions. The module contains the blocks. The name of the module shows up in GNU Radio Companion as the category header for the blocks it holds. 

Using gr-modtool is relatively easy. It sets up the right directory structure for you and it provides templates in either python or c++ for the implementation of your block. I'm not going to duplicate the tutorial here. Find this specific tutorial here https://wiki.gnuradio.org/index.php/Guided_Tutorial_GNU_Radio_in_C%2B%2B

If you walk through this tutorial you will be well on your way to being able to code GNU Radio blocks. 

After doing the tutorial a couple of times, we attacked the problem of demodulating pi/2 BPSK, since in order to do the correlation we have to get the correct received symbols. 

We started with the definition in the spec.

"SOF shall correspond to the sequence 18D2E82HEX (01-1000-....-0010 in binary notation, the left-side bit being the MSB of the PLHEADER)" 90 degree BPSK, so in complex notation, it's…

"The PLHEADER, represented by the binary sequence (y1, y2,...y90) shall be modulated into 90 π/2BPSK symbols according to the rule:
 I sub 2i-1 = Q sub 2i-1 = (1/√2) (1-2y sub 2i-1), I sub 2i = - Q sub 2i = - (1/√2) (1-2y sub 2i) for i = 1, 2, ..., 45 "

The information seems to be encoded as the direction that the vector moves, whether 90 degrees clockwise or 90 degrees counterclockwise, at each clock tick. The signal does not stay in the same quadrant. That would be considered an error and erased. The signal does not move 180 degrees across the center. That would be an erasure as well. The signal moves either clockwise or counterclockwise depending on whether it is encoding a zero or a one. 

This really needs to be reviewed to make sure we interpreted it correctly. Code for this block can be found at the following repository and discussed in the code review channel in Slack. https://github.com/phase4ground/correlator

Once we thought we understood the way pi/2 BPSK worked, we wrote quality assurance test code. The gr-modtool sets up unit testing templates for you, so that you can test first like highly evolved and successful programmers always do.*

Then we wrote some demodulation code. It didn't work. We wrote more. It didn't work either. QA tests kept failing. We went back to the drawing board and realized that it would never work. We proved that the problem couldn't be simplified combinatorially. We then wrote a table lookup for the combinations of previous and current symbols. Here's the table we started with and went back to.

I_previous	Q_previous	I_current	Q_current	Result
0		0		0		0		erasure
0		0		0		1		clockwise
0		0		1		0		counterclockwise
0		0		1		1		erasure
0		1		0		0		counterclockwise
0		1		0		1		erasure
0		1		1		0		erasure
0		1		1		1		clockwise
1		0		0		0		clockwise
1		0		0		1		erasure
1		0		1		0		erasure
1		0		1		1		counterclockwise
1		1		0		0		erasure
1		1		0		1		counterclockwise
1		1		1		0		clockwise
1		1		1		1		erasure


We receive a series of complex signal snapshots. We establish a history, where we tell GNU radio that we need to keep track of the previously received complex signal along with the current one. This means we use the set_history function in the constructor. The history value is 2. We need the previous signal in order to tell which direction the signal moved and whether or not that move was valid. 

In our complex signal world, the previous result and the current result are each composed of a real and imaginary part. The real and imaginary part are floats. 0 is positive 1.0 and 1 is negative 1.0

Clockwise is positive 1
Counterclockwise is negative 1
Errors are erasures and result is set to zero. 


The lookup is achieved by taking the signs of previous I, previous Q, current I, current Q with the signbit macro, and converting those sign bit results into an integer by multiplying by place values 8, 4, 2, and 1. There's a trick to using the sign bit this way, and it's a double bang. Check it out.

After some more tests, we realized that the set_history function didn't work exactly the way we thought it did. We adjusted our thinking and fixed the indexing and it passed the tests.

Assuming that the demodulation is correct, the next step is to take our start of frame and look for received patterns that match it. When this happens, we produce a tag. Tags in GNU Radio are synchronized bits of information that are attached to samples. It's metadata that can be used by other blocks. For this block, we are going to follow the conventions in the general correlation estimation block. This means that there will be several tags that can be used by downstream blocks that need them and have already implemented functions that consume the tags.

The list of tags that we are looking to produce are corr_est, phase_est, time_est, and amp_est. They stand for Correlation Estimate, Phase Estimate, Time Estimate, and Amplitude Estimate. 

Amplitude Estimate provides a scaling factor for the input stream to normalize the data to +/- 1. We think of this as AGC. An older implementation of correlation block in GNU Radio required incoming samples to already be normalized by an external AGC block or function. It now appears to be built in, and we're going to do the same. 

Phase Estimate is the calculated phase offset of the incoming signal. It's determined by doing a cross-correlation. Time Estimate seems to be the frequency error, but we haven't looked at this as hard as the others. Correlation Estimate is a tag that shows exactly where the start of the correlated symbols are.


*Yes, we seriously wrote the unit test first this time, like you're supposed to. It helped! Learn more about test driven development here: https://en.wikipedia.org/wiki/Test-driven_development
