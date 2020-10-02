Weekly Report! GNURadio's Goals + SiLabs Chipset + FPGA Team Kickoff

GNURadio's Goals

I got some extremely valuable feedback concerning the Day 1 Report about the 2016 GNU Radio Conference that is important for me to share. 

I wrote "So, the question "why isn't GNU Radio used more in industry" to me makes not a lot of sense at the moment. It's being used to its strengths, today, here and now. Maybe to increasing saturation, maybe not. If it was used in production, then it would require dramatic changes that the GNU radio people seem wholly uninterested in making." 

Attending conferences and meetings in person allows for enormous strides forward in understanding. After I posted this, one of our list members, who also is a core GNU Radio developer, said that they found this assessment to be unfair and bit harsh.

I heard the message "GNU Radio is not a prototyping tool" and "we want to be used more in industry" throughout the first day of the conference, which is also known as New User Day. The message wasn't entirely clear to me. Taking GNU Radio from a strength (prototyping tool) to a relative weakness (mass manufactured radio brains?) seemed a confusing move. Therefore I wrote what I wrote. 

What became clear through conversation is that the GNU Radio community wants the message to be "GNU Radio is not JUST a prototyping tool". This one word makes a big difference. 

The overriding concern here from the point of view of the GNU Radio core team is that there's a tendency to fence GNU Radio in and treat it as if it's limited to prototyping. This perception of being fenced in and limited to a particular type of role is what the GNU Radio community is trying very hard to overcome. Like any marketing effort, it takes a lot of work, and you will have people (like me) that misunderstand the message.

Why worry about this? Why clarify? Because we are doing exactly what GNU Radio wants. We are not only using GNU Radio as a prototyping tool, but GNU Radio is what we are going to use as the reference design for a wide variety of solutions for Phase 4 Ground. GNU Radio is flying in the 4B payload. We simply cannot complete this project without GNU Radio. It's absolutely essential.

Better understanding and using GNU Radio is the first step to contributing back to the GNU Radio project in efforts to improve it. Yes, there are plenty of improvements that can be made. From sitting through days of updates and presentations, it's obvious to me that the core GNU Radio teams takes it seriously and has made continual and substantial improvements. Since March, they have upped their game and gotten a lot more organized. They are looking for more volunteers. They are taking feedback seriously.

The take home here is that GNU Radio wants you to know that it's not just for prototyping anymore, and they are upping their game to make it possible to use GNU Radio in production radios.

SiLabs Chipset

The evaluation of the SiLabs DVB chip enabled Ron Economos to fully test the blocks he wrote for GNU Radio that do VL-SNR DVB-S2X. Being able to test the blocks is a big step forward. The other thing we learned is that the SiLabs chip does not do exactly what we need.

We can put pads in as a stuff option for this or any other chip. There are other choices out there, but most of the chips that more fully implement VL-SNR DVB-S2X are not sampling yet. If they are sampling, then we must put effort into negotiating for the loan of an evaluation module, if one exists. 

I believe that we should proceed on FPGA work and continue to monitor and evaluate the DVB chipset market. VL-SNR and DVB-S2X continues to gain traction at trade shows. Press releases abound. What we need right now is someone to step up and become DVB chipset component engineering lead. This means taking ownership of the draft tracking document and keeping up with suppliers. I need someone to take this over as soon as possible. It's a very low number of hours a week or month. We simply need to know when to start contacting a supplier. If they start sampling a DVB solution or have a successful demonstration, then we must move to evaluate. If an ASIC is a superior fit then we can design a lower cost radio around it. 

The take home here is we need a component engineer to focus on the DVB ASIC landscape and alert us to potential solutions. 

In the meantime, FPGA full speed ahead, especially since we now have two full toolchain licenses from Xilinx. We can target any size chip from Xilinx. Removing impediments to development is a good thing! Let's take full advantage of the opportunities we have. 

FPGA Development

There are two big scary technologies that we're tangling with. GNU Radio and FPGA development.

Let's talk about FPGA design. We are going to kick off our own tutorial learning sessions as of today. If you are experienced at FPGA design, then you can help advise and support. If you joined Phase 4 to learn how to do this sort of work, or get back into to this sort of work, then this will ramp you up. All of the activities will build upon one another. We will start with toys but end up with things that actually make radios. You will have fun. It's not worth doing if it's not fun. You will feel frustrated too, because it's kind of hard. Things worth doing are rarely easy, and we will all help each other out.

First off: You are going to need Vivado from Xilinx. There's lots of choices of toolchains. We may have to use another toolchain down the line. That's OK. Do not panic if that happens. In fact, just don't panic at all. Nothing has exploded (yet). 

For now, though, you are going to be using Vivado and Xilinx. Go install it. Linux or Windows are your choices. Sorry MacOS people (like me) no Vivado for you. You'll have to go get a Windows or Linux machine. If you already have Vivado, then update it. 

That's it! That's the first assignment. Go do it. Take a photo of your installation and send it to me. 

The people that have indicated interest or proficiency or both in FPGA design are the following.
Mike Murphree 
Dave Smith
Michael Pfeuffer
Wally Ritchie
Eric Nichols
Bob McGwier, his students, and myself
Jonathan Brandenberg
Steve Hicks? consulting services? 

If your name didn't appear, and you want to contribute as a named member to Phase 4 Ground FPGA development, then speak up.

If your name is here, and you are having an anxiety attack because it's there in black and white, then talk to me and I'll… talk you into it! It's going to be fun and we need you.

-mdt