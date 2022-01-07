We kick off this week's report with two demonstrations of DVB-S2 transmission from the LimeSDR. The first from Charles Brain G4GUO, and the second from Paul KB5MU and Michelle W5NYV. Charles has live video and Paul and Michelle are transmitting a pre-recorded work of art called Adventure Time. 

Mike Seguin N1JEZ has some LimeSDR spectral analysis to report. 

First, 850 MHz Phase Noise 10 kHz offset 1 kHz resolution bandwidth

-58.36 - 10LOGBW = -88.36 dBc/Hz

If I read the LMS7002M Spec sheet right, it should be down around -96 dBc/Hz? PDF is in the Phase 4 Ground Github link is in the show notes. 

https://github.com/phase4ground/documents/tree/master/Engineering/SDRs/LimeSDR

Second, 2850 MHz Phase Noise 10 kHz offset 1 kHz resolution bandwidth

-49 - 10LOGBW = -79 dBc/Hz spec around -87 dBc/Hz?

Third image is at 2850 MHz +/-200 kHz

Check out those curious 200 kHz spurs

Fourth image is 2850 MHz 100 MHz Span

A broader view - we need to go digging deeper.

Final image is 2850 MHz 388 kHz spur

small spur on the low side?

Output power varies. He's seen upwards of +15 dBm. He is powering the LimeSDR board off an external supply.

He is using LimeSuite to set up the transmit output on TX1-1. There are so many settings it's possible/probable we're missing something.

He has also have done rudimentary noise figure measurements. Paul, W1GHZ loaned him a homebrew noise head he had built from his QEX article in 1996? on Noise Figure. He used it to measure the NF, but had to rely on a chart for ENR. So assumptions!!! He found he definitely had to use a preamp in front of the Lime. He used an AD6IW wideband pre for testing.

"I need to do more real world tests on the bands…." -Mike Seguin

In the next segment of this report Paul described how to use the examples folder in GNU Radio to get to the DVB flowgraphs we've been using for experiments. 

Charles G4GUO shares his plan for next steps for DVB-S2 receive. He is looking at how to do the front end that finds the start of a frame and compensates for frequency error. He is pondering how to do this and has some ideas. He also has the low density parity check (LDPC) decoder to do but has not yet planned it out. He has the BCH decoder done and the bit that decodes the preamble code FEC.

Charles explains that the whole of DVB-S2 has been designed for the parallel processing powers of ASICs/FPGAs/GPUs. He has decided to attack the problem using GPUs. 

He asserts that GPUs don't have such a steep learning curve as some of the other technologies. He believes that the symbol tracking and root raised cosine filtering is best done in the FPGA on the LimeSDR. His thoughts are to re-write some of the Lime code so he can alter the ADC sample rate in fractions of a symbol. Then use the host to calculate the timing error and send the correction to the Lime FPGA code. The Lime can also do fine frequency error correction using a complex mixer. The error can be calculated in the host from the phase change in the preamble sequence. 

The central question is how to fit it into the memory model of the GPU to keep all the threads fully occupied. This means properly balancing the combination of LDPC decoding, parallel thinking and NVIDIA GPU programming. One of the many questions he has is how to cope with the final XOR of the parity bit for each block as that makes every bit in the whole thing dependent on every other bit. He believes that there must be a short cut so you can break the problem at the receiver down into a load of independent blocks (divide and conquer).

It is all very DVBS2 specific but when a sub block of the code meets a condition where all its parity check equation are correct it can be marked as finished and the decoder can then move on to the next sub block. It requires a lot of thinking about and Charles welcomes your feedback. 

So! Lots of programming! We are here to help with this effort! It's going to be a big one. 

Please join AMSAT, TAPR, ARRL, and any other local or regional club that is helping advance the state of the art in amateur radio. Projects like ours cannot exist without your membership. 

