# Debricking a Pluto

When loading a new bitstream into flash memory on an ADALM PLUTO device, it's possible to end up in a state where the Pluto is unusable and normal firmware update procedures don't work.

One way we've discovered is to screw up AXI-LITE register access in such a way that when the IIO driver in the Linux kernel (part of your firmware in the Pluto) polls the PlutoSDR device (also part of your firmware, implemented in the FPGA part of the Pluto) during bootup, the access fails. This crashes Linux, and the result is a boot-crash loop. That is, Linux gets most of the way through booting, then crashes and has to start over with the boot process, only to repeat this sequence endlessly. One way to see this is to watch the Pluto on the connected host's (or VM's) USB bus. Assuming a Linux host, this can be done with

```watch -n 0.2 lsusb``` 

in a terminal. You'll see the entry for the Pluto appear for a few seconds, then disappear for a while, over and over.

Unfortunately, the Pluto doesn't stay booted long enough for any of the normal firmware update procedures to succeed. We say (somewhat imprecisely) that the Pluto is "bricked". We'll need some special recovery procedures to get back to a working state.

These are largely taken from the Analog Devices wiki:
[https://wiki.analog.com/university/tools/pluto/users/firmware](https://wiki.analog.com/university/tools/pluto/users/firmware)

## Pluto's USB Connection(s)

The primary data connection to the Pluto is on the micro-B USB connector near the center of the device, opposite the antennas. This port is marked with a USB symbol. It is OTG-capable (meaning it can be the host connecting to USB peripherals), but for our purposes we use it in the normal peripheral mode. This port enumerates with vendor ID of 0x0456 and device ID of either 0xb673 (for normal operation, including serial console and Ethernet over USB) or 0xb674 (for DFU mode). The USB port description varies in detail but always seems to start with "Analog Devices, Inc." When connected to a Linux or macOS system (and not in DFU mode) this port shows up as `/dev/ttyACM0`, or `/dev/ttyACM1` for a second device, etc.

The other USB port, near the corner of the device, is mainly for providing external power. It is marked with either an on/off switch logo or a picture of an AC adapter. Analog Devices says that there is a theoretical possibility that the Pluto might require more current than a standard USB port can supply on the other port, so they provided this port as a solution, but that they have never encountered a situation where that is needed. Rev C/D Plutos have a separate UART serial port capability on this connector, which enumerates with vendor ID of 0x0403 and device ID of 0x6015, and description of "Future Technology Devices International, Ltd Bridge(I2C/SPI/UART/FIFO)". When connected to a Linux or macOS system, this port shows up as `/dev/ttyUSB0`, or `/dev/ttyUSB1` for a second device, etc.

The Pluto has an internal port for JTAG and UART connections. The connector for this port is not installed by the factory, but it's not too hard to solder one in yourself. You will then need two adapters, a JTAG-HS3 from Digilent and a ADALM UARTJTAG from Analog Devices. The JTAG_HS3 plugs into the UARTJTAG, and a provided narrow ribbon cable connects the UARTJTAG to the user-installed JTAG connector on the Pluto circuit board. There are now two places where a micro-B USB cable can be connected between the adapters and a host computer:

- one on the free end of the JTAG-HS3, which provides JTAG connectivity, and
- one on the UARTJTAG, which provides a serial console

The JTAG port enumerates with vendor ID of 0x0403 and device ID of 0x6014, and description of "Future Technology Devices International, Ltd FT232H Single HS USB-UART/FIFO IC". When connected to a Linux or macOS system, this port shows up as `/dev/ttyUSB0`, or `/dev/ttyUSB1` for a second device, etc. When one of the Xilinx programs that talks to a JTAG device is connected to this port, its USB enumeration disappears.

The console UART port enumerates with a vendor ID of 0x10c4 and a device ID of 0xea60, and description of "Cygnal Integrated Products, Inc. CP2102/CP2109 UART Bridge Controller [CP210x family]". When connected to a Linux or macOS system, this port shows up as `/dev/ttyUSB0`, or `/dev/ttyUSB1` for a second device, etc.

If you plug in both, they will show up as `/dev/ttyUSB0` and `/dev/ttyUSB1`, or some other pair of `/dev/ttyUSBx` ports. When you have different types of serial port, as we do in this case, you can usually figure out which serial port is which by examining the output of this Linux command:

```
ls -l /dev/serial/by-id/
```

Most of our Plutos are now equipped with the JTAG connector, and we have spare connectors in stock. We have only one of the stack of adapters, though, so we can only support remote de-bricking on a single Pluto as of this writing.

## Try DFU Mode First

The Pluto implements DFU, Device Firmware Upgrade, which is a special mode in which the Pluto (as seen via USB) stops being a PlutoSDR and instead acts as a programmer device. On the USB bus, it stops enumerating this way:

```
Bus 001 Device 009: ID 0456:b673 Analog Devices, Inc. LibIIO based AD9363 Software Defined Radio [ADALM-PLUTO]
```
and instead enumerates this way:
```
Bus 001 Device 011: ID 0456:b674 Analog Devices, Inc. USB download gadget
```
Note that while the vendor ID remains `0456`, the device ID changes from `b673` to `b674` and the description changes. The new description is a lot harder to spot in a long list of USB devices!

DFU mode works through the primary USB port on the Pluto. It does not require a JTAG adapter, unless the firmware that supports transitioning to DFU mode also needs to be restored.

### Getting into DFU Mode

If you have normal access to the Pluto via an SSH session or a serial terminal, you can enter DFU mode with a command like this:
```
[pluto3:~]# device_reboot sf
```
However, if your Pluto is bricked, you don't have that access.

If you can get to a u-boot prompt, you can enter DFU mode with a command like this:
```
run dfu_sf
```
If your Pluto is bricked, you probably can't get to the u-boot prompt on the Pluto's USB port.

If you have physical access to the Pluto, there's a button. Disconnect the Pluto from any power source (USB cable), press and hold the button with a bent paperclip, and reconnect power to the Pluto before releasing the button. If things aren't too screwed up, you should now see the LED marked `LED1` on continuously, and the LED marked `Ready` off, and the Pluto should be in DFU mode.

If you're a remote user of ORI's Remote Labs, you don't have physical access to the Pluto. You can always ask us to restore a bricked Pluto by posting in the #remote_labs channel on our Slack, but it may take a while for us to get into the lab with enough free time to do it for you.

All is not lost, if the bricked Pluto is equipped with the adapters for JTAG access, and wired to a host for both ports. You will use the JTAG port (connected to the JTAG-HS3) to reset the processor, starting the boot process. Then, you will use the serial console provided on the UART port (on the UARTJTAG) to interrupt the boot process while it is still in u-boot. This will leave you at the u-boot prompt (`Pluto>`) in the serial console, where you can type the command `run dfu_sf` to place the Pluto into DFU mode.

Step by step:

1. Connect the UARTJTAG and JTAG-HS3 to the Pluto. Or, find out that they are already connected and to what computer in the Remote Lab, and skip ahead two steps.
1. Connect a USB cable from the JTAG-HS3 to a host computer capable of running Vivado.
1. Connect a USB cable from the UARTJTAG to a host computer capable of serial terminal emulation (`screen`, or any other program you prefer). These can be the same computer or two different ones.
1. On the Vivado computer, open a terminal.
1. On the terminal on the Vivado computer, get ready to use Vivado tools as usual, which will look something like this:
```source /tools/Xilinx/Vivado/2022.2/settings64.sh```
1. On the terminal on the Vivado computer, type `xsct` and be patient, waiting for it to start up and give you a prompt.
1. On the terminal on the Vivado computer, type `connect` and again be patient, waiting for it to launch a `hw_server` and connect to it. This opens a JTAG connection through the JTAG-HS3 and the UARTJTAG.
1. On the terminal on the Vivado computer, type `target 2`. This sets the first CPU core of the Pluto as the current target for commands.
1. On the other computer, run your terminal emulation program. This might look something like this:
```screen /dev/ttyUSB0 115200```
1. Back on the Vivado computer, type `rst` and immediately switch to the terminal computer and start hitting any key rapidly. The space bar is a good choice. You should see some messages go by, including u-boot messages, and then a u-boot prompt.
1. When you see that the terminal session is stopped at a u-boot prompt, you might need to hit return to clean out any extra keystrokes you rapidly typed.
1. On the terminal computer, type `run dfu_sf`. If you don't see any errors, the Pluto should finally be in DFU mode. Hurray!

The above procedure should always work if your Pluto problem is the same one I described at the beginning of this article, where the Pluto is well on the way to being booted up before crashing. If you have a problem that stops the Pluto earlier in the startup process, before it is fully running u-boot, this procedure will fail.

If you can't get a u-boot prompt following the above steps, the u-boot partition is probably corrupted and you need to reload it using JTAG. The procedure for this is not that well documented and it has changed over the years. The best and most up-to-date summary I've found is in this forum thread, which unfortunately is about somebody who has failed to make the procedure work, and no final working solution is arrived at before the thread goes silent: [https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://ez.analog.com/adieducation/university-program/f/q-a/588710/unbricking-plutosdr-in-2024&ved=2ahUKEwimr-P87duQAxUnMEQIHfFREAMQFnoECBgQAQ&usg=AOvVaw1oIRYBd6JuZCxIr3tUxvOj](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://ez.analog.com/adieducation/university-program/f/q-a/588710/unbricking-plutosdr-in-2024&ved=2ahUKEwimr-P87duQAxUnMEQIHfFREAMQFnoECBgQAQ&usg=AOvVaw1oIRYBd6JuZCxIr3tUxvOj)

One idea worth trying, which I have not yet tried, is to use an older version of Vivado, old enough to include the command `xmd`. The original debricking script `run.tcl` is designed to be run with `xmd -tcl run.tcl`, where the script `run.tcl` comes in the `plutosdr-jtag-bootstrap-<firmware version>.zip` file provided with each release of firmware for the Pluto. It seems possible that the script might still work if you had an environment with `xmd` support.

### First Steps in DFU Mode

Once the Pluto is in DFU mode, we interact with it using a program called `dfu-util`. It may already be installed on your host system (typically, on Linux) or you may need to install it using your package manager (such as HomeBrew on macOS). This program is not specific to the Pluto.

First, see what DFU devices dfu-util can see. The `-l` command line flag lists them.

```
kb5mu@pisdr:~ $ dfu-util -l
dfu-util 0.11

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2021 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

dfu-util: Device has DFU interface, but has no DFU functional descriptor
Deducing device DFU version from functional descriptor length
dfu-util: Cannot open DFU device 0456:b674 found on devnum 44 (LIBUSB_ERROR_ACCESS)
```

Oops, that's wrong. The important clue here is the error code, `LIBUSB_ERROR_ACCESS`. That means you don't have permission. Disregard the partial results, and solve the permission problem. The easy way is to use `sudo`:

```
kb5mu@pisdr:~ $ sudo dfu-util -l
dfu-util 0.11

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2021 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Found DFU: [0456:b674] ver=0221, devnum=47, cfg=1, intf=0, path="1-1.3", alt=4, name="spare.dfu", serial="UNKNOWN"
Found DFU: [0456:b674] ver=0221, devnum=47, cfg=1, intf=0, path="1-1.3", alt=3, name="uboot-env.dfu", serial="UNKNOWN"
Found DFU: [0456:b674] ver=0221, devnum=47, cfg=1, intf=0, path="1-1.3", alt=2, name="uboot-extra-env.dfu", serial="UNKNOWN"
Found DFU: [0456:b674] ver=0221, devnum=47, cfg=1, intf=0, path="1-1.3", alt=1, name="firmware.dfu", serial="UNKNOWN"
Found DFU: [0456:b674] ver=0221, devnum=47, cfg=1, intf=0, path="1-1.3", alt=0, name="boot.dfu", serial="UNKNOWN"
```

That's better. Now we have confirmed that dfu-util can see the four "partitions" on the Pluto: firmware, boot, uboot-env, and uboot-extra-env, plus a spare.

The other way to solve the permissions problem would be to set up a udev rule to grant access permissions. This would eliminate the need for `sudo` in this particular context, which is good from a security perspective and saves some typing, but it's very easy to forget about that udev rule when you switch to a different host computer. Then you'll have to understand and solve the permission problem all over again on the new computer.

### Start with a Known-Good Set of DFU Images

We'll restore the Pluto to an official Analog Devices build, just to make sure everything is going to work. Go to the GitHub releases page at [https://github.com/analogdevicesinc/plutosdr-fw/releases](https://github.com/analogdevicesinc/plutosdr-fw/releases) and pick a release. Unless you know a reason to pick a particular release, you might as well pick the latest one (v0.39 as of this writing). Scroll down to the `Assets` section and download the zip file with a name like `plutosdr-fw-<version>.zip`. Unzip it, and `cd` into the directory containing the files.

### Re-establishing Sanity by Writing the DFU Partitions

Now that we're in DFU mode, we can just load everything and put the Pluto back into its factory-fresh state.

```
sudo dfu-util -a firmware.dfu -D ./pluto.frm
sudo dfu-util -a boot.dfu -D ./boot.dfu
sudo dfu-util -a boot-env.dfu -D ./boot-env.dfu
```

For a complete transcript of what that looks like, check the wiki page mentioned near the top of this document. The `-a` argument tells it which partition to update, and the `-D` argument tells it to download the specified local file into the Pluto. You probably need to do all three, in the order listed. You might want to try doing just the first one if you were able to get to a u-boot prompt, on the theory that the other two partitions are probably fine. Or just go ahead and do all three.

If all goes well, the Pluto is reloaded with good firmware but still in DFU mode. To exit DFU mode from here, you can add the `-R` command line flag to any valid dfu-util command. There doesn't seem to be any way to use just the -R flag by itself.

```
sudo dfu-util -R -a boot-env.dfu -U ./junk-copy-of-boot-env.dfu
```

I've added the `-R` flag to a harmless command, that copies the smallest partition from the Pluto to your host (`-U`).

### Check the Results

In a terminal on the host connected to the Pluto's primary USB port, run `lsusb` to see that we're back out of DFU mode.

```
Bus 001 Device 009: ID 0456:b673 Analog Devices, Inc. LibIIO based AD9363 Software Defined Radio [ADALM-PLUTO]
```

Check that the Pluto is making available its USB serial port:

```
ls -lart /dev/ttyACM*
```
you should see something like this:
```
crw-rw---- 1 root dialout 166, 0 Nov  3 08:01 /dev/ttyACM0
```

Connect to the Pluto's serial console. On Linux or macOS, use `screen` with the serial port you just identified and the standard baud rate:

```
screen /dev/ttyACM0 115200
```

You'll probably have to hit Enter to get the login banner:

```
Welcome to Pluto
pluto login: root
Password:
```

Log in as `root` with password `analog`.

```
Welcome to:
______ _       _        _________________
| ___ \ |     | |      /  ___|  _  \ ___ \
| |_/ / |_   _| |_ ___ \ `--.| | | | |_/ /
|  __/| | | | | __/ _ \ `--. \ | | |    /
| |   | | |_| | || (_) /\__/ / |/ /| |\ \
\_|   |_|\__,_|\__\___/\____/|___/ \_| \_|

v0.39
https://wiki.analog.com/university/tools/pluto
# 
```

### Reconfigure the Pluto

We've wiped out much of the configuration of the Pluto by loading `boot-env.dfu` (unless you skipped that step). This includes the host name and static IP address settings. If you were using custom settings, as we generally do, you'll need to put them back.

The easiest way is to edit the file named `config.txt` in the mass storage volume on the Pluto, which may be mounted automatically on your host system. For instance, on my Raspberry Pi it is `/media/kb5mu/PlutoSDR/config.txt`. If you have multiple Plutos connected, you'll see PlutoSDR, PlutoSDR1, PlutoSDR2, etc. and have to pick the right one. Edit `config.txt` and it'll be obvious how to make the necessary changes.

The non-obvious part is that you MUST now __eject__ the mass storage device. Otherwise, the changes you made to config.txt will be lost. On my system, this is
```
sudo eject /dev/sda
```
If you have multiple devices connected, it might be sda, sdb, sdc, etc. If in doubt, you can physically disconnect all devices other than the one you're operating on.

When you eject the device, the Pluto should reboot with the new settings. If you're talking to it over the network, you might have to adjust your connection accordingly.

### Re-Install Custom Firmware

At this point you will probably want to re-install some version of your custom firmware. If you install the same version that bricked the Pluto, it will likely brick it again, but that's OK, since you now know exactly how to restore it. You might also decide to install the previous working version, or a newer purportedly-fixed version. Use your normal firmware installation procedure. For example, you can use the mass storage device again: write your new firmware into `pluto.frm` in the mass storage volume, and then __eject__ the device.

If you anticipate a lengthy struggle with firmware that may brick your Pluto, you might find it more convenient to download the firmware versions under test to the Pluto's RAM, rather than installing each version to flash and risking another bricking. See [https://wiki.analog.com/university/tools/pluto/devs/reboot](https://wiki.analog.com/university/tools/pluto/devs/reboot) for details.