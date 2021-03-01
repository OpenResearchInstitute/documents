**Part 1 – General Information 1**

**Chapter 1 Necessary Overhead 2**

Origin of this Document 2

Preface 4

**Chapter 2 Link Budget 65**

**Chapter 3 System Time 65**

**Chapter 4 Tolerances 65**

**Chapter 5 Forward Compatibility Rules 75**

**Part 2 – Requirements for Operation 76**

**Chapter 6 Transmitters 76**

Frequencies 76

Voice Signal Quality 76

Emission Type 86

Emission Type Designation 86

**Chapter 7 Receivers 1312**

Frequencies 1312

Emission Type 1312

Emission Type Designation 1413

**Chapter 8 Supervision 1413**

**Chapter 9 QSO Processing (System Access!) 1413**

**Chapter 10 Reconfiguration 1413**

**Chapter 11 Idle State 1413**

**Chapter 12 Emergency Communications 1514**

**Chapter 13 mesh operation 1514**

**Chapter 14 Gateways to Other Services 1514**

Amateur Television Network 1514

Amateur Radio Emergency Data Network 1514

-=-=-=-=-=-=-=-=-=-=-

# Part 1 – General Information

## Chapter 1 Necessary Overhead

numeric information, domain specific definitions, preface, section summaries so you know where to go quickly, how necessary it is for the system to be fun and easy to use while also allowing for advanced communications experiments. Motivation, why, where, how, when, and how long the system will be active. What you will be able to do with your equipment after the satellite mission completes or changes! This is very important! Reuse of equipment on other space systems, reuse of equipment in terrestrial applications.

### Origin of this Document

This document originated with the Proposed Table of Contents for the Phase4 Requirements Definition Project. What documents were produced from this content?

1. Common Air Interface, defines how to interface to the system over the air. If you build a circuit that complies with the standard, then it should &quot;just work&quot;. The bulk of the system definition is in here.

2. User Terminal Requirements, defines requirements of the hardware and software of the user terminals. If you build it to where it complies with the requirements, and then comply with the Common Air Interface, then it should &quot;just work&quot;. In general, this content will come from Phase 4 Ground.

3. Space Segment Requirements are the requirements of the hardware and software of the space segment(s). If you build it to where it complies with the requirements, and then comply with the Common Air Interface, then it should &quot;just work&quot;. In general, this content will come from the space segment team.

The Common Air Interface drives the other two. So, we began with that.

![](RackMultipart20201002-4-9hdcj2_html_cbd4344ceab1a4a9.gif)

### Justification

Phase 4 Ground finds justification in part 97 of the United States Code of Federal Regulations. In all aspects, Phase 4 Ground serves the public good. The project provides emergency communications support, contributes to international goodwill, increases the quality of the technical corps, advances the radio arts, and can be employed in a variety of public service roles, whether directly as a communications resource or as a gateway for other communication services.

![](RackMultipart20201002-4-9hdcj2_html_d3eea81edcae4913.jpg)

### Preface

Phase 4 Ground and Space are engineering efforts from Open Research Institute. The focus of this effort is to produce an ensemble of open source solutions for microwave digital payloads.

The amateur radio service has a space allocation in both 5GHz and 10GHz (Five and Dime). This is where the microwave satellite strategy is directed. 

Phase 4 Ground is pursuing both a manufactured solution. We are also committed to developing a set of documents to enable motivated operators in assembling their own stations. These stations can range from completely custom rigs to systems integrated from commonly available SDRs and RF chains.

This document will provide the information necessary to create (or appreciate) the physical waveforms that the satellite will recognize. This document also describes what is required to be done by the operator in order to comply with the default authentication and authorization schemes. For any particular deployment, additional steps may be necessary at the discretion of the controlling organization or authority. This document fully describes what is required in order to comply with the default set of authentication and authorization conditions.

Re-use of ground terminal equipment from one microwave digital payload to the next is accomplished by standardization. DVB-S2/X was chosen for the satellite downlink. It is also expected to be useful for terrestrial deployments. DVB-S, DVB-S2, and DVB-S2X are supported by Amateur Television networks and operators. 

The reasons for choosing DVB-S2/X as the downlink protocol are as follows.

