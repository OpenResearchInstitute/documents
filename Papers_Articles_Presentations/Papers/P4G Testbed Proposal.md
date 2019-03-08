Phase 4 Ground System Testbed Prototyping Scheme Proposal
=========================================================
2019-03-08 Paul Williamson, KB5MU, paul@mustbeart.com

The Phase 4 Ground project has had a reasonably well-defined top-level system architecture  for several years now. So far, work has mainly concentrated on some of the known "hard parts", such as DVB-S2/X reception including the LDPC decoder, dual-band feeds, and 5 GHz power amplifiers. Now it's time to build a testbed that approximates the planned system architecture so that we can demonstrate and experiment with some of the other interesting parts of the system.

The specific goal of this document is to plan a set of incremental steps that can take us smoothly from a fresh start to a testbed system that implements and/or simulates all the main parts of a complete Phase 4 Ground system. Each step should be "easy" in the sense that no major new development work is required and it is reasonably clear what needs to be done. This will mean that some interesting parts of the system have to be dummied out or grossly simplified. For example, the part of the payload that multiplexes the data from all the received uplinks is complicated, but it can be temporarily replaced by a simple round-robin multiplexer that doesn't support features like authentication and authorization. It will also mean that some performance parameters of the desired system will have to be compromised. For example, we want to be able to receive enough channels of uplink data to effectively utilize the entire 10 MHz of the 5 GHz Amateur Satellite Service uplink band, but to accomplish this may require a higher-performance (presumably FPGA-based) receiver solution than we have ready at this time. However, a receiver subsystem that can handle just a few channels is within reach.

Once the testbed system is in place, we hope it will serve in two main ways.

First, a testbed system that resembles the desired system architecture should make a very effective demonstration. This will make it much easier to communicate the design and get the community excited about its possibilities. It should contribute to recruiting more volunteers to work on the project, and it should make our story for fundraising much more convincing.

Second, a testbed system can serve as a platform for development of the more advanced subsystems that haven't yet been fully worked out. It should make it easier to identify requirements for these subsystems. When prototype subsystems become available, it should be possible to integrate those prototypes into the testbed and perform some level of testing on those subsystems.


System Architecture Review
--------------------------

The system architecture assumes a single central payload and many user stations. The central payload may be aboard a geosynchronous satellite or may be at a terrestrial site with good coverage. We adopt the satellite nomenclature and call the user station a "ground" station. The link from the ground station to the central payload is called the "uplink" and the link from the central payload to the ground stations is called the "downlink".

The downlink is a single broadband transmission in the well-defined industry standard format DVB-S2 or S2X for satellite systems. Terrestrial systems may use DVB-S2/X as well, or may use the DVB-T2 standard instead for better performance in the multipath environment. The downlink is shared among all the active ground stations at any given time. This is done by treating all user signals as generic digital data and incorporating that data into the DVB signal according to the industry standard for Generic Stream Encapsulation (GSE).

When DVB-S2/X is used commercially, the various user data streams (video or data) are generally transmitted over the Internet or other data links to a large central ground station. These links are not covered by any particular DVB standard. The central ground station is then responsible for multiplexing the signals according to proprietary business rules, and creates one big data stream on the ground. The central station then transmits this big data stream as a DVB-S2/X signal and uplinks it to the satellite payload. The satellite payload is typically kept as "dumb" as possible, and merely retransmits the uplinked DVB-S2/X signal on the downlink.

This common commercial architecture does not translate well to amateur radio. There is (as yet) no robust amateur infrastructure for relaying data to a central station. Some entity would have to operate the central ground station, which would be expensive, politically fraught, and probably not very fun. Worse, the central ground station would be a fragile single point of failure for the system. Instead, the P4G architecture places the multiplexing function in the payload, on board the satellite in the case of a space-based system.

