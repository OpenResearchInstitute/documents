# Project Reports

## DEFCON 30 Report

Open Research Institute's amateur radio open source showcase at the annual hacker convention DEFCON was located in RF Village (RF Hackers Sanctuary) in The Flamingo Hotel. A volunteer crew of seven people from three US states staffed the exhibit that ran from Friday 12 August to Sunday 14 August 2022. 

RF Village hosts a very popular wireless Capture the Flag (CTF) event. It is a top tier contest at DEFCON and the winners are recognized at closing ceremonies. RF Village also has a peer-reviewed speaking track. See previous talks in the YouTube playlists here: https://www.youtube.com/c/RFHackersSanctuary

RF Village generously offers space for exhibits from the community. For 2022, the exhibits included Open Research Institute, Kent Britain PCB Antennas, Alexander Zakharov (ALFTEL Systems Ltd.), and Starlink (SpaceX). Starlink brought two stations and allowed visitors to experiment with network and physical security. 

Total attendance at DEFCON 30 was estimated at 27,000. Conference events were held in the new Caesar's Forum + Flamingo, Harrah's, and Linq convention centers.

Open Research Institute's exhibit had multiple parts. The entry to the exhibit was a poster session. Posters presented were ITAR/EAR Regulatory Relief for Amateur Satellite Service, Libre Space Foundation's Manifesto, Authentication and Authorization Protocol for Amateur Satellites, and the Ribbit Project Introduction and Architecture. 

All posters were enthusiastically well-received. Specific technical feedback was received on the Authorization protocol that will improve the design. There will be a presentation about the Authorization and Authentication protocol at the September 2022 QSO Today Ham Expo. 

Visitors understood the purpose and potential of Ribbit and could download the free open source Android app from a QR code on the poster. The code was also on the Ribbit stickers handed out at the booth. All 300 of the Ribbit stickers were handed out by Sunday morning. Ribbit allows an amateur operator to type in SMS messages on an Android app. Each SMS message is converted to digital audio tones. The tones are played out the phone's speaker into the microphone of an amateur radio handheld or mobile rig. This can turn any analog HT into part of a digital messaging network. The app can do point-to-point communications and also has a repeater mode. 

Find the Ribbit "Rattlegram" application here: https://play.google.com/store/apps/details?id=com.aicodix.rattlegram

There will be a Ribbit presentation at the September 2022 QSO Today Ham Expo. 

The ITAR/EAR Open Source amateur satellite regulatory relief poster garnered a lot of attention. A very large fraction of DEFCON attendees are familiar with ITAR/EAR, which are a set of regulations that govern the way we design communications satellites in the USA. People that read the poster at DEFCON understood and appreciated the value of the work, which provides long-awaited regulatory relief for the amateur satellite service. The poster presentation lead to an invitation to Policy Village Sunday afternoon for a panel session hosted by the Office of the National Cyber Director. Summary of that session can be found in ORI's 19 August 2022 project report. The ITAR/EAR poster will be part of the projects display at the September 2022 QSO Today Ham Expo. 

Foot traffic flowed past the posters and into the live demonstrations.

