Welcome to the Phase 4 Ground Weekly Report!

409!

Video link
https://youtu.be/6tW04jWZGjM

## 2 4 6 8 Everybody Correlate!

Correlator team had a conference call on Thursday 5 April 2018. Jordan, Brennan, Ed, and I talked on the conference bridge Ed set up for us for about 45 minutes. We covered a lot of ground and got some idea of next steps. We have a repository that has GNU Radio draft blocks that do the Pi/2 BPSK demodulation and decoding, and we need to get it working as a correlator.

We also have a correlation estimation block in GNU Radio that has an issue. 

Brennan Ashton reviewed our block and didn't see any major issues yet, and then went out to see what he could see about the correlation estimation block.

Please review Brennan's pull request here:
https://github.com/gnuradio/gnuradio/pull/1725

This is an attempt to solve this issue here:
https://github.com/gnuradio/gnuradio/issues/1207

Which if successful will help us and a lot of other people. 

This effort is in progress and will be updated as the code is reviewed and feedback from GNU Radio given.

## 10GHz Filter

We have a 10GHz filter design proposed from Jeffrey Pawlan. 

It covers the 10GHz amateur band, has 0.1dB variation over the band, 0.1dB insertion loss, and 20-30dB return loss. It's a high-performance filter and we are talking about how to get it published, how many prototypes to build, and what the potential market might be. Here's the first four documents from Jeffrey. These are in the repository at the link in the notes. If you have feedback we want to hear it. 

https://github.com/phase4ground/DVB-receiver/tree/master/Pawlan-10GHz-Filter

## Block Party at GNU Radio Conference 2018

We are sponsoring a Block Party at GNU Radio Conference 2018. This is a multi-day hackfest, workshop, and summit all about making an open source DVB-S2 and DVB-S2X receiver in GNU Radio. Come and help. We have five solid technical docents for the event and could use more. The goal is to bring blocks and write blocks on site, test interoperability, and leave the conference with a working DVB-S2 receiver. This is the central mission for successful continued research and development and we need all hands on deck. 

If you've have never coded a block in GNU Radio, then don't worry. It wasn't until the past year that I had ever coded up a block for GNU Radio. I just had never needed to. There is a series of guided tutorials from GNU Radio's website. The link is in the notes. 

https://wiki.gnuradio.org/index.php/Guided_Tutorials

Go there, or search them up with "gnu radio guided tutorials", walk through them, and you will have the tools and the workflow experience to be able to contribute. 

Having said that, if you are only comfortable coding in python or C++ then that's ok too. If you have an idea for getting some part of the DVB-S2 digital signal processing done, and either don't have time to work through block coding or pybombs distribution, then you can certainly still help by sharing your signal processing code. Don't let GNU Radio block configuration stop you. You're needed and appreciated.

## KA9Q SDR - stereo field

Phil Karn has shared a work in progress with us. He calls it the KA9Q SDR. However, the module in this SDR code that I'd like to highlight is a stereo field audio adapter. 

This works by taking in multicast audio streams. Each audio stream comes from an individual audio source, or participant. These participants in a round table audio conference are placed at different points in the stereo spectrum. 

Phil Writes:

I'm writing a lightweight, modular SDR package that uses IP multicast
for inter-module communication. Multicasting is very flexible and
convenient for this sort of real-time application, and I really think
it should become standard practice.

One module is an audio decoder-player. I'm often running several SDRs
at once so I wrote it to handle multiple multicast streams. Since
several mixed audio streams can be confusing, I've been experimenting
with ways to help the user distinguish them.

I started with a simple text display that lists the streams and their
types and sources, highlighting those that are currently active. You
can individually adjust levels or ignore those you don't want.

Since most sources are mono, I added the ability to give each one its
place in the stereo aural image. I'm trying to recreate the famous
"cocktail party effect" that, in person, helps you pick out one voice
from several talking at once.

Audio engineers typically place a source in a stereo image with a
mixer "pan pot" that adjusts its gain in each channel. This works -
sort of. I wanted to find something better.

So I read up auditory perception. I learned that we distinguish the
direction of a sound only partly by the level difference between our
ears, as that doesn't actually change much as your head turns.  The
*real* cue is the difference in arrival time. The speed of sound is
about 340 m/s, so if our ears are 30 cm apart (measuring around the
head) that's a little less than a millisecond.

This didn't seem like much, but it was very easy to add these small
delays to the "pan pots" in my player. And it works! The effect is
almost eerie; you have to listen to each channel in turn to convince
yourself that the levels are almost the same.

Conference calls (or "round tables" as we hams call them) are very
important in communications. I've long thought we can make them much
better, especially in how we handle several simultaneous speakers.  If
we use this scheme to place each participant in a round table we
should get a lot closer to that "in person" experience that's so
difficult to produce in electronic communications.

All this requires that each participant receives every other
participant as a separate stream -- there's no central "conference
bridge" that mixes everybody together. This is a perfect application
for IP multicasting. Not only can you put each participant in its
place, the status display shows you at a glance who's talking. You can
squelch an individual who keeps disrupting the meeting, and you can
even have a private aside by sending unicast traffic rather than
multicasting to the entire group.

A lot of this was done as research in the early days of what became
'voice over IP' (VoIP) but it seems to have fallen by the wayside. It
really deserves to be more widely recognized and used.

Phil Karn, KA9Q  
9 April 2018



## Careful COTS SDR 

We are making great progress on the Careful COTS re-layout of a USRP E310 with future plans to tackle the E320. We're collaborating with AMSAT Golf on this and have gained enthusiastic support from Ettus Research engineering. The next steps are to negotiate what's needed on the business side. Scheduling talks is in progress. 

If you're not familiar with the term, Careful COTS - COTS means commercial off the shelf - is taking something that wasn't designed specifically for space and making it work for space environments. This is done by selection of the right components, designing in redundancy at the system level, and testing the entire system for radiation tolerance. 

We have a high degree of confidence that the Ettus USRP will work and some volunteers willing to do the work. If you are interested in this part of the project, let me know. 

## Badge Update

The Transionospheric badge prototypes are being built at a contract manufacturer in San Diego right now. We are working hard to have them at Hamvention for sale. All proceeds benefit Phase 4 Ground! They aren't just for show, they will be a radio peripheral for Phase 4 Ground radios, providing a lot of visual reinforcement on what your radio is doing and the health and status of your link. Whether you have a satellite or a terrestrial system, the same information will be stylishly displayed. We are working hard to make it possible to command other radios as well. More on that as it develops! 

If you want to be part of the effort, then join our Slack and mailing list at http://lists.openresearch.institute/mailman/listinfo/ground-station

Write me for an invitation to Slack. All are welcome. This project is intended to spread enjoyment, appreciation, and success in broadband digital communications at microwave for amateur radio use. A lot of what we do is complex and challenging, but we are here to help and you can contribute at any level. 

Thank you for all the support and interest. If you have suggestions or questions or something you think we need to know about, let us know. If all goes well, we'll see you next week! 

