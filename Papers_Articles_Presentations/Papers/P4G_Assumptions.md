Wally Ritchie has begun some work on an Internet based simulator for a p4b geosat. It focuses on the Narrowband Multiplexor entity that relays the data from the uplinks to the DVB-S2 downlink.

In the process he has collected a random assortment of "sort of consensus" thinking from the slack channels over the last year or two. 

Please comment here or on slack regarding any that are not actual likelies or are not understood. 

Wally WU1Y


1. The Downlink will likely have power output of 10W – 100W into a hemispherical beam.
2. The Downlink will likely have symbol rate of 1 Mbaud to 10 Mbaud. 
3. The downlink will likely have a saturated and unfiltered final. 
4. The downlink will likely provide a DVB-S2 carrier.
5. The downlink will likely use GSE supporting multiple streams and ACM/VCM. 
6. The primary stream will likely be a flow of UDP broadcast packets at 25 pps. These will carry the relayed narrowband channel data and system data. 
7. System data will likely include both telemetry and operational data (e.g. logs) and will be unencrypted except where necessary. 
8. A narrow band multiplexor (NBM) entity will likely combine the system streams and the relayed narrowband channels into a single UDP packet flow which will have priority over other flows. 
9. Wideband channels will likely be supported and relayed in separate IP packet flows (or perhaps repeated BBFRAMES). 
10. System data may in some cases utilize separate IP packet flows. 
11. Narrowband uplinks will likely be handled by a multi-channel receiver with 64 – 128 channels spaced at 25kHz (or somewhere between 12.5 to 75kHz). Note that with 64 25kHz channels the narrowband input spectrum would be 1.6MHz. 
12. Earth stations will likely require a sub-ppm accuracy station clock with Frequency Accuracy and Stability on the order of 100ppb for 25kHz channels. The clock may have to be synchronized to the downlink. Note that 1ppm at 5GHz corresponds to 5kHz frequency shift.
13. Uplinks will need to control power output, frequency, and timing to arrive in their assigned uplink slot.
14. Narrowband Uplink modulation will likely be some form of GMSK or QPSK and could vary over the lifetime of the repeater. 
15. Narrowband Uplink PSD will need to maintain power in the adjacent channels below specified tbd limits.
16. Uplink spurious outputs both in-band and out-out of band will need to be kept below specified tbd limits. 
17. The possible (and wildly optimistic) presence of other satellites with 5GHz uplinks as close as 2 degrees should be recognized. 
18. Narrowband Uplink transmissions will likely be framed in 40ms slots matching the NBM frame rate. 
19. Narrowband Uplink symbol rates will likely be on the order of 5000 baud to 2000 baud for 25KHz channel spacing. 
20. Narrowband Uplink transmissions from active stations will be continuous back to back frames. Where the frame does not carry relayed speech (e.g. silence intervals) identification or alternate data may be transmitted and relayed.
21. Frames containing station identification will likely be FEC coded (e.g. Golay Coding).  
22. Preambles on each frame will likely be required for synchronization and adaptive equalization. 
23. Longer preambles may be required on the initial frames of a transmission. 
24. Identification will likely be required on the first frame of a sequence and periodically during a continuous sequence. 
25. Data within a frame will only be relayed through the NBM when fully conforming to the rules.
26. Where the receiver is unable to synchronize and decode a frame, parametric data related to the transmission will likely be substituted for the missing payload.  
27. Dedicated channel sets on both band edges will be used for testing and commissioning. 
28. Stations will not be permitted to transmit on regular channels until they have been commissioned using automated procedure that take place using the commissioning channels. Any transmission by an un-commissioned station will be considered intentional interference.
29. A cease transmission command will likely be provided in the NBM output requiring all stations to immediately and temporarily cease transmission. This might be used to support processes to identify and locate interference or unauthorized transmissions.  
30. Commissioning will likely involve short transmission bursts on the order of 3 to 5 frames in a test channel. Commissioning transmissions will likely be separated in time (many seconds for an individual station). 
31. Commissioning channels will likely dedicate one or more adjacent guard channels to be used in the commissioning process (e.g. proving adjacent channel power, frequency, and frame alignment measurement to verify that the station is within tbd limits.
32. Allocation of a commissioning channel to a station will likely involve a fair hash algorithm based on offered demand and capacity. Transmission Collisions will be possible and expected during commissioning. 
33. Allocation of channels to commissioned stations will likely use a channel allocation protocol operating within single channels (as opposed to the multiple channels used for commissioning/test). Note that a station cannot be identified until its transmissions can be decoded by the receiver. 
34. Once a station is able to transmit a compliant signal in the commissioning channel it will acquire a secure access token through interaction with the server. This will likely involve authentication. The token will be used to identify the station in transmissions. The receiver will likely substitute the station's actual callsign for the token in the downlink.  
35. The NBM output configuration will likely be flexible allowing for a variable number of active uplink channels of various payload rates with an aggregate relayed payload on the order of 256kps.
36. The NBM will likely support Nx800 channel allocations with N <= 12 (i.e. 800 to 9600bps). 
37. During any given frame (UDP packet), an NBM channel segment may carry Uplink Payload, Uplink Identification (Station ID and payload type), Parametric Receiver Data, or System Data. 