With the multiplexing function in the payload, P4G needs a standardized way to pass data on the uplink from ground stations to the payload. This needs to be relatively simple, since the payload (which has restrictions on size, power, and complexity) must be able to receive and process many of these signals simultaneously. We have not identified any industry standard that is suitable for this type of service, so P4G is defining its own uplink. The basics are that each ground station transmits a separate MFSK carrier in one (or more, for higher data rates) of about 100 non-overlapping uplink channels of about 100 kHz each. The ground stations and the payload cooperate to determine which channel may be used by each ground station, and when. Channel-sharing parameters will be broadcast by the payload in overhead messages in the downlink. Other overhead messages will convey in real time which channels are in use, and by which stations, and establish a common timebase for channel assignments. A protocol will be specified by which a ground station may be required to authenticate its identity and be checked against authorization policies set by the payload operator. Development of these details into a rigorous protocol specification is one of the major development activities remaining.

A ground station receives the entire multiplexed downlink, but is probably not capable of or interested in making use of all the data on the downlink. It will want to select one or more of the multiplexed data streams for further processing. For example, if the ground station is participating in a roundtable voice conversation with several other ground stations, it will want to process the data streams from each of the the other participants. Perhaps it will decode audio from every stream and mix the audio together for the local user's headphones. If it can't decode that many audio channels simultaneously, or if the local user doesn't want that, it may implement a smart algorithm to decide which audio channel(s) to decode and present. Similar considerations apply to other types of data streams. Except for certain mandatory control messages transmitted by the payload itself, the ground station is free to decode and process as much or as little of the downlink as it chooses.


Simplifying Assumptions
-----------------------

In order to make the demo more visually comprehensible, and to restrict the complexity of any one component for the testbed system, the payload, ground station transmitter, and ground station receiver will be implemented in three separate subsystems. In some cases the station functions will be further divided into multiple sub-subsystems for convenience. The ground station transmitter and/or ground station receiver subsystems may be replicated to create a more elaborate and capable demonstration testbed. When it's time to test protocols that involve both the uplink and the downlink, ground station transmitters may be interconnected one-to-one with ground station receivers in order to create a complete ground station.

Within the scope of this plan, we won't try to implement any channel allocation protocol, authentication, or authorization. That work does need to be done, though.

Within the scope of this plan, we won't try to simulate the earth-space-earth or terrestrial channels in any detail. We'll use attenuators to match signal strengths, but won't simulate any fading or noise or delay or Doppler shift. Those might be interesting things to add in later phases.

We will use some simple packets and Opus encoded voice for the tests and demonstrations. That's only a tiny representative slice of the possible applications.

The plan is written for DVB-S2/X, but there's no particular reason why a similar plan wouldn't apply as well to a DVB-T2 system.


Proposed Testbed Development Phases
-----------------------------------

Each of these phases is intended to be simple and incremental, and includes a demo that exercises the function(s) implemented in that phase. Some of the demos are just sanity checks for the lab, while others would make good public demonstrations.

First, we will concentrate on the ground station receiver side.

Phase 1. Set up a Raspberry Pi with audio output to a speaker. This will be the beginning of a ground station receiver.

Demo: play an audio file from the Raspberry Pi's local storage.

Phase 2. Configure the Raspberry Pi to listen to Ethernet for a multicast IP stream containing Opus-encoded digital audio. This can be implemented using the existing program VLC.

Demo: on a laptop, use existing tools like opusenc and multicat to transmit a multicast IP stream via Ethernet. Play an audio file from the laptop's disk (or use a live microphone) and hear it come out of the Raspberry Pi's speaker.

Phase 3. Add the SR-1 (commercial DVB-S2/X receiver with GSE capability) to the system. Connect its data output port to the Raspberry Pi's Ethernet. On a fast laptop (NOT connected to the Ethernet) run the GSE+DVB-S2 transmit flowgraph in GNURadio Companion (as already demonstrated at GNURadio Conference 2018) through a USRP B210 SDR. This is the beginning of the payload transmitter. Connect the SDR's RF output through suitable attenuators to the SR-1's RF input. Again run opusenc and multicat, either on the fast laptop or on another laptop, and arrange networking interconnects (like we did at GNURadio Conference) so that the multicast IP stream goes over the GSE+DVB-S2 link.

