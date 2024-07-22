# How to Add Our Blocks to the Analog Devices HDL Reference Design

>ORI 6 November 2023 Abraxas3d ad_connect documentation and adrv9371 tcl file names

>ORI 8 November 2023 Abraxas3d error messages from API Mismatch problem, SD card creation

>ORI 29 March 2024 keaston successful integration of IP with HDL Reference Design

>ORI 12 April 2024 Abraxas3d documented [how to integrate IP into PLUTO HDL Reference Design](https://github.com/OpenResearchInstitute/documents/blob/master/Remote_Labs/Adding-Our-Blocks-to-the-Analog-Devices-HDL-Reference-Design.md#integrating-custom-ip-into-the-pluto-sdr-hdl-reference-design)

>ORI 22 April 2024 Abraxas3d documented [Updating the PLUTO Firmware with New HDL](https://github.com/OpenResearchInstitute/documents/blob/master/Remote_Labs/Adding-Our-Blocks-to-the-Analog-Devices-HDL-Reference-Design.md#updating-the-pluto-firmware-with-new-hdl)

>ORI 22 July 2024 Abraxas3d documented [Integrating Custom IP into the PLUTO HDL Reference Design Using Out of Tree Module Method](https://github.com/OpenResearchInstitute/documents/blob/master/Remote_Labs/Adding-Our-Blocks-to-the-Analog-Devices-HDL-Reference-Design.md#integrating-custom-ip-into-the-pluto-sdr-hdl-reference-design-using-out-of-tree-module-method)

## Library Block Method
In order to take advantage of the ADI-specific environment and build macros, one way to integrate IP into the HDL Reference Design is to make new blocks look like other blocks in the adi build tree. This is accomplished by installing new blocks should at hdl/library/blockname, where they are automatically picked up by the top level build, and editing the Makefile and blockname_ip.tcl in that directory along the lines as that presented in the following guide:
https://wiki.analog.com/resources/fpga/docs/hdl/creating_new_ip_guide

## Files that Need to be Modified

There is at least one file that will need to be modified in order to add our custom logic to the Analog Devices HDL reference design. 

Using the repository example https://github.com/OpenResearchInstitute/adi_adrv9371_zc706 as an example, we integrate our blocks into the reference design by editing this type of file:

hdl/projects/adrv9371x/common/adrv9371x_bd.tcl

The entire file at the time our DVB-S2 block was integrated is included in Appendix A. It has all the commands that connect and configure all the logic blocks for the reference design. 

The adrv9371x in the directory path indicates the radio card that is being used. So, in order to add logic to the adrv9009 reference design, we need to find the corresponding file in the adrv9009 directory structure. For the adrv9009, you would therefore expect to find this "hook things up" file to be located at:

hdl/projects/adrv9009/common/adrv9009_bd.tcl

Let's look at the specific commands. There are a lot of 

`ad_connect from_this_port to_this_port`

commands in this file.

What is ad_connect?

ad_connect is defined in .../scripts/adi_board.tcl:

```proc ad_connect {name_a name_b} {
set type_a [ad_connect_int_class $name_a]
set type_b [ad_connect_int_class $name_b]
set obj_a [ad_connect_type $name_a]
set obj_b [ad_connect_type $name_b]
if {!([string first intf $type_a]+1) != !([string first intf $type_b]+1)} {
error "ERROR: ad_connect: Cannot connect non-interface to interface: $name_a ($type_a) <-/-> $name_b ($type_b)"
}
```

The first thing ad_connect does is compare interface types. That's how I learned AXI Smartconnect was the wrong choice (in one of two ways) for trying to upsize the bus to the DACFIFO many months ago.

There's then a large switch case statement to return the names and types in question.

After the switch case statement is:

```# Continue working on nets that connect to constant. obj_b is the net/pin
set width [ad_connect_int_width $obj_b]
set cell [ad_connect_int_get_const $name_a $width]
connect_bd_net [get_bd_pin $cell/dout] $obj_b
puts "connect_bd_net [get_bd_pin $cell/dout] $obj_b"
}
```

connect_bd_net is a Xilinx tcl command. ad_connect is an ADI command (defined as described above in .../scripts/adi_board.tcl)

The link to the connect_bd_net documentation is https://docs.xilinx.com/r/en-US/ug835-vivado-tcl-commands/connect_bd_net

I believe that connect_bd_net gets all the pins with get_bd_pin.

These mechanisms are being leveraged by ad_connect in this reference design tcl script to connect blocks together. 

## Using the tcl file

In order to add something to the reference design, we edit this tcl file and add in whatever ad_connect is needed. If something needs to be inserted, we comment out the default ad_connect from A to B, and insert an ad_connect A to NEW and then ad_connect NEW to B.

Here's how we connected the encoder in between the transmit DMA and the DAC FIFO.

```ad_connect axi_ad9371_tx_dma/m_axis_data dvbs2_encoder_wrapper_0/s_axis_tdata
ad_connect axi_ad9371_tx_dma/m_axis_last dvbs2_encoder_wrapper_0/s_axis_tlast
ad_connect axi_ad9371_tx_dma/m_axis_valid dvbs2_encoder_wrapper_0/s_axis_tvalid
ad_connect axi_ad9371_tx_dma/m_axis_ready dvbs2_encoder_wrapper_0/s_axis_tready

ad_connect axi_ad9371_dacfifo/dma_data dvbs2_encoder_wrapper_0/m_axis_tdata
ad_connect axi_ad9371_dacfifo/dma_xfer_last dvbs2_encoder_wrapper_0/m_axis_tlast
ad_connect axi_ad9371_dacfifo/dma_valid dvbs2_encoder_wrapper_0/m_axis_tvalid
ad_connect axi_ad9371_dacfifo/dma_ready dvbs2_encoder_wrapper_0/m_axis_tready
```

There's other things to add in this file. For example:

```ad_connect $sys_cpu_clk dvbs2_encoder_wrapper_0/clk
ad_ip_parameter dvbs2_encoder_wrapper_0 CONFIG.INPUT_DATA_WIDTH 32
ad_connect $sys_cpu_resetn dvbs2_encoder_wrapper_0/rst_n
```

Above are commands that connect a clock to our IP Instance, set an IP block parameter, and connect a reset signal. 

It is important to assign addresses to all the AXI modules in the design. This is how we are able to access CPU registers to communicate with our blocks.  

`ad_cpu_interconnect 0x44AC0000 dvbs2_encoder_wrapper_0`

Note that the axi interface should strictly match the interface of other blocks so as to stitch into the axi interconnect correctly.
You may likely need to add the following command to have the busses treated as such and not as individual inputs or outputs per bit.

set_param ips.enableInterfaceArrayInference false



## Timing Constraints

Particular timing constraint considerations for the block may need to be configured via hdl/projects/adrv9009/zc706/system_constr.xdc
for example, the need to treat the axi as asynchronous from the polyphase filter system clock and hence no timing arc between regimes is specified in that file as:

set_false_path -from [get_clocks clk_fpga_0] -to [get_clocks mmcm_clk_0_s_1]
set_false_path -from [get_clocks mmcm_clk_0_s_1] -to [get_clocks clk_fpga_0]

Here the clock identifiers may need to be tracked down within vivado, tracing clock regimes to their source and using a report_clocks command to determine the
logical clock name associated with that root.

## Commands Specific to the DVB Encoder

This IP instance (the DVB encoder in the example repository) is called up like this:

```# ===================================== DVB MODULATOR ===============================
source ../../../../dvb_fpga/build/vivado/add_dvbs2_files.tcl
add_files ../../../../dvb_fpga/build/vivado/dvbs2_encoder_wrapper.vhd
```

There's a tcl file in the source code of the block add_dvbs2_files.tcl. Then we add_files and point to the encoder wrapper.

Immediately following the add_files is:

```# Create instance: dvbs2_encoder_wrapper_0, and set properties
  set block_name dvbs2_encoder_wrapper
  set block_cell_name dvbs2_encoder_wrapper_0
  if { [catch {set dvbs2_encoder_wrapper_0 [create_bd_cell -type module -reference $block_name $block_cell_name] } errmsg] } {
     catch {common::send_gid_msg -ssname BD::TCL -id 2095 -severity "ERROR" "Unable to add referenced block <$block_name>. Please add the files for ${block_name}'s definition into the project."}
     return 1
   } elseif { $dvbs2_encoder_wrapper_0 eq "" } {
     catch {common::send_gid_msg -ssname BD::TCL -id 2096 -severity "ERROR" "Unable to referenced block <$block_name>. Please add the files for ${block_name}'s definition into the project."}
     return 1
   }
```


Where we set the block name and the block cell name. I'm not confident that I know the difference between these two things and would have to go back and re-read the add_dvbs2_files.tcl file.

At a very high level, hdl/projects/adrv9009/common/adrv9009_bd.tcl is the file to modify to add our blocks. I don't expect that the process will be exactly the same for the dvb-s2 encoder as it will be for the multirate filter or COBS decoder or other blocks that we need to add. We need to figure this out.

## Modifying the Reference Design vs. Porting to a New Board
  
I found this web page useful in terms of describing "what is what" in the reference design:

https://wiki.analog.com/resources/fpga/docs/hdl/porting_project_quick_start_guide

We aren't "porting" a reference design to a new fpga dev board, but we are modifying the radio card dev board file - in our case, the adrv9009_bd.tcl 

## Integrating Custom IP into the PLUTO SDR HDL Reference Design using Library Block Method
### Steps Required to add the Opulent Voice Transmitter and Receiver Blocks
#### Setting up the HDL Reference Design for Editing

First, set up the environment for working with the HDL Reference Design. In our case, this means sourcing the setup script for the Version of Vivado that we want to use for the build. (Depending on the size of the target FPGA, one may also need to check out a license for Vivado. For the PLUTO SDR, checking out a license is not necessary)

`source /tools/Xilinx/Vivado/2022.2/settings64.sh`

In a working directory, clone the hardware description language reference design from Analog Devices.

```
abraxas3d@chococat:~$ cd documentation-friday/
abraxas3d@chococat:~/documentation-friday$ git clone https://github.com/analogdevicesinc/hdl
Cloning into 'hdl'...
remote: Enumerating objects: 85282, done.
remote: Counting objects: 100% (3636/3636), done.
remote: Compressing objects: 100% (1502/1502), done.
remote: Total 85282 (delta 2277), reused 2952 (delta 1870), pack-reused 81646
Receiving objects: 100% (85282/85282), 32.10 MiB | 15.65 MiB/s, done.
Resolving deltas: 100% (60702/60702), done.
abraxas3d@chococat:~/documentation-friday$ 
```

There are a large number of branches in this repository. We need the correct branch that matches the Pluto hardware. For other targets that we use, the branch is named after the specific version of Vivado used. However, that does not appear to be the case for the PLUTO SDR. 

First, move into the checked out repository root directory. This is where the .git directory is located, and is where git commands, such as listing branches and checking in and out code, will work. 

`abraxas3d@chococat:~/documentation-friday$ cd hdl`

Next, list all the branches that have "pluto" in their title. 

```
abraxas3d@chococat:~/documentation-friday/hdl$ git branch -a | grep pluto
  remotes/origin/dev_pluto_ng_cmos
  remotes/origin/dev_pluto_ng_gpio_reorder
  remotes/origin/dev_pluto_ng_mipi
  remotes/origin/pluto_phaser
  remotes/origin/pluto_phaser_sim
  remotes/origin/pluto_phaser_sync
  remotes/origin/plutosdr-fw-v038_m2k-fw-v032
abraxas3d@chococat:~/documentation-friday/hdl$ 
```

We need the last one, `plutosdr-fw-v038_m2k-fw-v032`. Next, we designate this branch as the one we're going to be working with. 

```
abraxas3d@chococat:~/documentation-friday/hdl$ git checkout plutosdr-fw-v038_m2k-fw-v032 
branch 'plutosdr-fw-v038_m2k-fw-v032' set up to track 'origin/plutosdr-fw-v038_m2k-fw-v032'.
Switched to a new branch 'plutosdr-fw-v038_m2k-fw-v032'
abraxas3d@chococat:~/documentation-friday/hdl$ 
```

Next we need to build this design. We navigate to the place in the directory structure that corresponds to our hardware. If we were working with the zc706 and an ADRV9009, we'd go to `/documentation-friday/hdl/projects/adrv9009/zc706`

For the PLUTO SDR, we go to `/documentation-friday/hdl/projects/pluto`

We make the design. We haven't added any of our hardware yet. We're just building the reference design transceiver as-is. Running make runs a series of scripts and makefiles. This process also creates a Vivado project for the entire design, using whichever version of Vivado is in our environment. The version of Vivado comes from the source command we did before we cloned the HDL repository. 

Here is the directory contents before we run make:
```
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ ls
Makefile  Readme.md  system_bd.tcl  system_constr.xdc  system_project.tcl  system_top.v
```

Here's the output of the make command. I use `time make` simply to find out how long these builds take. PLUTO takes a relatively short amount of time compared to some of the other hardware combinations in Remote Lab.

```
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ time make
Building axi_ad9361 library [/home/abraxas3d/documentation-friday/hdl/library/axi_ad9361/axi_ad9361_ip.log] ... OK
Building util_cdc library [/home/abraxas3d/documentation-friday/hdl/library/util_cdc/util_cdc_ip.log] ... OK
Building util_axis_fifo library [/home/abraxas3d/documentation-friday/hdl/library/util_axis_fifo/util_axis_fifo_ip.log] ... OK
Building axi_dmac library [/home/abraxas3d/documentation-friday/hdl/library/axi_dmac/axi_dmac_ip.log] ... OK
Building axi_tdd library [/home/abraxas3d/documentation-friday/hdl/library/axi_tdd/axi_tdd_ip.log] ... OK
Building util_cpack2 library [/home/abraxas3d/documentation-friday/hdl/library/util_pack/util_cpack2/util_cpack2_ip.log] ... OK
Building util_upack2 library [/home/abraxas3d/documentation-friday/hdl/library/util_pack/util_upack2/util_upack2_ip.log] ... OK
Building pluto project [/home/abraxas3d/documentation-friday/hdl/projects/pluto/pluto_vivado.log] ... OK

real	127m25.982s
user	32m34.364s
sys	15m5.450s
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ 
```

Here's the contents of our project directory after the make command. 

```
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ ls
axi_ad9361_delay.log  pluto.gen            pluto.runs  pluto_vivado.log  system_bd.tcl       system_top.v      vivado.jou
Makefile              pluto.hw             pluto.sdk   pluto.xpr         system_constr.xdc   timing_impl.log   vivado.log
pluto.cache           pluto.ip_user_files  pluto.srcs  Readme.md         system_project.tcl  timing_synth.log
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ 
```
From here, we launch Vivado (we type "vivado") and then open `pluto.xpr`, the pluto xilinx project file. 

From the graphical user interface, we can open the block diagram and look at the way the blocks of the transceiver design are put together. We can look at many other reports and build artifacts. We are in the default or "stock" state of the Pluto design. 

#### Adding A Block to the Transmitter

Our transmitter blocks are placed in between the digital to analog converter direct memory access controller block and the transmitter channel unpacker block. We will call these blocks the DAC_DMA and UPACK. These two transmitter chain blocks are connected to each other by an AXI stream interface. Each of them has a reset and a clock. 

Our theory of operation here is that the IQ sample stream coming out of the DAC_DMA can be modified by a block. Every time that we get a new sample from memory, it's then clocked into our block, changes are made, and then it's clocked out to the UPACK. The IQ samples then proceed on their way to the transmitter. 

The master port of the DAC_DMA connects to the slave port of the UPACK. We disconnect these wires, and interpose our new block (AXI_OPV4UPR) in between them. The master port of the DAC_DMA goes to the slave port of the AXI_OPV4UPR, and the master port of AXI_OPVUPR goes to the slave port of the UPACK.

In the HDL Reference design, blocks are connected with tcl scripts. The tcl script that instantiates the blocks and connects their ports is in the project directory and is called system_bd.tcl. 

First, we instantiate our "intellectual property" (IP), and then we connect it up.

We'll add these commands that achieve this functionality towards the bottom of the file, right above the section designated `# interconnects`. ad_ip_instance has the module name first and the instance name second. ad_connect has "from" port and then "to" port. The block name is separated from the signal name with a slash. 

Commands added:
```
ad_ip_instance axi_opv4upr axi_opv4upr_0

ad_connect tx_upack/s_axis axi_opv4upr_0/m_axis
ad_connect axi_ad9361_dac_dma/m_axis axi_opv4upr_0/s_axis
```

(We currently do not have a CPU interface but we will be adding one later. For right now, we are focusing on getting the AXI stream, clock, and resets connected properly)

Now that we have our connections listed in this board level file, the next line we look at is `ad_connect tx_upack/s_axis  axi_ad9361_dac_dma/m_axis`

This is a connection we are going to comment out, because we have interposed our block between these two blocks (see above). We leave the clock and resets for DAC_DMA and UPACK where they are. We leave the inputs to the DAC_DMA and the outputs of the UPACK as they are.

Comment out this connection:
`#ad_connect tx_upack/s_axis  axi_ad9361_dac_dma/m_axis`

We're going to use the same clock that the UPACK block uses. We set up that connection by adding this:
`ad_connect  axi_ad9361/l_clk axi_opv4upr_0/clk`

We're going to use the same reset that the UPACK block uses. We set up that connection by adding this:
`ad_connect  logic_or_1/Res  axi_opv4upr_0/reset`

If we run make at this point, we will get an error because we've referred to a block instance that doesn't exist. While we have to have the instance added and the ports connected up in this file, we are definitely not done yet. 

```
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ make
Building pluto project [/home/abraxas3d/documentation-friday/hdl/projects/pluto/pluto_vivado.log] ... FAILED
For details see /home/abraxas3d/documentation-friday/hdl/projects/pluto/pluto_vivado.log

../scripts/project-xilinx.mk:100: recipe for target 'pluto.sdk/system_top.xsa' failed
make: *** [pluto.sdk/system_top.xsa] Error 1
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ 
```
Here's the relevant portion of the log file:

```
connect_bd_net /logic_or_1/Res /tx_upack/reset
## ad_ip_instance axi_opv4upr axi_opv4upr_0
WARNING: [Coretcl 2-175] No Catalog IPs found
ERROR: [BD 41-74] Exec TCL: Please specify VLNV when creating IP cell axi_opv4upr_0
ERROR: [BD 5-7] Error: running create_bd_cell  -type ip -name axi_opv4upr_0 .
ERROR: [Common 17-39] 'create_bd_cell' failed due to earlier errors.
```
Make can't find our IP in the "catalog". create_bd_cell is called by ad_ip_instance, and fails, because there is nothing in the library named axi_op4upr. Let's fix that. 

The next place we need to go is the /hdl/library/ directory further back in the hierarchy. Here's the contents of this library directory. 

```
/home/abraxas3d/documentation-friday/hdl/library
abraxas3d@chococat:~/documentation-friday/hdl/library$ ls
ad463x_data_capture  axi_ad9684           axi_generic_adc     axi_sysid     util_axis_fifo       util_gmii_to_rgmii
axi_ad5766           axi_ad9739a          axi_gpreg           axi_tdd       util_axis_fifo_asym  util_hbm
axi_ad7606x          axi_ad9783           axi_hdmi_rx         cn0363        util_axis_resize     util_i2c_mixer
axi_ad7616           axi_ad9963           axi_hdmi_tx         common        util_axis_upscale    util_mfifo
axi_ad7768           axi_adaq8092         axi_i2s_adi         cordic_demod  util_bsplit          util_mii_to_rmii
axi_ad777x           axi_adc_decimate     axi_intr_monitor    data_offload  util_cdc             util_pack
axi_ad9122           axi_adc_trigger      axi_laser_driver    intel         util_cic             util_pad
axi_ad9250           axi_adrv9001         axi_logic_analyzer  interfaces    util_dacfifo         util_pulse_gen
axi_ad9265           axi_clkgen           axi_ltc2387         jesd204       util_dec256sinc24b   util_rfifo
axi_ad9361           axi_clock_monitor    axi_pulse_gen       Makefile      util_delay           util_sigma_delta_spi
axi_ad9434           axi_dac_interpolate  axi_pwm_gen         scripts       util_do_ram          util_tdd_sync
axi_ad9467           axi_dmac             axi_rd_wr_combiner  spi_engine    util_extract         util_var_fifo
axi_ad9625           axi_fan_control      axi_spdif_rx        sysid_rom     util_fir_dec         util_wfifo
axi_ad9671           axi_fmcadc5_sync     axi_spdif_tx        util_adcfifo  util_fir_int         xilinx
abraxas3d@chococat:~/documentation-friday/hdl/library$ 
```

Each of these directories contains the information about the circuits that the make process needs to build the design. First, let's add our IP to the Makefile in library. We add it in two places, the "clean" and "clean all" lists. 

Here's what that looks like:

```
clean:
	$(MAKE) -C ad463x_data_capture clean
	$(MAKE) -C axi_opv4upr clean
	$(MAKE) -C axi_ad5766 clean
	$(MAKE) -C axi_ad7606x clean
```
and, lower down:
```
clean-all:clean
lib:
	$(MAKE) -C ad463x_data_capture
	$(MAKE) -C axi_opv4upr
	$(MAKE) -C axi_ad5766
```

Next, make our block directory under library. Move in there and let's start constructing the necessary files. 

```
abraxas3d@chococat:~/documentation-friday/hdl/library$ mkdir axi_opv4upr
abraxas3d@chococat:~/documentation-friday/hdl/library$ cd axi_opv4upr/
abraxas3d@chococat:~/documentation-friday/hdl/library/axi_opv4upr$ 
```

Let's look at the contents of the directories of the blocks we are connecting ours up to, the DAC DMA and the UPACK. There's information in there that may help us build up our directory.

Here's the DAC DMA directory. 

```
abraxas3d@chococat:~/documentation-friday/hdl/library/axi_dmac$ ls
address_generator.v      axi_dmac.ip_user_files       axi_dmac.v            dmac_2d_transfer.v    splitter.v
axi_dmac_burst_memory.v  axi_dmac_pkg_sv.ttcl         axi_dmac.xpr          gui                   src_axi_mm.v
axi_dmac.cache           axi_dmac_regmap_request.v    axi_register_slice.v  inc_id.vh             src_axi_stream.v
axi_dmac_constr.sdc      axi_dmac_regmap.v            bd                    Makefile              src_fifo_inf.v
axi_dmac_constr.ttcl     axi_dmac_reset_manager.v     component.xml         request_arb.v         tb
axi_dmac.hw              axi_dmac_resize_dest.v       data_mover.v          request_generator.v   vivado.jou
axi_dmac_hw.tcl          axi_dmac_resize_src.v        dest_axi_mm.v         response_generator.v  vivado.log
axi_dmac_ip.log          axi_dmac_response_manager.v  dest_axi_stream.v     response_handler.v    xgui
axi_dmac_ip.tcl          axi_dmac_transfer.v          dest_fifo_inf.v       resp.vh
abraxas3d@chococat:~/documentation-friday/hdl/library/axi_dmac$ 
```

There's a lot in there. This is a complex block that does a lot of things and has several different types of interfaces. It has the AXI streaming inteface we are going to connect to, it has an interface to memory, and it has an interface to the CPU in order for it to be configured and controlled via register reads and writes. 

Our block is simpler in structure and has fewer files than this one, but we need the same types of things that are in this directory. These are talked about on the ADI wiki website discussed at the top of this document (https://wiki.analog.com/resources/fpga/docs/hdl/creating_new_ip_guide). We will have an axi_opv4upr_ip.tcl, a Makefile, and our source code axi_opv4upr.vhd. We also need a component.xml file, which we get from the process of packaging our IP. This is a process done in Vivado. This xml file contains (at the least) information that is necessary for our block to show up in the board diagram graphical user interface. 

Let's look at the UPACK block library directory contents. Note that the UPACK directory is a subdirectory of a library directory. This is because there are multiple variants of the pack/unpack block, and the designers probably wanted to keep all of them together to make the directory structure cleaner. We could choose to do the same with our transmit and receive blocks by having an OPV directory and then transmit and receive subdirectories. 

```
abraxas3d@chococat:~/documentation-friday/hdl/library/util_pack/util_upack2$ pwd
/home/abraxas3d/documentation-friday/hdl/library/util_pack/util_upack2
abraxas3d@chococat:~/documentation-friday/hdl/library/util_pack/util_upack2$ ls
component.xml      util_upack2.hw      util_upack2_ip.log         util_upack2.v    vivado.log
Makefile           util_upack2_hw.tcl  util_upack2_ip.tcl         util_upack2.xpr  xgui
util_upack2.cache  util_upack2_impl.v  util_upack2.ip_user_files  vivado.jou
abraxas3d@chococat:~/documentation-friday/hdl/library/util_pack/util_upack2$ 
```
Here we see the same types of files. We have a component.xml, source files, a util_upack2_ip.tcl, and a Makefile. 

The _ip.tcl files in these two directories have commands that set up the AXI stream interface as a bus. This is how we get the collapsing/expanding effect in our block diagram. Let's follow the lead of the blocks we're connecting to, and try to set our block up as a bus. This way, it's a single line to connect the AXI stream interface in the system_bd.tcl file to connect two blocks together, intead of multiple single connections. 

In util_upack2_ip.tcl, there's a command that sets up a bus. 

```
adi_add_bus "s_axis" "slave" \
  "xilinx.com:interface:axis_rtl:1.0" \
  "xilinx.com:interface:axis:1.0" \
  [list {"s_axis_ready" "TREADY"} \
    {"s_axis_valid" "TVALID"} \
    {"s_axis_data" "TDATA"} \
  ]
adi_add_bus_clock "clk" "s_axis" "reset"
```
Note that the clk and reset signals below the bus appear to be set here, and not in the system_bd.tcl file. (?)

So, in our axi_opv4upr_ip.tcl file, we have the commands we were instructed to include from the wiki, and also a set of re-written adi_add_bus commands, using util_upack2 as a model.

```
adi_add_bus "m_axis" "master" \
  "xilinx.com:interface:axis_rtl:1.0" \
  "xilinx.com:interface:axis:1.0" \
  [list {"m_axis_ready" "TREADY"} \
    {"m_axis_valid" "TVALID"} \
    {"m_axis_data" "TDATA"} \
  ]
adi_add_bus_clock "clk" "m_axis" 


adi_add_bus "s_axis" "slave" \
  "xilinx.com:interface:axis_rtl:1.0" \
  "xilinx.com:interface:axis:1.0" \
  [list {"s_axis_ready" "TREADY"} \
    {"s_axis_valid" "TVALID"} \
    {"s_axis_data" "TDATA"} \
  ]
adi_add_bus_clock "clk" "s_axis" "reset"

```

The entire axi_opv4upr_ip.tcl file is:

```
source ../../scripts/adi_env.tcl
source $ad_hdl_dir/library/scripts/adi_ip_xilinx.tcl

adi_ip_create axi_opv4upr


adi_ip_files axi_opv4upr [list \
        "axi_opv4upr.vhd"]

# use this command if we have AXI lite for register controls
#adi_ip_properties axi_opv4upr

# use this command if we do not use AXI for register control
adi_ip_properties_lite axi_opv4upr

adi_add_bus "m_axis" "master" \
  "xilinx.com:interface:axis_rtl:1.0" \
  "xilinx.com:interface:axis:1.0" \
  [list {"m_axis_ready" "TREADY"} \
    {"m_axis_valid" "TVALID"} \
    {"m_axis_data" "TDATA"} \
  ]
adi_add_bus_clock "clk" "m_axis" 


adi_add_bus "s_axis" "slave" \
  "xilinx.com:interface:axis_rtl:1.0" \
  "xilinx.com:interface:axis:1.0" \
  [list {"s_axis_ready" "TREADY"} \
    {"s_axis_valid" "TVALID"} \
    {"s_axis_data" "TDATA"} \
  ]
adi_add_bus_clock "clk" "s_axis" "reset"


ipx::save_core [ipx::current_core]
```

Our Makefile here is as simple as we can make it (pun intended). 

```
####################################################################################
## Copyright (c) 2018 - 2023 Analog Devices, Inc.
### SPDX short identifier: BSD-1-Clause
## Auto-generated, but was modified
####################################################################################

LIBRARY_NAME := axi_opv4upr

GENERIC_DEPS += axi_opv4upr.vhd

XILINX_DEPS += axi_opv4upr_ip.tcl

include ../scripts/library.mk
```

Our (dummy or do-little) block source code is:

```
----------------------------------------------------------------------------------
-- Company: Open Research Institute, Inc.
-- Engineer: Ken Easton, Abraxas3d, Paul Williamson, Rose Easton
--
-- Create Date: 04/06/2024 11:46:41 PM
-- Design Name: OPV4UPR
-- Module Name: passthrough - Behavioral
-- Project Name: Opulent Voice for University of Puerto Rico
-- Target Devices: PLUTO SDR etc.
-- Tool Versions: 2022.2
-- Description: a block inserted into the transmit chain that makes modifications
-- to the stream of IQ values coming from DMA
--
-- Dependencies:
--
-- Revision:
-- controlled in Git
-- Additional Comments:
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;
entity axi_opv4upr is
    Port ( clk         : in STD_LOGIC;
           reset       : in STD_LOGIC;
           m_axis_data : out STD_LOGIC_VECTOR (63 downto 0);
           s_axis_data : in STD_LOGIC_VECTOR (63 downto 0);
           s_axis_ready : out STD_LOGIC;
           s_axis_valid : in STD_LOGIC;
           m_axis_valid : out STD_LOGIC;
           m_axis_ready : in STD_LOGIC);
end axi_opv4upr;

architecture Behavioral of axi_opv4upr is
-- internal copies of the signals we are going to use
           signal output_data    :  STD_LOGIC_VECTOR (63 downto 0);
           signal input_data     :  STD_LOGIC_VECTOR (63 downto 0);
           signal s_axis_valid_i :  STD_LOGIC;
           signal m_axis_valid_i :  STD_LOGIC;
  -- constant 64 bit value of all zeros
           signal all_zeros      : STD_LOGIC_VECTOR(input_data'range) := (others => '0');
           signal all_ones       : STD_LOGIC_VECTOR(input_data'range) := (others => '1');
begin
-- asynchronous assignments-- pass along the data
    m_axis_data <= output_data;
    input_data <= s_axis_data;
    -- get the axis_ready signal we get from upack and pass it along to DMA
    s_axis_ready <= m_axis_ready;
    -- receive axis_valid on our slave port
    s_axis_valid_i <= s_axis_valid;
    -- present our axis_valid on our master port
    m_axis_valid <= m_axis_valid_i;    
 
 
    -- processes    
 
    pass_data : process (reset, clk)
    begin
        if reset = '1' then
            m_axis_valid_i <= '0';
        elsif rising_edge(clk) then
            if s_axis_valid_i = '0' then
            -- clock signal happens and invalid data at input
            -- pass the input data through to the output.
                output_data <= input_data;
        -- and then send the input data to the output data
                m_axis_valid_i <= '0';
        -- indicate to the channel unpacker that this is invalid data (just for fun)
            else 
                    -- clock signal happens and valid data at input
        -- overwrite the fetched value from DMA with all 1s.
                output_data <= all_ones;
        -- and then send the input data to the output data
                m_axis_valid_i <= '1';
        -- indicate to the channel unpacker we have valid data
            end if;
        end if;
    end process pass_data;
end Behavioral;
```

What happens if we run `make` at this point, without the component.xml file? No surprise, it still fails. 

```
connect_bd_net /logic_or_1/Res /tx_upack/reset
## ad_ip_instance axi_opv4upr axi_opv4upr_0
WARNING: [Coretcl 2-175] No Catalog IPs found
ERROR: [BD 41-74] Exec TCL: Please specify VLNV when creating IP cell axi_opv4upr_0
ERROR: [BD 5-7] Error: running create_bd_cell  -type ip -name axi_opv4upr_0 .
ERROR: [Common 17-39] 'create_bd_cell' failed due to earlier errors.
```

The final piece is the component.xml file. We go to our block project in Vivado and use the IP Packager tool to create it. Now we can place our block in the system block diagram.

We move the component.xml file to the /library/axi_opv4upr directory. Until we figure out how to export this file without the wrong directory locations embedded in it (help needed) then we hand-edit the component.xml file to point to the axi_opv4upr.vhd file sitting right by it. 

When we packaged our IP, we included the testbench file axi_opv4upr_tb.vhd and the waveform configuration file. Instead of fighting things, we went ahead and included the testbench and the stimulus file in the library block. We also included the simple stimulus file so that if someone wanted to take the source code from the library directory and run the testbench, they could do so. 

We run make and get a new error:

```
## ad_ip_instance axi_opv4upr axi_opv4upr_0
## ad_connect tx_upack/s_axis axi_opv4upr_0/m_axis
ERROR: ad_connect: Cannot connect non-interface to interface: tx_upack/s_axis (bd_intf_pin) <-/-> axi_opv4upr_0/m_axis (newnet)
    while executing
"error "ERROR: ad_connect: Cannot connect non-interface to interface: $name_a ($type_a) <-/-> $name_b ($type_b)""
    invoked from within
"if {!([string first intf $type_a]+1) != !([string first intf $type_b]+1)} {
    error "ERROR: ad_connect: Cannot connect non-interface to interface: $..."
    (procedure "ad_connect" line 8)
    invoked from within
"ad_connect tx_upack/s_axis axi_opv4upr_0/m_axis"
    (file "system_bd.tcl" line 354)
```

Matthew Wishek wrties, 

"The issue is related to the I/Os on axi_opv4upr are not defined as bd_intf_ports/pin or bd_ports/pins.

Reviewing the axi_tdd block shows an approach that would work. In that block a BD wrapper is created which instantiates the axi_tdd block. The wrapper has the requisite create_bd_intf_pin/ports commands.

Reviewing the axi_dmac block I don't see  create_bd_intf_pins/ports or create_bd_pins/ports commands anywhere, so it isn't clear how that is happening, but it is happening. But, I have been able to confirm that axi_dmac ports are of the bd_pin/port and/or bd_intf_pin/port."

We connected the individual elements of the AXI streaming bus together. 

This resulted in warnings such as the one below, for each of the six connections (axis_data, axis_ready, axis_valid on both slave and master ports). 

```
## ad_connect axi_ad9361_dac_dma/m_axis_data axi_opv4upr_0/s_axis_data
WARNING: [BD 41-1306] The connection to interface pin </axi_ad9361_dac_dma/m_axis_data> is being overridden by the user with net <axi_ad9361_dac_dma_m_axis_data>. This pin will not be connected as a part of interface connection <m_axis>.
```

Help needed here. We'd like to have an interface connection, and following the way it was done in the blocks we're connecting to didn't work.

And, a new error:

```
## ad_connect axi_ad9361/l_clk axi_opv4upr_0/clk
ERROR: [BD 41-85] Exec TCL - Illegal Name: The name 'axi_opv4upr_0/clk' contains illegal characters. It must only contain alphanumeric characters and '_' 
ERROR: [BD 5-4] Error: running connect_bd_net.
ERROR: [Common 17-39] 'connect_bd_net' failed due to earlier errors.

    while executing
"connect_bd_net -net $name_b $obj_a"
    ("bd_pin,newnet" arm line 2)
    invoked from within
"switch $type_a,$type_b {
    newnet,newnet {
      error "ERROR: ad_connect: Cannot create connection between two new nets: $name_a <-/-> $name_b"
   ..."
    (procedure "ad_connect" line 12)
    invoked from within
"ad_connect axi_ad9361/l_clk axi_opv4upr_0/clk"
    (file "system_bd.tcl" line 368)

    while executing
"source system_bd.tcl"
    (procedure "adi_project_create" line 129)
    invoked from within
"adi_project_create pluto 0 {} "xc7z010clg225-1""
    (file "system_project.tcl" line 5)
INFO: [Common 17-206] Exiting Vivado at Sun Apr 14 20:11:11 2024...
```

Retyping the command twice didn't resolve the error. It is all alphanumeric or underscores in the name.

This error turned out to be a stale component.xml file. If you chanage your block source code, be sure to replace the component.xml file. If there is a mismatch in the port names, then you will most likely get the error above. 

To get past the "cannot connect interface to non-inteface" error, we connected the individual s_axis and m_axis pins. This is done in the system_bd.tcl file. 

Here are the excerpted commands from system_bd.tcl file. We have successfully interposed a block on the transmit side. Now we need to build the pluto firmware with the new bitfile and test it. "Export Hardware" from Vivado, and "Include Bitstream" in order to get this file. 

When updating the source code for the block in the library, the system_bd.tcl file has to be touched, or project make will not restart. 

```
# Opulent Voice for University of Puerto Rico

ad_ip_instance axi_opv4upr axi_opv4upr_0

ad_connect axi_ad9361_dac_dma/m_axis_data axi_opv4upr_0/s_axis_data
ad_connect axi_ad9361_dac_dma/m_axis_ready axi_opv4upr_0/s_axis_ready
ad_connect axi_ad9361_dac_dma/m_axis_valid axi_opv4upr_0/s_axis_valid
ad_connect tx_upack/s_axis_data axi_opv4upr_0/m_axis_data
ad_connect tx_upack/s_axis_valid axi_opv4upr_0/m_axis_valid
ad_connect tx_upack/s_axis_ready axi_opv4upr_0/m_axis_ready

ad_connect axi_ad9361/l_clk axi_opv4upr_0/clk
ad_connect logic_or_1/Res axi_opv4upr_0/reset
```


Here are the final axi_opv4upr_ip.tcl commands. 

```
source ../../scripts/adi_env.tcl
source $ad_hdl_dir/library/scripts/adi_ip_xilinx.tcl

adi_ip_create axi_opv4upr

adi_ip_files axi_opv4upr [list \
	"axi_opv4upr.vhd"]

# use this command if we have AXI lite for register controls
#adi_ip_properties axi_opv4upr

# use this command if we do not use AXI for register control
adi_ip_properties_lite axi_opv4upr

ipx::save_core [ipx::current_core]
```

After these files are updated, make at the project level is run. For the Pluto, typical project build results are below. 

```
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ time make
Building pluto project [/home/abraxas3d/documentation-friday/hdl/projects/pluto/pluto_vivado.log] ... OK

real	61m13.971s
user	18m21.787s
sys	7m0.981s
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ 
```

### Updating the PLUTO Firmware with new HDL

This is a Work log for PLUTO HDL modifications 

source of instructions`https://wiki.analog.com/university/tools/pluto/devs/embedded_code`

But! We had to get x86_64 instead of i686 version of the cross compiler, because we are on a 64 bit OS and not a 32 bit OS. 

Set the path:

`export PATH=/usr/local/bin/gcc-linaro-7.2.1-2017.11-x86_64_arm-linux-gnueabihf/bin:$PATH`

`arm-linux-gnueabihf-gcc -mfloat-abi=hard  --sysroot=$HOME/pluto-0.38.sysroot -std=gnu99 -g -o pluto_stream ad9361-iiostream.c -lpthread -liio -lm -Wall -Wextra`

`scp pluto_stream root@pluto.local:/tmp/pluto_stream`

`ssh -t root@pluto.local /tmp/pluto_stream`

Refer to the HDL Reference design project we modified with our custom IP above.

```
abraxas3d@keroppi:~/pluto-opv-transmitter/hdl/projects/pluto$ time make
Building axi_tdd library [/home/abraxas3d/pluto-opv-transmitter/hdl/library/axi_tdd/axi_tdd_ip.log] ... OK
Building util_cpack2 library [/home/abraxas3d/pluto-opv-transmitter/hdl/library/util_pack/util_cpack2/util_cpack2_ip.log] ... OK
Building util_upack2 library [/home/abraxas3d/pluto-opv-transmitter/hdl/library/util_pack/util_upack2/util_upack2_ip.log] ... OK
Building pluto project [/home/abraxas3d/pluto-opv-transmitter/hdl/projects/pluto/pluto_vivado.log] ... OK
real	107m50.934s
user	24m13.667s
sys	13m49.347s
```

The plan was that once we updated bitfile and xsa that then we can update the firmware for Pluto.

Get sources for firmware

`git clone --recursive https://github.com/analogdevicesinc/plutosdr-fw.git`

prerequisites - set vivado version

`source /tools/Xilinx/Vivado/2022.2/settings64.sh`

Set the environmental variables to point to the right places. Let's try 2022.2 with stock firmware first. This is the same version we used to make our custom IP.

```
export CROSS_COMPILE=arm-linux-gnueabihf-
export PATH=$PATH:/tools/Xilinx/Vitis/2022.2/gnu/aarch32/lin/gcc-arm-linux-gnueabi/bin
export VIVADO_SETTINGS=/tools/Xilinx/Vivado/2022.2/settings64.sh
```

Make "stock" firmware image. Type "make" in firmware directory.

We had to sudo apt install libmpc-dev. It was a missing dependency.

```
legal-info/legal-info.sha256
legal-info/buildroot.config
rm linux/arch/arm/boot/dts/zynq-pluto-sdr-revc.dtb
linux/arch/arm/boot/dts/zynq-pluto-sdr.dtb
linux/arch/arm/boot/dts/zynq-pluto-sdr-revb.dtb
real	228m11.127s
user	67m39.744s
sys	26m7.405s
```

Test stock firmware image.

Next, get the xsa and bit files from our modified HDL reference design. This is an export from Vivado. 

Travis writes:
```
The Makefile method does not expect you are using an HDF file generated externally. 
If you want to use it you will need to modify this stage: 
https://github.com/analogdevicesinc/plutosdr-fw/blob/master/Makefile#L135 
to copy your prebuilt HDF into the relevant directory.

If you do not understand Makefiles it would likely be easier to just follow the 
individual steps below the automated process. If you have already run the 
unchanged Makefile this would also be faster since you have the dependent pieces already.

You just need to change the pluto.frm file. Follow from 
"Build FPGA Hardware Description File" through "Build Firmware FRM image".

If it's not clear, the mkimage tool will consume zImage (the kernel), 
root.cpio.gz (userspace), and system_top.bit. 
This is your main entrypoint for your new bitstream.

-Travis
```

The script calls out an hdf file, but support for that format from Xilinx was dropped long ago.

So, we will try and use our xsa file instead of the hdf file. 

The steps Travis is referring to are on this page:

https://wiki.analog.com/university/tools/pluto/building_the_image


#### Build FPGA Hardware Description File
`source /opt/Xilinx/Vivado/2021.2/settings64.sh`
`make -C hdl/projects/pluto`
`cp hdl/projects/pluto/pluto.sdk/system_top.hdf build/system_top.hdf`

#### Build FPGA First Stage Bootloader (FSBL)
`source /opt/Xilinx/Vivado/2021.2/settings64.sh`
`xsdk -batch -source scripts/create_fsbl_project.tcl`
`cp build/sdk/hw_0/system_top.bit build/system_top.bit`

#### Build multi component FIT image (Flattened Image Tree)
`u-boot-xlnx/tools/mkimage -f scripts/pluto.its build/pluto.itb`

#### Build Firmware DFU image
`cp build/pluto.itb build/pluto.itb.tmp`
`dfu-suffix -a build/pluto.itb.tmp -v 0x0456 -p 0xb673`
`mv build/pluto.itb.tmp build/pluto.dfu`

#### Build Firmware FRM image
`md5sum build/pluto.itb | cut -d ' ' -f 1 > build/pluto.frm.md5`
`cat build/pluto.itb build/pluto.frm.md5 > build/pluto.frm`




## Integrating Custom IP into the PLUTO SDR HDL Reference Design using Out of Tree Module Method
Here is a set of instructions for getting this minimum shift keying (MSK) transceiver implementation to work on a PLUTO SDR using an out of tree module approach. The pluto_msk repository is an example of this method. 

Clone the pluto_msk repository.

```
git clone --recursive https://github.com/OpenResearchInstitute/pluto_msk.git
```

The repository should clone to the latest stable PLUTO firmware release commit. Here is an example of how to change to another branch of the hdl reference design. hdl_2022_r2 was used for VHDL development. Don't change branches of hdl unless you have to.

```
/pluto_msk/hdl$ git checkout hdl_2022_r2 
Previous HEAD position was 1978df298 axi_dac_interpolate: Improve the ctrl logic
branch 'hdl_2022_r2' set up to track 'origin/hdl_2022_r2'.
Switched to a new branch 'hdl_2022_r2'
```

If you are working on ORI virtual machine, then source the version of Vivado needed as follows. 

```$ source /tools/Xilinx/Vivado/2022.2/settings.sh```

You can check which version of Vivado is currently being used as follows. 

```
$ which vivado
/tools/Xilinx/Vivado/2022.2/bin/vivado
```
Change directories to the PLUTO project directory and run make. 

```
/hdl/projects/pluto$ make
```
A useful log file for information, warnings, and errors is pluto_vivado.log

This repository is organized as an out of tree module. The source files do not have to be installed in the /library directory. What we do instead is to expand the number of places that Vivado looks for the information needed to build the modules. 

Key lines in system_bd.tcl are:

https://github.com/OpenResearchInstitute/pluto_msk/blob/942aa516f8cc30af73a5a0c9ce3f8266012989e8/projects/pluto/system_bd.tcl#L7-19

```
set_property ip_repo_paths [list $ad_hdl_dir/library ../../library]  [current_fileset]
update_ip_catalog
```
The ip_repo_paths property lets us create a custom IP catalog for use with Vivado. It defines the path to one or more directories containing user-defined intellectual property (IP), like our blocks. The specified directories, and any sub-directories, are searched for files to add to the Vivado IP catalog. The property is assigned to the current fileset of the current project. 

ip_repo_paths will look for a <component>.xml file, where <component> is the name of the IP to add to the catalog. This XML file lists the files that define the module. Subdirectories are searched through. We don't have to list out each individual module's <component>.xml.

Where does our component.xml file come from? It's create by the msk_top_ip.tcl file. A version can be found here:
https://github.com/OpenResearchInstitute/pluto_msk/blob/main/library/msk_top_ip.tcl

Setting the ip_repo_paths property needs to be followed by update_ip_catalog. 

Example syntax:

```
set_property IP_REPO_PATHS {c:/Data/Designs C:/myIP} [current_fileset]
update_ip_catalog
```
Running make in the project directory should be all that one has to do in order to build the HDL reference design with custom IP. 



## Appendix A: Modified TCL File
```
#
# Parameter description:
#   [TX/RX/RX_OS]_JESD_M  : Number of converters per link
#   [TX/RX/RX_OS]_JESD_L  : Number of lanes per link
#   [TX/RX/RX_OS]_JESD_S  : Number of samples per frame
#   [TX/RX/RX_OS]_JESD_NP : Number of bits per sample
#
set MAX_TX_NUM_OF_LANES 4
set MAX_RX_NUM_OF_LANES 2
set MAX_RX_OS_NUM_OF_LANES 2

# TX parameters
set TX_NUM_OF_LANES $ad_project_params(TX_JESD_L)      ; # L
set TX_NUM_OF_CONVERTERS $ad_project_params(TX_JESD_M) ; # M
set TX_SAMPLES_PER_FRAME $ad_project_params(TX_JESD_S) ; # S
set TX_SAMPLE_WIDTH 16                                 ; # N/NP

set TX_SAMPLES_PER_CHANNEL [expr $TX_NUM_OF_LANES * 32 / \
                                ($TX_NUM_OF_CONVERTERS * $TX_SAMPLE_WIDTH)] ; # L * 32 / (M * N)

# RX parameters
set RX_NUM_OF_LANES $ad_project_params(RX_JESD_L)      ; # L
set RX_NUM_OF_CONVERTERS $ad_project_params(RX_JESD_M) ; # M
set RX_SAMPLES_PER_FRAME $ad_project_params(RX_JESD_S) ; # S
set RX_SAMPLE_WIDTH 16                                 ; # N/NP

set RX_SAMPLES_PER_CHANNEL [expr $RX_NUM_OF_LANES * 32 / \
                                ($RX_NUM_OF_CONVERTERS * $RX_SAMPLE_WIDTH)] ; # L * 32 / (M * N)

# RX Observation parameters
set RX_OS_NUM_OF_LANES $ad_project_params(RX_OS_JESD_L)      ; # L
set RX_OS_NUM_OF_CONVERTERS $ad_project_params(RX_OS_JESD_M) ; # M
set RX_OS_SAMPLES_PER_FRAME $ad_project_params(RX_OS_JESD_S) ; # S
set RX_OS_SAMPLE_WIDTH 16                                    ; # N/NP

set RX_OS_SAMPLES_PER_CHANNEL [expr $RX_OS_NUM_OF_LANES * 32 / \
                                   ($RX_OS_NUM_OF_CONVERTERS * $RX_OS_SAMPLE_WIDTH)] ;  # L * 32 / (M * N)

set dac_fifo_name axi_ad9371_dacfifo
set dac_data_width [expr $TX_SAMPLE_WIDTH * $TX_NUM_OF_CONVERTERS * $TX_SAMPLES_PER_CHANNEL]
set dac_dma_data_width [expr $TX_SAMPLE_WIDTH * $TX_NUM_OF_CONVERTERS * $TX_SAMPLES_PER_CHANNEL]

source $ad_hdl_dir/library/jesd204/scripts/jesd204.tcl
source $ad_hdl_dir/projects/common/xilinx/adi_fir_filter_bd.tcl

# ad9371

create_bd_port -dir I dac_fifo_bypass
create_bd_port -dir I adc_fir_filter_active
create_bd_port -dir I dac_fir_filter_active

# dac peripherals

ad_ip_instance axi_clkgen axi_ad9371_tx_clkgen
ad_ip_parameter axi_ad9371_tx_clkgen CONFIG.ID 2
ad_ip_parameter axi_ad9371_tx_clkgen CONFIG.CLKIN_PERIOD 8
ad_ip_parameter axi_ad9371_tx_clkgen CONFIG.VCO_DIV 1
ad_ip_parameter axi_ad9371_tx_clkgen CONFIG.VCO_MUL 8
ad_ip_parameter axi_ad9371_tx_clkgen CONFIG.CLK0_DIV 8

ad_ip_instance axi_adxcvr axi_ad9371_tx_xcvr
ad_ip_parameter axi_ad9371_tx_xcvr CONFIG.NUM_OF_LANES $TX_NUM_OF_LANES
ad_ip_parameter axi_ad9371_tx_xcvr CONFIG.QPLL_ENABLE 1
ad_ip_parameter axi_ad9371_tx_xcvr CONFIG.TX_OR_RX_N 1
ad_ip_parameter axi_ad9371_tx_xcvr CONFIG.SYS_CLK_SEL 3
ad_ip_parameter axi_ad9371_tx_xcvr CONFIG.OUT_CLK_SEL 3
ad_ip_parameter axi_ad9371_tx_xcvr CONFIG.LPM_OR_DFE_N 0

adi_axi_jesd204_tx_create axi_ad9371_tx_jesd $TX_NUM_OF_LANES

ad_ip_instance util_upack2 util_ad9371_tx_upack [list \
  NUM_OF_CHANNELS $TX_NUM_OF_CONVERTERS \
  SAMPLES_PER_CHANNEL $TX_SAMPLES_PER_CHANNEL \
  SAMPLE_DATA_WIDTH $TX_SAMPLE_WIDTH \
]

ad_add_interpolation_filter "tx_fir_interpolator" 8 $TX_NUM_OF_CONVERTERS 2 {122.88} {15.36} \
                            "$ad_hdl_dir/library/util_fir_int/coefile_int.coe"

adi_tpl_jesd204_tx_create tx_ad9371_tpl_core $TX_NUM_OF_LANES \
                                             $TX_NUM_OF_CONVERTERS \
                                             $TX_SAMPLES_PER_FRAME \
                                             $TX_SAMPLE_WIDTH

ad_ip_instance axi_dmac axi_ad9371_tx_dma
ad_ip_parameter axi_ad9371_tx_dma CONFIG.DMA_TYPE_SRC 0
ad_ip_parameter axi_ad9371_tx_dma CONFIG.DMA_TYPE_DEST 1
ad_ip_parameter axi_ad9371_tx_dma CONFIG.CYCLIC 1
ad_ip_parameter axi_ad9371_tx_dma CONFIG.AXI_SLICE_SRC 0
ad_ip_parameter axi_ad9371_tx_dma CONFIG.AXI_SLICE_DEST 1
ad_ip_parameter axi_ad9371_tx_dma CONFIG.ASYNC_CLK_DEST_REQ 1
ad_ip_parameter axi_ad9371_tx_dma CONFIG.ASYNC_CLK_SRC_DEST 1
ad_ip_parameter axi_ad9371_tx_dma CONFIG.ASYNC_CLK_REQ_SRC 1
ad_ip_parameter axi_ad9371_tx_dma CONFIG.DMA_2D_TRANSFER 0
ad_ip_parameter axi_ad9371_tx_dma CONFIG.DMA_DATA_WIDTH_DEST $dac_dma_data_width

ad_dacfifo_create $dac_fifo_name $dac_data_width $dac_dma_data_width $dac_fifo_address_width

# adc peripherals

ad_ip_instance axi_clkgen axi_ad9371_rx_clkgen
ad_ip_parameter axi_ad9371_rx_clkgen CONFIG.ID 2
ad_ip_parameter axi_ad9371_rx_clkgen CONFIG.CLKIN_PERIOD 8
ad_ip_parameter axi_ad9371_rx_clkgen CONFIG.VCO_DIV 1
ad_ip_parameter axi_ad9371_rx_clkgen CONFIG.VCO_MUL 8
ad_ip_parameter axi_ad9371_rx_clkgen CONFIG.CLK0_DIV 8

ad_ip_instance axi_adxcvr axi_ad9371_rx_xcvr
ad_ip_parameter axi_ad9371_rx_xcvr CONFIG.NUM_OF_LANES $RX_NUM_OF_LANES
ad_ip_parameter axi_ad9371_rx_xcvr CONFIG.QPLL_ENABLE 0
ad_ip_parameter axi_ad9371_rx_xcvr CONFIG.TX_OR_RX_N 0
ad_ip_parameter axi_ad9371_rx_xcvr CONFIG.SYS_CLK_SEL 0
ad_ip_parameter axi_ad9371_rx_xcvr CONFIG.OUT_CLK_SEL 3
ad_ip_parameter axi_ad9371_rx_xcvr CONFIG.LPM_OR_DFE_N 1

adi_axi_jesd204_rx_create axi_ad9371_rx_jesd $RX_NUM_OF_LANES
ad_ip_parameter axi_ad9371_rx_jesd/rx CONFIG.SYSREF_IOB {false}

ad_ip_instance util_cpack2 util_ad9371_rx_cpack [list \
  NUM_OF_CHANNELS $RX_NUM_OF_CONVERTERS \
  SAMPLES_PER_CHANNEL $RX_SAMPLES_PER_CHANNEL \
  SAMPLE_DATA_WIDTH $RX_SAMPLE_WIDTH \
]

adi_tpl_jesd204_rx_create rx_ad9371_tpl_core $RX_NUM_OF_LANES \
                                             $RX_NUM_OF_CONVERTERS \
                                             $RX_SAMPLES_PER_FRAME \
                                             $RX_SAMPLE_WIDTH

ad_ip_instance axi_dmac axi_ad9371_rx_dma
ad_ip_parameter axi_ad9371_rx_dma CONFIG.DMA_TYPE_SRC 2
ad_ip_parameter axi_ad9371_rx_dma CONFIG.DMA_TYPE_DEST 0
ad_ip_parameter axi_ad9371_rx_dma CONFIG.CYCLIC 0
ad_ip_parameter axi_ad9371_rx_dma CONFIG.SYNC_TRANSFER_START 1
ad_ip_parameter axi_ad9371_rx_dma CONFIG.AXI_SLICE_SRC 0
ad_ip_parameter axi_ad9371_rx_dma CONFIG.AXI_SLICE_DEST 0
ad_ip_parameter axi_ad9371_rx_dma CONFIG.ASYNC_CLK_DEST_REQ 1
ad_ip_parameter axi_ad9371_rx_dma CONFIG.ASYNC_CLK_SRC_DEST 1
ad_ip_parameter axi_ad9371_rx_dma CONFIG.ASYNC_CLK_REQ_SRC 1
ad_ip_parameter axi_ad9371_rx_dma CONFIG.DMA_2D_TRANSFER 0
ad_ip_parameter axi_ad9371_rx_dma CONFIG.DMA_DATA_WIDTH_SRC [expr $RX_SAMPLE_WIDTH * \
                                                                  $RX_NUM_OF_CONVERTERS * \
                                                                  $RX_SAMPLES_PER_CHANNEL]

ad_add_decimation_filter "rx_fir_decimator" 8 $RX_NUM_OF_CONVERTERS 1 {122.88} {122.88} \
                         "$ad_hdl_dir/library/util_fir_int/coefile_int.coe"

# adc-os peripherals

ad_ip_instance axi_clkgen axi_ad9371_rx_os_clkgen
ad_ip_parameter axi_ad9371_rx_os_clkgen CONFIG.ID 2
ad_ip_parameter axi_ad9371_rx_os_clkgen CONFIG.CLKIN_PERIOD 8
ad_ip_parameter axi_ad9371_rx_os_clkgen CONFIG.VCO_DIV 1
ad_ip_parameter axi_ad9371_rx_os_clkgen CONFIG.VCO_MUL 8
ad_ip_parameter axi_ad9371_rx_os_clkgen CONFIG.CLK0_DIV 8

ad_ip_instance axi_adxcvr axi_ad9371_rx_os_xcvr
ad_ip_parameter axi_ad9371_rx_os_xcvr CONFIG.NUM_OF_LANES $RX_OS_NUM_OF_LANES
ad_ip_parameter axi_ad9371_rx_os_xcvr CONFIG.QPLL_ENABLE 0
ad_ip_parameter axi_ad9371_rx_os_xcvr CONFIG.TX_OR_RX_N 0
ad_ip_parameter axi_ad9371_rx_os_xcvr CONFIG.SYS_CLK_SEL 0
ad_ip_parameter axi_ad9371_rx_os_xcvr CONFIG.OUT_CLK_SEL 3
ad_ip_parameter axi_ad9371_rx_os_xcvr CONFIG.LPM_OR_DFE_N 1

adi_axi_jesd204_rx_create axi_ad9371_rx_os_jesd $RX_OS_NUM_OF_LANES
ad_ip_parameter axi_ad9371_rx_os_jesd/rx CONFIG.SYSREF_IOB {false}

ad_ip_instance util_cpack2 util_ad9371_rx_os_cpack [list \
  NUM_OF_CHANNELS $RX_OS_NUM_OF_CONVERTERS \
  SAMPLES_PER_CHANNEL $RX_OS_SAMPLES_PER_CHANNEL\
  SAMPLE_DATA_WIDTH $RX_OS_SAMPLE_WIDTH \
]

adi_tpl_jesd204_rx_create rx_os_ad9371_tpl_core $RX_OS_NUM_OF_LANES \
                                                $RX_OS_NUM_OF_CONVERTERS \
                                                $RX_OS_SAMPLES_PER_FRAME \
                                                $RX_OS_SAMPLE_WIDTH

ad_ip_instance axi_dmac axi_ad9371_rx_os_dma
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.DMA_TYPE_SRC 2
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.DMA_TYPE_DEST 0
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.CYCLIC 0
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.SYNC_TRANSFER_START 1
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.AXI_SLICE_SRC 0
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.AXI_SLICE_DEST 0
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.ASYNC_CLK_DEST_REQ 1
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.ASYNC_CLK_SRC_DEST 1
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.ASYNC_CLK_REQ_SRC 1
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.DMA_2D_TRANSFER 0
ad_ip_parameter axi_ad9371_rx_os_dma CONFIG.DMA_DATA_WIDTH_SRC [expr $RX_OS_SAMPLE_WIDTH * \
                                                                     $RX_OS_NUM_OF_CONVERTERS * \
                                                                     $RX_OS_SAMPLES_PER_CHANNEL]

# common cores


ad_ip_instance util_adxcvr util_ad9371_xcvr
ad_ip_parameter util_ad9371_xcvr CONFIG.RX_NUM_OF_LANES [expr $MAX_RX_NUM_OF_LANES+$MAX_RX_OS_NUM_OF_LANES]
ad_ip_parameter util_ad9371_xcvr CONFIG.TX_NUM_OF_LANES $MAX_TX_NUM_OF_LANES
ad_ip_parameter util_ad9371_xcvr CONFIG.TX_OUT_DIV 2
ad_ip_parameter util_ad9371_xcvr CONFIG.CPLL_FBDIV 4
ad_ip_parameter util_ad9371_xcvr CONFIG.RX_CLK25_DIV 5
ad_ip_parameter util_ad9371_xcvr CONFIG.TX_CLK25_DIV 5
ad_ip_parameter util_ad9371_xcvr CONFIG.RX_PMA_CFG 0x00018480
ad_ip_parameter util_ad9371_xcvr CONFIG.RX_CDR_CFG 0x03000023ff20400020
ad_ip_parameter util_ad9371_xcvr CONFIG.QPLL_FBDIV 0x120

# xcvr interfaces

set tx_ref_clk     tx_ref_clk_0
set rx_ref_clk     rx_ref_clk_0
set rx_obs_ref_clk rx_ref_clk_$MAX_RX_NUM_OF_LANES

create_bd_port -dir I $tx_ref_clk
create_bd_port -dir I $rx_ref_clk
create_bd_port -dir I $rx_obs_ref_clk
ad_connect  $sys_cpu_resetn util_ad9371_xcvr/up_rstn
ad_connect  $sys_cpu_clk util_ad9371_xcvr/up_clk

# Tx
ad_connect  ad9371_tx_device_clk axi_ad9371_tx_clkgen/clk_0
ad_xcvrcon  util_ad9371_xcvr axi_ad9371_tx_xcvr axi_ad9371_tx_jesd {1 2 3 0} ad9371_tx_device_clk {} $MAX_TX_NUM_OF_LANES
ad_connect  util_ad9371_xcvr/tx_out_clk_0 axi_ad9371_tx_clkgen/clk
ad_xcvrpll  $tx_ref_clk util_ad9371_xcvr/qpll_ref_clk_0
ad_xcvrpll  axi_ad9371_tx_xcvr/up_pll_rst util_ad9371_xcvr/up_qpll_rst_0

# Rx
ad_connect  ad9371_rx_device_clk axi_ad9371_rx_clkgen/clk_0
ad_xcvrcon  util_ad9371_xcvr axi_ad9371_rx_xcvr axi_ad9371_rx_jesd {} ad9371_rx_device_clk {} $MAX_RX_NUM_OF_LANES
ad_connect  util_ad9371_xcvr/rx_out_clk_0 axi_ad9371_rx_clkgen/clk
for {set i 0} {$i < $MAX_RX_NUM_OF_LANES} {incr i} {
  set ch [expr $i]
  ad_xcvrpll  $rx_ref_clk util_ad9371_xcvr/cpll_ref_clk_$ch
  ad_xcvrpll  axi_ad9371_rx_xcvr/up_pll_rst util_ad9371_xcvr/up_cpll_rst_$ch
}

# Rx - OBS
ad_connect  ad9371_rx_os_device_clk axi_ad9371_rx_os_clkgen/clk_0
ad_xcvrcon  util_ad9371_xcvr axi_ad9371_rx_os_xcvr axi_ad9371_rx_os_jesd {} ad9371_rx_os_device_clk {} $MAX_RX_OS_NUM_OF_LANES
ad_connect  util_ad9371_xcvr/rx_out_clk_$MAX_RX_NUM_OF_LANES axi_ad9371_rx_os_clkgen/clk
for {set i 0} {$i < $MAX_RX_OS_NUM_OF_LANES} {incr i} {
  # channel indexing starts from the last RX
  set ch [expr $MAX_RX_NUM_OF_LANES + $i]
  ad_xcvrpll  $rx_obs_ref_clk util_ad9371_xcvr/cpll_ref_clk_$ch
  ad_xcvrpll  axi_ad9371_rx_os_xcvr/up_pll_rst util_ad9371_xcvr/up_cpll_rst_$ch
}

# dma clock & reset

ad_connect  $sys_dma_reset axi_ad9371_dacfifo/dma_rst

# connections (dac)

ad_connect  axi_ad9371_tx_clkgen/clk_0 tx_ad9371_tpl_core/link_clk
ad_connect  axi_ad9371_tx_jesd/tx_data tx_ad9371_tpl_core/link

ad_connect  axi_ad9371_tx_clkgen/clk_0 util_ad9371_tx_upack/clk
ad_connect  ad9371_tx_device_clk_rstgen/peripheral_reset util_ad9371_tx_upack/reset

ad_connect  axi_ad9371_tx_clkgen/clk_0 axi_ad9371_dacfifo/dac_clk
ad_connect  ad9371_tx_device_clk_rstgen/peripheral_reset axi_ad9371_dacfifo/dac_rst

ad_connect tx_fir_interpolator/aclk axi_ad9371_tx_clkgen/clk_0

for {set i 0} {$i < $TX_NUM_OF_CONVERTERS} {incr i} {
  ad_connect  tx_ad9371_tpl_core/dac_enable_$i  tx_fir_interpolator/dac_enable_$i
  ad_connect  tx_ad9371_tpl_core/dac_valid_$i  tx_fir_interpolator/dac_valid_$i

  ad_connect  util_ad9371_tx_upack/fifo_rd_data_$i  tx_fir_interpolator/data_in_${i}
  ad_connect  util_ad9371_tx_upack/enable_$i  tx_fir_interpolator/enable_out_${i}

  ad_connect  tx_fir_interpolator/data_out_${i}  tx_ad9371_tpl_core/dac_data_$i
}

if {$TX_NUM_OF_CONVERTERS <= 2} {
  ad_connect  tx_fir_interpolator/valid_out_0  util_ad9371_tx_upack/fifo_rd_en
} else {
  ad_ip_instance util_vector_logic logic_or [list \
    C_OPERATION {or} \
    C_SIZE 1]

  ad_connect  logic_or/Op1  tx_fir_interpolator/valid_out_0
  ad_connect  logic_or/Op2  tx_fir_interpolator/valid_out_2
  ad_connect  logic_or/Res  util_ad9371_tx_upack/fifo_rd_en
}

ad_connect  tx_fir_interpolator/active dac_fir_filter_active

# TODO: Add streaming AXI interface for DAC FIFO
ad_connect  util_ad9371_tx_upack/s_axis_valid VCC
ad_connect  util_ad9371_tx_upack/s_axis_ready axi_ad9371_dacfifo/dac_valid
ad_connect  util_ad9371_tx_upack/s_axis_data axi_ad9371_dacfifo/dac_data

ad_connect  $sys_dma_clk axi_ad9371_dacfifo/dma_clk
ad_connect  $sys_dma_clk axi_ad9371_tx_dma/m_axis_aclk
#ad_connect  axi_ad9371_dacfifo/dma_valid axi_ad9371_tx_dma/m_axis_valid
#ad_connect  axi_ad9371_dacfifo/dma_data axi_ad9371_tx_dma/m_axis_data
#ad_connect  axi_ad9371_dacfifo/dma_ready axi_ad9371_tx_dma/m_axis_ready
ad_connect  axi_ad9371_dacfifo/dma_xfer_req axi_ad9371_tx_dma/m_axis_xfer_req
#ad_connect  axi_ad9371_dacfifo/dma_xfer_last axi_ad9371_tx_dma/m_axis_last
ad_connect  axi_ad9371_dacfifo/dac_dunf tx_ad9371_tpl_core/dac_dunf
ad_connect  axi_ad9371_dacfifo/bypass dac_fifo_bypass
ad_connect  $sys_dma_resetn axi_ad9371_tx_dma/m_src_axi_aresetn

# connections (adc)

ad_connect  axi_ad9371_rx_clkgen/clk_0 rx_ad9371_tpl_core/link_clk
ad_connect  axi_ad9371_rx_jesd/rx_sof rx_ad9371_tpl_core/link_sof
ad_connect  axi_ad9371_rx_jesd/rx_data_tdata rx_ad9371_tpl_core/link_data
ad_connect  axi_ad9371_rx_jesd/rx_data_tvalid rx_ad9371_tpl_core/link_valid
ad_connect  axi_ad9371_rx_clkgen/clk_0 util_ad9371_rx_cpack/clk
ad_connect  ad9371_rx_device_clk_rstgen/peripheral_reset util_ad9371_rx_cpack/reset

ad_connect rx_fir_decimator/aclk axi_ad9371_rx_clkgen/clk_0

for {set i 0} {$i < $RX_NUM_OF_CONVERTERS} {incr i} {
  ad_connect  rx_ad9371_tpl_core/adc_valid_$i rx_fir_decimator/valid_in_$i
  ad_connect  rx_ad9371_tpl_core/adc_enable_$i rx_fir_decimator/enable_in_$i
  ad_connect  rx_ad9371_tpl_core/adc_data_$i rx_fir_decimator/data_in_${i}

  ad_connect  rx_fir_decimator/enable_out_$i util_ad9371_rx_cpack/enable_$i
  ad_connect  rx_fir_decimator/data_out_${i} util_ad9371_rx_cpack/fifo_wr_data_$i
}

ad_connect  rx_fir_decimator/valid_out_0 util_ad9371_rx_cpack/fifo_wr_en
ad_connect  rx_ad9371_tpl_core/adc_dovf util_ad9371_rx_cpack/fifo_wr_overflow

ad_connect rx_fir_decimator/active adc_fir_filter_active

ad_connect  axi_ad9371_rx_clkgen/clk_0 axi_ad9371_rx_dma/fifo_wr_clk
ad_connect  util_ad9371_rx_cpack/packed_fifo_wr axi_ad9371_rx_dma/fifo_wr
ad_connect  $sys_dma_resetn axi_ad9371_rx_dma/m_dest_axi_aresetn

# connections (adc-os)

ad_connect  axi_ad9371_rx_os_clkgen/clk_0 rx_os_ad9371_tpl_core/link_clk
ad_connect  axi_ad9371_rx_os_jesd/rx_sof rx_os_ad9371_tpl_core/link_sof
ad_connect  axi_ad9371_rx_os_jesd/rx_data_tdata rx_os_ad9371_tpl_core/link_data
ad_connect  axi_ad9371_rx_os_jesd/rx_data_tvalid rx_os_ad9371_tpl_core/link_valid
ad_connect  axi_ad9371_rx_os_clkgen/clk_0 util_ad9371_rx_os_cpack/clk
ad_connect  ad9371_rx_os_device_clk_rstgen/peripheral_reset util_ad9371_rx_os_cpack/reset
ad_connect  axi_ad9371_rx_os_clkgen/clk_0 axi_ad9371_rx_os_dma/fifo_wr_clk

ad_connect  rx_os_ad9371_tpl_core/adc_valid_0 util_ad9371_rx_os_cpack/fifo_wr_en
for {set i 0} {$i < $RX_OS_NUM_OF_CONVERTERS} {incr i} {
  ad_connect  rx_os_ad9371_tpl_core/adc_enable_$i util_ad9371_rx_os_cpack/enable_$i
  ad_connect  rx_os_ad9371_tpl_core/adc_data_$i util_ad9371_rx_os_cpack/fifo_wr_data_$i
}
ad_connect  rx_os_ad9371_tpl_core/adc_dovf util_ad9371_rx_os_cpack/fifo_wr_overflow
ad_connect  util_ad9371_rx_os_cpack/packed_fifo_wr axi_ad9371_rx_os_dma/fifo_wr

ad_connect  $sys_dma_resetn axi_ad9371_rx_os_dma/m_dest_axi_aresetn

# ===================================== PFB ===============================

set_param ips.enableInterfaceArrayInference false

ad_ip_instance pfb_wrapper pfb_wrap_0

ad_connect  axi_adrv9009_rx_clkgen/clk_0 pfb_wrap_0/clk
ad_connect  adrv9009_rx_device_clk_rstgen/peripheral_reset pfb_wrap_0/sync_reset


ad_connect util_adrv9009_rx_cpack/packed_fifo_wr_en pfb_wrap_0/packed_fifo_wr_en
ad_connect util_adrv9009_rx_cpack/packed_fifo_wr_data pfb_wrap_0/packed_fifo_wr_data
ad_connect util_adrv9009_rx_cpack/packed_fifo_wr_overflow pfb_wrap_0/packed_fifo_wr_overflow
ad_connect util_adrv9009_rx_cpack/packed_fifo_wr_sync pfb_wrap_0/packed_fifo_wr_sync

ad_connect axi_adrv9009_rx_dma/fifo_wr_en pfb_wrap_0/fifo_wr_en
ad_connect axi_adrv9009_rx_dma/fifo_wr_din pfb_wrap_0/fifo_wr_data
ad_connect axi_adrv9009_rx_dma/fifo_wr_overflow pfb_wrap_0/fifo_wr_overflow
ad_connect axi_adrv9009_rx_dma/fifo_wr_sync pfb_wrap_0/fifo_wr_sync

# interconnect (cpu)

ad_cpu_interconnect 0x44A00000 rx_ad9371_tpl_core
ad_cpu_interconnect 0x44A04000 tx_ad9371_tpl_core
ad_cpu_interconnect 0x44A08000 rx_os_ad9371_tpl_core
ad_cpu_interconnect 0x44A80000 axi_ad9371_tx_xcvr
ad_cpu_interconnect 0x43C00000 axi_ad9371_tx_clkgen
ad_cpu_interconnect 0x44A90000 axi_ad9371_tx_jesd
ad_cpu_interconnect 0x7c420000 axi_ad9371_tx_dma
ad_cpu_interconnect 0x44A60000 axi_ad9371_rx_xcvr
ad_cpu_interconnect 0x43C10000 axi_ad9371_rx_clkgen
ad_cpu_interconnect 0x44AA0000 axi_ad9371_rx_jesd
ad_cpu_interconnect 0x7c400000 axi_ad9371_rx_dma
ad_cpu_interconnect 0x44A50000 axi_ad9371_rx_os_xcvr
ad_cpu_interconnect 0x43C20000 axi_ad9371_rx_os_clkgen
ad_cpu_interconnect 0x44AB0000 axi_ad9371_rx_os_jesd
ad_cpu_interconnect 0x7c440000 axi_ad9371_rx_os_dma
ad_cpu_interconnect 0x7c480000 pfb_wrap_0

# gt uses hp3, and 100MHz clock for both DRP and AXI4

ad_mem_hp3_interconnect $sys_cpu_clk sys_ps7/S_AXI_HP3
ad_mem_hp3_interconnect $sys_cpu_clk axi_ad9371_rx_xcvr/m_axi
ad_mem_hp3_interconnect $sys_cpu_clk axi_ad9371_rx_os_xcvr/m_axi

# interconnect (mem/dac)

ad_mem_hp1_interconnect $sys_dma_clk sys_ps7/S_AXI_HP1
ad_mem_hp1_interconnect $sys_dma_clk axi_ad9371_tx_dma/m_src_axi
ad_mem_hp2_interconnect $sys_dma_clk sys_ps7/S_AXI_HP2
ad_mem_hp2_interconnect $sys_dma_clk axi_ad9371_rx_dma/m_dest_axi
ad_mem_hp2_interconnect $sys_dma_clk axi_ad9371_rx_os_dma/m_dest_axi

# interrupts

ad_cpu_interrupt ps-8 mb-8 axi_ad9371_rx_os_jesd/irq
ad_cpu_interrupt ps-9 mb-7 axi_ad9371_tx_jesd/irq
ad_cpu_interrupt ps-10 mb-15 axi_ad9371_rx_jesd/irq
ad_cpu_interrupt ps-11 mb-14 axi_ad9371_rx_os_dma/irq
ad_cpu_interrupt ps-12 mb-13- axi_ad9371_tx_dma/irq
ad_cpu_interrupt ps-13 mb-12 axi_ad9371_rx_dma/irq

# ===================================== DVB MODULATOR ===============================
source ../../../../dvb_fpga/build/vivado/add_dvbs2_files.tcl
add_files ../../../../dvb_fpga/build/vivado/dvbs2_encoder_wrapper.vhd


# Create instance: dvbs2_encoder_wrapper_0, and set properties
  set block_name dvbs2_encoder_wrapper
  set block_cell_name dvbs2_encoder_wrapper_0
  if { [catch {set dvbs2_encoder_wrapper_0 [create_bd_cell -type module -reference $block_name $block_cell_name] } errmsg] } {
     catch {common::send_gid_msg -ssname BD::TCL -id 2095 -severity "ERROR" "Unable to add referenced block <$block_name>. Please add the files for ${block_name}'s definition into the project."}
     return 1
   } elseif { $dvbs2_encoder_wrapper_0 eq "" } {
     catch {common::send_gid_msg -ssname BD::TCL -id 2096 -severity "ERROR" "Unable to referenced block <$block_name>. Please add the files for ${block_name}'s definition into the project."}
     return 1
   }

#added $ to sys_cpu_clk -mdt
ad_connect $sys_cpu_clk dvbs2_encoder_wrapper_0/clk
ad_ip_parameter dvbs2_encoder_wrapper_0 CONFIG.INPUT_DATA_WIDTH 32

ad_connect $sys_cpu_resetn dvbs2_encoder_wrapper_0/rst_n
#ad_cpu_interconnect 0x43C10000 dvbs2_encoder_wrapper_0
#below is original zc706 address
#ad_cpu_interconnect 0x44AB8000 dvbs2_encoder_wrapper_0
#below is a test to see if 64k alignment is better than 32k
#this is a long shot but we should know how to change the address
ad_cpu_interconnect 0x44AC0000 dvbs2_encoder_wrapper_0

ad_connect axi_ad9371_tx_dma/m_axis_data dvbs2_encoder_wrapper_0/s_axis_tdata
ad_connect axi_ad9371_tx_dma/m_axis_last dvbs2_encoder_wrapper_0/s_axis_tlast
ad_connect axi_ad9371_tx_dma/m_axis_valid dvbs2_encoder_wrapper_0/s_axis_tvalid
ad_connect axi_ad9371_tx_dma/m_axis_ready dvbs2_encoder_wrapper_0/s_axis_tready

ad_connect axi_ad9371_dacfifo/dma_data dvbs2_encoder_wrapper_0/m_axis_tdata
ad_connect axi_ad9371_dacfifo/dma_xfer_last dvbs2_encoder_wrapper_0/m_axis_tlast
ad_connect axi_ad9371_dacfifo/dma_valid dvbs2_encoder_wrapper_0/m_axis_tvalid
ad_connect axi_ad9371_dacfifo/dma_ready dvbs2_encoder_wrapper_0/m_axis_tready


if 0 {
ad_connect dvbs2_encoder_wrapper_0/s_axis axi_ad9361_dac_dma/m_axis

ad_ip_instance axis_data_fifo interclk
ad_ip_parameter interclk CONFIG.FIFO_DEPTH 16
ad_ip_parameter interclk CONFIG.FIFO_MODE 1
ad_ip_parameter interclk CONFIG.IS_ACLK_ASYNC 1
ad_ip_parameter interclk CONFIG.HAS_TLAST.VALUE_SRC USER
ad_ip_parameter interclk CONFIG.HAS_TLAST 0

ad_connect sys_cpu_clk interclk/s_axis_aclk
ad_connect interclk/m_axis_aclk axi_ad9361/l_clk
ad_connect sys_cpu_resetn interclk/s_axis_aresetn

set rrc_2interpol [ create_bd_cell -type ip -vlnv xilinx.com:ip:fir_compiler:7.2 rrc_2interpol ]
set_property -dict [ list \
   CONFIG.Clock_Frequency {61.44} \
   CONFIG.CoefficientSource {COE_File} \
   CONFIG.Coefficient_File {../../../../../../filterrrc_4_63.coe} \
   CONFIG.Coefficient_Fractional_Bits {0} \
   CONFIG.Coefficient_Sets {1} \
   CONFIG.Coefficient_Sign {Signed} \
   CONFIG.Coefficient_Structure {Inferred} \
   CONFIG.Coefficient_Width {16} \
   CONFIG.ColumnConfig {8} \
   CONFIG.DATA_Has_TLAST {Not_Required} \
   CONFIG.Data_Fractional_Bits {15} \
   CONFIG.Decimation_Rate {1} \
   CONFIG.Filter_Architecture {Systolic_Multiply_Accumulate} \
   CONFIG.Filter_Type {Interpolation} \
   CONFIG.Interpolation_Rate {4} \
   CONFIG.M_DATA_Has_TREADY {true} \
   CONFIG.Number_Channels {1} \
   CONFIG.Number_Paths {2} \
   CONFIG.Output_Rounding_Mode {Symmetric_Rounding_to_Zero} \
   CONFIG.Output_Width {16} \
   CONFIG.Quantization {Integer_Coefficients} \
   CONFIG.RateSpecification {Frequency_Specification} \
   CONFIG.S_DATA_Has_FIFO {true} \
   CONFIG.Sample_Frequency {15.36} \
   CONFIG.Zero_Pack_Factor {1} \
 ] $rrc_2interpol

ad_connect dvbs2_encoder_wrapper_0/m_axis rrc_2interpol/S_AXIS_DATA
ad_connect  sys_cpu_clk rrc_2interpol/aclk
ad_connect rrc_2interpol/M_AXIS_DATA interclk/S_AXIS
ad_connect interclk/M_AXIS tx_upack/s_axis

#without interpol
#ad_connect dvbs2_encoder_wrapper_0/m_axis interclk/S_AXIS
}
```
