-   [Emergency Communications](#emergency-communications)
-   [Ham Radio Operations](#ham-radio-operations)
-   [Ham Radio Experimenter](#ham-radio-experimenter)
-   [Amateur Radio Access Point](#amateur-radio-access-point)
    -   [Single-channel ARAP](#single-channel-arap)
    -   [Multiple-channel ARAP](#multiple-channel-arap)
-   [Education](#education)
-   [Machine-to-Machine](#machine-to-machine)

<img src="Engineering/Requirements/Use_Cases/Phase 4 Use Cases/media/image1.png" style="width:3.3325in;height:2.43939in" />

The use cases listed here are best effort predictions of how Phase 4
radios will be used. The list will not be perfect or exhaustive, but
will guide decisions that must be made in order to produce real
hardware.

We are assuming operational radios for these use cases. We assume that
the radios comply with our current understanding of the electromagnetic
as well as the policy environment.

Emergency Communications
========================

We emphasize emergency communications for two reasons. First, emergency
operations must not differ from normal amateur operations unless
absolutely necessary. Therefore, anything necessary to emergency
communications has immediate relevance to any other use case. Second,
providing emergency communications demonstrations and support is a
primary justification of the project. Emergency communications is
therefore the fundamental use case.

Phase 4 radios must “just work”. This is understood to be that Phase 4
radios must work with a minimum of configuration and setup in general,
and either minimal or completely eliminated differences between normal
and emergency operation.

Phase 4 radios in an emergency must be able to respond to authorization.
This is understood to mean that satellite access may be controlled in an
emergency, and Phase 4 radios must comply with this uplink access
control.

Phase 4 radios fall into a category of non-voice-centric (NVC)
telecommunications devices. This expands the use case from voice-centric
telecommunications devices that many amateur radio operators are
familiar with or have trained to provide service with. The addition of
images, text, and data enhances emergency communications, but also
places additional demands and complexities on operations. It is the
operator that must properly use the radio given the challenges of any
particular deployment. It is our job to make that operator’s decisions
as easy as possible.

Phase 4 radios intended for emergency communications must be durable and
rugged enough in order to serve in difficult environments. Efforts must
be made to design them to run on emergency or limited power. We
acknowledge that ensuring high levels of durability may be very
difficult or expensive goals to meet. We commit to best possible efforts
in terms of ensuring durability.

Using Phase 4 radios in emergency communications services require
training. We believe that regularly scheduled drills on Groundsat or
Satellite will enable operators to be better prepared for emergency
communications. We strongly encourage a requirement for emergency
communications drills on the deployed satellite and for it to be
included in the operational requirements.

Spectral displays, demodulator options, options for filtering and
grouping communications types and stations, logging contacts, sending
and receiving ICS forms, monitoring, responding to authorizations, and
other normal and emergency communications functions are all available in
the emergency communications use case.

Ham Radio Operations
====================

Access to radio functions for normal communications is through the
application space. Applications include programs such as gqrx or
something like gqrx. Spectral displays, demodulator options, options for
filtering and grouping communications types and stations, logging
contacts, browsing, and other normal communications functions are all
available. Applications written by the community are available to be
added to the application space in order to provide additional functions.

The current use case would have an operator install gqrx (or something
like it) on a machine that can run it, connect a USRP to a USB port,
connect the TX port to a 5 GHz amplifier, connect the RX port to the IF
output from a 10 GHz LNB, connect the appropriate antenna or antennas,
and point at the satellite. 

As hardware is developed or alternative parts of the communications
chain identified, a variety of recipes will emerge.

Ham Radio Experimenter
======================

The experimenter use case envisions operators that want to interact
directly with their Phase 4 radio. For example, an experimenter will be
able to use GNUradio and GNU Radio Companion directly. This allows
operators to build flowgraphs in order to change the way their radio
operates.

This use case assumes greater technical knowledge on the part of the
operator. This use case needs to be studied in order to ensure that
there aren’t any incompatibilities between Experimenter stations and
Emergency stations. The best way to determine incompatibilities or
problems is to have regular emergency drills on the Phase 4 systems.

Amateur Radio Access Point
==========================

The amateur radio access point (ARAP) use case is intended to allow
access to the satellite from radios that would not normally be able to
communicate through the satellite. Radios that are not powerful enough
or use a modulation scheme that the satellite doesn’t support are the
anticipated users. ARAPs can support emergency, normal, and experimenter
operations.

Single-channel ARAP
-------------------

Single-channel ARAPs can be constructed by adding hardware to a normal
Phase 4 radio. The hardware consists of an antenna and transceiver
designed to support the desired modes. The hardware connects to the
Phase 4 radio with microphone in/line out. This would allow a
single-channel Phase-4 radio to relay local traffic. Throughput is
limited, but 2-way communications through the satellite would be
possible with relatively lightweight and inexpensive gear.

Multiple-channel ARAP
---------------------

The current demonstration software (“The 2015 Symposium Demonstration”)
supports four local channels. Four FM radios can transmit at the same
time. The channels are digitized and then multiplexed. The reverse link
would require the FM channels to be assigned internal tactical IDs in
order to transmit back to the correct channel. Multi-channel ARAPs are
expected to be more complex and more expensive than single-channel
ARAPs.

Education
=========

Phase 4 radios are useful in at least two educational roles. First, the
process of building a Phase 4 radio provides the opportunity for many
lessons in both design and integration. Second, radio modes and
operations can be introduced by using Phase 4 radios as the teaching
instrument.

Machine-to-Machine
==================

Machine-to-machine operation is possible with Phase 4 radios. They can
be set up for unattended monitoring. They can be scripted to wait for
and then react to specific conditions or sets of conditions.

Use Cases

| Name of Case    | Licensed Operation                                                                                                           |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|
| Description     | Phase 4 is part of the licensed amateur radio service.                                                                       |
| Actors          | Alice and Bob                                                                                                                |
| Pre-conditions  | None                                                                                                                         |
| Basic Flow      | Alice and Bob think Phase 4 sounds awesome. They learn they have to get radio licenses. They study, take, and pass the test. |
| Post-conditions | Alice and Bob successfully obtain their amateur radio licenses.                                                              |
| Alternate Flow  | Alice and Bob fail their test and can’t use Phase 4 radios.                                                                  |

| Name of Case    | Phase 4 Registration                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description     | Phase 4 radios require registration.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Pre-conditions  | Alice and Bob are licensed operators.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Basic Flow      | Alice and Bob obtain Phase 4 radios. Registration is fraught with peril. Is registration required? The assumption that access to the satellite needs to be controlled seems to imply registration. Registration is related to authentication and authorization. Authentication is the process of verifying "you are who you say you are". Authorization is the process of verifying "you are permitted to do what you are trying to do". Authentication is required for authorization. |
| Post-conditions | Alice and Bob successfully register their Phase 4 radio.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Alternate Flow  | Alice and Bob do not register. When they attempt to use their radios, the radios do not respond.                                                                                                                                                                                                                                                                                                                                                                                       |

| Name of Case    | 2-way Voice Communications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description     | Amateur radio operators have a 2-way voice communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Actors          | Alice and Bob                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pre-conditions  | Alice and Bob are licensed operators. They are registered on the Phase 4 system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Basic Flow      | Alice decides to call Bob. She turns on the Phase 4 radio. If the antenna is not pointed, then she uses whatever means are necessary to point the antenna at the satellite. If a beacon is implemented, basic information about the satellite is available, up to an including information that may allow for automated pointing as well as what mode the satellite is in. The beacon may or may not have a map of available channels. She picks up the microphone and presses PTT. The radio is randomly assigned a channel that is currently open. If the Phase 4 radio hears its own signal on the downlink, then all is well. Alice calls Bob. Bob hears Alice, and answers. |
| Post-conditions | Alice and Bob successfully have a QSO.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Alternate Flow  | If the Phase 4 radio does not hear its own signal on the downlink, then at least two things may have happened. It has either not been heard at all, or it has been heard but has lost synchronization, and it will need to re-attempt synchronization.                                                                                                                                                                                                                                                                                                                                                                                                                           |

| Name of Case    | Basic Radio Experimentation                                                                                                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description     | Ham radio operator wants to experiment with a new codec.                                                                                                                                                                                                                                              |
| Actors          | Alice and Bob                                                                                                                                                                                                                                                                                         |
| Pre-conditions  | Alice and Bob are licensed operators. They are registered on the Phase 4 system. They are able to have successful 2-way voice communications.                                                                                                                                                         |
| Basic Flow      | Bob decides to try a new codec. Bob researches codecs, picks a new one, and specifies the use of that codec at the application layer. He collaborates with Alice, who also installs the codec. Bob successfully calls Alice, and they discuss whether or not the new codec makes Bob’s butt look big. |
| Post-conditions | Alice and Bob successfully have a QSO where part of the radio has been modified.                                                                                                                                                                                                                      |
| Alternate Flow  | The QSO fails due to a failure of either the installation or performance of the codec.                                                                                                                                                                                                                |

<table>
<thead>
<tr class="header">
<th>Name of Case</th>
<th>Declared Emergency</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Description</td>
<td>Hams provide emergency communications support. During a declared emergency, where the satellite is involved, uplink access to the satellite is restricted to equipment that is authorized to operate.</td>
</tr>
<tr class="even">
<td>Actors</td>
<td>Alice and Bob</td>
</tr>
<tr class="odd">
<td>Pre-conditions</td>
<td>Alice and Bob are licensed operators. They are registered on the Phase 4 system. They are able to have successful 2-way voice communications. There is a declared communications emergency or declared emergency drill.</td>
</tr>
<tr class="even">
<td>Basic Flow</td>
<td><p>A communications emergency or communications emergency drill is declared. All or part of the communications resources of a Phase 4 satellite is set aside for emergency communications use. The satellite mode is changed to Emergency Mode by those responsible for its operational status. This enforces a filter on the uplink. The filter allows authorized radios to access the uplink. Authorized communications take place. Unauthorized radios would not be able to pass the filter. Unauthorized communications do not take place.</p>
<p>Filtering can be accomplished with a challenge and response. This requires two-way communications. Filtering can be accomplished with a white list. This does not require two-way communications, but does require some sort of identification in the uplink header or elsewhere in the transmission. White list stations would to be identified in advance. Ad hoc or day-of-emergency additions to the white list would require an additional procedure or mechanism.</p>
<p>What happens to unauthorized communications? Are they demodulated, but not transmitted on the downlink? Are they not demodulated at all? Answering this question directly affects uplink header content. With the minimal header we are currently considering, without station or equipment identification included, signal authentication and authorization would be carried out later in the communications flow.</p></td>
</tr>
<tr class="odd">
<td>Post-conditions</td>
<td>Alice and Bob support emergency communications by operating their Phase 4 radios in authorized emergency communications mode.</td>
</tr>
<tr class="even">
<td>Alternate Flow</td>
<td><p>1. Alice and Bob cannot access the satellite because they do not know how to configure their radio to respond in emergency communications mode.</p>
<p>2. Alice and Bob cannot hear the satellite (are uplink-only due to damage, position, or other impediments) and despite knowing how to respond to the challenge, cannot respond to the challenge, and are therefore unable to access the satellite.</p>
<p>3. An unattended Phase 4 radio is taken over by Jason, who becomes an unintentional or intentional jammer.</p>
<p>4. An unattended Phase 4 radio successfully authorizes, yet continues to transmit large amounts of telemetry or other machine-to-machine data, which inadvertently uses up system bandwidth.</p>
<p>5. Forgo authentication and authorization entirely and allow open access to the satellite at all times, including emergencies.</p></td>
</tr>
</tbody>
</table>
