posted 12 December 2018

## Code of Conduct reference links and free eBook

There is a book about Codes of Conduct available now for free. It's called “How to Respond to Code of Conduct Reports" and is written by Valerie Aurora and Mary Gardiner and edited by Annalee Flower Horne. 

This guide includes:
* Basic code of conduct theory
* How to prepare to enforce a code of conduct
* Step-by-step instructions on how to respond to a report
* In-depth discussion of relevant topics
* Dozens of real-world examples of responding to reports

Valerie Aurora and Mary Gardiner were the lead authors of the Ada Initiative anti­-harassment policy, which is the basis of thousands of codes of conduct in use today. Valerie has 7+ years of professional experience writing and implementing codes of conduct for software-related companies, venture capital firms, and non-profits.

The book is available under the Creative Commons BY-SA license, allowing free reuse and modification of the materials as long as you credit the authors. It can be downloaded from https://files.frameshiftconsulting.com/books/

Phase 4 Ground uses the code of conduct from Open Research Institute. Our participant policies and code of conduct can be found at https://openresearch.institute/developer-and-participant-policies/


## Donated Dish Update and Yes There are More Dishes

Doug Phelps will need some help with distributing the "smaller" dishes. He has everyone's names still, is putting up with my nagging about it, and has promised to give an update. 

But in addition to that, he has rescued a set of 6 foot aluminum dishes with feeds, mounting hardware, and radomes. These are safe at his friend's farm, so he's motivated to get them moving! 

There are four available and here are the details: 

## HEO and GEO Launches

We don't like keeping secrets. However, we do have some secrets. 

The Phase 4B payload, and the other related projects that we have actively supported (like CQC) all require launches. 

We have a launch with the Wide Field of View payload with the Air Force. The good news is how well we did in getting engineering approval for this launch. We have a ride. The bad news is the cost of the launch. It is $6 million and they can guarantee us about one year and not even guarantee us it will be over the United States. We have decided we cannot ask the community for $6M to support this launch. It's just not a good deal for US hams. 

Fortunately there's been a lot of work going on behind the scenes for additional launches. This work has been going on for a while. 

I can't share the details. I can say that our prospects have never been better. Anyone following along and helping the project, anyone that has been with us through a lot of challenging experiences, deserves to know that we are absolutely serious, focused, and unrelenting in obtaining multiple launches for this technology.

Traditionally, an amateur launch would be announced and then a payload developed. With modern digital technologies taking significantly longer development time than legacy technologies, and with opportunistic short-notice launches becoming more the norm, this design pattern really can't work for us. That's one of the reasons we need to work hard, now, as if the launch was imminent. Howie DeFelice and I wrote an article for QEX about this. 

Working hard without a launch date is a lot to ask of people that are not getting paid and in some cases not being given the support or recognition they should be getting.

In the new year, we'll be doing just that and asking for more in terms of technology demonstration and development from the team. The next big technology demonstration will be HamCation, and the most ambitious goal for that is to have LDPC working on an FPGA with interactive controls. This is the heart of the coding part of the receiver. 

A GNU Radio LDPC demonstration can be seen in a recent video report, and the GPU version can be run by anyone with a late model Nvidia GPU. 

Until HamCation, our goal is to get the air interface into the best possible shape. We need to capture the excellent progress we've made and make it as easy as possible for upcoming payloads to say "Yes!" to Phase 4 Ground. 

There's plenty going on. Progress is good. Launch prospects are part of that good news. A lot of the work is invisible during the negotiating process, but we are working as hard as we can to make it more than worth the wait.  

More soon! Happy Holidays :+)

---
posted 10 December 2018

# LDPC Update

Low Density Parity Check forward error correction is one of the most challenging areas of our radio project. It's required for DVB-S2/X, therefore our receiver must be able to decode it and the payload must be able to encode it. A wide variety of code rates (the ratio of bits input to the encoder over the number of bits output from the encoder) are specified in the standard. Our goal is to support them all.

The version of LDPC for GNU Radio is progressing with a variety of refinements and speedups tested over the past few weeks. The core code is located at https://github.com/xdsopl/LDPC and the GNU Radio module is located at https://github.com/drmpeg/gr-dvbs2rx

Speed improvements through more efficient memory layout has been the focus of the most recent work, along with moving the decoder constructor. SIMD parallel processing is progressing, and the tradeoffs with respect to expensive initialization routines are being considered. Some results are 

Give the module a try! There are some test flow graphs in the GNU Radio module's apps directory. 

---
posted 10 December 2018

Thanks to the enormous generosity of MyriadRF, Phase 4 Ground has some hardware help!

Five LimeSDR Mini Kits have been given to Phase 4 Ground for open source satellite communications development work. 

We want to get these into as many hardworking hands as possible! Write me today with your need and let's get you up and running. 

I recently set up a LimeSDR Mini with GNU Radio with one of our list members and it went very well. This is a wonderful SDR. The LimeSuite GUI allows prototyping with what feels like every register setting on the controller. Performance is very good. 

For a talk about LimeSDR (and the extended frequency range chip) from Microwave Update 2018 from Mike Seguin N1JEZ, please see https://youtu.be/F76BzezuCmw

LDPC-BCH decode on the FPGA is a current area of great interest for us. LDPC-BCH is the forward error correction for DVB-S2/X. But, we are also interested in doing more with Polar codes. There is at least one open source satellite payload project that has specified Polar forward error correcting codes. There is very little open source work here, it's cutting edge, and Polar codes are specified for use in 5G communications. Polar codes are the first family of error-correcting codes that achieve the Shannon capacity for a wide range of communication channels with efficient encoding and decoding. 

The FPGA on the LimeSDR mini is the Intel MAX 10 (10M16SAU169C8G 169-UBGA). How far can we take it? 

What else needs doing? How about a SatNOGS station with the LimeSDR mini? A proof of concept of Phase 4 Ground authentication and authorization scheme? Handling the Generic Stream Encapsulation streams properly from the downlink for amateur communications? Plenty to do! Dive in and we will help you.

Contact Michelle W5NYV w5nyv@arrl.net to sign on and get kitted up. 

---
posted 12 December 2018

Five Four LimeSDR Mini Kits from Myriad-RF have been made available to Phase 4 Ground for open source satellite communications development work. This donation was made possible by a generous and expansive commitment from the European Space Agency. The ESA uses and emphasizes open source technology in a variety of missions and roles. This attention, assistance, and support is a growing part of the open source space landscape. We are extremely excited to be included!

Contact Michelle W5NYV w5nyv@arrl.net to sign on and get kitted up. 