Demo: again transmit Opus-encoded voice and hear it come out of the Raspberry Pi's speaker, after passing over the air in DVB-S2 GSE format.

Phase 4: Modify the transmit flowgraph by adding a simple frame mux at the input to the GSE module. One input of the mux gets the multicast IP packet stream from the Opus encoder, as before. Other inputs stream from file sources or, optionally, from other multicast IP packet streams from other computers.

On the Raspberry Pi, wrap VLC in a simple UI that allows a user to select which of several multicast IP addresses to monitor.

Demo: show that the Raspberry Pi can switch around among the multiple audio streams at will.

Phase 5: Add additional copies of the Raspberry Pi.

Demo: show that multiple streams can be received in parallel. We are of course faking the multiple reception to some extent, since all the Raspberry Pis are listening to the same SR-1. The SR-1 has powerful enough hardware to handle the entire downlink.


Partial success can be declared here. We've demonstrated a multiplexed downlink over GSE and a minimal ground receiver with the ability to select and receive one of the streams. Since we're using Opus at a decent bit rate, the audio quality ought to be outstanding. This might be a good time to set aside the downlink and work on the downlink, but there's still more to do on the downlink.


Phase 6: Add our open-source DVB-S2/X receiver (perhaps it is a flowgraph) running on suitable hardware. Split the RF signal between the SR-1 and our receiver. Split the Ethernet into two segments, each with one or more of the Raspberry Pis. Let the SR-1 continue to feed one segment and let our receiver feed the other segment.

Demo: as before. Show that the open source receiver works like the SR-1. Adjust the downlink attenuators and see how the performance compares near the threshold. Now the demo is less fake, since we have two completely separate receivers.

Phase 7: Replicate the DVB-S2/X receiver and connect each one separately to its own Raspberry Pi.

Demo: as before, but even less fake

Phase 8: Incorporate the functions of the Raspberry Pi into the hardware that's running the DVB-S2/X receiver.

Demo: as before, but with less clutter


Set that aside and start on the uplink. This could also be started in parallel, resources permitting.

Phase A. Set up a fast laptop with GNU Radio. This will be the beginning of the payload receiver. Create a simple flowgraph that implements a polyphase filter bank to receive 4 contiguous 100 kHz channels. Connect each of the four output channels to spectrum visualizers. Connect another SDR (perhaps the USRP X310) to the flowgraph as a signal source. Connect an off-the-shelf signal generator's output to the SDR's RF input.

Demo: Run the flowgraph and observe the four channels of vacant spectrum. Manually sweep the signal generator across the band, and watch the carrier sweep across each of the four spectrum visualizers in turn.

Phase B: Set up a separate SDR with GNU Radio on a laptop. This will be the beginning of the ground station transmitter. Create a flowgraph that alternates a fixed synchronization preamble with a packet data source, and transmits it in a MFSK burst (i.e., turning the transmitter on, sending a preamble and some data, and then turning it off). Feed it with random data packets for now. Make it transmit near the middle of one of the four channels the polyphase filter bank is receiving, and connect its RF output through suitable attenuators to the RF input of the payload receiver SDR (removing the signal generator).

Demo: See the bursts of data in one of the spectrum visualizers on the payload receiver.

Phase B1: Try replacing the ground station transmitter laptop with a Raspberry Pi. If it works we can more cheaply and conveniently replicate multiple ground stations for later testing.

Demo: same as Phase B.

Phase C: Modify the flowgraph in the payload receiver to add a MFSK demodulator and a correlation detector on each of the four outputs of the PFB. Add a time visualizer at the output of each correlation detector.

Demo: See the transmitted preambles cause a pulse on the corresponding time visualizer.

