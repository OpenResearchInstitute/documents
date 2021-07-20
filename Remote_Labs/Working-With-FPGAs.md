# ORI Remote Labs: Working With FPGAs

DRAFT 2021-07-19 Paul Williamson KB5MU

The remote labs operated by Open Research Institute support development of open source projects using certain Xilinx FPGAs.

You can do much of the development work at home on your own computer, assuming you have enough disk space to spare and a reasonably modern machine. The Xilinx development tools are free to download and use for a subset of basic operations. When you need to use certain advanced components, or when you need to synthesize a bitstream for larger devices, you need a paid-up license. ORI makes available a "floating license" you can use on open source projects. A floating license is one that can be used on any computer anywhere, but only one computer at a time. In order to enforce this restriction, there's a way to obtain the license over the Internet, and release it when you're done actively using it. This document will cover how to set that up.

Another expensive thing you will need to complete your FPGA project is access to a development board for a suitable device. The ORI Remote Lab in San Diego has two development boards set up and available for use: a ZCU106 (Zynq UltraScale+™ MPSoC) and a ZC706 (Zynq-7000 SoC). The ZC706 is equipped with an Analog Devices ADRV9371 wideband RF transceiver board. Each development board is connected to dedicated USB ports associated with a particular Linux virtual machine (VM) running on the lab's high-performance PC. Similar equipment is expected to be available at the Remote Lab East. This document will cover how to get started using the development board with the VM.

## The Floating Vitis (Vivado) License

Xilinx has several different ways to manage licenses for their FPGA tools. We use what's called a "floating license" that can be checked out from a computer called a license server over the network. In a typical corporate environment, the license server would generally be located somewhere on the corporate network, and getting a connection to it would be as simple as plugging your computer into the network. Since we are spread around the world, we have to go to a bit more trouble.

In order to get a secure connection to the license server over the Internet, we use SSH (the secure shell program) to create TCP tunnels from your machine (the one you're running the Xilinx tools on) and the license server. A tunnel forwards data between a certain port number on one machine and a port number (same or different) on another machine. In this case, we need to connect two ports, and by convention we will use the same port numbers on both ends: 2100 and 2101. In order to authenticate these connections, we use your SSH public keys registered with Github.

To set things up:

1. On the computer (or VM) where you intend to use Xilinx tools, log in to the account you intend to use. I'm going to assume this is a Linux computer, but procedures for Windows should be similar. (Xilinx tools don't support macOS.)

2. See if you have an SSH key pair already. By default, it will be a pair of files named `~/.ssh/id_rsa` (that's the private key) and `~/.ssh/id_rsa.pub` (that's the public key). You may also have `~/.ssh/id_ed25519` and `~/.ssh/id_ed25519.pub`, which are more modern. If you have the ED25519 files, we will use them. If not, create them by typing

	```
	ssh-keygen -t ed25519
	```

	Hit enter to accept the default file name. At the next two passphrase prompts, you can just hit enter (for maximum convenience) or enter a secret phrase, which you'll have to type in each time you use the key (for better security). Don't forget your passphrase!

3. Now that you have a `~/.ssh/id_ed25519.pub` file, copy its contents. Be sure you're copying the file with the `.pub` extension.

4. Log into your GitHub account on the web. If you don't have one, create one.

5. On the GitHub page, click on your avatar (in the upper right corner) and select Settings.

6. In the left column, click on "SSH and GPG keys".

7. Click on "New SSH key".

8. Enter a title to help you remember what this key is about.

9. Paste the key you copied above into the Key field.

