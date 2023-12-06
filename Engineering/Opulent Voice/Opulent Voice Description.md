<!-- Copy and paste the converted output. -->

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 16

Conversion time: 12.91 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Wed Dec 06 2023 10:55:14 GMT-0800 (PST)
* Source doc: Opulent Voice
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!


WARNING:
You have 10 H1 headings. You may want to use the "H1 -> H2" option to demote all headings by one level.

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 16.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>
<a href="#gdcalert16">alert16</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# Opulent Voice



Version 0.2



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")



# PREFACE

This is a protocol description document for Opulent Voice, a voice and data digital communications protocol intended for microwave band use. It uses high bitrate vocoders. If you are curious about the differences between vocoders and why high bitrate matters, then review this page of vocoder samples, with and without background noise added. [https://www.nist.gov/ctl/pscr/speech-intelligibility-demo](https://www.nist.gov/ctl/pscr/speech-intelligibility-demo)


# ACKNOWLEDGMENTS

 \
P25, Yaesu System Fusion, ICOM D-Star, DMR, and M17 have all provided strong motivation for a modern protocol with better voice quality. 


# HOW TO JOIN THIS PROJECT

Please read [https://www.openresearch.institute/getting-started/](https://www.openresearch.institute/getting-started/)


# INTRODUCTION

VHF/UHF/HF digital voice protocols have bandwidth limitations, which limit the vocoder bitrate. Commercial VHF/UHF voice products generally use proprietary codecs, notably AMBE. M17 uses CODEC2 at 3200 bits per second.  \
 \
The microwave bands (Amateur Radio Service) can have much higher bitrates. This allows for the design and use of a high definition voice protocol. This work can be adapted to any communications service that can legally transmit the signal.  \
 \
Opulent Voice features include the following.



1. Flexibility in the high-bitrate codec choice
2. Flexibility in the sublayer protocol options 
3. Data and voice can be sent without changing the mode
4. Existing standards are heavily leveraged in order to speed adoption and increase ease of use

Encryption is not required. Encryption can be added. See IMPLEMENTATION RECOMMENDATIONS for details on encryption. 



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.jpg "image_tooltip")



# OVERVIEW

Overview of current implementation. 



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


Overview of final design. 



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")



## THE PHYSICAL LAYER

Physical layer description of 4-ary minimum frequency shift keying.


## P4XT UPLINK FRAMES

Here is the P4XT Uplink frame format. 



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


 \
SOT*			Start of Transmission		01 1000 1101 0010 1110 1000 0010

PREAMBLE		Preamble tone			Composed of one frame’s worth of symbols from the


                            outer two tones, leading with +3

SYNC			Synchronization frame	2 bytes, unencoded

STATION_ID		e.g. Callsign + SSID		6 bytes e.g. KK6OOZ-13 \


FLAGS		Flags and Fields		3 bytes \


FLAGS:BERT		Bit Error Rate Test		0 = BERT mode inactive and normal payload         \
							delivered


                            1 = BERT mode active


                            	

FLAGS:EOS		End of stream bit		0 = This is not the last frame

							1 = This is the last frame

 \
TOKEN		Claimed authorization token	3 bytes Station generated n-bit PRNG token

PLDATA		Physical Layer Data		This is the place where all the burritos go

*Start of Transmission (SOT) is an alternate preamble under discussion. We would re-use the preamble from DVB-S2/X. There is an argument for a unique preamble for the uplink in order to not confuse uplink and downlink if point to point communications are a requirement. Comments are requested.  \
 \
Originating Station ID is captured in the STATION_ID field. For the implemented prototype, this is an Amateur Radio Service call sign and secondary ID, in order to enable multiple stations from the same licensed call sign. Any unique Station ID can go here. \
 \
Physical layer payload data is contained in the field PLDATA. 


## IP

This layer is IP packets. It is formed by adding/removing an IP header.

 


## UDP

This layer is UDP packets. It is formed by adding/removing a UDP header.


## RTP

This layer is RTP. It is formed by adding/removing an RTP header.


## OPUS \


A single payload frame is two 20 mS OPUS protocol frames, formed into an OPUS Packet. 16 kbps is the first implementation. 


# AUTHENTICATION AND AUTHORIZATION


## Definitions

Authentication is the process of confirming a licensee's declared identity.

Authorization is the process of allowing particular identities access to particular resources.

Satellite is any equipment that serves as the payload for any Phase 4 Ground system. This includes but is not limited to an orbiting satellite payload, satellite simulator (Groundsat), or terrestrial hub. 

Phase 4 Radio or ground station is equipment that complies with the Phase 4 Air Interface. 

Stop List is a list of stations that are positively not authorized to transmit through the satellite. There are probably at least two levels of Stop List: stations that have merely failed to authenticate, and stations which are permanently banned regardless of their authentication status.

Pass List is a list of stations that are positively authorized to transmit through the satellite.

Ground Control Station is a station that can command the satellite. 

Misuse is communications that are illegal or damaging to the communications system. 


## Introduction

If the satellite has no state, then every frame has to speak for itself. Therefore, authentication and authorization are affected. 

Logbook of the World (LoTW) is an QSO confirmation (QSL and awards verification) application from ARRL, built upon the OpenSSL family of cryptographic functions. In order to prevent QSL fraud, LoTW issues certificates to verified licensees that are used to cryptographically sign QSO records, certifying them as originating with the station licensee. These certificates could be used to sign other records for our purposes.

[https://lotw.arrl.org](https://lotw.arrl.org)

Within the United States, successful LoTW account establishment confirms that the address on file at the Federal Communications Commission (FCC) for an amateur radio licensee can receive and respond to information received at that postal address. That serves as the basis for licensee authentication. 

The address given to the FCC comes from the address that that license applicant submits on their form 605. The FCC does not validate this address. The FCC relies upon the volunteer examiner coordinator (VEC) to review the form 605 and ensure that the applicant has provided a mailing address in the United States. The applicant provides the address. The VEC is not required to independently confirm this mailing address. The applicant’s name on the form 605 must match the name on accepted forms of identification.

This is the limit of authentication provided to, and therefore by, the licensing authority. In the US, this is the FCC. 

There are two fundamental questions.

Does it make sense to exceed this level of authentication?

What sort of authentication and authorization is required of Phase 4 Ground radio traffic?

The default security implementation of Phase 4 Ground is the process described within this document. The Phase 4 Ground process must defer to a process selected by the satellite, if that security process selected by the satellite needs to claim priority. If there is a different process selected by the satellite, then a full specification must be provided to Phase 4 Ground as part of the Air Interface documentation. This serves as a “we can’t read your mind” clause. 


## Phase 4B Satellite State 

Phase 4 Ground considers a process of authentication and authorization in this document. This process involves state in the satellite and in the Phase 4 Radio. 

The state in the satellite requires the following things.

1. Memory for a database. 

2. The ability to read from this database.

3. The ability to write to this database.

4. The ability to demand and process authentication from the Phase 4 Radio.

5. The ability to do some processing using data received from uplink communication frames and information from the database.

The state in the Radio requires the following things. 

1. The ability to generate a token.

2. Memory to store the token.

3. Memory to store private key.

4. Memory to store a certificate.

5. Ability to sign a message containing the generated token with the private key. 

6. Ability to send the signed message plus the certificate to the satellite when it is demanded by the satellite.


## Authentication Process Overview

The process is as follows. 

Stations that comply with the air interface can transmit through the satellite. The station is configured with an amateur radio callsign, plus a Secondary Station Identifier (SSID) of TBD bits to allow a particular licensee to operate multiple simultaneous stations, and with the ARRL-issued private key and certificate for that callsign. In addition, the station must generate a token of TBD bits chosen at random. Every transmitted uplink frame contains in its header the callsign, SSID, and token.

The callsign and SSID will be retransmitted in the downlink frame header, but the token is never transmitted on the downlink. Since it is fairly difficult to intercept an uplink transmission, this makes it difficult for an impostor to hear another station's authenticated callsign:SSID and start using it.

The satellite stores the token, the claimed call sign, the claimed SSID associated with the call sign, and a time stamp. This is a tuple that forms the rows of a database. 

(satellite time stamp : callsign : SSID : token)

When each uplink frame is received by the satellite, it decides whether to accept it for retransmission on the downlink, or discard it. It may also choose to initiate an authentication transaction with the ground station. Alternatively, or in addition, a Ground Control Station may initiate an authentication transaction with any or all active station(s). Unless and until an authentication transaction with a given station has been attempted AND FAILED, the satellite must accept its frames for retransmission (unless that station has already been Stop Listed for another reason).

This achieves two important goals. Communication is unimpeded, and the loss of Ground Control Stations can be well-tolerated. When Ground Control Stations are not required for normal communications, system durability and reliability is greatly increased. 

When authentication is not frame-by-frame, or required to initiate the process of accessing and transmitting through the satellite, efficiency and performance are greatly increased. In particular, the very first message from a station is not delayed for formalities or blocked entirely; in an emergency situation this could be essential.


## Mitigation of Misuse

The risk of bad actors is recognized, but management of bad actors is achieved through Stop Listing known bad actors after complaint or system statistics or some other method reveals that the problem is Misuse.

Phase 4 Ground recommends that Misuse must be assumed to be misunderstanding or misconfiguration until proven otherwise. If Misuse is deliberate and there are irreconcilable differences, then Stop Listing is the mechanism for resolving the Misuse.

The satellite may be configured to automatically initiate an authentication with each new station it receives, and/or periodically at some interval, or it may rely entirely on Ground Control Stations to request authentications. The satellite controls the rate at which authentication transactions can take place, so it can never be overloaded by the required calculations.

When there is a cause for authentication, a request for authentication can be made by a Ground Control Station. Requests for authentication can be made to all rows with expired time stamps (time stamp &lt; some value : * : * : *), a particular row of the database (* : call sign: SSID : *), all rows that have a particular call sign (* : call sign : * : *), all call signs (* : * : * : *), or some other combination.

Regardless of how the authentication is initiated, the transaction begins with a message from the satellite addressed to one particular (call sign : SSID).

Upon receiving a request for authentication, the station addressed would generate and transmit a response message with the usual header (including callsign, SSID, and token). The token could be the same one it was already using, or it could be a new one (which it would then use for future transmissions). The payload of the message is the cryptographic signature of the message header, including the certificate associated with the callsign. This challenge response is identified in the PLHEADER by setting the CERT bit. With this information (and its pre-programmed knowledge of the ARRL's root certificate) the satellite can verify the signature.

If the authentication response is not received in a timely manner, after TBD number of attempts, the station is Stop Listed. 

If the authentication response is received, the satellite checks that the certificate is valid by comparing with the root certificate (LoTW root certificate is through GoDaddy). If the certificate is not valid, the station is Stop Listed.

If the certificate is valid, then the signature is checked. If the signature is not valid, the station is Stop Listed.

If the signature checks out, then the row corresponding to the station in the satellite security database is updated.

The result of each authentication transaction is reported on the downlink, where it is visible to the ground stations and to Ground Control Stations.

Action Item: work out the rules for changing tokens. If two (or more!) stations are trying to use the same callsign:ssid with different tokens, the one(s) that can successfully authenticate should be allowed, and the other one(s) should not. But we also need to prevent a bad guy from defeating the system by simply choosing a new token for each transmission. And yet we don't want to stop a station that had to reboot from starting over with a new token.

Action Item: work out a way for a station that is Stop Listed for authentication failure to request a do-over, after the operator corrects the configuration.


## Authorization Process Overview

The authentication procedures outlined above just verify the identity of stations trying to use the satellite. Separate authorization procedures are used if not all licensed amateurs are welcome to use the satellite.

For example, an agency that has an MOU with the satellite, and has authority over the operations of a Ground Control Station, could impose an authorization policy. A combination of Stop List and Pass List techniques could be used. 

Examples:

"All stations that participated in Red Cross Drills within the past 9 months”

"All stations that support a throughput of greater than 500kbps” 

"All stations that have registered to participate in the weekend contest"

In cases where a list of authorized stations is available, the satellite could be configured with a Pass List and instructed to limit all other stations to short message transmissions only. Phase 4 Ground recommends that stations never be entirely banned from access, since (1) banned stations may have critical emergency traffic that should not be blocked, and (2) banned stations may need to message the authorities to request and justify being unbanned.

Stop Lists and Pass Lists are managed by Ground Control Stations. Ground Control Stations can also choose to implement potentially complex policies on the ground, by monitoring the downlink for any unauthorized activity and taking action to stop it. The controlling interest of the Ground Control Station sets Stop List and Pass List policies. 

Phase 4 Ground recommends that Stop Lists should time out whenever possible. Stop Lists should reset upon satellite reset. Stop Listing should be quite temporary by default. If the Ground Control Stations all go offline in a disaster, it is better to open up the system than to leave it locked down in a way that will eventually cause problems.

AI: define uplink and downlink messages relating to authorization. Downlink messages should give non-authorized stations notice so they don't keep trying to transmit, and should ideally give them an explanation so they know why they are not authorized. Uplink messages might explicitly request authorization in certain cases. One use case we've heard is that a Served Agency distributes a secret code that can be used to gain access; that would be implemented through some messaging.

AI: there may be more levels of authorization than simply authorized and not authorized. Some stations may be allowed only short text messages, while others may be allowed to use realtime voice streams, and yet others may be allowed to grab as much bandwidth as they can manage. 


## Threat Assessments

The primary threat to this amateur communications resource is people outside the community using the spacecraft. If it's easy to gain illicit access then capacity is drained. Using the satellite without authorization needs to be hard enough that it is rendered rare, while also not making normal legitimate operation a miserable experience. 

The community is defined as licensed ham radio operators that are cooperative.

Cooperative means that the operators stop transmitting if asked, are disciplined, do not produce intentional harmful interference, rectify unintentional harmful interference, and defer to emergency traffic. 

If the identification of primary threat is accurate, then LoTW cert checking is a solution. LoTW excludes non-hams. 

We assume that the large majority of licensed hams are cooperative. We then assume that the list of uncooperative hams, whether they became uncooperative, or have always been uncooperative, is short and can be effectively managed through Stop Listing. 

Stations can be added to a Stop List by several methods including but not limited to observation, complaint, or statistical detection. Positive confirmation with a human in the review loop is ideal. 

The threat can be refined. The following categories are either licensed operators that became uncooperative or unlicensed operators that are by definition uncooperative. 


## Imposters

An operator that takes on the identity of a legitimate operator that has authentication and authorization is called an Imposter. 

The required information to become an Imposter must not be present in the downlink. However, it is available through eavesdropping on an uplink. If an Imposter is able to eavesdrop on an uplink, they will be able to obtain the call sign, SSID, and token of the legitimate operator, and form frames that appear to come from a legitimate user already in the database, and therefore would be passed as legitimate traffic by the satellite. Another potential Imposter method is to overwrite the payload part of the frame with a new payload. This requires precise timing and greater transmit power than the legitimate station. 

An Imposter can be eliminated by several methods.

1. Frames could be serialized, with duplicate or out-of-sequence frames discarded. This adds some overhead. This method can be circumvented by deserializing or overwriting. 

2. "Signed transmission mode": Forcing the signature, by private key held within the Phase 4 radio, of every frame. This adds substantial overhead. This can be circumvented by stealing the private key. 

How would these methods be implemented?

If a Phase 4 radio is able to see payloads in the downlink that it did not send, then it could send a message to the Ground Control Station. The Ground Control Station could then put the Phase 4 Radio in "signed transmission mode". This requires something like a traffic summary which would have to have enough information for either an algorithm or an operator to notice extra traffic.

This could be an extension of presence awareness. This could include looking for too large of a variance in Eb/No. 

Adaptive Coding and Modulation can potentially hide traffic from potential Imposters. As a side effect, ACM could make it substantially more difficult to steal the identity of a legitimate operator. 

An ongoing eavesdropper can defeat anything aside from a cryptographic solution. The cost of preventing ongoing eavesdropping leading to Imposters gaining satellite access must be balanced against the probability of this type of threat. 


## Jammers

Jammers are stations that produce intentional interference with the goal of denying access to a communications resource. This could range from loud signals aimed blindly at the satellite up to and including correctly formatted frames that are designed to interfere with the normal operations of the satellite. 

If the satellite simply doesn't demodulate signals that do not comply with the air interface, then some jammers are eliminated simply due to the fact that the satellite doesn't demodulate waveforms that it is not programmed to receive. However, by aiming loud signals at the satellite the jammer can increase the noise level at the satellite, and therefore the signal-to-noise ratio for one (or more) channels. Since the satellite is FDMA, and the channels (satellite sub-band) are well-known, and the occupied channel list will appear in the downlink, the channel (or all channels) can be targeted for jamming. Causing the satellite ADC to saturate may prevent the satellite from receiving. Detecting the presence and the source of this type of jammer needs to be discussed. Attempting to hide which channels are occupied is insufficient considering that a motivated jammer can simply occupy the entire uplink bandwidth.  

A more sophisticated jammer transmits a properly modulated waveform. If the satellite drops traffic that does not contain a token, does not contain a payload, or does not contain a call sign, SSID pair, then more potential jammers are eliminated. The traffic, while demodulated, will not appear in the downlink. The traffic does consume satellite resources.

Signals that comply with the air interface, contain a plausible call sign, SSID, a payload, and a token, but are designed to consume authorization and authorization resources, are also jammers.

Potential attacks include causing the satellite, by either following either onboard rules or upon (subverted) direction from the Ground Control Station, to perform functions in excess of processing resources.

Traffic that uses a different token and/or SSID and/or call sign every frame forces a large amount of database activity and processing.

 

The Ground Control Station could be compromised or tricked into directing the satellite to re-authenticate or re-authorize in excess of processing resources. In this case, the traffic is not at fault, but instead the mechanisms that are in place at the controlling agencies are subverted or abused. 

Attacks designed to cause the satellite to run out of space in the database are a type of buffer overrun attack. The database is of finite size. 

Attacks designed to cause the satellite to process itself to death are a type of denial of service attack. There is a finite amount of processing available to check tokens. There is a finite amount of processing available to provide authentication. 

There are several ways to address these potential threats. Some of these methods involve keeping additional state in the satellite. Therefore, the cost of the additional state and/or additional processing must be balanced against the probability of this type of attack occurring. 


#  \
EXAMPLES FOR OPULENT VOICE

For a simple example of coding and decoding with OPUS please see: [https://chromium.googlesource.com/chromium/deps/opus/+/1.1.1/doc/trivial_example.c](https://chromium.googlesource.com/chromium/deps/opus/+/1.1.1/doc/trivial_example.c)

For a more comprehensive example of coding and decoding with Opus, download the libopus source code from [https://opus-codec.org/downloads](https://opus-codec.org/downloads) and look for `opusdemo.c` in the `src` directory.


# IMPLEMENTATION RECOMMENDATIONS


## Terrestrial Open Source HT at 1.2 GHz

A 1.2 GHz point-to-point terrestrial implementation is in progress for a target demonstration of prototypes at DEFCON 2022 in mid-August. 

Starting with the 1.2 GHz (23 cm) band plan, we first make decisions about where the prototype hardware should be programmed to transmit and receive.  \
 \


<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


One can see there are at least two sub-bands for Digital Communications and one that is designated for experimentation and satellite uplinks.  \
 \
Prototype hardware of a HackRF SDR and a Portapack for User Interface was selected. The build environment for Mayhem was cloned and confirmed working. 


# ENCRYPTION


# REFERENCES

This section shows how the codebase from Mobilinked was adapted from M17 Protocol to Opulent Voice.  \
See [https://github.com/OpenResearchInstitute/opv-cxx-demod](https://github.com/phase4ground/opv-cxx-demod) for source code. 


## Modulator


### Transmit Thread From the M17 Codebase


## 

<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")



### Transmit Thread Modified for Opulent Voice


## Demodulator


### Demodulator State Diagram from the M17 Codebase



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.png "image_tooltip")



### Demodulator State Diagram Modified for Opulent Voice


### Frame Decoder Operator From M17 Codebase



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")



### Frame Decoder Operator Modified for Opulent Voice



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.png "image_tooltip")



### Decode LSF From M17 Codebase



<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.png "image_tooltip")



### Decode LSF Modified for Opulent Voice

The LSF frame, sent once immediately after the Preamble, is removed in Opulent Voice. This slightly increases efficiency and reduces complexity. 


### Decode Lich From the M17 Codebase



<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image12.png "image_tooltip")



### Decode Lich Modified for Opulent Voice


### Decode Stream From the M17 Codebase



<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image13.png "image_tooltip")
 \



### Decode Stream Modified for Opulent Voice


### Decode BERT From the M17 Codebase



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image14.png "image_tooltip")



### Decode BERT Modified for Opulent Voice


### BERT Mode From the M17 Codebase



<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image15.png "image_tooltip")



### BERT Mode Modified for Opulent Voice


### Decode Packet From the M17 Codebase



<p id="gdcalert16" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image16.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert17">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image16.png "image_tooltip")



###  \
 \
Decode Packet Modified for Opulent Voice