Phase D: Modify the payload receiver flowgraph to use the correlation sync pulse to parse the data burst into a header of N bits and a body of M bits. Add a data display widget that shows the header and another data display widget that shows the first bits of the body.

Demo: See that the first N bits of the random packet data shows up the header widget and the next few bits of the random packet data shows up in the body widget.

Phase E: Modify the ground station transmitter flowgraph to encode a header and body. Define certain bits of the header to be a length field. Add a UI widget to set the length field. Modify the payload receiver flowgraph to parse out the length field from the header and display it.

Demo: Set various values in the length field on the ground station transmitter, and see them show up in the length display on the payload receiver.

Phase F: Modify the ground station transmitter flowgraph to accept a packet input, determine its length, pack that value into the length field of the header, and use the data from the packet to fill the body part of the transmission.

Demo: send various length packets into the ground station transmitter flowgraph, and see that the length display on the payload receiver shows the same lengths.

Phase G: Modify the payload receiver flowgraph to use the received length value to grab that much of the received body data and output it as a packet. Use Wireshark to monitor the packet output.

Demo: Send packets from the ground station transmitter and see them appear in the Wireshark display.

Phase H: Combine the payload receiver flowgraph with the multiplexed GSE+DVB-S2 (payload transmitter) flowgraph from Phase 4. Have the packets that were output in Phase G go into the multiplexer instead. Move the Wireshark to monitor the ground station receiver's Ethernet.

Demo: send packets from the ground station transmitter and see them appear in the Wireshark display, after going over DVB-S2.

Phase I: Move the opusenc+multicat source to the ground station transmitter's Ethernet. Arrange for the multicast IP stream to go into the packet transmitter.

Demo: transmit Opus-encoded voice and hear it come out of the Raspberry Pi's speaker, after passing through both the uplink and the downlink.

Phase J: Replicate one or more copies of the ground station transmitter.

Demo: transmit multiple streams of Opus-encoded voice and receive them on the multiple ground station receivers from Phase 5.


That's already a pretty nice demo. Since we have physical separation between the ground station transmitter, the payload, and the ground station receiver, we can label them and point to them and make the demo visually compelling. We have all the major components of the system, albeit in simplified form.


Going beyond the demo scope, some next steps might be:

Phase K: Replace the multiplexer in the payload flowgraph with a custom block. Have it generate an on-the-fly status report and transmit that on its own multicast IP stream, muxed in with the user streams. Add a process to the ground station receiver to accept the status report stream and display it.

Demo: see the system status live on the ground station receiver.

Phase L: Add a block in the payload flowgraph to generate an overhead information stream and feed it to the multiplexer. Add a process to the ground station receiver to accept the overhead stream and display it.

Demo: see the system overhead information on the ground station receiver.

Phase M: Modify the payload flowgraph to alternate long transmissions at the regular MODCOD as before with short transmissions of canned GSE data at the most robust MODCOD.

Demo: increase the attenuation on the downlink RF until the regular MODCOD can no longer be received. Note that the SR-1 still locks up on and receives the robust MODCOD. This simulates initial ground station acquisition. Note that the SR-1 is not designed for burst reception, so the "short" transmissions may have to be rather long for this demo to work.

Phase N: If we have reached Phase 6 on the downlink side, modify the DVB-S2/X receive flowgraph to handle the MODCOD switching back and forth, if necessary.

Demo: as in Phase M, only with our own DVB-S2/X receiver.

Phase O: (maybe this makes sense) Modify the DVB-S2/X receiver to take advantage of information and synchronization obtained from the robust MODCOD to improve acquisition performance at the regular MODCOD. Maybe it would help if the information sent under the robust MODCOD included the index of the regular MODCOD.

Demo: vary the attenuation on the downlink RF and see if our receiver can now acquire the downlink at a lower signal strength, or more quickly.


In Conclusion
-------------

This plan doesn't finish the project. It does plan substantial forward progress, and creates specific and effective public demonstrations.
