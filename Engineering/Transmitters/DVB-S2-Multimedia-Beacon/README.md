# DVB-S2/X Multimedia Beacon at 10 GHz

Video of the following demonstration can be viewed at: https://youtu.be/vjfRI1w_dSs?t=610

As you have seen, one of our projects is a multiple access broadband digital system at microwave, that is designed to be used in very high altitude payloads in space, or terrestrially.

Channels divided in frequency are the uplink. The uplink is on 5 GHz. The processor on the payload digitizes and multiplexes these signals and uses DVB-S2 as a single time-division downlink. The downlink is on 10 GHz. The system adapts to channel conditions and handles things like quality of service decisions. For example, low and high latency digital content. The uplink is divided up using a polyphase channelizer, which opens the possibility of reconfiguring uplink channels in orbit or in the field.

While most amateur television systems use the MPEG transport stream, we replace this with another DVB protocol called Generic Stream Encapsulation, so that any type of data is efficiently transmitted.

The end to end system is coming together in an FPGA based design that can then become a custom ASIC.

Part of the system is a default digital downlink. When there is no or light traffic, we want to play signals that run through all the combinations of modulations and forward error correction coding, so that people can fully test their receivers.

This payload function is essentially a beacon, so we are making a small number of them. This is an early prototype and will go up in Southern California as quickly as possible.

When we say broadband, we mean on the order of 10 MHz. The symbol rate is fixed, and the modulation and error correction coding vary to allow different capability stations, experiencing different channel conditions, to close the loop. This is called adaptive coding and modulation.

For this prototype, we are only using MPEG transport stream, but generic data is the goal. This beacon signal is 5 MHz wide and we are using one modulation and one error coding (yet). We are not yet rotating through all the allowed combinations in DVB-S2 (yet).

And here is Paul Williamson KB5MU with a demonstration of the hardware and software involved.






