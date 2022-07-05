Project Reports

# FPGA for P4DX

Anshul is travelling this week and sends in a report. 

_Status Update:
I can interact with DMAC from a c program (that Michelle shared) running on PS side.
IIO program is running for me on the target.
Went through the code  Evariste shared and now porting it to zc706._

We have libiio running on the target in Remote Labs West as well. The recipe for this involves adding a yocto layer called meta-adi to the petalinux build. Otherwise, as we found out, iid appears to be there, but really isn't. 

The procedure will be included in the Petalinux guide in the Remote Labs documentation. 

What does this allow us to do? DMA on the target, which now works for petalinux the same way it was working for the Kuiper linux build. 

We changed the bus width between DMA and DAC FIFO from 128 bits to 32 bits so that the encoder can drop in. We originally thought that the entire transmit chain had to be redone in terms of bus width. This is not the case. It took two days of learning, but we now have a very lightly edited reference design that works, and not a heavily altered one that never did. Thank you to Ken Easton for guidance, Travis at ADI for advice and the pointer to meta-adi, and everyone working to make the transmitter happen. 

With the encoder in the path, we see all of the expected effects. Symbols read from memory make no sense to the encoder, which expects baseband frames. The next step is to feed the encoder baseband frames from memory. 

Here is the way it's currently hooked up. I'm not sure that this is correct yet, because there is a signal from DMA to DACFIFO that we are concerned about. Please review this. We'll be digging in to this particular aspect next, along with proper transport stream data input and continuing to refine the uplink protocol. 

https://drive.google.com/file/d/1PBuykauwDZj3dn-h34uF4agmO8Eq-BpA/view?usp=sharing

Here are the errors discussed on the fpga channel in Slack. These errors prevented building the project. 

## Missing files:

abraxas3d@chococat:~/adi-encoder/adi_adrv9371_zc706/hdl/library/interfaces$ ls
interfaces_ip.tcl  Makefile

abraxas3d@chococat:~/adi-encoder-test/hdl/library/interfaces$ ls -lrt
total 24
-rw-rw-r-- 1 abraxas3d abraxas3d 1720 Jun 19 04:14 Makefile
-rw-rw-r-- 1 abraxas3d abraxas3d 4089 Jun 19 04:14 interfaces_ip.tcl
-rw-rw-r-- 1 abraxas3d abraxas3d  796 Jun 19 04:14 fifo_wr.xml
-rw-rw-r-- 1 abraxas3d abraxas3d 3311 Jun 19 04:14 fifo_wr_rtl.xml
-rw-rw-r-- 1 abraxas3d abraxas3d  794 Jun 19 04:14 fifo_rd.xml
-rw-rw-r-- 1 abraxas3d abraxas3d 2811 Jun 19 04:14 fifo_rd_rtl.xml

Copied all of these over, and error resolved.

## Missing file:

encoder/adi_adrv9371_zc706/hdl/projects/common/zc706/zc706_plddr3_mig.prj": no such file or directory

abraxas3d@chococat:~/adi-encoder-test/hdl/projects/common/zc706$ ls
zc706_plddr3_adcfifo_bd.tcl  zc706_plddr3_dacfifo_bd.tcl  zc706_system_bd.tcl
zc706_plddr3_constr.xdc      zc706_plddr3_mig.prj         zc706_system_constr.xdc
abraxas3d@chococat:~/adi-encoder-test/hdl/projects/common/zc706$ cd /home/abraxas3d/adi-encoder/adi_adrv9371_zc706/hdl/projects/common/zc706/

abraxas3d@chococat:~/adi-encoder/adi_adrv9371_zc706/hdl/projects/common/zc706$ ls
zc706_plddr3_adcfifo_bd.tcl  zc706_plddr3_constr.xdc  zc706_plddr3_dacfifo_bd.tcl  zc706_system_bd.tcl  zc706_system_constr.xdc
abraxas3d@chococat:~/adi-encoder/adi_adrv9371_zc706/hdl/projects/common/zc706$ 

File was copied over. Error resolved.

## Hardcoded path:

abraxas3d@chococat:~/adi-encoder/adi_adrv9371_zc706/hdl/projects/adrv9371x/common$ cat adrv9371x_bd.tcl | grep anshul
source /home/anshul/phase4/adi_adrv9371_zc706/dvb_fpga/build/vivado/add_dvbs2_files.tcl
add_files /home/anshul/phase4/adi_adrv9371_zc706/dvb_fpga/build/vivado/dvbs2_encoder_wrapper.vhd
abraxas3d@chococat:~/adi-encoder/adi_adrv9371_zc706/hdl/projects/adrv9371x/common$ 

Path was adjusted, but only with a relative path. This is fragile and should probably be done better. But, the error resolved. 

## Where can I help? 

Details are summarized in the issue https://github.com/phase4ground/adi_adrv9371_zc706/issues/1

Contact Anshul Makkar if you can help with a pull request. 

