# Using Petalinux

Easiest way to get Zynq-based cards up and running seems to be using Petalinux.
Here's some basic instructions on how to get the ZC706 to run the DVB Encoder
test design.

## Prerequisites

1. [Download][vivado download] and install Vivado
1. [Download][petalinux download] and install Petalinux
    - Also download the BSP for the card you're targeting

## Building the OS

1. Build the [DVB Encoder for the ZC706][dvb_fpga_zc706]
    - The script creates a directory called `zc706` in the working directory and
    after a successful build will export the hardware platform to
    `zc706/dvbs2_encoder.xsa`.
1. Create the Petalinux project by using both the BSP and the XSA. Please note
   that we pass the path to the `zc706` directory as argument, not the path to
   the XSA file itself.

    ```bash
    # Create the project based on the BSP
    petalinux-create --type project --source <path/to/zc706.bsp>
    # Configure the project using the exported hardware platform
    petalinux-config --silentconfig --get-hw-description <path/to/dvb_fpga/zc706>
    ```

1. Configure Petalinux rootfs packages
    - Run `petalinux-config -c rootfs`
    - Navigate to "Filesystem Packages", "misc", "python3" and select Python3
    - Navigate to "Apps" and select "peekpoke"
    - Exit and save the changes when prompted
1. Run `petalinux-build` to build the project
1. Open the UART terminal, default baud rate is 115200
1. Boot the card via JTAG: `petalinux-boot --jtag --kernel`
    - You can connect to an existing JTAG server using `--hw_server-url
  TCP:<hostname>:<port/number>`
1. Program the FPGA after the card completes the boot process

## Fully remote boot

### Loading Linux components in RAM
Assuming you have your network already setup, a working u-boot onto the SD card, you can load the Linux kernel over an IPv4 network using the [TFTP protocol](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol).

1. Install the tftp server. This step is distribution specific. [Debian](https://wiki.debian.org/TFTP)
1. From u-boot console
```
tftpboot 0x1000000 <tftp server ip>:<path to image.ub>; tftpboot 0x2000000 <tftp server ip>:<ramdisk or initrd cpio.gz.u-boot>; tftpboot 0x3000000 <tftp server ip>:<path to system.dtb>; bootm 0x1000000 0x2000000 0x3000000
```
Refer [here](https://www.denx.de/wiki/view/DULG/UBootEnvVariables) for more informations.

#### Mounting the rootfs remotely via NBD
[Network Block Device](https://en.wikipedia.org/wiki/Network_block_device) is a network protocol, supported in Linux, that is able to map a [block device](https://en.wikipedia.org/wiki/Device_node) remotely through an IP network.
The rootfs is hence offloaded from RAM and the entire rootfs become a file hosted onto a server.

1. Add NBD kernel driver, NBD client and the initramfs script to map and mount the NBD as root device.
2. Generate the initramfs file system, e.g. `petalinux-build -c petalinux-initramfs-image`.
 
[Here](https://github.com/salvatorelionetti/meta-ori) you can finf a custom layer for this.

Now the server, nbd-server package in Debian buster:
1. ```$ nbd-server 127.0.0.1:10809 -C nbd_server.conf```

where the conf file can be as simple as
```
[generic]
[rootfs.img]
exportname=<change with abs path>/rootfs.img
```

Finally just add this bootargs to u-boot:
1. ```root=/dev/nbd0 nbdroot=<nbd server ip:10809/<path to rootfs remote file>```

## Troubleshooting

### `petalinux-boot` fails with `Memory read error at 0xF8007080`

Need to use `xsdb` (provided with Vivado) to reset the PS.

1. Run `xsdb` from a regular shell with Vivado env set up
1. Once inside `xsdb`, run

    ```
    connect
    targets 1
    rst
    exit
    ```

1. Rerun the `petalinux-boot` command

[dvb_fpga_zc706]: https://github.com/phase4ground/dvb_fpga/tree/master/build/vivado/zc706
[petalinux download]: https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools.html
[vivado download]: https://www.xilinx.com/support/download.html

### `meta-user` layer is ignored

Need to set YOCTO_MACHINE_NAME to zc706-zynq7, accordingly to [UG1144](https://www.xilinx.com/support/documentation/sw_manuals/xilinx2020_1/ug1144-petalinux-tools-reference-guide.pdf) page 144.

1. Run `petalinux-config` from a bash shell after sourced petalinux settings.sh
2. Select `Yocto Settings`
3. Select `YOCTO_MACHINE_NAME` 

### Reboot from the SD using JTAG channel

In case you would like to restart the board, e.g. to experiment with u-boot by changing boot parameters, this line is your friend:
```
petalinux-boot --jtag --u-boot --after-connect "exec sleep 1" --after-connect "jtag targets" --after-connect "jtag target 3" --after-connect "target 1" --after-connect "rst -system" --after-connect "exec sleep 2000"
```
Just after the command you have the time to stop u-boot count-down and gain the boot console.
This command can be performed while Linux is running.
