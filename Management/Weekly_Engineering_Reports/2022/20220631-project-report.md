# Project Report

## P4DX

Authentication and Authorization work in progress at https://github.com/phase4ground/documents/tree/master/Engineering/AAAAA

### FPGA

Tuesday's FPGA Stand-up meeting video is here: 

https://youtu.be/abp2zHINA-g

Uplink simulator work can be found here:

https://github.com/phase4ground/documents/tree/master/Engineering/Uplink%20Modem/Simulator

Nothing new will be added to this until we work through required changes to the demod codebase from mobilinkd to move from 3200 bps CODEC2 to 16 kbps OPUS. High bitrate voice mode is called Opulent Voice.

Here's the (updated) state diagram we start with in the demodulator:

https://drive.google.com/file/d/1L3DJ7vEKKnR4eT2ai8B-9Lv2nZOWfixM/view?usp=sharing

Here's the protocol tracking document for Opulent Voice:

https://docs.google.com/document/d/1vmOwcjmGKwMgAqcdLQ-7zk8PMv6MAcV1hhGDVRyijsQ/edit?usp=sharing

Uplink voice and data streams will be received and multiplexed onto the downlink. 

Codebase is here: https://github.com/phase4ground/opv-cxx-demod

#### Encoder

Our encoder is integrated into the reference design from ADI, and is on the PLUTO in Remote Lab West (keroppi). 
Our encoder has been integrated into the reference design from ADI in Remote Lab UK. This design now builds successfully but the fixes need to be pulled in to the repo. 
Our encoder is in the process of being integrated into the reference design from ADI in Remote Lab South, but this is delayed due to physical plant upgrades necessary to expan the lab for biomedical work. 

We have libiio working on the target in the lab, and this allows DMA access for transmit. This was necessary to use the encoder in the design. Here is the process that achieves a linux build that supports all the hardware. 

abraxas3d@chococat:~/adi-encoder-meta-adi$ source ~/petalinux2021.1/settings.sh

PetaLinux environment set to '/home/abraxas3d/petalinux2021.1'
WARNING: This is not a supported OS
INFO: Checking free disk space
INFO: Checking installed tools
INFO: Checking installed development libraries
INFO: Checking network and other services

abraxas3d@chococat:~/adi-encoder-meta-adi$ petalinux-create -t project --template zynq --name meta-adi

INFO: Create project: meta-adi
INFO: New project successfully created in /home/abraxas3d/adi-encoder-meta-adi/integrate-iio

abraxas3d@chococat:~/adi-encoder-meta-adi$ ls

integrate-iio

abraxas3d@chococat:~/adi-encoder-meta-adi$ git clone https://github.com/analogdevicesinc/meta-adi.git

Cloning into 'meta-adi'...
remote: Enumerating objects: 1553, done.
remote: Counting objects: 100% (54/54), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 1553 (delta 37), reused 33 (delta 33), pack-reused 1499
Receiving objects: 100% (1553/1553), 270.48 KiB | 958.00 KiB/s, done.
Resolving deltas: 100% (891/891), done.

abraxas3d@chococat:~/adi-encoder-meta-adi$ ls

integrate-iio  meta-adi

abraxas3d@chococat:~/adi-encoder-meta-adi$ cd integrate-iio/

abraxas3d@chococat:~/adi-encoder-meta-adi/integrate-iio$ ls

config.project  project-spec

abraxas3d@chococat:~/adi-encoder-meta-adi/integrate-iio$
 petalinux-config --get-hw-description
../../adi-encoder-tcl-script-sd-card/system_top.xsa

At this point, the menuconfig opens, and you must add the two layers of meta-adi that are available to you from the cloned repository in the previous step. First add the core, then add the xilinx, as illustrated in the procedure starting at https://wiki.analog.com/resources/tools-software/linux-build/generic/petalinux but showed about halfway down the page at https://github.com/analogdevicesinc/meta-adi/tree/master/meta-adi-xilinx


[INFO] Sourcing build tools
INFO: Getting hardware description...
INFO: Renaming system_top.xsa to system.xsa
[INFO] Generating Kconfig for project
[INFO] Menuconfig project
*** End of the configuration.
*** Execute 'make' to start the build or try 'make help'.
[INFO] Sourcing build environment
[INFO] Generating kconfig for Rootfs
[INFO] Silentconfig rootfs
[INFO] Generating plnxtool conf
[INFO] Adding user layers
[INFO] Generating workspace directory

abraxas3d@chococat:~/adi-encoder-meta-adi/integrate-iio$
 echo "KERNEL_DTB"=\"{zynq-zc706-adv7511-adrv9371}"" >>
project-spec/meta-user/conf/petalinuxbsp.conf

abraxas3d@chococat:~/adi-encoder-meta-adi/integrate-iio$ cd build/

abraxas3d@chococat:~/adi-encoder-meta-adi/integrate-iio/build$ petalinux-build

<snipped>