10. Finally, click the "Add SSH key" button. Unless you get an error message, you now have an SSH public key on file with GitHub, which is readable by anyone. (Or you have one more than before, that's fine too.)

11. If you expect to work from more than one computer or more than one account, you can either copy the `~/.ssh/id_ed25519*` files (both public and private) to all the other computers, or else repeat the above procedure for all the other computers. 

12. Next you need to send your GitHub user name in to ORI and request access to the Xilinx floating license. If we don't already know what you're planning to do with it, please provide a brief explanation. Choose one of the following options:

    A. If you're also requesting access to the remote lab, include your GitHub user name in the email you send to sandiego-lab@openresearch.institute.
    
    B. Or, if you're already on the Phase 4 Ground Slack workspace, add your GitHub user name to this [thread on Slack](https://phase4ground.slack.com/archives/C2W37HSLX/p1595566930376800).
    
    C. Or, just send an email to sandiego-lab@openresearch.institute.
    
13. Create a script file somewhere you'll be able to execute it from, such as `/usr/local/bin/license_vivado.sh`. Model your script file on this one:

	```
	#!/bin/bash
	
	# connect to server
	ssh -f -N -L 127.0.0.1:2100:127.0.0.1:2100 -L 127.0.0.1:2101:127.0.0.1:2101 XXXXXXX@flexlm-server.openresearch.institute
	
	# report status on the tunnels
	lsof -i :2100
	
	# set the license server location
	export XILINXD_LICENSE_FILE=2100@127.0.0.1
	
	# start vivado
	. /tools/Xilinx/Vivado/2020.2/settings64.sh
	/tools/Xilinx/Vivado/2020.2/bin/vivado
	
	# drop the tunnels to the license server
	kill -HUP `lsof -t -i :2100`
	
	# report status on the tunnels (silent if the kill succeeded)
	lsof -i :2100
	```

	You'll need to change `XXXXXXX` to your GitHub user name. Depending on where you installed your Xilinx tools, you may need to change that path in two places. Or, if you want to run Vitis instead of Vivado, change that. Etc.

	Note that this script keeps the tunnel open for the entire time you're running the Xilinx tool, but closes it down immediately after you exit the tool. Please do exit the tool as soon as you're done using it, to free up the floating license for other users. Please don't use this script if you're working in the Xilinx tool in a way that does not require the license.

14. Make the script executable, like this:
	```
	chmod +x /usr/local/bin/license_vivado.sh
	```

15. Once you've been notified that your account is set up, try running the script.

You should see something more or less like this:
```
COMMAND   PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
ssh     21850 kb5mu    4u  IPv4 181890      0t0  TCP localhost:2100 (LISTEN)

****** Vivado v2020.2 (64-bit)
  **** SW Build 3064766 on Wed Nov 18 09:12:47 MST 2020
  **** IP Build 3064653 on Wed Nov 18 14:17:31 MST 2020
    ** Copyright 1986-2020 Xilinx, Inc. All Rights Reserved.

start_gui
```

The first two lines are a report about the tunnels being set up. The rest are the startup messages from Vivado. You should then see the Vivado GUI window appear. (More on that later.)

You should leave this window open while you're working with Vivado.

Then later, when you exit Vivado, you should see a message from Vivado, like this:
```
INFO: [Common 17-206] Exiting Vivado at Sun Jul 18 23:12:27 2021...
```

### Possible Problems

After you exit Vivado, you should not see another report about tunnels; if you do, it means that your tunnels were not torn down properly.

When you start up your script, you might see these messages:

```
bind: Address already in use
channel_setup_fwd_listener_tcpip: cannot listen to port: 2100
bind: Address already in use
channel_setup_fwd_listener_tcpip: cannot listen to port: 2101
Could not request local forwarding.
```

That means that tunnels were already set up. These could be your tunnels from a prior session that was improperly terminated, or they could be tunnels belonging to another user. If those messages are immediately followed by a tunnel report, the tunnels are yours:

```
bind: Address already in use
channel_setup_fwd_listener_tcpip: cannot listen to port: 2100
bind: Address already in use
channel_setup_fwd_listener_tcpip: cannot listen to port: 2101
Could not request local forwarding.
COMMAND   PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
ssh     22919 kb5mu    4u  IPv4 193958      0t0  TCP localhost:2100 (LISTEN)
```

If the tunnels are yours, you can go ahead and use Vivado; they will be torn down normally at the end of your session.

If the tunnels belong to another user, you should try to coordinate with them (e.g., on the remote-labs channel on Slack). You can't both be using the same floating license at the same time. If and when this becomes a routine problem, let us know; ORI may be able to obtain additional licenses. In the event you can't contact the other user, a remote lab administrator can solve the conflict. 

### Updating Your SSH Public Keys

If you need to update the SSH public keys you use, go ahead and register the new key(s) on GitHub as before. Before you can use the new key(s) with the license server, you will need to notify us so we can update the license server.

This process could be automated if it turns out to happen very often. Let us know if you anticipate changing your SSH keys frequently.

## Using VMs in the Remote Lab

Each remote lab has a powerful PC that's configured with Unraid as a hypervisor to run virtual machines, and FPGA development boards connected to that machine. Typically an FPGA development board has an Ethernet interface and two USB interfaces.

The Ethernet interface is configured with a fixed IP address and a domain name like `zc706.sandiego.openresearch.institute`. It can be accessed by any computer on the remote lab's private LAN (including your computer if you have Wireguard set up and enabled). The function of this interface depends on what code you have running on the processor core in the FPGA on the dev board. 

One USB interface is based on an FTDI chip and implements the JTAG interface for programming and debugging on the dev board, sometimes called a "Digilent JTAG cable" in the documentation. The other USB interface is based on a Cygnal Integrated Products UART Bridge, which provides one or four UART interface(s) that can be used for any purpose by the programs you create on the dev board. Both of these USB interfaces are connected to a small USB hub, and that hub is connected to a USB port in the PC that has its own dedicated USB controller. That USB controller is mapped exclusively to the VM corresponding to that development board. This setup allows the software running in the VM to treat the USB devices as if they were ordinary local hardware.

Each development board has many other interfaces, and may be connected to additional hardware. These can be connected up in whatever way is needed for your development purposes. Contact the lab administrators to discuss your needs. The specifics of these interfaces are beyond the scope of this document.

In order to use the equipment in the remote labs, you must first set up access to the labs. This is covered in detail in [Setting Up for Remote Access to ORI Labs](https://github.com/phase4ground/documents/blob/master/Remote_Labs/ORI-Lab-User-Setup.md). This involves some setup on your own computer, and an email sent to sandiego-lab@openresearch.institute. When you send that email, or later when the need arises, include a request to be set up for access to whichever VM you need to use. We will set you up with a login on the VM.

At the San Diego lab, the overall PC is called Chonc, and the VMs for FPGA development are called chococat and keroppi. Chococat is connected to the ZC706 dev board, which is equipped with an Analog Devices ADRV9371 transceiver board. It has a single-port Cygnal UART bridge that shows up as /dev/zc706_uart1. Keroppi is connected to the ZCU106 dev board, which has a four-port Cygnal UART bridge (/dev/zcu106_uart1 through /dev/zcu106_uart4).

### Vivado Remote or Local?

Many Vivado operations can be completed without access to the hardware. These can be done on your local computer. You may nonetheless want to run some procedures on a VM in the lab PC, because it's very probably much faster than your home PC. For instance, a large synthesis operation might be quite a bit quicker to run on the VM.

Other Vivado operations do require access to the hardware. The most obvious way to handle this is to run Vivado on the VM in the lab PC, which has direct access to the hardware. In this case, you'd use your local computer as a way to remotely view the GUI screen of the VM. That works, but is subject to certain limitations. The virtual screen size of the VM is limited to 1920x1080, and operating a GUI through remote access can be a bit clunky, especially on slow or unreliable Internet connections.

A better way may be to split Vivado into two pieces. The only part that actually requires access to the hardware is called `hw_server`. It's possible to run hw_server on the VM, and the rest of Vivado on your local computer. In this case, you'd have a local GUI running on your own computer like any other program, and only rely on the network for communication with hw_server. This is likely to be much smoother and more reliable than running the whole Vivado GUI through screen sharing.

Details on setting up for split operation with hw_server running on the VM will be provided here as soon as we figure them out.

### Vivado Licenses on VMs

The remote lab VMs for FPGA development do not have dedicated licenses for the Xilinx tools. Use the procedures described earlier in this document for obtaining a floating license when you need to use the tools in a way that requires a license. Please do use the suggested script, to help ensure that the floating license is not tied up when you're not using it.

Note that running just hw_server on the VM does not require a license. You may or may not require a license for your local computer when accessing the remote hw_server, depending on what you're doing. Generally you will not need a license for operating the dev board remotely, but you will need a license if you need to resynthesize your FPGA bitstream.

### SSH Access to the VMs

You can use SSH to log in to the VM. The document [Setting Up for Remote Access to ORI Labs](https://github.com/phase4ground/documents/blob/master/Remote_Labs/ORI-Lab-User-Setup.md) shows how to set this up in your `~/.ssh/config` file.

The SSH configuration can also be used to transfer files to and from the VM via SCP (secure copy). Examples:

```
scp w1abc@chococat:~/some_directory/filename.log .
scp myfile.c w1abc@chococat:~/somedirectory/myfile.c
```

You can omit the username (w1abc@ in the examples above) if your local username is the same as your username on the VM.

### GUI Access to the VMs

The document [Setting Up for Remote Access to ORI Labs](https://github.com/phase4ground/documents/blob/master/Remote_Labs/ORI-Lab-User-Setup.md) covers several ways to set up for running the GUI desktop on a remote lab VM.

That document mentions, but does not recommend, setting up screen sharing using X11 forwarding, as detailed in document [Setting Up for X11 Forwarding](https://github.com/phase4ground/documents/blob/master/Remote_Labs/ORI-Lab-X11-Setup.md). It seems tempting to use X11 forwarding to run Vivado, especially if you have a large screen on your local computer, because it doesn't impose any limits on virtual screen size. The TigerVNC server setup on the VMs is limited to a virtual screen size of 1920x1080, which is pretty small for the information-rich displays in Vivado. Unfortunately, there are parts of Vivado that do not seem to work properly with X11 forwarding. In particular, the online help system doesn't work at all. We don't know why. Feel free to try using X11 forwarding with Vivado for yourself. If it works well enough for the parts of Vivado you need to use, it may be worth the trouble. Let us know if you learn any tricks for using Vivado successfully with X11 forwarding.

### UART Access on the VMs

It's common to use a UART on the dev board to output test results or to control the application running on the dev board. Sometimes all you need at the other end is a dumb terminal emulation. On the VMs you can use `screen` or `minicom` for this.

Screen is the simpler of the two options. All you need to do is put the device name and the baud rate on the command line, like this:

```
screen /dev/zc706_uart1 115200
```

To exit the terminal emulation, hit `Control-A` and then `k`, then `y` to confirm. That's all you need to know for basic operation; you can use `man screen` to learn more.

Minicom is more full-featured text-based terminal emulation program. Read `man minicom` to learn more.


