Phase 4 Ground was established in April 2015, and has grown rapidly since October 2015. We have a lot of new people, and a lot of new things to think about, provide, and consider going forward. Here is a recap and summary of our current mission, followed by engineering reports for the week. 

Who are we and what are we doing?

Phase 4 Ground is an AMSAT-sponsored all-volunteer team providing an ensemble of ground terminal solutions for the "five and dime" band plan. 

When we say an "ensemble of ground terminal solutions", we mean we provide you as many recipes as possible. Want to build your own station from scratch? As long as you comply with the developing air interface document, and the station requirements, then you can! Want to put a station together from existing modules? We will provide recipes that specify boards or modules or GNUradio flow graphs. Want to buy a complete station? We are working hard on identifying manufacturers that are willing to make our radio.

"Five and Dime" is the 5GHz uplink 10GHz downlink strategy that AMSAT has embraced for microwave satellite projects. Phase 4 is expected to provide ground terminal solutions for Phase 4B geosynchronous launch in late 2018 early 2019, the phase 3E high earth orbit satellite, and also to provide receiver support for AMSAT's entry into the NASA Cube Quest Challenge. 

There is a lot of range here. Cube Quest Challenge is going to the moon, where the path loss will be substantial, and very large dishes will be required to receive telemetry. Phase 4B has much lower path loss, but we want to implement variable rate coding and modulation and provide an emergency communications support role. Phase 3E is the least specified of the three projects, but our goal is to design as common an air interface between the three as possible. The user terminals must be re-used.

Above all, operators should come to expect a high quality consistent user interface that takes advantage of all that digital has to offer across these AMSAT projects. This is an ambitious tall order, and we need help in making it happen. We will continue to actively recruit and welcome volunteers. Our goal is to have no bulky software installations. The radio is accessed as if it was a web app. 

The trojan horse project inside these satellite projects is terrestrial microwave. We love the microwave bands, and we simply don't have enough solutions that make it easy and fun for people to operate. We need to go out there and use our spectrum. Phase 4 radios will be designed so that they can either adapt or be configured to use modulation schemes that are better able to deal with terrestrial multi path. This is one of the reasons why we are spending so much time investigating DVB-S2 and DVB-T2. 

Imagine having a radio that "just knows" when it's pointed at a terrestrial Groundsat, and uses the right modulation for that communication. When it's pointed at a satellite, however, it switches to something like DVB-S2. Whether this is a manual switch or something that is sensed inside the SDR, the result is the same. We want to design an adaptable radio that appeals to terrestrial microwave enthusiasts as much as it appeals to satellite operators. 

Amateur Radio Access Points (ARAP) are another part of the project. This allows legacy radios, FM handhelds, or emergency traffic to be shipped up to the satellite from anywhere that an ARAP can be deployed. The demonstration from 2015 AMSAT Symposium and several other meetings shows this in action at a small scale. There is a lot of excitement about ARAPs because the expected cost of a Phase 4 radio is expected to be at least $1000. Having an ARAP would enable communications through the satellite with much less expensive gear. Think of it as like Yaesu Wires-X. 

Here's reports about specific activities this past week on the project. 

A meeting with Escondido city officials at Dixon Lake was very successful. As you may know, Dixon Lake is one of the sites we want to use for the San Diego Groundsat experiment. We were postponed at Dixon Lake by concerns about providing AC power. We are proceeding with battery and solar as well as AC power as of this week. Power is required in order to install equipment to support San Diego Groundsat experiments. The equipment that had been installed was removed until the question of whether and how to provide AC power was resolved. We are now able to reinstall the mast and antennas, move forward with computers and modems, and are prepared to power the experiment with AC mains and solar/battery backup.

Flex Radio discussions began this week. Flex Radio approached AMSAT President Barry Baines in June 2015 at Hamcom and indicated an interest in building AMSAT ground terminals. Providing an off-the-shelf solution is one of "the ensemble of solutions" for Phase 4 Ground. Flex Radio is aware that there are some potential objections, and this next week it is our goal to start fully specifying them and finding options to resolve them. This is going to involve some discussions about open source, open process, open hardware, platform potential, whether or not our radio could or should anchor or be leveraged into other markets, manufacturability, profitability, and a lot of other factors. There are areas of discussion that will be contentious, and there are areas of discussion where there will be great harmony. From this process, we will be able to make a decision for this project. This same process will be required for any specific manufacturer that we approach. 