DVB-S2/X is a widely adopted satellite standard. It is an open standard. The documentation is available free of charge from [https://www.dvb.org](https://www.dvb.org/).

By adopting this standard, we enable technical volunteers to learn, implement, and engineer with an industry-standard methodology. This provides many educational opportunities.

By adopting a well-known, widely-deployed standard, we minimize the risk of a critical design error that could cripple the mission, or unnecessarily restrict future flexibility. Risk is minimized by using known-good reference platforms and reference designs in the course of development. 

By adopting this standard, we increase the amount of commercial gear that can receive our amateur signals. DVB-S2 receiver cards are widely available.


## Chapter 2 Link Budget

detailed description of our environment and link budget.

Current working link budgets can be found in the link budget folder at [https://github.com/phase4ground/documents/tree/master/Engineering/Requirements/Air\_Interface](https://github.com/phase4ground/documents/tree/master/Engineering/Requirements/Air_Interface)

For example, we expect a common station type to consist of a 2W 5GHz uplink with a 5kHz data rate from an 18-inch DSS style dish with 1 Watt transmit power to GEO. This leaves 6dB of margin.

Since station types will vary, adaptive coding and modulation is available in order to allow each station to achieve optimal throughput.

Adaptive coding and modulation means a dynamic link budget. Instead of a single modulation and coding selected to close a worst-case link, we can provide a set of modulations and codes that allow for a range of performance. This adds complexity.

The benefit of the added complexity is a higher performance system that provides an educational opportunity in advanced wireless digital communications techniques like variable and adaptive coding and modulation.

## Chapter 3 System Time

define system time, how it is derived, and how it is used in the system.

## Chapter 4 Tolerances

what parts of the system have a lot of margin and what do not have a lot of margin. In SDR-based systems, some parts of the system are high performance so that other parts don&#39;t have to be. This chapter defines what those are and how much slop we have. The use of the Rincon SDR for the space segment means much of this is already known, but the other parts of the system that are affected by the Rincon SDR must be well-understood in order to fully utilize the donations we have been offered.

## Chapter 5 Forward Compatibility Rules

if there is extra room for future expansion in the message formats (and there better be) then extra bits are defined and marked as &quot;0&quot;.

# Part 2 – Requirements for Operation

## Chapter 6 Transmitters

### Intermediate Frequencies

A 4745 LO for the 5660 Tx/Rx with 915 MHz IF nominal band center.

For 10.475 GHz, a 1270 MHz center Tx/Rx IF to stay away from the 915 MHz of the other band.

### Frequencies

| Mission | Uplink Frequency Band | Bandwidth | Access Type |
| --- | --- | --- | --- |
| Phase 4B | 5655 – 5665 MHz | 10MHz | FDMA 100kHz channelized |
| Phase 3E | 5655 – 5665 MHz | 10MHz | TBD |
| Groundsat | 5675 – 5685 MHz | 10MHz | FDMA 100kHz channelized |

channel spacing and designation

frequency tolerance

phase noise

power output characteristics: This could be a table of estimated EIRPs that will close the link depending on the coding/modulation used. This could be helpful for operators planning a station and knowing the amount of power out plus the antenna gain needed be able to get up to the payload.

carrier on/off conditions, power output and power control, modulation characteristics,

### Voice Signal Quality

There is widespread disappointment with perceived voice quality in most CODECs borrowed from industry. Voice codecs literally are the voice of the system. A radio design can be exemplary, but if the codec has low intelligibility, the entire system will be harshly judged.

There are many factors in quality voice coding and decoding. Things like compression, pre-emphasis, deviation limitation, limit filters, and transmit level adjustments all affect voice signal quality.

Phase 4 Ground recommends and implements the following CODECs.

CODEC2

OPUS

…wideband data characteristics, encoding, modulation, limitations on bandwidth,

### Emission Type

### Emission Type Designation

emission designation, conducted and radiated spurious emissions.

#### Downlink

Downlink shall be DVB-S2X. Cube Quest Challenge, which Phase 4 Ground also supports, is pursuing DVB-S2X. Phase 4 Ground terrestrial efforts are experimenting with DVB-T and DVB-T2. Homebrew CDMA, BPSK, and QPSK have also been discussed. The downlink shall be linearly polarized, and cross-polarized with respect to the uplink.

 MCW, phone, image, RTTY, data, SS, and test are authorized on 5 GHz and 10 GHz. This is from §97.305 Authorized emission types. This is from the table in (c).

§97.307 Emission standards.
 (8) A RTTY or data emission having designators with A, B, C, D, E, F, G, H, J or R as the first symbol; 1, 2, 7, 9 or X as the second symbol; and D or W as the third symbol is also authorized.

[https://en.wikipedia.org/wiki/Types\_of\_radio\_emissions](https://en.wikipedia.org/wiki/Types_of_radio_emissions)

Our downlink emission type designation is 10M0D7W.

#### Uplink

Uplink shall be 4-ary minimum shift keying. The uplink shall be linearly polarized, and cross-polarzied with respect to the uplink.

Our uplink emission type designation is 10M0G7W.

![](RackMultipart20201002-4-9hdcj2_html_809f7619044c1250.jpg)

Uplink is expected to be 100 is expected to be 5kHz data rate (modulation TBD) within 100kHz FDMA channels. Signal shall be linearly polarized, and cross-polarized with respect to the downlink.

Low Data Rate

SatChat 1k mode is expected to be 1kHz (modulation TBD) within a subdivided 100kHz channel. We expect to achieve 25 subdivisions within a 100kHz channel.

![](RackMultipart20201002-4-9hdcj2_html_b0eb01940169bf61.jpg)

Uplink Preamble

The Phase 4 FDMA uplink channel is currently assumed to be 10MHz wide, consisting of one hundred 100kHz channels.

There are certain things we need from our uplink signal. We need a constant envelope signal. We need reliable signal acquisition at the satellite. We want to reduce adjacent channel interference. We do not want to spend more power than necessary.

We believe that reliable signal acquisition at the satellite can be enabled with a preamble on uplink transmissions. The purpose of the preamble is for the satellite to identify a Phase 4 signal from the earth, obtain symbol timing, obtain frame timing, and then set the modulation, coding, and data rate for the transmission that follows.

Since a user terminal can hear itself on the downlink, it will not have to resynchronize as long as its own signal is being received. If it loses its own signal, then the preamble is resent. For cases where there are uplink-only stations, such as emergency operations, automated operations, or equipment failure, another mechanism must be required that forces resynchronization.

Below are the major components of the preamble in time order.

![](RackMultipart20201002-4-9hdcj2_html_376d147225d109d5.gif)

A fixed-sized header is then sent at the lowest modulation rate. This header describes the packet. The contents of the header are as follows.

![](RackMultipart20201002-4-9hdcj2_html_a6ff363dc0c94f82.gif)

The next header field contains the following information. The modulation, coding, and data rate combinations may be encoded in order to make them as compact as possible.

![](RackMultipart20201002-4-9hdcj2_html_5cb3a68672bac16a.gif)

## Chapter 7 Receivers

### Frequencies

| Mission | Downlink Frequency Band | Bandwidth | Access Type |
| --- | --- | --- | --- |
| Phase 4B | 10450-10460 MHz | 10MHz | TDM |
| Phase 3E | 10450-10460 MHz | 10MHz | TBD |
| Groundsat | 10475 center MHz | up to 10MHz | TDM |

channel spacing and designation, demodulation characteristics, voice signal stuff,

### Emission Type

The emission type is a single-channel digital time-division multiplex downlink. Modulations for 4B are include 90° BPSK, QPSK, and 8QPSK. Frames are encoded using LDPC-BCH in accordance with DVB-S2/X.

### Emission Type Designation

limitations on emissions, conducted spurious emissions, radiated spurious emissions, security and identification, authentication, station ID, registration, registration memory, access overload (proposed quality of service scheme from 2008), storing and forwarding, MESH networking requirements.

## Chapter 8 Supervision

control operation, failure detection. It may be best to have this controlled by a small team in order to protect access to the space segment.

## Chapter 9 QSO Processing (System Access!)

initialization, system parameters, paging vs. traffic channels, access parameters, access attempt procedures, logging of failures, delay after failures, message passing, how to handle retries, signaling formats. This can make or break the entire project, either by making it irrelevant, or so flexible that it can&#39;t &quot;just work&quot;. Smart people will break this down to several chapters.

### System Access

Radio is powered on.

Receiver turns on.

#### Symbol Timing Recovery

The first stage of the demodulator is the symbol timing recovery. Symbol rate may fluctuate from the satellite to the receiving station. One way to accomplish symbol timing is by a method called Gardner TED. This method is capable of operating under random symbols and unknown carrier frequency offset error without precise carrier synchronization.

#### Frame Synchronization

After the symbol timing recovery has stabilized, the next job is frame synchronization. Search for the physical layer header (PLHEADER). One way to do this is to use a correlator that operates on a symbol-by-symbol basis.

Differential detection is a method that allows for accurate frame synchronization even when the carrier has substantial frequency errors.

A shift-register structure can be used to detect the frame boundaries.

The PLHEADER has two parts, the Start of Frame (SOF) and the Physical Layer Signaling code (PLSC). SOF is a known-in-advance 26-symbol pattern. The PLSC is a 64-bit linear binary code. The shift register has two sections. The first is associated with the SOF and the second is associated with the PLSC. The output of the correlator drives a peak detector. Maximum value occurs when the whole PL header appears in the shift register lined up properly with the detecting sections.

#### Frame Descrambling

After frame synchronization has been achieved, the data symbols (I/Q) of each frame are descrambled. The scrambling process at the transmitter randomizes the symbols in order to disperse energy. This randomization helps improve accurate timing recovery at the receiver, improves automatic gain control, and helps with other adaptive receiver circuits. Scrambling eliminates the dependence of a signal&#39;s power spectrum upon the actual transmitted data.

Descrambling sequences can be precalculated and stored locally.

## Chapter 10 Reconfiguration

this is very important to get right, and it may need to be in a document that is logically above the Common Air Interface, as the Reconfiguration Definition drives the Common Air Interface. Who is in charge of deciding when and how the system is reconfigured? The SDR allows reconfiguration so that the system can be deployed in many different ways, with different modulations, and different experimental modes. This chapter lays down the law on what has to happen in order to reconfigure user and space segments. What needs to be included is the process of how to propose new modes and schemes, and a history of what modes and schemes have been proposed, why they were accepted or rejected, and what happened when they were tried. This is a political and technical area with great potential, that needs to be fully explored and agreements need to be in place.

Virginia Tech should be a gate-keeper in the reconfiguration process as they will have an engineering model that will be as close to an identical copy to the flight unit as possible. New software packages can be uploaded to the engineering model and test performed in order to assess and test key parameters for operations.

## Chapter 11 Idle State

power savings possibilities, or the ability to swap in science projects when traffic is low enough and processing power is available. Defining how to get into and out of idle in order to be able to use the idle state for either just saving power, or some other purpose that we haven&#39;t thought up yet. Using idle cycles could be super useful, but is optional.

## Chapter 12 Emergency Communications

what constitutes an emergency state for the system, what services are provided by both user terminals and space segment in an emergency. There are at least two categories. A declared communications emergency changes the spacecraft state and may change user terminal state. A locally determined emergency does not change the spacecraft state.

## Chapter 13 mesh operation

User terminals will operate as MESH stations. When they are close enough together, then will form ad-hoc networks on their own. This mode should require the user to opt-in and should require minimal configuration. Discuss security implications in detail.

## Chapter 14 Gateways to Other Services

User terminals are capable of operating as gateways. This mode should require the user to opt-in and should require minimal configuration. Regulatory compliance and security are important considerations for any gateway.

### Amateur Television Network

The Amateur Television Network [http://atn-tv.org/](http://atn-tv.org/) is in the process of transitioning to DVB-T at some of their stations. Providing interoperability to this service should be relatively straightforward.

### Amateur Radio Emergency Data Network

Amateur Radio Emergency Data Network provides terrestrial broadband digital service. Phase 4 Ground radios could provide WAN access to connect AREDN networks. Learn more about AREDN at [http://www.aredn.org/](http://www.aredn.org/). As AREDN is an amateur service, then providing a gateway to this service is relatively straightforward from a regulatory and security point of view.

Interconnection could be achieved with olsrd, which stands for Optimized Link State Routing Protocol. It was designed to help establish and maintain routes in mobile ad hoc networks. Read more about it here [https://en.wikipedia.org/wiki/Optimized\_Link\_State\_Routing\_Protocol](https://en.wikipedia.org/wiki/Optimized_Link_State_Routing_Protocol).

AREDN is IPv4. Phase 4 Ground is IPv6. If Phase 4 Ground uses olsrd, then the networking interface can be achieved. Not all implementations of olsrd support IPv6. Therefore, some care is required in selecting the implementation.

The recommended implementation is olsrd2. It can handle both IPv4 and IPv6 at the same time. We don&#39;t need a configuration file for this setup.

-=-=-=-=-=-=-=-=-=-=-

Comment and critique welcomed and encouraged. This document will be developed in collaboration with the space segment team.

Editorial Contact:

Michelle Thompson (Phase 4 Ground) w5nyv@yahoo.com
