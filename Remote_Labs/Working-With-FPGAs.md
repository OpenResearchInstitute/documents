# ORI Remote Labs: Working With FPGAs

DRAFT

The remote labs operated by Open Research Institute support development of open source projects using certain Xilinx FPGAs.

You can do much of the development work at home on your own computer, assuming you have enough disk space to spare and a reasonably modern machine. The Xilinx development tools are free to download and use for a subset of basic operations. When you need to use certain advanced components, or when you need to synthesize a bitstream for larger devices, you need a paid-up license. ORI makes available a "floating license" you can use on open source projects. A floating license is one that can be used on any computer anywhere, but only one computer at a time. In order to enforce this restriction, there's a way to obtain the license over the Internet, and release it when you're done actively using it. This document will cover how to set that up.

Another expensive thing you will need to complete your FPGA project is access to a development board for a suitable device. The ORI Remote Lab in San Diego has two development boards set up and available for use: a ZCU106 (Zynq UltraScale+™ MPSoC) and a ZC706 (Zynq-7000 SoC). The ZC706 is equipped with an Analog Devices ADRV9371 wideband RF transceiver board. Each development board is connected to dedicated USB ports associated with a particular Linux virtual machine (VM) running on the lab's high-performance PC. Similar equipment is expected to be available at the Remote Lab East. This document will cover how to get started using the development board with the VM.

In addition, the San Diego lab has an ADALM-PLUTO (aka PlutoSDR) from Analog Devices connected to one of the VMs. The Pluto is a lower-priced platform that shares many characteristics with the target platforms from Xilinx. The idea here is that individual developers may already be familiar with development on the Pluto, and may have one available for local experimentation. It may be easier to get started on Remote Lab projects using the familiar Pluto, and only then transition to the Xilinx platforms.

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

Each remote lab has a powerful PC that's configured with Unraid as a hypervisor to run virtual machines, and FPGA development boards connected to that machine. Typically a Xilinx FPGA development board has an Ethernet interface and two USB (serial port) interfaces. (The Pluto board does not have a physical Ethernet interface, but its one USB interface can provide network connectivity.)

The Ethernet interface is configured with a fixed IP address and a domain name like `zc706.sandiego.openresearch.institute`. It can be accessed by any computer on the remote lab's private LAN (including your computer if you have Wireguard set up and enabled). The function of this interface depends on what code you have running on the processor core in the FPGA on the dev board. 

One USB interface is based on an FTDI chip and implements the JTAG interface for programming and debugging on the dev board, sometimes called a "Digilent JTAG cable" in the documentation. The other USB interface is based on a Cygnal Integrated Products UART Bridge, which provides one or four UART interface(s) that can be used for any purpose by the programs you create on the dev board. Both of these USB interfaces are connected to a small USB hub, and that hub is connected to a USB port in the PC that has its own dedicated USB controller. That USB controller is mapped exclusively to the VM corresponding to that development board. This setup allows the software running in the VM to treat the USB devices as if they were ordinary local hardware.

Each development board has many other interfaces, and may be connected to additional hardware. These can be connected up in whatever way is needed for your development purposes. Contact the lab administrators to discuss your needs. The specifics of these interfaces are beyond the scope of this document.

