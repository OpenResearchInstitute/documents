## Project Report

### P4DX GEO Transponder 

#### FPGA

Thank you to Suoto, Thomas Parry, Leonard Diguez, Anshul Makkar, Evariste, and Paul KB5MU for all of the substantial recent progress on getting our IP up and running over the air. The strategy of using both the PLUTO and the ADRV9371/zc706 in parallel to debug tools issues and some subtle logic errors. 

FPGA implementation of M17 (our uplink protocol) on PYNQ is in progress from WX9O. Find our fork of WX9O's work here: https://github.com/phase4ground/m17-pynq/tree/master

Another FPGA implementation, using MATLAB HDL Coder, is in the very early stages. Find fred harris' MATLAB script, an in-progress conversion to a live script, notes, and results here: https://github.com/phase4ground/documents/tree/master/Engineering/Uplink-Systems-Engineering

If there's another FPGA implementation, we're interested in supporting it!

Integrating uplink and downlink will happen as soon as possible. 

Next demonstration is DEFCON in Las Vegas, NV in August 2022. 

#### Multimedia Beacon

Baseband is (still) working. Enclosure Number 1 obtained, thanks to SDMG members Dan and Drew. Power amplifier obtained. There's more work required before it's ready to install on a local mountaintop, but the enclosure sets a large number of the mechanical and fitting requirements. The beacon is intended to be upgradeable to a full transponder. 

### Ham Expo Autumn 2022

Met with Eric Guth on Thursday to discuss Ham Expo in Autumn 2022 and how ORI can participate and support the event.

### AI/ML Working Group FCC Technological Advisory Committee

Meeting was Wednesday. We got through half of the first of two agenda items. 

1. AI/ML for Spectrum Sharing

Addressing the fundamental aspects of propagation, interference, signal processing, and protocols.

Spectrum sharing and propagation models are the first item. When we look at issues such as propagation, what are the important parameters and circumstances? What kind of data must be made available in order to be successful at this.

2. AI/ML for Telecommunications Networks

Evaluate the use of AI/ML methods and techniques applied to assuring the safety, security, and performance of network equipment, network control, and network operations in a network environment that increasingly relies on automation.

The current regime is formal. It assigns rights per location. Where else does the signal end up? Is it safe to assign it? Without even considering dynamic spectrum allocation in real time, we still have to have better propogation models than we do now. Can AI/ML do this?

