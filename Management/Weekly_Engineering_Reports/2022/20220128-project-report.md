## Weekly Report

Reminder: please review the pull request at https://github.com/phase4ground/documents/pulls

### DVBS2_ENCODER and FPGA Work

IP block of most of curent focus is located at: 

https://github.com/phase4ground/dvb_fpga

This project aims to implement RTL components for DVB-S2, initially focusing on the transmission side. Efforts this week resulted in progress integrating the encoder into the ADRV9371+zc706 in Remote Lab West. Multiple issues solved (packaging, IQ bit width) with status by Friday of scripted integration and synthesis in the ADI reference design. Refining integration into the ADI reference design still looks like the best way to go. 

pyadi-iio does not appear to allow feeding input data at the correct level for encoder testing. The pyadi-iio transmit functions deliver symbols directly to the transmitter using the iio interface. We want to write an application using the SDK, that sends data to the programmable logic side through direct memory access. 

MATLAB needs an answer about the startup program participation. Package has been sent to the board. This appears to be the only path forward that enables the HDL Coder, GPU Coder, and MATLAB Coder toolboxes. 

Device tree overlay bitstream programming (at the Linux level) is still not working. In the meantime, bitstreams are loaded onto the SD card. 

### M17 Project

Substantial and productive discussion on the priority and process of improving the codec. 

Re-alignment of the goal of integrating a radio. 

Progress on scheduling the protocol stadardization talk from Erin.

### Quarterly Technical Advisory Committee Meeting

Planning complete, related fundraiser organized (To be announced shortly), 

### AmbaSat Respin

All boards distributed to firmware team. Trello card moved to "done". Firmware team exploring some options enabled by the new chip. Slack access and meeting scheduling in progress. It is anticipated that there will be a weekly meeting. 

### HamCation Planning

All planning complete. 

ORI Board meeting will be held at HamCation.

### DEFCON Demonstrations

Site selected and village communications established. Multiple talks in multiple villages highly likely. ORI Board meeting will be held at DEFCON. 

### Grant Applications

SBIR search committee met on Tuesday and resolved to participate in Debris Mitigation related grants with NASA. 

Positive feedback received from a machine learning submission, but no award in that round. 
