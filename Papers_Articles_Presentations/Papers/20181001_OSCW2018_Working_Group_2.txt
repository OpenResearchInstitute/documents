Workgroup 220181002 by Abraxas3d - participants in working group, please revise and extend
One of the activities at the Open Source CubeSat Workshop 2018 was a set of working groups. These small groups met after the presentation sessions on both of the two days of the conference. The working groups lasted between 60 and 90 minutes. Each working group had a topic or question. Discussion was free ranging, encouraged, and productive. 

This working group was chaired by Manolis Surligas, a member of the SatNOGS core team responsible for software development for client and gnuradio. 

The goal was information gathering from the community in order to improve SatNOGS.

The central questions of this working group were:

What is your experience with SatNOGS? 
What needs to be improved?
What do you expect from SatNOGS?

A contingent of librarians and astronomers were present in this group. They explained that they found the waterfall, images, sound files, and sets of hex numbers to be confusing in two ways.

First, "observations" do not equal "data" in their field. "Observations" are the act of taking the data. Second, there was a lot to SatNOGS software that wasn't defined or placed in context. It was hard to figure out why the functions and data were cool and why one would want to use or have them. There was an unmet expectation of a tutorial.

As SatNOGS grows, the number of people outside the traditional populations will grow. Those traditional populations include amateur radio operators. Radio amateurs are in general familiar with antennas, waterfall displays, Keplerian elements, call signs, and so forth. The documentation and instructions are written, in general, for this population that has a particular technical background. 

In order to scale up into communities and populations that may not have the traditional SatNOGS background, a guided tutorial can help bridge the gap. A guided tutorial may include basic definitions, expansions of acronyms, workflow, and an explanation of rotator vs. non-rotator stations. 

Current instructions assume everyone approaching SatNOGS is interested in and enthusiastic about building. The astronomer or data scientist may be much more interested in the data produced than in the build process.

Some of the participants were confused about how to find out the purpose of the CubeSats in the database. The functions of the payloads did not appear to be listed. This would be very useful information for people looking for particular telemetry streams. 

To build a station, it was unclear where to start. The point of entry is assumed to be relatively high in terms of skill sets. A guided build would fill this gap. 

"How to build SatNOGS for normal people" was a suggested web page. 

Manolis explained that the development team understood the stations to have become too Raspberry Pi centric. This is being addressed. The station needs to be modular in terms of processor, SDR, and all other major components, and if the station is too dependent on one particular architecture, then extending and adapting becomes difficult. 

At what point does the Raspberry Pi saturate or become unusable when the SDR is upgraded? Are there any benchmarks for this? 

Binary packages for SatNOGS are a development team goal. Ubuntu Snaps, pip, and apt-get install SatNOGS were mentioned as desirable deployments. 

Installing and configuring the software, building the hardware, learning how to configure the station through the bring-up process, deploying a station, maintaining a station - these are all non-trivial tasks.

The success of the network is notable. SatNOGS went from 10 stations a year ago to over 100 stations at the conference. In order to scale further, the stations must achieve fully automated status. Having any people in the loop (more than absolutely necessary for debugging or development) is a big problem for scale. SatNOGS core team is keenly aware of this.

Kitting was discussed. Kits of SatNOGS stations would increase the rate of deployment. When Manolis asked the group if kits were of interest, there was a strong positive response. SatNOGS core team viewed kits as a positive addition to the network and it had come up in previous discussions. 

