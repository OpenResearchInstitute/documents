## 20220226 Project Report


### ARRL Letter

ARRL featured our HamCation report in the current ARRL Letter. Read the article here: http://www.arrl.org/arrlletter?issue=2022-02-24

Project work gets coverage through documentation and publishing.

Without active and creative projects, documentation and publishing have little value.

The activity and creativity of all volunteers that generously share their time, in many cases after full-time paid work, is the reason for any success. ORI exists to help all of us get the most out of our volunteer time.

Thank you to everyone that helped all along the way with all the projects mentioned in the ARRL Letter.

It's a great honor to be able to help raise the profile of the work being done in high-tech open source amateur radio. Please let me and any of the directors and officers of ORI know how we can do a better job.


### MATLAB on keroppi in Remote Labs West

The "startup" licensed version of MATLAB R2021a, which is compatible with Vivado 2019.1, has been installed on the keroppi virtual machine on CHONC in Remote Labs West.

This has every single toolbox under the sun. Including HDL Coder and many others that turn MATLAB scripts into HDL, GPU, or general purpose processor code. The version of Vivado we use also has HLS. If you have ever wanted to try these things out to make advanced open source products, then now is the time to dig in.

user: abraxas3d
email: ori@openresearch.institute

Please join #fpga on our Slack account to get the password. You will (we believe) need it to run this version of MATLAB.

While installing, the cache filled up on CHONC again, but it was rapidly fixed by the lab director Paul KB5MU. This has been an ongoing challenge with the VMs and Paul is working on solving it.

An Analog Devices PLUTO is connected to keroppi. MATLAB successfully "drove" the PLUTO using a simple Simulink script. This required the installation of a (no cost) PLUTO hardware support package. The PLUTO received signals transmitted from a signal source, over the air, on 70 cm.

The goal is to take MATLAB code, such as the M17 scripts from fred harris, turn it into HDL, program the PLUTO, and operate over the air. The HDL Coder toolbox will require training and practice and documentation on how to use it. It is expected to be a difficult learning curve. We are also very interested in figuring out and documenting any open source licensing issues with this toolchain. We do not know of any at this time, but it's always a good idea to examine things like this very carefully, and then try and fix any problems that emerge.


### AmbaSat Re-spin

Jay Francis reports: "Project crossover work... M17 folks were looking at using different RF chipsets. I took a look at the SX1276 (of course!), and found hacks for direct modulation of transmit, and demodulation of receive. The transmit side works. I suspect the receive side does too (need a bit more testing - it's trickier).

The hacks were inspired by Woj (M17 project) doing similar hacks to get a different chip working (CC1200).

I'm in the process of writing up the info for the M17 wiki.

This isn't really feasible with the ATmega328. The processor is too slow. I started with an ESP32 and then just punted up to a Teensy 4.1 (600MHz microcontroller!!! oh yeah...). But... the technique used might be interesting to experiment with in addition to all the other things we're doing.

It also might encourage us to switch to a higher end microcontroller over time.

Receiver... (a bit glitchy, lots of reasons why that could be, will be investigating). SX1276 demodulating using the frequency error/offset register, streaming deviation values over UDP to a gnuRadio flowgraph, deviation values scaled in flowgraph and saved to a file. What the video shows is deviation (baseband) file being piped into m17-demod and the demod/decoded audio is played."


See

https://youtu.be/adOSRfhXsy8



### CODEC Comparator

Here’s an idea that we’ve (Douglas Quagliana et al) been kicking around that needs someone to implement it. We call it the "Codec comparator." We want people to hear their own voice as it sounds when encoded by various codecs so that they can judge the relative quality of the audio and compare the same audio as it sounds when encoded using different codes. People will be able to record themselves saying a sentence (or perhaps calling “CQ”) and then compare their original (un-coded) audio and the exact same audio as encoded in Codec2, AMBE, DMR, FUSION or whatever other codecs are available. The comparator might be implemented on a webserver. Does AMBE still require a licensing dongle attached to the computer doing the AMBE encoding? If so, it might not be able to be implemented as a stand-alone piece of software that anyone can just download and run. Or, it could be implemented on a laptop at a booth at a convention so that people could walk up and try it.

The idea is that someone could grab a microphone, call CQ or say something into the microphone, and whatever they say is recorded. The recorded audio can then be played back as the "original" un-encoded audio, so you can see what it "really" sounds like (just in case you were too close to the microphone or talking too loud or it got clipped or whatever) and then that same audio can be played back after it has been encoded using various OTHER codecs. This way you can compare how the SAME audio sounds after processing by each codec. In addition, what you’re listening to is not some arbitrary recording that was cherry-picked so that it sounds good when encoded using a particular codec. This is what the person just recorded, right now, using the microphone.

