# How to Add Our Blocks to the Analog Devices HDL Reference Design

>ORI 6 November 2023 Abraxas3d ad_connect documentation and adrv9371 tcl file names

>ORI 8 November 2023 Abraxas3d error messages from API Mismatch problem, SD card creation

>ORI 29 March 2024 keaston successful integration of IP with HDL Reference Design

>ORI 12 April 2024 Abraxas3d documented how to integrate IP into PLUTO HDL Reference Design 

## General Guidelines
For new block integration to go smoothly, and in order to take advantage of the ADI-specific environment and build macros, it's recommend to make new blocks look like other blocks in the adi build tree. This is accomplished by installing new blocks should at hdl/library/blockname, where they are automatically picked up by the top level build, and editing the Makefile and blockname_ip.tcl in that directory along the lines as that presented in the following guide:
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

## Integrating Custom IP into the PLUTO SDR HDL Reference Design
### Steps Required to add the Opulent Voice Transmitter and Receiver Blocks

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

We make the design. We haven't added any of our hardware yet. We're just building the reference design transceiver as-is. We run a series of scripts and makefiles. This process also creates a Vivado project for the entire design, using whichever version of Vivado is in our environment. The version of Vivado comes from the source command we did before we cloned the HDL repository. 

Here is the directory contents before we run make:
```
abraxas3d@chococat:~/documentation-friday/hdl/projects/pluto$ ls
Makefile  Readme.md  system_bd.tcl  system_constr.xdc  system_project.tcl  system_top.v
```

Here's the output of the make command. I use `time make` simply to find out how long these builds take. PLUTO takes a relatively short amount of time compared to some of the other hardware combinations. 






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