I took the action item to reach out to TAPR (https://www.tapr.org/) to explore whether or not TAPR could support SatNOGS with station kits. TAPR offers productization, a store front, bridge capital, communications resources, a history of supporting open source kit sales from a variety of amateur radio sources, and an active membership fully in line with the interest profiles of SatNOGS station and network builders. TAPR just commenced a collaboration with space scientists to study the ionosphere, and there is great potential in finding ways for the SatNOGS network to participate in this scientific endeavor. 

It was emphasized that stations close to each other are not "in each other's way". Having multiple stations in close geographical area means that each station can be assigned to watch for a different payload. It is a misunderstanding that once a place is covered by a station that another one close by is of lesser value, or competes against local stations.

The cost of the stations was discussed. Some of the participants believed that the cost guidance on the SatNOGS website was a bit low. The group settled on guidance of "expect to pay $60 for a static station and $200 for a rotator". 

Manolis asked if anyone was designing SatNOGS into a CubeSat project, and the answer from some members of the working group was yes. 

Manolis asked if there was any difficulty in finding whether it could support your type of telemetry? The answer was somewhat muddled by an intervening discussion of what it meant to be part of the telemetry library in SatNOGS, and how that process was handled, and the level of frustration SatNOGS developers had experienced in the difficulty of getting CubeSat communications cooperation from some missions. In general, the participants that were already familiar with SatNOGS network found it easy to figure out how they could include their type of telemetry or communications protocols, and the people that were not already familiar with SatNOGS network found it to be difficult. This is an area of potential improvement.

In general, if the telemetry used by a CubeSat team matches up to an open standard, it's probably already in the SatNOGS software. 

SatNOGS can produce some very lovely graphs in real time. Access is under the developer tab. This was news to some operators, who had no idea this tab existed and the screens were available to them. This is a possible opportunity for an improvement to the UI or instructions. 

For some operators, it is hard to tell how powerful SatNOGS stations are without someone walking you through it. This is an opportunity for a video walkthrough. 

UPSat was discussed. SatNOGS was of great value in troubleshooting right after launch. The value is not only in being able to have the telemetry from the science payload. Knowing that there's a problem when your CubeSat is over some other part of the globe is high-value knowledge. There was one participant that did not agree, since they "couldn't do anything about it anyway."

Being able to set the priority of observations was discussed. Stations owners may be keeping back their stations from participation in SatNOGS because the owner does not want to lose the ability to prioritize the missions they are most interested in. By not joining, they can point at whatever they want to whenever they want to.

Gamification and paying people to point at stations that are underserved was discussed. Games are motivational and points, awards, levels, swag, monetary compensation, bonus bling, and plenty of other things can motivate stations to compete to cover more of the search space. 

De-conflicting observations, handling special requests, scheduling the "best" observations based on a variety of objective functions, time-frame band sharing, priority lists, machine learning, and scheduling future time slots were suggested. 

Calibrating the link quality of stations or "learning" the local environments (buildings blocking sight lines, local frequency dependent interference, curfews) was discussed. Characterization of stations, elevation and azimuth keep outs, polar plots, noise floors, and other very interesting statistics were discussed.

What came through during this part was how much statistics already exist in SatNOGS, and how close the system currently is to being ready for extremely powerful data fusion. The station dashboard is advanced and useful. More people using it means more interesting things found, more connections made and more data science done. 

Manolis asked the group "What do you expect from SatNOGS?

To participate in the community.
To give back and contribute to the community. 

There is an IRC and there is a community forum. Some of the participants were not aware of it. Improved "How to get in touch with us" web resource was requested. 

A highly visible link to the observation database was requested.

A form where one could submit about their mission in order to start the process of inclusion. Satellite owners need to be able to reach out easily.

Device, RF gain, etc. is in the metadata. Ambient data from the network offers a potential wealth of leverage in answering a wide variety of space communications questions. 

Advice from Manolis to the participants that did not have a traditional (radio amateur) background was to start out with a simple static station and upgrade parts to a more complex dynamic (tracking) station, instead of starting out with a complex build from the beginning. 

There was a series of questions about how to get an arbitrary antenna into the program, how to use predict, how to use SDR sharp, and how to convert images. Weather satellites are an active area of a lot of interest and development. 

There was a series of questions about how to integrate rotating antenna systems. In general, if it can be handled by RotCtl, then SatNOGS already knows how to handle it. 

The process of getting a station included in the network is: Build, register, passkey, testing mode, install gnu radio, install gr-SatNOGS, select SDR, enter production mode. 

Higher frequencies and more SDRs in SatNOGS are the goal, and is the primary reason that Phase 4 Ground attended the Open Source CubeSat Workshop. This was an excellent working group that resulted in a lot of great feedback for SatNOGS as well as substantial information and support for the community members present. 

Corrections, additions, and expansions welcome to w5nyv@arrl.net