Imagine a screen with several buttons to click on. “Click here” to record audio. "Click here" to listen to the original un-encoded audio that you just recorded. Click over "here" to listen to the Codec2 encoded version of that same audio. Click over "there" to hear the same audio as it would be heard on a Fusion repeater. Click on this other button for the audio you would hear via DSTAR, and so on.


### Ham Expo 12-13 March 2022

Presentations have been completed and uploaded to Ham Expo. The event will be held 12-13 March 2022.

DVB-S2 (LDPC) on FPGA at Ham Expo by Andre Suoto and M17 Project by Ed Wilson are our two main track presentations this time around. They are excellent!

An ORI booth and lounge will be available, with all projects supported. We need PDFs and links to videos to be installed, but the back-end is up and running and configuration is proceeding.

Try out the Lounge at https://www.kumospace.com/ori2022

Please visit the booth, take a shift, hang out in the lounge, and enjoy the many wonderful presentations in the main track.


### DVB-S2/X GNU Radio testbed re-build

Starting over after a delay. Douglas Quagliana installed the gr-dvbs2rx package, which is based on earlier work by Dr. MPEG. It required a later gnuradio than I had, and I thought I had the latest one for Ubuntu 20.04. I tried to upgrade from the gnuradio ppa repository but that corrupted my gnuradio installation and I had to start over. Got the "latest" gnuradio installed, then through trial and error discovered that I was missing (read: "I hadn't installed yet") libsndfile-dev, doxygen, and graphviz. and then cmake completed successfully but "make" didn't. Added liborc-0.4-dev (I had liborc-0.4 but not the -dev) and then make completes but gives warnings.

In other words, a completely normal GNU Radio experience. Work will continue, but in order to get where we want to get, we'll first use MPEG transport stream, then GSE, then M17 transported by GSE.


### Please welcome Anshul Makkar as our newest Director

Anshul Makkar has volunteered to serve as an ORI Director. Please welcome him to the job and give him your support, feedback, and ideas. He is an accomplished working engineer, extremely active in open source, and regularly presents and participates in open source and amateur conferences around the world.

Anshul is establishing a third Remote Labs, with a smaller footprint than Remote Lab West and Remote Lab South. This lab is focused on FPGA development with the Analog Devices 9371 and Xilinx Zynq chips. This is the fourth physical lab location related to ORI projects. A fifth is in development for bacteriophage work.

The establishment, maintenance, accessibility, and productivity of these labs are not just unique in amateur radio, but highly unusual in open source. Read about Remote Labs West/South here: https://github.com/phase4ground/documents/tree/master/Remote_Labs


### Fundraising to Clear the "Public Support Test"

For continued success, we will need to do some fundraising. We have been "too successful" in fundraising from large foundations. We will need to offset the large grants from the four foundations that have supported our work so far with smaller private donations in order to ensure our 501(c)(3) status. This particular rule from the US IRS is called the "33.3% rule" or "public support test".

Here's an article about this rule from Foundation Group, who helped ORI with our initial incorporation and filing.

https://www.501c3.org/understanding-the-501c3-public-support-test/

As you can see from the article, this test means we have a need with a deadline. Want to help? Donate what you can and encourage others to do so as well. There's a PayPal link on nearly every page at https://openresearch.institute

You will hear more about fundraising throughout 2022. Fundraising goals will be a priority until a specific target is reached. If you want to think of this like a PBS telethon, then please do! If you have experience with targeted goals fundraising, or have ever wanted to try it out to see how you'd do, then this is a golden opportunity to make a difference. The faster we make the ratio, the less people have to hear about it.

Two year fundraising goal: $180,000 total, with individual donations being under $20,000. This individual donation limit sounds high, but it is part of the public support test. All of the numbers are based on a sliding window of 5 years.

We will set up a page to track our funding situation with a graphic that shows where we're at. If we don't make the number, then we go through a narrative interview process. We may be allowed to remain a public charity due to the circumstances we face. Or we may have to operate as a Private Foundation. The work will remain the same, but the formal structures are different and there are different rules. Private Foundations do not have to follow some of the rules that organizations like ORI have to follow. For example, rules about conflicts of interest are relaxed and transparency in several categories is not required.


### "Money Isn't The Most Important Thing in Open Source"

#### From the book Working in Public: The Making and Maintenance of Open Source Software by Nadia Eghbal

