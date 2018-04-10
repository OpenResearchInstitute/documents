Welcome to the Phase 4 Ground Weekly Report!

413!

Stereo Fields and Multicast

Here's some captioned screenshots from the KA9Q SDR.

And here's a screen shot of the 'radio' program. (Note the frequency. I'm a night owl, and that repeater is often busy through the night, so it's a good test source)

Or this one, with an active signal (note detection of PL tone frequency)

I measure the tone with a 10-second-long FFT so I can get 0.1 Hz precision. Works well.

And here I am calibrating the HF receiver on channel 8's ATSC pilot:

Three WhatsApp image files:
Phil Karn: Here's an example for USB on 20m. All three are receiving USB with a carrier frequency of 14190 kHz and a passband from +100 Hz to +3000 Hz.
Phil Karn: SSB is traditionally 300 to 3000 Hz but I find that many (but not all) signals sound excellent if you lower the low end to 100 Hz. I assume these signals are coming from DSP/SDR transmitters that can produce the necessary sharp filters to keep the other sideband suppressed even though it starts only 200 Hz away.
Phil Karn: That, plus improved frequency stability, makes modern SSB sound often sound better than FM, which I have to high pass filter at 300 Hz to remove PL tones.
The phasing example is the most straightforward. The (suppressed) SSB carrier is brought down to 0 Hz and then a (complex) filter selects only the positive frequencies from +100 to +3000 Hz. This is how I usually operate.

2 4 6 8 Everybody Correlate!