The first live demonstration visitors encountered was from OpenRTX (https://openrtx.org). This demonstration used a tablet computer running OpenWebRX to display modified MD-380 transmissions. Visitors could use headphones to hear live transmitted signals. Posters at the table explained the modifications required to implement the M17 protocol on the MD-380 and also described the motivation and value of the work, with an emphasis on the use of the free and open CODEC2 voice codec. The use of CODEC2 in M17 replaces the proprietary AMBE codec found every other digital voice protocol for VHF/UHF ham radio. There was strong interest in both the M17 and the DMR work from OpenRTX, broad understanding of why proprietary codecs are not ideal, and consistently positive feedback. 500 OpenRTX business cards were printed with QR codes for the OpenRTX website and nearly all of them were handed out. 

The second demonstration was Opulent Voice. This is a high bitrate open source voice and data protocol. It's designed as the uplink protocol for ORI's amateur satellite program. The Authentication and Authorization fields are built in and sending data does not require a separate packet mode. The baseline voice codec for Opulent Voice is OPUS at 16 kbps. Higher bitrates are a build-time option. For the DEFCON demonstration, Opulent Voice was transmitted from an Analog Devices PLUTO SDR and received on an RTL-SDR/Raspberry Pi. Visitors could use headphones to listen to the received audio. The modulator and demodulator code can be found at https://github.com/phase4ground/opv-cxx-demod. 300 custom art stickers for Opulent Voice were ordered and all were handed out. 

The two demonstrations compared and contrasted voice quality (3.2 kbps vs 16+ kbps), regulatory limitations (VHF/UHF vs. microwave), and approach to framing (P25 style vs. COBS/UDP/RTP).


The next station had stickers, buttons, patches, ORI's Tiny CTF, Haifuraiya proposal printouts, and a Trans-Ionospheric badge display. See https://www.openresearch.institute/badge 

ORI's "Tiny CTF" was a hidden web server, accessible from the wifi access point located at the OpenRTX demonstration. The access point allowed people to view the OpenWebRX display directly on their connected devices. Participants that found the hidden web server and then blinked the LEDs on a certain piece of equipment at the booth received a prize.

Haifuraiya (High Flyer) is an open source highly elliptical orbit communications satellite proposal. Microwave amateur band digital communications at 5, 10, and 24 GHz are proposed. Transmissions are frequency division multiple access Opulent Voice up, and DVB-S2/X time division multiplexed down. A presentation about this proposal will be at the September 2022 QSO Today Ham Expo.

Based on the feedback about the Trans-Ionospheric, ORI will update and build another round of these badges. Round one of the Trans-Ionospheric badge was a very successful fundraiser. The badges have been enduringly popular in the community, and they can serve as radio peripherals that display link and payload health over bluetooth. The artistic design of the badge is based on the front panel of the Zenith Trans-Oceanic radio. 

There were very high levels of interest, enthusiasm, and positive feedback throughout the weekend. Friends from Ham Radio Village and Aerospace Village visited the booth and shared their experiences, the organizational support from RF Village leads was excellent, and ORI will return to DEFCON in 2023 with another round of open source digital radio work to share. 


## ONCD Panel at DEFCON 30 Report

### Introduction

An Office of the National Cyber Director (ONCD) Cybersecurity Strategy Workshop was held at DEFCON 30 in the Policy Collaboratorium from 14:00 to 15:00 on 14 August 2022. 

The ONCD team provided an overview of the National Cybersecurity Strategy that is currently under development and expected to be released early winter 2022. ONCD Panelists presented their goals, organizational structure, and actively solicited feedback from participants. 

Facilitators were Jason Healey, Senior Strategy and Research Advisor, ONCD, White House. Samantha Jennings, Senior Strategy and Research Advisor, ONCD, White House. Osasu Dorsey, Senior Strategy and Research Advisor, ONCD, White House.

Open Research Institute was invited to the workshop by DEFCON Policy Village leadership. 

Presentation was given using Chatham House Rule, where content can be shared as long as the statements are not attributed to an individual. 

One of the reasons that DEFCON has panels, keynotes, and workshops like this one from ONCD is due to a years' long move towards becoming much more involved in US national government policy work. As we become more and more interconnected, issues of equity and security increase in importance. Hackers have direct experience with the consequences of policy decisions made by public, private, and other actors on the internet. An increasing involvement in policy work became more complicated with STUXNET, Wikileaks (Ghidra), and Edward Snowden, and has deepened to include engagement with the US government at many levels. 

ONCD came to DEFCON to present their plan for a revision of the National Cybersecurity Strategy and to directly solicit feedback from the community. 

Previous revisions of the Strategy were 1998, 2003, and 2018. The current revision is expected to be published late autumn 2022 early winter 2023. 

### Presentation

The panelists were introduced. Experience ranged from military, ethics, legal, and academia. 

The panel asserted that there had been limited stakeholder engagement to date for the Strategy revision and was actively seeking feedback from communities such as DEFCON. 

The mandate of the Strategy document was presented as below. The full description can be found here: https://www.whitehouse.gov/wp-content/uploads/2021/10/ONCD-Strategic-Intent.pdf

1) Federal coherence - who do you go to? People have no clue who to reach out to or who does what in terms of network security, cybersecurity, or safe uses of our communications infrastructure.

2) Resources need to be aligned to aspirations. We have to be accountable for spending money on goals. 

3) Public-private partnerships and collaboration are necessary to defend our networked ecosystem. 

4) Resilient networks - we need a workforce with a clue and the government needs to back that workforce up.

These four mandates were split into four offices of the ONCD. All of the panelists were from the Strategy and Budget team. 

The Strategy document will be aligned with particular national security documents and will follow the "one pen, many voices" process. Stakeholder engagement was emphasized again, along with the desire for a large dynamic range of input. There are acknowledged obstacles to cooperation and collaboration. 

In terms of national defense, the panel asserted that we must align to democratic values but not be stupidly vulnerable. We need capable actors to take on more defensibility at scale. We must stop expecting entities that have the least amount of resources to do the most amount of work. We must shift the burden of resilient and defensible networking to where more of the work is done by entities with more resources. 

### Question and Answer

Q) These strategies have been out before. What's different this time? 

A) The shift from low resource to high resource people, the alignment of roles and responsibilities being done more correctly and at scale. End users are the least equipped to drive security. There is a theory of change at work in this strategy document where in the past there was too much focus on "The Adversary". We have seen what does not work. now we try something more sophisticated. Relying solely on the market isn't working. Government has levers it can pull. What levers? They will be in the strategy document. How can we utilize the Cyber Director office? How can we utilize international partners? This needs to be described clearly and it needs to be able to scale. That is the goal of the revision of the Strategy document. What is the change? It actually has a strategy. Strategy means particular things in policy work. For example, during the cold war, the strategy of the US government could be described in one word: "containment". We need something like that for the current crises of cybersecurity. 

