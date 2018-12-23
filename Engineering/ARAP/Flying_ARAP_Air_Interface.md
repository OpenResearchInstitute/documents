-   [Part 1 – General Information](#part-1-general-information)
    -   [Chapter 1 Necessary Overhead ](#chapter-1-necessary-overhead)
        -   [Origin of this Document](#origin-of-this-document)
        -   [Motivation](#motivation)
    -   [Chapter 2 Link Budget ](#chapter-2-link-budget)
    -   [Chapter 3 System Time ](#chapter-3-system-time)
    -   [Chapter 4 Tolerances ](#chapter-4-tolerances)
    -   [Chapter 5 Forward Compatibility
        Rules](#chapter-5-forward-compatibility-rules)
-   [Part 2 – Requirements for
    Operation](#part-2-requirements-for-operation)
    -   [Chapter 6 Transmitters](#chapter-6-transmitters)
        -   [Frequencies](#frequencies)
        -   [Voice Signal Quality](#voice-signal-quality)
        -   [ ](#section)
        -   [](#section-1)
        -   [Emission Type](#emission-type)
        -   [Emission Type Designation](#emission-type-designation)
    -   [Chapter 7 Receivers](#chapter-7-receivers)
        -   [Frequencies](#frequencies-1)
        -   [Emission Type](#emission-type-1)
        -   [Emission Type Designation](#emission-type-designation-1)
    -   [Chapter 8 Supervision](#chapter-8-supervision)
    -   [Chapter 9 QSO Processing (System
        Access!)](#chapter-9-qso-processing-system-access)
    -   [Chapter 10 Reconfiguration ](#chapter-10-reconfiguration)
    -   [Chapter 11 Idle State](#chapter-11-idle-state)
    -   [Chapter 12 Emergency
        Communications](#chapter-12-emergency-communications)
    -   [Chapter 13 mesh operation](#chapter-13-mesh-operation)
    -   [Chapter 14 Gateways to Other
        Services](#chapter-14-gateways-to-other-services)

Part 1 – General Information 1

Chapter 1 Necessary Overhead 2

Origin of this Document 2

Motivation 2

Chapter 2 Link Budget 3

Chapter 3 System Time 3

Chapter 4 Tolerances 3

Chapter 5 Forward Compatibility Rules 3

Part 2 – Requirements for Operation 3

Chapter 6 Transmitters 3

Frequencies 3

Voice Signal Quality 4

Emission Type 4

Emission Type Designation 4

Chapter 7 Receivers 5

Frequencies 5

Emission Type 5

Emission Type Designation 5

Chapter 8 Supervision 5

Chapter 9 QSO Processing (System Access!) 6

Chapter 10 Reconfiguration 6

Chapter 11 Idle State 6

Chapter 12 Emergency Communications 6

Chapter 13 mesh operation 6

Chapter 14 Gateways to Other Services 7

-=-=-=-=-=-=-=-=-=-=-

Part 1 – General Information
============================

Chapter 1 Necessary Overhead 
-----------------------------

numeric information, domain specific definitions, preface, section
summaries so you know where to go quickly,

### Origin of this Document

This document originated as a fork of the Phase 4 Ground Air Interface
working document. Flying ARAP is a Phase 4 Ground project.

### Motivation

The Flying ARAP Project was proposed by Howie DeFelice as a way to test
the Symposium Demonstration GNU Radio flow graph in low earth orbit. The
Symposium Demo flow graph has four FDMA NBFM channels received,
digitized, and multiplexed into a single digital downlink and is the
basis for the Phase 4 Ground ARAP.

Anticipated receivers for Flying ARAP are off-the-shelf VHF-capable SDRs
and receiver dongles. The Flying ARAP is a lightweight version of the
Phase 4 Ground ARAP. Flying ARAP provides testing of core concepts in an
inexpensive easy-to-construct experiment. Flying ARAP is a 1U spacecraft
that (if approved) will be launched from ISS in 2017.

It will be active for only a few months. Therefore the user interface
and functionality needs to be simple, powerful, and intuitive.

Reuse of this design is possible on other missions. Reuse of this design
is possible in terrestrial applications.

Chapter 2 Link Budget 
----------------------

detailed description of our environment and link budget.

Chapter 3 System Time 
----------------------

define system time and how it’s derived and used in the system.

Chapter 4 Tolerances 
---------------------

what parts of the system have a lot of margin and what do not have a lot
of margin. In SDR-based systems, some parts of the system are high
performance so that other parts don’t have to be. This chapter defines
what those are and how much slop we have.

Chapter 5 Forward Compatibility Rules
-------------------------------------

if there is extra room for future expansion in the message formats (and
there better be) then extra bits are defined and marked as “0”.

Part 2 – Requirements for Operation
===================================

Chapter 6 Transmitters
----------------------

### Frequencies

| **Mission** | **Uplink Frequency Band** | **Bandwidth** | **Access Type**  |
|-------------|---------------------------|---------------|------------------|
| Flying ARAP | 70cm                      | 20kHz         | NBFM channelized |

Channel spacing and channel bandwidth vary with respect to local band
plan and are therefore configurable within the ARAP.

The number of uplink channels is limited by hardware capability,
hardware configuration, and the regulations that apply to the particular
downlink band used.

Having more uplink channels than the downlink can legally accommodate is
not optimal. Therefore, the capacity of the downlink provides an upper
limit on the number of uplink channels.

For the Flying ARAP Project, the four NBFM uplink channels shall be on
70cm.

Four voice channels shall be supported.

These channels follow the Phase 4 Ground Air Interface sub channel
specification, where transmissions are identified by
call\_sign:SSID:subchannel.  
  
This allows the traffic to be successfully routed to or from any Phase 4
radio.

<embed src="Engineering/ARAP/doc_media/Flying_ARAP_Air_Interface/image2.emf" style="width:6in;height:4.63081in" />

Finding, filtering, and sorting sub channel traffic depends upon using
the right application layer tool.

### Voice Signal Quality

There is unhappiness with the lack of attention paid to voice quality in
most CODECs borrowed from industry. Voice codecs literally are the voice
of the system. A radio design can be exemplary, but if the codec sounds
harsh, the entire system will be harshly judged.

There are many factors in quality voice coding and decoding. Things like
compression, pre-emphasis, deviation limitation, limit filters, and
transmit level adjustments all affect voice signal quality.

Phase 4 Ground recommends and implements the following.

CODEC2

OPUS

Flying ARAP implements CODEC2.

###  

### 

### Emission Type

### Emission Type Designation

emission designation, conducted and radiated spurious emissions.

Chapter 7 Receivers
-------------------

### Frequencies

| **Mission** | **Downlink Frequency Band** | **Bandwidth** | **Access Type** |
|-------------|-----------------------------|---------------|-----------------|
| Flying ARAP | 2m                          | TBD           | TDM             |

For the Flying ARAP Project, the single digital downlink channel shall
be on 2m. 9600 baud was assumed to be a practical limit.

Bill Werner suggested using the same signal that NOAA’s EMWIN uses. This
satellite transmits an OQPSK 20kHz wide downlink at 1692.7MHz from GOES
East and West (75 and 137 degrees GEO stationary). Bill reports that
“After all the FEC is done, it delivers a very respectable 17,500 bps of
data.” There is software in the public domain to receive it, which
provides significant advantages.

EMWIN stands for Emergency Managers Weather Information Network.
Information about the satellite and the receiver documentation and
software can be found here: http://www.nws.noaa.gov/emwin/index.htm

### Emission Type

The emission type is a single-channel digital time-division multiplex
downlink. The possible modulations are (TBD). Frames are encoded using
(TBD).

### Emission Type Designation

limitations on emissions, conducted spurious emissions, radiated
spurious emissions, security and identification, authentication, station
ID, registration, registration memory, access overload (proposed quality
of service scheme from 2008), storing and forwarding, MESH networking
requirements.

Chapter 8 Supervision
---------------------

control operation, failure detection. It may be best to have this
controlled by a small team in order to protect access to the space
segment.

Chapter 9 QSO Processing (System Access!)
-----------------------------------------

System access is achieved by transmitting a narrow-band FM signal on the
correct frequency, with enough power to be received by the satellite.

All successfully received signals are multiplexed into the downlink. The
uplink channel that the transmitted station used is the subchannel
designation. Phase 4 Ground subchannel designations are letters in
English alphabetical order.

If there are four subchannels, then they are designated A, B, C, and D.

The subchannel designation is how different uplinks are sorted,
filtered, and distinguished by the application layer.

Chapter 10 Reconfiguration 
---------------------------

Flying ARAP space deployment is not reconfigurable.

Reconfigurations of the terrestrial deployments of the Flying ARAP are
achieved by editing the GNU Radio flow graph installed on board the
processor.

Chapter 11 Idle State
---------------------

When there is capacity, then onboard telemetry is transmitted. Excess
capacity occurs when channel utilization is less than 100%.

Onboard telemetry for the spacecraft is traditional spacecraft
telemetry. Data streams from terrestrial projects can include weather,
APRS, images, or any other digital data that the ARAP can collect or
generate.

The term for swapping in data when there is excess capacity is called
“stat-muxing”.

Chapter 12 Emergency Communications
-----------------------------------

Declared communications emergencies do not change the status or
configuration of this mission. It can be used in an emergency just like
any other amateur radio communications resource. Due to the nature of
this project, as it is in LEO, emergency communications usability may be
limited.

Chapter 13 mesh operation
-------------------------

Mesh operation is not required for this mission. Mesh operation can be
implemented as an option for terrestrial deployments.

Chapter 14 Gateways to Other Services
-------------------------------------

Gateways to other services are not specified for Flying ARAP.

-=-=-=-=-=-=-=-=-=-=-

Comment and critique welcomed and encouraged. This document will be
developed in collaboration with the space segment team.

Editorial Contact:

Michelle Thompson (Phase 4 Ground) w5nyv@yahoo.com
