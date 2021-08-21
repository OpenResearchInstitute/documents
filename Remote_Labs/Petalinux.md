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