Currently  2 running tasks (4817 of 5284)  91% |###########################################################################################         |


(got some staging errors, but I get those, and usually they go away when petalinux-build is re-run

We know something different is happening here with these new additional layers because the number of tasks has gone up from ~3800 to ~5300.


$ cat petalinuxbsp.conf
#User Configuration
#OE_TERMINAL = "tmux"
KERNEL_DTB="zynq-zc706-adv7511-adrv9371"



NOTE: Executing Tasks
NOTE: Tasks Summary: Attempted 5284 tasks of which 5049 didn't need to be rerun and all succeeded.
INFO: Successfully copied built images to tftp dir: /tftpboot
[INFO] Successfully built project
abraxas3d@chococat:~/adi-encoder-meta-adi/integrate-iio/build$


Now, petalinux package and boot the usual TFTP way, or SD card way, whichever one you are using. 

Here, we used TFPT package and boot. 

petalinux-package --prebuilt --fpga <path to bitstream from the analog devices reference design + our IP, exported from hardware manager>

petalinux-boot --jtag --prebuilt 2 --hw_server-url TCP:chococat:3121

Before you boot, set up:

screen -L -Logfile <log file name> /dev/ttyUSBx 115200

most of the time, the zc706 tends to show up on ttyUSB1. Move around if you don't see it. 

There will be a lot of messages from the zc706. When they stop, here's what we do.

zynq> setenv server 10.73.1.93
zynq> setenv padder 10.73.1.9 
zynq> pxe get
zynq> pxe boot


on target:
root@meta-adi:~# iio
iio_adi_xflow_check  iio_info             iio_stresstest
iio_attr             iio_readdev          iio_writedev
iio_genxml           iio_reg              iiod
root@meta-adi:~# iio



Python script from a computer using the zc706 as a remote host, seems to find the right stuff. 

iio_tests/python$ python3 ad9371-1ch.py 
<adi.ad9371.ad9371 object at 0x7f4f99133da0>
8 devices found:
ad7291
xadc
ad9528-1
ad9371-phy
axi-ad9371-rx-obs-hpc
axi-ad9371-tx-hpc
axi-ad9371-rx-hpc
None
RX LO 2510000000
TX FS: 245760000.0

Transmit was successful. The script sets up a DMA buffer and sends signals to the transmitter. Transmission was confirmed on the spectrum analyzer in Remote Labs West. 
#### Decoder

Very exciting area of progress is the DVB-S2/X HDL decoder. Decoder work has begun. Base is Ahmet's repo. There will be improvements and a new revision donated back to the repository. 

## Remote Lab South

Budget allocated; building has commenced. Some of the Lab equipment in storage in NorCal will arrive at Remote Lab South as soon as practical. Keith Wheeler was here this week in San Diego for business, and spent time after work in talks about ORI and the Lab. Thank you to Keith and the rest of the board for all the support, interest, and expertise to stand up an open source lab in an underserved community (central Arkansas, USA). 

## OpenRTX

We support OpenRTX and will show their work at DEFCON. See below in Event Planning.

## Ribbit Updates

Rattlegram is *in the Android store*. You can download it for free and play with it. There will be a poster session at DEFCON 30 in the RF Village. 

## FCC TAC 

Weekly AI/ML working group assignment on Bandwidth metrics and how AI/ML will affect policies concerning Bandwith is proceeding with the assistance of our FCC liaison. Prototype with either CBRS or inexpensive ultrasonic transducers is what we're talking about in the working group. 

## Components Engineering

47 GHz transponder components engineering proceeding, and the first batch of components has been received. 

## Grants and Fundraising

SBIR/STTR grants are the focus. Two FDA grants look good and are under consideration. There's plenty more out there at grants.gov. 

A large grant application is proceeding with a potential project partner, and we look forward to announcing good news this year. 

Our dedicated fundraising portal (from Commit Change) is set up and will be used for several campaigns revolving around unique items. It's also available to any project that uses ORI as a fiscal sponsor. Here is our first campaign! Please help spread the word. 

https://us.commitchange.com/ca/san-diego/open-research-institute/campaigns/where-will-we-go-next

## Event Planning

### DEFCON will be August 11-13, 2022

In-person demonstrations of everything we have working, plus we discussed whatever doesn't, and why. Excellent support from DEFCON over the past week - thank you to all helping out here. 

### Ham Expo will be September 17-18, 2022

Virtual event with booth and multiple speaking track. Has been a very successful event for ORI. Should we have our next quarterly TAC at Ham Expo? 

### ORI will be the November 2022 program for San Bernardino Microwave Society. 

Update about ORI's work and in-person demonstrations. 

### ORI Supports OSCW

We support Open Source Cubesat Workshop. We expect it will most likely be held in October. We've contributed feedback about the dates and location on their survey.

### HamCation 2023?

Anshul and Art are interested in going. We'll need more people to commit in order to be a formal part of the show.

### IMS2023 

Time to start submitting for inclusion on the floor and in the ham social demo area.