[We do not have a concretely identified enemy or threat like we did in the cold war. One word may or may not work for us when we deal with Safe Uses of AI/ML. AI/ML isn't the USSR.]

Q) I am former military, I now work as an IT project manager with allied partners doing secure communications. This strategy could be funded and could be collaborative but with five different nations with five very different regulatory environments, exactly how are you going to bring in international people? 

A) Strategy contains norms and standards that are definitely commonly shared values. The things that make it possible for Five Eyes to work are the things that must be leveraged in order to have a secure and resilient network. 

The strategy knows where it is because it knows where it isn't. 

If shared values just cannot be had at the very least identify shared goals and focus on them. It has to be at least a coalition of the willing. If we don't clean up the mess out there others will move in that do not share our democratic values. The regulators are already getting involved. Without regulatory harmonization, we cannot effectively leverage our considerable power to effect positive change and reduce corporate espionage, denial of services, and attacks on infrastructure. 

[AI/ML makes things like advanced persistent threats many times worse.]

Q) What is the command and control structure here? Or is it just agencies gone wild?

A) We don't want a dust-collecting document. 

Q) Strategies need strategies of their own to implement. 

A) We will be clear with agencies. This document has directives that will be signed by the US president.

Q) How do we enforce all of this?

A) We haven't yet had a negatable strategy. In other words, we haven't yet had a strategy document that advises what not to do. This will. Strategies that the agencies don't like? That is what the White House is for. It is kind of a referee and has deputies that ride herd and yes, disagreements happen, but directives will be the final word on US government strategies. That is why it is so important to get broad feedback now. 

Strategies, even when they are good and have al the right ingredients, good strategic messages are not only what are we going to stop doing, but also must supply a vision of where we want to get to. 

Q) What is the dumb shit we are going to stop doing?

A) Do we need to regulate more? To make things more secure? We have a set of priorities but they are not all-inclusive. The focus is on highest priorities.  It's trade spaces all the way down. Speed and scale and pushback from stakeholders are things that must happen in order to properly identify the dumb shit we should stop doing. Government doesn't like stopping things. Awareness and speed/scale are pretty much missing. We need to stop doing things that prevent us from having awareness and that prevent us from acting quickly and being able to scale up or down. 

Q) The overall narrative of democratic values, fighting authoritarianism, defensible internet, surveillance, free speech are all things we are hearing from you. What's the relationship between fighting other authoritarian regimes and having a defensible internet? 

A) International capacity building and defining what we want to see as outcomes. Less naiveté about the internet. We need to make systemic change in order to have what we want. Otherwise, authoritarianism will keep winning.

Q) Can you talk about the economics? Infrastructure is very expensive. How to lower the cost barrier to resiliency? There are people that don't know this is a problem and there are people that just don't care. 

A) Theory of change is at the top of our mind. Killing off innovation is not what we want. We want to provide opportunities. But, this needs to be smart not fratricide or death by 1000 reporting mechanisms. For example, the situation in Big Pharma. We must mitigate risks by offering rewards.

There are baseline standards for software. We keep talking about this in terms of software testing standards and software quality. Getting the market to work better. What is unacceptable is that those that have the least cannot be dumped on the front lines to defend us from threats. End users cannot be the foot soldiers in what is quite obviously a war. 

Q) For the National Security Coalition, what is specific to a system? For example CISO compared to DEFCON. 

A) What happens in an organization is policy 98% of the time. For us, it's 1) what do we do about the adversary? Deter, defend forward? We match response to actions. 2) how do we get orgs to patch better or write better software? 3) Things that affect everyone for example DNS, google, facebook. Where is the biggest bang for the buck to improve security and reduce harm from these produces and services?

Q) Is there an Easy Button for privileged information? Is there a single source of information? How can we encourage organizations to share bad news about security failures? So that we can all learn.

A) Information sharing is huge. Critical infrastructure, public/private collaboration centers are attacking this exact problem. Sanitizing the information is important. Are we doing this in a cohesive way? This goes back to 1990 and the BPD60, or ISACS where it was proposed to have a "CDC for the Internet". No real consensus exists on any of this. There is a culture of DC vs. Commercial interests. We can't tinker around with this. It requires some muscularity and resolve. 

Do we want compliance or do we want results? A culture shift is necessary. Systemic change is necessary. This will be a slow, brutal, and painful process. This cultural shift can be seen in the policy documents.

Open source solutions were emphasized as vital, especially since they allow speed and scale, visibility into failures, and publicly accessible solutions to cybersecurity problems.

ONCD welcomes questions, thoughts, and comments. 

https://www.whitehouse.gov/oncd/#:~:text=The%20Office%20of%20the%20National,the%20first%20National%20Cyber%20Director.