AHA discussions happened this week. AHA, a design center specializing in forward error correction and data compression, has implemented the DVB-S2X standard on a USRP x310. They have presented their work to the community at a recent GNUradio conference. They are enthusiastic about amateur radio in general and this AMSAT effort in particular. They are in the business of selling IP cores. One possible path forward is to purchase their implementation. There is the possibility that we should consider this for the payload, rather than the ground terminal. It would then be our responsibility as ground terminal designers to implement the SVB-S2X receiver. This would almost certainly be done in an FPGA.

Space segment team Common Air Interface document collaboration has increased. I was granted access to the space segment document repository and discussion forum this past week and have joined their conference calls. More volunteers have been added and we should expect to see collaboration and discussion increase and progress made. We agreed on cross-polarizing 5GHz and 10GHz links. We agreed to pursue DVB-S2/X for the downlink. Space segment is assuming OQPSK for the uplink. We were assuming MSK. These are very related modulations, but the same. 

Donor meetings are happening. I can't talk about them, but the news is good. 

HackRF doing uplink is getting closer. We are going to put out a call for HackRF owners to step up and join a team to test uplink GNUradio flow graphs. If you have one, or have been on the fence about buying one, now is the time. They are great SDRs and will probably end up being one of the recommended modules for an uplink solution. Kent Britain and others are on top of the reality that filters may be necessary for this to work full-duplex. 

OET Bulletin 65 study worksheet revision has been published. Bulletin 65 specifies the maximum permissible RF exposure that we can allow for controlled and uncontrolled environments. We need to discuss the results. It's not terrible, but it seems clear that if you use more than a watt into an 18 inch dish, you will not be in compliance. Pragmatically, this means we have to include warnings. The operator needs to be aware of which combinations of equipment will create an exposure situation. We have a spreadsheet in the repository, and are considering how to work RF exposure limits into the user interface. 

Phase 4 Ground antenna team is working on a dual-band feed. Having one dish instead of two is almost necessary for emergency communications deployments, ease of use, and portability. The two-dish baseline configuration that will be common among hobbyists and experimenters is what we assume most stations will build, but providing a dual-band feed is a goal. In order to achieve this dual-band feed design, the uplink and downlink need to be cross polarized. We understand the polarization to be linear on each band. Cross polarization helps with the two-dish and other antenna solutions as well, but is critical to the dual-band feed design. Paul Wade is currently working on a dual-band feed experiment. 

Kerry Banke and Robson Pereira have developed a very low-cost prototype reference signal source to test the 10MHz comb generator approach for the 10GHz LNB-based receiver. Read more about it in Phase 4 Ground github repository in Tom Clark's Low Cost AMSAT X-band Ground Terminal presentation from 2015 Symposium. Kerry also has another experiment in the works that may greatly simplify this part of the receiver. More documentation is on the way. 

Pointing assist circuit supplies are on the bench, but the design hasn't gotten attention over the past week. Frame for the LPA and Use Case work got postponed due to all of the meetings and calls. Farming more out will be necessary, and these things are good candidates.

All of our documents and software are on github. This is where work in progress and completed documents live. As you can probably surmise, almost everything is a work in progress at this time, but comparing today to a month ago, there's some big strides forward. 

I'm here to help you find a way to contribute. I can't read your mind, so reach out to me and we'll find something fun and productive for you to work on. Most of it will require you to have good email or phone skills because we're spread out geographically. 

As always, please send me your video reports, photos, questions, answers, and documentation. Chocolate wouldn't be bad either. 

Find us on the web at https://github.com/phase4ground

We have a mailing list for announcements and discussion.

To volunteer for Phase 4 Ground and get on the mailing list, go here:
http://ww2.amsat.org/?page_id=1121

Want to help but don't have time? Join AMSAT. Join ARRL. Send AMSAT a check in any amount. Send us encouragement! 

More soon,
-Michelle