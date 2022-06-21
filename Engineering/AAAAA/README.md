# AAAAA for P4G
2020-06-30 kb5mu

Assembly, Acquisition, Access, Authentication, and Authorization for a Multiplexed Digital Communications System for the Amateur Radio and Amateur Satellite Services

## Introduction

The Phase Four Ground (P4G) project has defined, and various compatible payload projects are adopting, a digital communications system based on many single-user FDMA channels of digital uplink data and a single DVB-S2/X downlink channel multiplexed on board the payload using Generic Stream Encapsulation (GSE). Ground stations and payloads comply with a common _Air Interface_ specification that defines all interactions between stations in enough detail to ensure compatibility. The Air Interface codifies many of the design decisions that tailor the system to meet the identified system goals. The intention is that ground station equipment can come from a variety of sources, including commercial manufacturers, kits of parts for individual builders, and even independent DIY construction projects built from scratch by more advanced amateurs. The hope is that commercial equipment manufactured in quantity will be very affordable and relatively easy to use, while extremely flexible experimenter-friendly equipment can still be used to advance the state of the art. For all this to be possible, it is necessary to specify the detailed behavior of the ground station in full detail.

Several decades of experience with satellite communications systems has revealed a variety of problems that can arise from the fact that any satellite, at any given time, is potentially accessible by many people spread over a large area. Some of those people are welcome users of the system, and these people need a way to cooperatively share the limited resources of the satellite. Others may be eligible to use the system, but for some innocent reason are causing problems with the satellite, say by transmitting with excessive uplink power on a linear transponder. Another group may be causing problems maliciously, say by intentionally interfering with specific transmissions. In a worst-case scenario, organized groups of unlicensed stations may take over part or all of the system for their own use. This has been seen on disused military systems such as FLTSATCOM. To my knowledge, we have not experienced any systematic “pirate” usage of amateur satellites, perhaps in part because of their limited orbits and signal strengths. An easy-to-use geosynchronous system, such as we want to build, could be far more attractive to pirate users.

On an analog satellite, there is little or nothing that can be done about these problem stations, short of continuously monitoring for abuse and turning off the satellite when abuse is detected. Features like AMSAT-DL’s LEILA have had some success in mitigating the problems caused by excessive uplink power, but can only do so much on an analog transponder, because it isn’t practical to distinguish wanted signals from unwanted ones in the spacecraft payload. With all-digital transmission and a relatively powerful computer on board, we can do much more.

Here we focus on the interrelated set of system design issues we refer to as `AAAAA`. In roughly chronological order, these are:

## Assembly
When a new ground station is constructed, it must be configured to operate with the system, including the provisioning of any cryptographic secrets and certificates that may be required for participation in the security aspects of the system.

## Acquisition
When a ground station is turned on, it faces the problems of acquiring the downlink signal from the payload, and initializing itself to work with whatever operating state the system happens to be in.

## Access
When a ground station wishes to transmit through the system, it must go through special procedures to make its presence known to the payload and begin to communicate.

## Authentication
Whenever a ground station is participating in communications through the system, the payload has the option to request that the ground station prove that its claimed identity (its callsign) is authentic. Such requests would be driven by system policy, and might vary from payload to payload, from time to time, and from user to user, all driven by system policies.

## Authorization
The purpose of authentication is to enable the payload to enforce an authorization policy. That is, the payload may choose to impose limits on certain ground stations or even block them entirely from using the system.

Our AAAAA design goal is to make the system as painless to use and robust as possible, while strongly encouraging that systems be freely available to all licensed amateurs. By providing the mechanisms to defenestrate a few miscreants when necessary, we hope to make the system a joy to use for the vast majority of cooperative radio amateurs. Perhaps the very existence of the mechanisms will be enough to discourage bad behavior.