It's true. Money isn't the most important thing in open source work. We have enough funding to achieve our current technical goals. So, why exactly do we need to raise more money? If you want to know all the details, this section is for you. If you're not interested in the details or "why", stop here. 

Additional unplanned fundraising must happen because we received more money from ARDC (https://www.ampr.org/) than is allowed under the IRS public support test and still remain a 501(c)(3). If one exceeds this test for too long, one is converted to a Private Foundation. Not the end of the world, but it is a different type of non-profit than a public charity.

We proposed converting ARDC grants to program services. This would make it easier for all recipients, not just ORI, to deal with large grants from ARDC.

ARDC declined due to the amount of extra work involved.

We proposed becoming a Private Operating Foundation associated with ARDC, and accepting funding and being assigned projects by ARDC.

ARDC staff was interested in this plan. Becoming a PoF associated with ARDC was discussed in several meetings with ARDC staff and was summarized in email exchanges. ORI hired a law firm (Semachik) to review the plan and provide advice. This advice and documentation was provided back to ARDC as part of the process. This was treated seriously and with a lot of deliberation. The plan to convert to a foundation would have dovetailed perfectly with our trajectory (as ARDC was by far the largest donor), provided ARDC with a dedicated R&D unit, and made life a lot easier for everyone involved in administration. The agreement in principal was reached in May 2021.

ARDC reversed this plan in October 2021. The sticking point seemed to be when ORI requested a memorandum of understanding from ARDC to capture the intent of the plan in a formal way.

Lesson learned: get the MOU, even when you trust the organization and the people involved.

It was expected, and it could still happen, that the IRS will convert ORI from a public charity to a private foundation, based solely on ORI's sources of funding being heavily dominated by large grants from several foundations. This will happen after our fifth year of operation, as the public support test is calculated over a 5-year sliding window, unless we take action and raise some additional funds to "dilute" the larger grants, now. We are required to have at least 33.3% of our fundraising to come from small donations. We did get to 30%, but the M17 project grant put us further down in this "ratio test".

It's important to emphasize that we'd do things the exact same way if we had to do it over again. Adding the M17 Project (and offering to sponsor AMBE legal work) is definitely worth dealing with the IRS rules about public charities taking "big" donations from foundations. The M17 Project, along with *all* of the other projects we sponsor, are worth *far more pain* than anything the IRS can throw at us. Someone has to throw themselves under the bus to get things to happen. It may as well be people that can afford the bodily harm, with margin to spare.

The IRS *assumes* that large donors, like ARDC, will try and control, coerce, and influence the charity, unless that funding is diluted by others. These rules are designed to "brute force" independence from donors. The rules aren't bad in any way. I think anyone can understand the intention behind them. Having experience in multiple grant executions over many years, from FCC to FDA to SBIRs to amateur radio to arts to churches to entertainment, these rules exist for a reason. They are inconvenient for ORI in the short term. We're up to the challenge.

To be blunt and concise, ORI has been too successful in large-scale grant-writing. Our very flat structure does not have employees or staff dedicated to earning small donations. However, small donations are required by IRS rules to remain a 501(c)(3). We need to show we have broad appeal. Do we? Yes, we definitely do.

Do we have difficulty collecting small donations? Yes. Amateur radio does not have a history or tradition of widespread small donations. Please refer to any joke or meme about the "frugality" of "cheap" hams. The jokes endure and are funny because they have a core of truth to them. Worse than this, it is definitely the case that small and independent donations in amateur radio have dramatically declined due to the enormous influence of ARDC's outsized fund.

There isn't an authoritative article on where ARDC's money comes from. ARDC's website does not explain in any obvious way anything about the source of the money. ARDC is a TCP/IP networking organization for amateur radio. It managed IP addresses gifted to the amateur radio community in a very quiet and relatively closed manner for decades. ARDC sold about a quarter of the IP v4 addresses to Amazon.com. The fund size is not disclosed, but it has been estimated to have been between 80 and 180 million dollars at various times over the past three years.

We now regularly hear "Just get money from ARDC." It is hard to have something like a bake sale for a worthy cause taken seriously when a very wealthy Foundation shows up and starts handing out gobs of cash large enough to buy a California home without blinking an eye.

Government money, such as SBIR and STTR, count as public support.

Getting SBIR and STTR grants would engage ORI in the work we want to do while helping solve our "a bit too low" public support funding ratio. This might be the best path forward, but it requires people to staff, apply, and execute the grants. They are competitive. We have been involved in the process with three so far, and come close on getting one.

https://www.sbir.gov/tutorials/program-basics/tutorial-1
