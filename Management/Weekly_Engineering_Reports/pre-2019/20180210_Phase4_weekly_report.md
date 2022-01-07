Voltera available for Phase 4 Ground prototyping, 5GHz updates, Snickerdoodle Vivado, SDK, SDSoC progress and the release of our first music single from @Firmwarez.

https://youtu.be/moKFVagY_Ro

Voltera V-one available for circuit printing, solder paste and reflow. Send your Gerbers in!

5GHz updates described photographically.

Xilinx SDSoC and the Snickerdoodle FPGA board.

The FPGA or field programmable gate array is at the heart of many modern software defined radios. Having powerful reconfigurable digital logic realizes a lot of the promise of SDRs. Balancing the workload between the general purpose processor and the FPGA is a big challenge. We've talked about RFNoC, or Radio Frequency Network on a Chip from Ettus Research for the 300 series USRPs before. RFNoC lets you place blocks that run on the FPGA in GNU Radio as if they were being run by the host computer. This lets you use the FPGA to full advantage within GNU Radio Companion. You have to develop and properly package the FPGA code, but once you do that, your FPGA will be a lot less bored. 

Well, SDSoC is somewhat similar. It's a tool from Xilinx and you get a free license with the Snickerdoodle Black. So what is it? It stands for Software Defined System on a Chip. 

Instead of part of your team working on the FPGA code, and another part of your team working on the general purpose code, and constantly meeting up and trying to figure out if they have the right balance of work between general purpose processor and FPGA, with SDSoC, you write the entire thing in C or C++, and then run a profiler to find out which parts need to be optimized to run on the FPGA and which parts can run on, for example, an embedded ARM. You can then right click and assign functions to hardware. 

Sounds like magic? We're going to try it out and see if it works for us for our receiver. 

Last week, we unboxed and got the SD card set up and the Snickerdoodle running Linux. So far this week, we've gotten Vivado and the Xilinx SDK to see the Snickerdoodle. The SDSoC development environment terminal program connects to the Snickerdoodle, but the board isn't in the platform list, and we're not entirely sure what to do about that. 

We've asked for help on the forums and noticed other people asking about this. It may be that we don't need platform files, but I'd feel a lot better if we did. There are a lot of pins involved as you can see from the video, and properly defining them helps make functional code. 

Another thing we've done is ordered a JTAG cable designed especially for Xilinx chips and tools. This will help better communicate with the board and I'm hoping it will allow us to move code directly to it, instead of having to take out the SD card and physically move it to the development machine to transfer files. It's a HS3 from Digilent and connects directly to the breakout board. 

If you can help ease the process of learning this environment, please let us know! My contact information is at the end. Join us on either the #fpga or #dvb-receiver channels on our Slack for engineering discussions.  