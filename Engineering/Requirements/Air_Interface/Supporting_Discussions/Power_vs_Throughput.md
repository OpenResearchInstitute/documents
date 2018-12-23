**Section 97.313 Transmitter power standards.**

1.  **An amateur station must use the minimum transmitter power
    necessary to carry out the desired communications.**

This familiar regulation makes solid sense in a world of analog
communications. Power is the currency that we exchange for range and
intelligibility. It’s what allows us to bust up a pileup or bounce off
the moon.

More operators can be accommodated on amateur bands if everyone uses the
minimum transmitter power necessary to communicate. Power used affects
the bandwidth occupied. The goal here is to have more people
communicating per unit time, and that is a very worthy goal, and that is
why this regulation exists.

If we take on the goal of “more people being able to communicate per
unit time”, and we move to the realm of digital communications, then is
it still power that we should require operators to conserve?

It may not be. In order to achieve the goal of more people communicating
in a digital channel, we must confront the idea of throughput.

Optimizing throughput in the analog realm means minimizing power.
Optimizing throughput in the digital realm means that we have to
consider both power and coding gain.

Digital signals generally receive one or both of the following types of
coding. A signal is sampled, and converted into a series of discrete
numbers that represent the signal. Once we have that set of numbers, we
can remove unnecessary redundancy. This is, essentially, compression.
After that, we add the right type of redundancy in order to make the
signal resilient to all the things it will encounter as it’s sent over
the air. This is forward error correction coding. It’s like armor. The
end result of all this coding is very effective gain. Our signal acts
like it’s much more powerful. We can receive it and reconstruct a
perfect or almost-perfect version of the transmitted signal. This signal
can be sent at a lower power than an equivalent analog signal because we
can use math to help fix errors caused by noise or interference. We
don’t have to bull our way through the static with a loud analog signal.
We can correct errors.

An additional advantage is that with some other math tricks, we can
control the occupied bandwidth.

Deciding how and when to twiddle two knobs (power and coding gain)
instead of one knob (power) means the complexity has increased.
