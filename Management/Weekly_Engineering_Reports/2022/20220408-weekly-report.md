## Weekly Project Report

### Plan for the Week

- [x] P4DX over the air?

Good news - a proof of concept for the DVB-S2 encoder is working. A major component of the FPGA design for the downlink has been validated. 

Here is the video recording of the weekly FPGA meeting:

https://youtu.be/UqiPdq3gRmE

- [ ] MATLAB HDL Coder of M17 protocol

We have MATLAB code that has been converted to VHDL. A bitstream is successfully created by the MATLAB toolbox. 

Programming the FPGA for FPGA-in-the-loop is the current roadblock. The exact same bitstream can be manually programmed into the zcu106 development board using Vivdao's hardware manager, but HDL Coder returns an error.

The M17 script for MATLAB has been reviewed, and the spectrum is not as expected. We believe it needs a bit more work before it can be tried with HDL Coder. 
