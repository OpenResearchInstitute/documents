## ZCU106 Description

The ZCU106 Evaluation Kit enables designers to jumpstart designs for video conferencing, surveillance, Advanced Driver Assisted Systems (ADAS) and streaming and encoding applications. This kit features a Zynq® UltraScale+™ MPSoC EV device and supports all major peripherals and interfaces, enabling development for a wide range of applications. The included ZU7EV device is equipped with a quad-core Arm® Cortex®-A53 applications processor, dual-core Cortex-R5 real-time processor, Mali™-400 MP2 graphics processing unit, 4KP60 capable H.264/H.265 video codec, and 16nm FinFET+ programmable logic.

### ZCU106 References

xczu4cg-sfvc784-1LV-i is the target of https://github.com/phase4ground/dvb_fpga

ZCU106 Evaluation Board User Guide is https://www.xilinx.com/support/documentation/boards_and_kits/zcu106/ug1244-zcu106-eval-bd.pdf

Constraints file available from well-hidden link on Xilinx website. Found this in forum post: https://forums.xilinx.com/t5/Xilinx-Evaluation-Boards/ZCU106-Dev-Board-Master-Constraints-File-xdc/td-p/1085933

IP Integrator Guide is here: https://www.xilinx.com/support/documentation/sw_manuals/xilinx2013_2/ug994-vivado-ip-subsystems.pdf

We might want to package this up with IP Integrator? 

Next, there's an example design (above constraints are correct for this example) at: https://www.xilinx.com/support/documentation/ip_documentation/v_hdmi_tx_ss/v3_1/pg235-v-hdmi-tx-ss.pdf#page=67

For installing Petalinux on the Chococat VM on CHONC, the following was referenced: https://www.xilinx.com/support/documentation/sw_manuals/xilinx2020_2/ug1144-petalinux-tools-reference-guide.pdf

Embedded Design Tutorial for UltraScale+ MPSoC at this link: https://xilinx.github.io/Embedded-Design-Tutorials/master/docs/Introduction/ZynqMPSoC-EDT/README.html

The ZCU106 shows up in Unraid as "Future Technology Devices International FT232H Single HS USB-UART/FIFO IC (0403:6014)"

### Tutorial Videos for Vivado

How to connect Programmable Logic to Processing System

Part 1 https://www.youtube.com/watch?v=_odNhKOZjEo

Part 2 https://www.youtube.com/watch?v=AOy5l36DroY
