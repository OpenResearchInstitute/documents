# ORI Remote Labs: Working With PetaLinux Target Terminals

* [Introduction](#Introduction)
* [Booting the Target System](#booting-the-target-system)
* [Setting Up a Serial Port Based Terminal](#setting-up-a-serial-port-based-terminal)
    * [Using Screen for terminal emulation](#using-screen-for-terminal-emulation)
    * [Getting Out of Screen](#getting-out-of-screen)
    * [Troubleshooting Screen problems](#troubleshooting-screen-problems)
    * [Limitations of Screen](#limitations-of-screen)
* [Using Minicom instead of Screen](#using-minicom-instead-of-screen)
    * [Configuring Minicom](#configuring-minicom)
    * [Getting Out of Minicom](#getting-out-of-minicom)
    * [Useful Minicom Features](#useful-minicom-features)
* [Setting Up an SSH Based Terminal](#setting-up-an-ssh-based-terminal)
    * [Use of Passwords](#use-of-passwords)
    * [Use of ~/.ssh/config File](#use-of-sshconfig-file)
    * [Use of SSH Tunneling](#use-of-ssh-tunneling)

## Introduction
Our target architecture for projects such as Haifuraiya and Neptune is based on a Zync family system-on-chip (SoC) device, which features an ARM microprocessor core integrated with an FPGA fabric and other peripherals. The ARM core runs a customized embedded Linux flavor built with Xilinx tools including PetaLinux. As with any Linux system, most interaction between human users and the system is mediated by a shell running on a terminal. This document is about setting up a remote terminal for such purposes.

In a desktop system, local users rely on the attached display screen. At boot time, it displays console messages. The rest of the time, it may operate in text mode or as a graphical user interface. While the prototype target hardware does have support for a local screen, this is not the way we intend to use it. For economy and modularity and for the convenience of remote developers, we configure the embedded Linux to operate "headless", meaning there is no local display.

Lacking a local display, there are two main ways a terminal can be connected to the system: over a serial port, or over the network. Each of the hardware prototypes has one or more serial port interfaces, and one or more Ethernet interfaces. The serial port interfaces are connected to USB serial ports which are dedicated to the virtual machine (VM) used for development for that target. One of the Ethernet interfaces is connected to the remote lab LAN and assigned a fixed IP address. As of this writing:

| Project    | VM       | Board  | Radio    | IP Address | JTAG? | Console Serial Port | Other Serial Ports? |
|------------|----------|--------|----------|------------|-------|---------------------|-------|
| Haifuraiya | chococat | ZC706  | ADRV9009 | 10.73.1.9  | Yes   | /dev/ttyUSB0        | None  |
| Neptune    | keroppi  | ZCU102 | ADRV9002 | 10.73.1.16 | Yes   | /dev/ttyUSB1        | 3 + 1 |
|

Each of the hardware prototypes is also connected to an additional USB serial port, with hardware that supports a standardized JTAG interface to the SoC. Xilinx-provided software called `hw_server` runs on the host VM and provides access through this port to control the hardware directly.

## Booting the Target System

The target systems are capable of booting from an SD card or from the network. In a user deployment, it will probably boot from an SD card. However, this isn't convenient for remote development, since swapping and reprogramming the SD card is a hands-on operation at the remote lab. For development purposes, we will boot the target over the network. All the details about this procedure are set out in another document, [Working With FPGAs](Working-With-FPGAs.md). It's a multi-stage process.

Briefly, a target board configured for network boot initially starts up with no software. The `petalinux-boot` tool uses the JTAG interface and `hw_server` to begin the boot process by loading a loader program into the target and running it. Since there is no local display, the loader program prints out its stream of boot messages to the console serial port. If you (the developer) want to see these messages, you need to be connected to the console serial port during this stage of the process.

The loader is configured to automatically obtain the rest of the boot files over the network using `TFTP`, the Trivial File Transfer Protocol. The way we are currently booting, this attempt fails, because the loader doesn't use the right IP addresses for itself and the TFTP server. You will need to use your serial port connection to issue commands to change these two IP addresses and re-initiate the next two stages of booting, as detailed in [Working With FPGAs](Working-With-FPGAs.md) and shown here for the ZC706 case:

```bash
Zynq> setenv serverip 10.73.1.93
Zynq> setenv ipaddr 10.73.1.9 
Zynq> pxe get
Zynq> pxe boot
```

It should be possible to arrange for the target to use the correct IP addresses automatically. If we do change our build procedures to accomplish that, the boot process will normally succeed in completing without any developer intervention on the console serial port. However, if anything goes wrong during the boot process, you will still need to know how to connect to the console serial port to debug the problem.

So, a serial-port based terminal is essential during the boot process.

## Setting Up a Serial Port Based Terminal

Because the serial port(s) of the target hardware are connected to the corresponding virtual machine, you first have to connect to the VM from your local computer. This can be either an SSH session or a screen-sharing arrangement using VNC. The details on how to get access to the VM are documented in [Setting Up for Remote Access to ORI Labs](ORI-Lab-User-Setup.md).

Once you have a terminal open to the VM, you need to run a program to access the VM's serial port and provide what's called _terminal emulation_. The two most common programs for this purpose are called `screen` and `minicom`.

### Using `screen` for terminal emulation

`screen` is mainly a text-based screen manager and multiplexer, and supports fancy features like splitting the screen between two sessions or sharing a session between multiple terminals. For historical reasons, `screen` has the capability to open an interface directly to a serial port. That's all we need here, so we won't say anything more about the fancy features.

To start `screen` from the command line, we need to specify the name of the serial port device connected to the target's console serial port, and the baud rate used. Like this:

```
screen /dev/ttyUSB0 115200
```

You can also choose to use an alias name for the serial port. This may be more likely to keep working across changes to the target hardware configuration. Like this:

```
screen /dev/zc706_uart1 115200
```

Your screen will clear and, if the target is currently sending any text to the console, that text will start to appear on your screen. If the target is currently waiting for input, you won't see any text until you hit Return. You should then see the prompt, and whatever else you type will usually be echoed to your screen. If you're at a login prompt, the default login name is `root` and the password is `analog`.

If this doesn't happen, see the section below on __Troubleshooting `screen` problems__.

### Getting Out of Screen

When you're done with a `screen` session, type Control-A then K. It should prompt "Really kill this window [y/n]", and you should type Y to confirm. You should then get the "[screen is terminating]" message, which in this case is not an error.

If you want to do something else with a `screen` session, type Control-A then ? (question mark). You'll see lots of options. Read `man screen` for explanations.

### Troubleshooting `screen` problems

#### "screen is terminating"
If you __immediately__ see
```
$ screen /dev/ttyUSB0 115200
[screen is terminating]
$
```
this probably means that the serial port is already in use. Either you already have a `screen` session open somewhere else, or another developer does. You can check on this using `lsof` to list open files:
```
kb5mu@chococat:~$ lsof | grep ttyUSB
screen    14717                  kb5mu    5u      CHR              188,0       0t0               389 /dev/ttyUSB0
```
Look for a line of output that contains the right serial port device name (in this case, /dev/ttyUSB0). It also contains the username that has the port open (in this case, kb5mu). If it isn't you, try to coordinate with the other user. Only one program at a time can access the serial port. If you can't coordinate with the other user, and you really need to access the serial port right now, you can kick the other user off forcibly by killing their process. The process ID is shown as 14717 in the `lsof` output line above. This should do the trick:
```
sudo kill -9 14717
```

It is also possible that you don't have permission to access the port. Try this:
```
$ groups
kb5mu dialout sudo docker tftp wireshark
```
Look for `dialout` in the list of your groups. If it's not there, you won't have permission to access the serial ports. Ask on Slack for that permission to be added.

You will also see this message after you exit `screen` normally.

There are probably other conditions that could cause this error. Ask on Slack for help.

#### "cannot exec ..."
If you immediately see
```
Cannot exec '/dev/ttyUSB0': No such file or directory
```
in a reverse-video bar at the bottom of the screen that briefly appears, and then clears and shows the "[screen is terminating]" message shown above, then the problem is that the device you named doesn't exist. Either you mistyped the name, or there's something wrong with how the target hardware is set up. If it's not a typo, ask on Slack for help.

#### Blank screen
If you just get a blank screen, try hitting Enter a few times. If that doesn't work, try typing some other characters. If you get no response, then you've connected to a serial port on the VM that isn't connected to the target hardware, or is connected to the wrong port on the target hardware, or is connected correctly but the target hardware isn't in a proper state to respond on the serial port. Disconnect by typing Control-A then K. In this situation, it may take a few seconds for Control-A K to take effect. 

Some of the targets have multiple serial ports, and only one of them responds as the console serial port. We've tried to arrange for the console serial port to always have the same name on any given VM, but it's possible for this to get scrambled. If you suspect this may have happened, try each of the other serial ports. You can find their names like this:
```
kb5mu@keroppi:~$ dmesg | grep tty
[    0.145122] printk: console [tty0] enabled
[    1.121855] 00:00: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
[    3.781368] usb 5-1.4: cp210x converter now attached to ttyUSB0
[    3.784710] usb 5-1.4: cp210x converter now attached to ttyUSB1
[    3.788108] usb 5-1.4: cp210x converter now attached to ttyUSB2
[    3.791485] usb 5-1.4: cp210x converter now attached to ttyUSB3
[    7.988268] cdc_acm 7-1:1.3: ttyACM0: USB ACM device
```
On VM keroppi we have lots of serial ports. Ignore tty0 and ttyS0; these are not connected to target hardware. ttyUSB0 through ttyUSB3 are a four-port adapter on the ZC102 target hardware, one of which is the console serial port. The ttyACM0 port is connected to a Pluto SDR. Normally on keroppi we use /dev/ttyUSB1 as the console serial port, but you may also need to try /dev/ttyUSB0, /dev/ttyUSB2, and /dev/ttyUSB3.

If you can't get a response from any of the serial ports, the target software just isn't running correctly. Try starting over with a target boot. Try undoing whatever your last change was. Debug! If you're stumped, you can always ask for help on Slack.

### Limitations of `screen`
Screen has some limitations.

Only one terminal at a time can own the serial port. That means you can only have one terminal window open to the target, and if you do, nobody else can access it without forcibly kicking you off.

You can't scroll backwards in a plain `screen` session. If you try, your display gets scrambled up.

You can get normal scrollback by using `minicom` instead of `screen`. We'll cover that in the next section.

You can overcome both of the limitations by using SSH instead. We'll cover that later, too.

## Using `minicom` instead of `screen`

You can access the serial port using the much more flexible program `minicom` instead of `screen`. It just takes a bit more setup. `minicom` was designed in the days of dialup modems, and it still has lots of features to support them. We'll just ignore those features and use the ones that work with plain serial ports.

### Configuring `minicom`

If you just type
```
minicom
```
it will take its parameters from a default file. This probably won't work. Instead, you can specify a configuration file that has been pre-configured to match the target hardware. On chococat,
```
minicom zc706
```
Or on keroppi,
```
minicom zc102
```
If you need to change the settings,
```
sudo minicom -s
```
will take you directly to the setup menus. You need to use `sudo` because the configuration files are written in `/etc/minicom`, where you don't normally have permission to write. Use the menus to change whatever settings you think you need, then select "Save setup as..." and specify a name you invent. Please don't overwrite the standard `zc706` or `zc102` settings unless you're sure, and if you do, please announce the change on Slack. Then choose "Exit from Minicom", which saves your custom config file without trying to use it. Then, when you want to use those settings, just use your invented name on the `minicom` command line.

### Getting Out of `minicom`

When you're done with a `minicom` session, type Control-A then X. (Unfortunately, that's __not__ the same as in `screen`!) It should prompt "Leave Minicom?", and offer `Yes` (the default) and `No` answers. Hit Enter to take the default and exit the program.

If you want to do something else with a `minicom` session, type Control-A then Z. You'll see lots of options on multiple menus.

### Useful `minicom` Features

In `minicom` you can scroll back, and it works. Definitely useful!

You can also navigate and search the scrollback buffer. Control-A B.

You can tell `minicom` to capture everything to a file. Control-A L.

You can tell `minicom` to add timestamps to the screen (and thus to the capture file, if enabled). Control-A N repeatedly to sequence through several useful timestamping options.

You can clear the screen. Control-A C. (This also works in `screen`.)

You can send a file to the target to automate a standard sequence of actions. Control-A S.

You do lots of other (possibly less useful) things. Control-A Z for the whole menu.

But you can still only have one `minicom` attached to the serial port at a time. To get around that limitation, you need to use SSH.

## Setting Up an SSH Based Terminal

You should already be set up to use SSH as described in [Setting Up for Remote Access to ORI Labs](ORI-Lab-User-Setup.md). I'll assume you're already familiar with the basics.

### Use of Passwords
Unfortunately, the public key authentication we use for computers and VMs is not supported on the target operating system, so we have to use plain passwords. We rely on the security of the remote lab LAN in general (accessible only by SSH or Wireguard), so we just log in to the target as `root` with the default password `analog`.

### Use of `~/.ssh/config File`
You should already be using a `~/.ssh/config` file to manage your SSH hosts. You will probably want to add a stanza for each target hardware you want to connect to. Like this:
```
Host zc706
	HostName zc706.sandiego.openresearch.institute
	User root
	StrictHostKeyChecking no
	UserKnownHostsFile=/dev/null
	Port 22
```

With this in your config file, you can just type
```
ssh zc706
```
to connect to the target. It will prompt you for `root`'s password, which is `analog`.

The SSH client program doesn't provide any way for you to put your password in the config file, because that would generally be a terrible idea. So you'll just have to type it in each time. Luckily, `analog` is a lot easier to remember and type than a secure password would be.

By using the domain name `zc706.sandiego.openresearch.institute`, you're saved from remembering the IP address assigned to the ZC706 target.

This assumes that you have access to the Remote Lab LAN via Wireguard configured and enabled. If you don't want to use Wireguard, see the next section on SSH tunneling.

The lines for `StrictHostKeyChecking` and `UserKnownHostsFile` may be new to you. They are used because the network-booted target hardware doesn't have any non-volatile storage. Each time it boots, it has to randomly generate a new host key. If StrictHostKeyChecking is enabled, this will earn you an alarming error message, like this one:
```
kb5mu@chococat:~$ ssh root@10.73.1.9
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
SHA256:WsADaFnVRoT086GaaduVK2XJ40FBLfYjCJ8tWxFZvck.
Please contact your system administrator.
Add correct host key in /home/kb5mu/.ssh/known_hosts to get rid of this message.
Offending RSA key in /home/kb5mu/.ssh/known_hosts:21
  remove with:
  ssh-keygen -f "/home/kb5mu/.ssh/known_hosts" -R "10.73.1.9"
RSA host key for 10.73.1.9 has changed and you have requested strict checking.
Host key verification failed.
```
If you don't want to deal with that message every time you reboot the target system, always use the ~/.ssh/config file alias (here, "zc706") with "StrictHostKeyChecking no" set.

Setting the "UserKnownHostsFile" to "/dev/null" just prevents SSH from updating its record of the target's host key. This doesn't really matter with "StrictHostKeyChecking" turned off. It might be more convenient in a scenario where the target is sometimes booted from the SD card.

### Use of SSH Tunneling
We generally recommend installing and enabling Wireguard, so that you have direct access to the IP addresses of all the computers, virtual machines, instruments, and networked hardware targets in the Remote Lab. If you do have Wireguard working, you can skip this section.

It's also possible to access the target hardware by SSH tunneling. The easiest way is to add a ProxyJump line to your `~/.ssh/config` file. Like this:
```
Host zc706
    HostName zc706.sandiego.openresearch.institute
    User root
    StrictHostKeyChecking no
    UserKnownHostsFile=/dev/null
    Port 22
    ProxyJump ori-west
```
This assumes you already have an entry in `~/.ssh/config` named `ori-west`, as recommended in [Setting Up for Remote Access to ORI Labs](ORI-Lab-User-Setup.md).

If you sometimes use Wireguard and sometimes do not, for whatever reason, you can leave in the ProxyJump line and always use SSH tunneling. It'll work fine in parallel with the Wireguard connection. Or, if you want to use Wireguard when it's available, omit the ProxyJump line from the config file and use this modified command line when Wireguard is not available:
```
ssh -J ori-west zc706
```
The `-J ori-west` is equivalent to the `ProxyJump ori-west` line in the config file.