In order to use the equipment in the remote labs, you must first set up access to the labs. This is covered in detail in [Setting Up for Remote Access to ORI Labs](https://github.com/phase4ground/documents/blob/master/Remote_Labs/ORI-Lab-User-Setup.md). This involves some setup on your own computer, and an email sent to sandiego-lab@openresearch.institute. When you send that email, or later when the need arises, include a request to be set up for access to whichever VM you need to use. We will set you up with a login on the VM.

At the San Diego lab, the overall PC is called Chonc, and the VMs for FPGA development are called chococat and keroppi. Chococat is connected to the ZC706 dev board, which is equipped with an Analog Devices ADRV9371 transceiver board. It has a single-port Cygnal UART bridge that shows up as /dev/zc706_uart1. Keroppi is connected to the ZCU106 dev board, which has a four-port Cygnal UART bridge (/dev/zcu106_uart1 through /dev/zcu106_uart4). Keroppi is also connected to the Pluto.

### Vivado and the hw_server

When Vivado needs access to physical hardware, it uses a separate process called `hw_server`. Vivado finds its hw_server process through a TCP port. In the simplest setup, the hw_server process runs on the same host as Vivado and uses the default port number, 3121. Vivado calls this setup a "local server". Vivado can also find a hw_server process running on a different host and/or a different port number, and it calls that a "remote server". There is really nothing special about a local server; it's just a shortcut.

The hw_server process necessarily runs on the host that's physically connected to the target hardware. For the platforms in the Remote Lab, that host is a virtual machine. The hardware connection to any given target is (and must be) dedicated to one particular remote machine.

In a perfect world, the hw_server would be a permanent process running on the VM in the Remote Lab, and users would find it available when needed. In practice, developers may need to actively manage the hw_server, perhaps restarting it when problems arise with the target. When it's your turn to use the target hardware, you will need to start a hw_server for it. When you're done, you should stop your hw_server so that the next user can run their own. Two hw_servers cannot share the same target hardware. Multiple users can access the same hw_server, but only one of them can actually use the attached hardware platform at any given time.

In case only one hardware platform is connected to a VM, by convention we run the hw_server on the default port 3121. It can be thought of as a local server for instances of Vivado running on the VM. This is the case on chococat in San Diego, since only the ZC706 is connected to chococat.

If more than one hardware platform is connected to the VM, things are a little more complicated. This is the case on keroppi in San Diego, since that VM is connected to both the ZCU106 and the Pluto. By default, the hw_server will attach to and own every hardware platform it can find. That's fine if one developer is working with all the hardware, as would be the case in a non-remote lab situation. In our sitation, it's more often the case that one developer is using one hardware platform and a different developer is using another hardware platform. The best way to handle that is to restrict each hw_server process to use only one of the hardware platforms. Each developer manages the hw_server associated with the target hardware they are using. In order to have multiple hw_server processes running on the VM simultaneously, each hw_server will need its own port number.

Below are recommended command lines to use to start hw_server. First, you'll need to _source_ the settings script for the version of Vivado you're using:

```
. /tools/Xilinx/Vivado/2019.1/settings.sh
```

To run hw_server on chococat, where there is only one hardware platform connected, and leave hw_server connected to your shell, run simply:
```
hw_server
```
and leave that shell open while you need the hw_server. Hit ^C to stop it when you're done.

If you prefer to have hw_server run in the background on chococat, then run:
```
hw_server -d
```
In that case, to stop the hw_server you'll need to kill the process. If you have just the one hw_server process, the easy way is to run:
```
killall hw_server
```
But if you have multiple hw_server processes and only want to kill one, you'll need to find out its process ID. Run:
```
ps aux | grep hw_server
```
and find the process ID in the second field of the result. Like this:
```
kb5mu     2611  0.0  0.0 149292  5140 ?        Ssl  17:14   0:00 /tools/Xilinx/SDK/2019.1/bin/unwrapped/lnx64.o/hw_server
```
where the process ID is 2611. Then use that number like this:
```
kill 2611
```

If you need to kill a hw_server that another developer left running, here's how:
```
sudo kill -9 2611
```

On keroppi, we let the Pluto use the default port. To start the hw_server for the Pluto on keroppi, and leave hw_server connected to your shell, run:
```
hw_server -s tcp::3121 -e "set jtag-port-filter Digilent"
```
Notice that there are two colons between "tcp" and the port number. You can still add the `-d` flag if you want to run in the background. The `-e "set jtag-port-filter Digilent"` part restricts hw_server to only use hardware targets with the string "Digilent" in their names. That includes the Pluto and does not include any of our Xilinx boards.

To start the hw_server for the ZCU106 on keroppi, and leave hw_server connected to your shell, run:
```
hw_server -s tcp::3122 -e "set jtag-port-filter Xilinx" -p 4000
```
Notice there are two colons between "tcp" and the port number. You can still add the `-d` flag if you want to run in the background. The `-e "set jtag-port-filter Xilinx"` part restricts hw_server to only use hardware targets with the string "Xilinx" in their names. That includes the ZCU106 and does not include the Pluto. The `-p 4000` part tells hw_server to set up its software debugger (GDB) ports starting from port 4000, instead of the default port 3000, which would conflict with the ports used by the Pluto's hw_server. TBD: how to tell GDB to use these port numbers.

In Vivado when you open a new hardware target, you'll need to select the right hw_server. For the ZC706, if Vivado is running on chococat, you can just choose the "local" server. Otherwise, connect to a "remote" server. The host name can be "chococat" or "keroppi" if Vivado is running on any Remote Lab machine or VM. At home if you're running WireGuard, the host name can be "chococat.sandiego.openresearch.institute" or "keroppi.sandiego.openresearch.institute". If you're at home and not running WireGuard, then you'll have to set up an SSH tunnel. (SSH tunnel details are left as an exercise for the reader; WireGuard is the recommended solution.) Then the port number is 3121 (the default) unless you want to use the ZCU106 on keroppi, in which case it is 3122.

### Vivado Remote or Local?

Aside from the hw_server process described in the previous section, Vivado does not necessarily need to run on any particular computer. You can run Vivado in the Remote Lab VM (chococat or keroppi), and most of us do that, but you can also run Vivado on your own local computer.

In theory, the VM in the lab PC should run Vivado with very fast performance, probably faster than your home PC unless you have the latest and greatest hardware. In practice, the VM seems to be slower than it should be, and we're still trying to figure out why.

In order to run Vivado on the lab VM, you need a way to bring Vivado's GUI to your local screen. The recommended way to do that is with VNC. This is covered in detail in [Setting Up for Remote Access to ORI Labs](https://github.com/phase4ground/documents/blob/master/Remote_Labs/ORI-Lab-User-Setup.md). This will work for you as long as you have pretty fast Internet connectivity.

It's theoretically possible to run the X11 server on your local machine instead of remoting the whole screen with VNC. In our experience, that doesn't work with all of the features of Vivado. In particular, the help and documentation view fails.

If network performance is an issue and/or you want to have a very large high-resolution Vivado screen, the best way is probably to run Vivado on your local machine and only run the hw_server on the VM, as described in the previous section. This is likely to be much smoother and more reliable than running the whole Vivado GUI through screen sharing. (We don't have much experience with this yet, so there may be disadvantages we have yet to discover.)
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

### Working on the zc706 and attached ADRV9371 with the Analog Devices HDL Reference Design

These instructions are about how to use the zc706 with attached ADRV9371. Analog Devices provides an HDL reference design and petalinux support in order to allow you to incorporate your custom cores into the design and get them working over the air.

#### Get set up to use Vivado 2021.1
```
source /tools/Xilinx/Vivado/2021.1/settings64.sh
```
Make sure you do all the steps involving Vivado in a terminal where you have sourced the right settings64.sh.

Make sure you have a Vivado license available before proceeding. If you're using ORI's floating license, that means setting up the SSH tunnel to the license server and setting the environment variable `XILINXD_LICENSE_FILE` appropriately, in that same terminal.

#### Clone the Repository with all the HDL Elements
Clone the _appropriate_ branch of this repository. Check the README.md or check on Slack to get the right branch. Make sure you get submodules. 

```
git clone --branch adrv9371-zc706-dvbs2-integ --single-branch --recurse-submodules -j8 https://github.com/phase4ground/adi_adrv9371_zc706.git
```
(about 7 seconds and 26MB of disk space)

Navigate to this directory: adi_adrv9371_zc706/hdl/projects/adrv9371x/zc706

Assuming all the issues at: https://github.com/phase4ground/adi_adrv9371_zc706/issues/1 are cleared up, type make. 

```
make
```
(about 2.5 hours, 930MB used so far)

Open the resulting project `adi_adrv9371-zc706/hdl/projects/adrv9371x/zc706/adrv9371x_zc706.xpr` in Vivado. Export bitstream and xsa file (`File->Export->Export Bitstream File...` and `File->Export->Export Hardware...`. Choose the `Include bitstream` option when you export hardware, even though you have a separate bitstream file too.). You will need them to build petalinux and boot the zc706.

#### Build Petalinux with meta-adi

Following the instructions that start at this link: https://github.com/analogdevicesinc/meta-adi/tree/master/meta-adi-xilinx

Source Petalinux 2021.1.

Optionally, make a separate directory for your Petalinux and cd to that directory.

```
petalinux-create -t project --template zynq --name <project name>
```
This sets up the project directory structure for the right FPGA target.

```
git clone https://github.com/analogdevicesinc/meta-adi
```

This fetches everything needed to add the yocto layers of meta-adi to petalinux. We need this, otherwise we do not have the right device tree for all the HDL in the Analog Devices reference design. 

```
cd <project name>
petalinux-config --get-hw-description <path to .xsa file exported from Vivado>
```
When running the petalinux-config --get-hw-description=<path to xsa file>, a configuration menu will come up. Go to Yocto Settings->User layers and add the meta-adi-xilinx and meta-adi-core layers. These are from the meta-adi directory clone. Add core first, and xilinx second. Use an absolute path, not one starting with a tilde (~). Then hit SAVE and take the default location. Go to DTG Settings and set MACHINE_NAME to `zc706`.

If you want the target to have its official fixed IP address, and you should, in petalinux-config go to `Subsystem AUTO Hardware Settings` and choose `Ethernet Settings`. Deselect `Obtain IP address automatically` by cursoring to it and hitting the space bar. Then set the `Static IP address` to `10.73.1.9`, the `Static IP netmask` to `255.255.255.0`, and the `Static IP gateway` to `10.73.1.1`. Hit SAVE and take the default location.

```
echo "KERNEL_DTB=\"<name of the dts file to use from the list in meta-adi>\"" >> project-spec/meta-user/conf/petalinuxbsp.conf
```

The echo is a fancy way of setting up the petalinuxbsp.conf file. Here's what it should look like after this command. 
```
abraxas3d@chococat:~/adi-encoder-meta-adi/integrate-iio/project-spec/meta-user/conf$ cat petalinuxbsp.conf 
#User Configuration

#OE_TERMINAL = "tmux"

KERNEL_DTB="zynq-zc706-adv7511-adrv9371"
```
We proceed with building petalinux.

```
cd build
petalinux-build
```
(21.5 minutes (depends on downloads), total usage is now up to 22GB!)

Look carefully at the last few lines of output from petalinux-build. If it says `INFO: Failed to copy built images to tftp dir: /tftpboot` then somebody else's files are probably already in the /tftpboot directory. Coordinate on Slack. As root, go there and move the other user's files and directory `pxelinux.cfg` aside into a new directory. If you still have trouble writing to /tftpboot, run `groups` in your terminal and check that you're a member of the tftp group. If not, use `sudo adduser <you> tftp` to add yourself. You'll need to close your terminal, open a new one, and re-source the Vivado and Petalinux settings scripts.

####

Boot target. Below is how to use tftpboot. I used this page https://www.instructables.com/Setting-Up-TFTP-Server-for-PetaLinux/ and the Petalinux user guide from Xilinx to set up tftpboot on Chococat with the zc706. Current default state on chococat is that the zc706 is connected over JTAG and tftpboot can be used.

Make sure there's a hw_server process running.

Monitor the serial console of the target. This may be /dev/ttyUSB1 or /dev/ttyUSB2. If you can't use either port, somebody else may have the console port open.
```
screen /dev/ttyUSB1 115200
```

Now go for the boot:
```
petalinux-package --prebuilt --fpga <location of bitfile> --force
petalinux-boot --jtag --prebuilt 2 --hw_server-url TCP:chococat:3121
```

If you get `Will not program bitstream on the target` then you might have forgotten to choose the `Include bitstream` option when you exported the XSA file.

If you get a warning about your $XTERM and `Inappropriate ioctl for device.` you can ignore it.

If you get a `Memory read error` OR `No supported FPGA device found` then type `reboot` at the serial console prompt and wait for it to finish. It won't actually reboot and return to the prompt. Then retry the `petalinux-boot` command.

Watch the messages from petalinux-boot. Make sure it confirms that it is downloading the bitstream to the target.

On the target's serial console, watch for the `Zynq>` prompt.
There may be a bunch of messages claiming that the TFTP server died. Don't worry about that. Just wait for it to stop and display the `Zynq>` prompt.

```
Zynq> setenv serverip 10.73.1.93
Zynq> setenv ipaddr 10.73.1.9 
Zynq> pxe get
Zynq> pxe boot
```
This should boot petalinux on the zc706.

Note that the IP address set with setenv at the Zync> prompt does not stick. By default, the Linux system you built will use DHCP and get its own address. You can find out what address was assigned with `ip addr` on the serial console. If you followed the recommended procedure in petalinux-config above, it should already be set to `10.73.1.9`.

#### How to Solve the Problem of Not Being Able to Select "Create Platform Project" in Vitis

Source the version of Vitis you need to work with.
Open Vitis (from the command line, say `vitis`).pla
Open the xsct console (in the Xilinx menu).

Xilinx Software Command-line Tool (XSCT) is an interactive and scriptable command-line interface to Xilinx Software Development Kit (Vitis, or Xilinx SDK). As with other Xilinx tools, the scripting language for XSCT is based on Tools Command Language, or tcl. 

The following commands are entered into the xsct console. 
```
platform create -name <name> -hw <path to the xsa file you exported from Vivado> -os linux -proc ps7_cortexa9

platform active
```

This should return the name of the platform you just created. 

```	
platform config -fsbl-elf <path to zynq_fsbl.elf>
```

Example on TFTP boot system in Remote Labs West:
```
platform config -fsbl-elf /tftpboot/zynq_fsbl.elf
```
This specifies the boot image format file option in the GUI. (I believe)
```
platform config -prebuilt-data /tftpboot/
```				
This specifies the boot components directory option in the GUI. 
	
```
platform generate
```
This builds the platform elements. 

To Do: Double check hard if there's anything else that needs to be done at this point to cover all the options in the GUI. 

#### Build a Linux App in Vitis for Petalinux

Source 2021.1 Vitis.

Start the IDE. 

Select a workspace. 

Create a new platform project. See above workaround if you can't select this menu option in the drop down or in the GUI. 

Here are the instructions if the GUI works for you.

File - new - platform project

End the filename with _plat to make it easy to distinguish between this and other files.

Select: Create from hardware specification

Add the xsa file. 

Operating systen is linux.

Processor for the zc706 is ps7_cortexa9

uncheck Generate boot components. We're going to use what we made in Petalinux.

Click finish to esetablish the preojct structure. This is captured in the .spr file. 

Click Linux on ps7_cortexa9 item to open configuration window. 

Here is where we provide necessary intofmraiton for the platform. 

The following are required: Boot image format file. Boot components directory. 

The rest of the fields are optional. 

Select the _plat file in the explorer window. 

Click hammer to build the platform elements. 

Create a new application project by clicking file - new - application project.

Click Next.

Select our platform from the list. It may say "in repository". 

Click Next.

Create a name for your project. Some recommendations: 

_app as the end of the project name.

_system as the end of the system project. 

Click Next.

Domain is linux on ps7_cortexa9, language is c, sysroot should be empty. Root FS and Kernel Image can also be left empty.

Click Next. 

Pick Hello World template and click Finish. 

Expand the src folder in the navigation window to open the helloworld.c file. (It might be hiding behind the XSCT window if you left it open.) Double-click the helloworld.c entry.
	
Right click your application project in explorer and choose Build. This will take a while as it's building the whole runtime system as well as your code.

Make sure you've booted up the linux image on the target. 

Right click application in explorer and set up a run configuration:

Run as: Run configurations. Pick "single application debug". Double click this.

You have a configuration window and now can set up a connection to the hardware target. 

Click "new" next to connection field.

Name it something memorable for you. Host, if you are on chococat, is 10.73.1.9. Port can probably be left at the default. 

Test connection. Debug problems if necessary. 

Ok to create the run config. 

Apply 

Run

Output should be visible in the console within Vitis IDE. 

To run in the debugger, click the little bug icon in the toolbar.

When you run debug, it halts at the top of the main function. You are in the debugger. You can also simply run on the target, and the code will execute and results show up in the console. 

On the target, your executable file is now in `/mnt/sd-mmcblk0p1`. You can run it from the serial console if you like.
