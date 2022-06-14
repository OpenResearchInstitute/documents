# Setting Up for Remote Access to ORI Labs

Revised 2022-01-07 kb5mu

Note: the Little Rock lab is not yet available for general use at this time.

* [Description of the Network](#description-of-the-network)
* [Ways to Access the Private LAN](#ways-to-access-the-private-lan)
* [Preparations for SSH Access](#preparations-for-ssh-access)
* [Preparations for Wireguard VPN Access](#preparations-for-wireguard-vpn-access)
* [Advanced Wireguard Configurations](#advanced-wireguard-configurations)
* [Windows Remote Desktop Access](#windows-remote-desktop-access)
* [Linux Screen Sharing with VNC](#linux-screen-sharing-with-vnc)
* [Linux Screen Sharing with X11](#linux-screen-sharing-with-x11)
* [Support](#support)

The ORI remote lab in San Diego consists of three computers and an array of test
equipment, all sharing an isolated local area network (LAN). The ORI remote lab
in Little Rock consists of two computers and a similar array of test equipment,
all sharing another isolated LAN.

At each lab, a Raspberry Pi 4 running Raspberry Pi OS, with an extra Ethernet
port provided by a USB dongle, is responsible for all connections to and from
the Internet. It, in turn, is isolated from other network hosts in the building
by means of VLAN routing in an Ethernet switch. The San Diego Pi's local host
name is `ori-west` and it also has the domain name `sandiego.openresearch.institute`. 
Likewise, the Little Rock Pi is named `ori-south` and `littlerock.openresearch.institute`.

In San Diego, a decently powerful Windows machine named `Aperture` is connected only to the LAN.
It has an installation of Xilinx Vivado, and is enabled for Remote Desktop access.
This machine was installed as a temporary substitute for the third machine, but
for now will continue to be available. It also hosts two DVB-S2 satellite receivers on PCIe cards.

At each lab, an extremely powerful PC is connected only to the LAN.
In San Diego, it is named `Chonc`; in Little Rock, `Chubb`. It features
a 3970X Threadripper processor with 32 cores (64 threads), many lanes of PCIe
interconnect, 256GB of RAM, a 32TB disk array with double parity protection, dual
10GB Ethernet ports, and a Nvidia GEForce RTX 3080 graphics card. The operating
system running on the hardware is Unraid from Lime Technology. Unraid is a
flavor of Linux, combined with a flexible NAS-like storage manager and a
hardware-assisted virtualization host. Each machine is configured to host a number of
virtual machines, which run Windows 10 Pro or Linux as needed.

Typically, a remote lab user would log in to one of these VMs and work there,
without needing to consider that the environment is virtual, running on top of
Unraid, and sharing resources with other virtual machines. Users needing to set
up a new kind of test and development environment should consult with the lab
managers for help configuring a suitable virtual machine.

* A Windows 10 Pro virtual machine named `chonc-win10` is available for general use
in the San Diego lab.
It has direct-mapped access to the Nvidia graphics card, which enables its use for
GPU-assisted signal processing development work. (GPU usage remains untested.) This
VM auto-starts when Chonc boots, so it should always be running unless something
else is running that also needs to use the GPU.

* An Ubuntu 18.04.6 virtual machine named `chococat` is set up in the San Diego
lab for FPGA development
using Xilinx Vivado. This VM auto-starts when Chonc boots, so it should generally
always be running. It is connected to a Xilinx ZC706 via two USB serial ports,
one connected to the JTAG port and the other connected to the UART port. The ZC706
is also connected to the lab LAN, and hosts an Analog Devices ADRV9371 transceiver
development board.

* Another Ubuntu 18.04.6 virtual machine named `keroppi` is also set up in the
San Diego lab for FPGA development using Xilinx Vivado. This VM also auto-starts
when Chonc boots, so it should generally always be running. It is connected to a
Xilinx ZCU106 via five USB serial ports, one connected to the JTAG port and the
other four connected to UART ports. At times an ADALM Pluto SDR is also connected.
The ZCU106 is also connected to the lab LAN.

* An Ubuntu 20.04.2 virtual machine named `chonc-a` is set up in the San Diego lab for general Linux use.

* An Ubuntu 20.04 virtual machine named `chubb-xxl` is set up in the Little Rock lab
for general Linux use. It is configured with the maximum number of cores (31) and a
large RAM allocation (144GB), so it should be quite fast. It has only 200GB of disk
storage allocated for general use, but the `/tools` directory is allocated on the
main disk array and has disk space limited only by the total array size (32TB).
The idea is the `/tools` contains installations of large development toolchains
(such as Xilinx Vitis/Vivado) that can be shared among a number of Linux VMs.

* Additional virtual machines can be set up at will for any specific need. They can
share resources, and can be started and stopped as needed.

Equipment on the LAN is not directly accessible from the Internet, but each item
has a domain name that resolves to its local address on the LAN. For example, the
Windows machine Aperture is `aperture.sandiego.openresearch.institute`, and this
resolves to the non-routable IPv4 address 10.73.1.73. All the instruments on the LAN
have domain names that follow the same pattern. Their host names are generally the
model number of the particular instrument.

## Ways to Access the Private LANs

Presently there are two ways to access the LANs.

You can mix and match these methods. In each case there will be some things you need to set up on your own computer, and also some things the lab managers will have to set up on your behalf to authorize access.

### 1. Access Using SSH

SSH ("secure shell") is a program originally intended for login to a terminal session on  a remote computer, over a single encrypted TCP connection. Used this way, you can use SSH to log in to the Raspberry Pi. While running on the Pi, or any other computer or virtual machine on either LAN, you have direct access to everything on both LANs.

That single TCP connection doesn't have to be a login session on the Raspberry Pi. It can be configured to run any program on the Pi. In particular, it can be set to run SSH on the Pi and connect to another computer on the LAN. That session, in turn, can be a terminal login session or anything else. Using this capability to create a terminal login session, you can log on to any computer or VM on the private LANs, or to any development board that's currently configured to support SSH logins.

SSH can also be configured to create any number of additional encrypted TCP connections, to the Raspberry Pi or to any other host on the LAN. These extra connections are called _SSH tunnels_, and they exist only for the duration of the SSH session. An SSH tunnel creates a numbered port on your local computer that acts like a specific numbered port on the remote computer. Another program running on your local computer can then be configured to use the tunneled port through the loopback address 127.0.0.1 as if it were the remote port. This could be any program that uses a TCP connection. For example, we'll see how to set up Microsoft Remote Desktop to get GUI access to a Windows VM on the LAN.

SSH only provides TCP connections, and only the ones that are specifically configured by you. (It is possible to forward UDP through an SSH tunnel, but this requires extra networking trickery.)

It's common to do all this SSH configuration on the command line, but the syntax isn't the easiest. What's more, there are things that we want to do with SSH that simply cannot be done with command line arguments. Instead, we will use a configuration file that details all the settings for each kind of SSH session we wish to run. You give each set of settings in the config file a name. Once that's all set up, you can run a session of that type by simply entering
```
ssh configname
```
on your local terminal.

### 2. Access Using Wireguard

Wireguard is a relatively new way to implement virtual private networks (VPN). Instead of creating a few specific connections, it simulates a network interface on your local computer that is somehow magically connected to the remote network. You don't need to know in advance what ports will need to be connected, and it handles UDP as well as TCP connections.

The Wireguard VPN can be turned on and off on demand, but it can also be left on all the time, even when connectivity is not available. You can even plug in to a different Internet connection and your VPN will seamlessly continue to work. Wireguard is fast and has low overhead.

A VPN-style connection offers some advantages for some kinds of remote lab work. If you wish, you can run test scenarios on your own local computer, and it would have direct access to all the test equipment. You might use this to prototype tests that will eventually run on a lab computer, or to run one-off tests more conveniently. Of course, if performance is critical you may still need to run on an appropriately-configured VM that's physically in the remote lab, or even directly on a processor within the target hardware.

Much of what you can do with the VPN can also be done with SSH, but not everything. For instance, the VXI-11 protocol underlies the VISA instrument control protocol used by most of the remote lab test equipment. VXI-11 requires access to arbitrary TCP ports, so you have no way to configure them in advance as required by SSH. This is no problem if you're running on a lab computer or VM, and it's also no problem for remote access over a Wireguard VPN.

Running programs that need access to remote resources can also be much easier with the Wireguard VPN. For instance, programs like Microsoft Remote Desktop can access the various Windows desktops without any special setup on your end.


## Description of the Network

The Raspberry Pi ori-west, the Windows PC Aperture, the Unraid server Chonc, and all the network-capable test equipment in the San Diego lab are connected to a Netgear GS316 16-port unmanaged gigabit Ethernet switch. We also have a fancy Netgear XS708T managed 10-gigabit Ethernet switch, which will be used to interconnect Chonc and test gear (such as FPGA development boards) with high bandwidth requirements.

The Raspberry Pi ori-south, the Unraid server Chubb, and all the network-capable test equipment in the Little Rock lab are connected to TBD switches.

Everything on the network is assigned a static IP address. These addresses are in the 10.73.1.x block in San Diego and the 10.73.2.x block in Little Rock. These addresses are not directly routable on the Internet. All access to the private LAN from outside the labs is mediated by one of the Raspberry Pis, known by the domain name `sandiego.openresearch.institute` or `littlerock.openresearch.institute` respectively. These domain names go through a dynamic IP provider so that sandiego.openresearch.institute or littlerock.openresearch.institute will always refer to the Raspberry Pi at the corresponding lab, even if the local ISP changes its IP address.

Even though the equipment is not directly accessible on the Internet, each item has a DNS host name so you don't need to know the individual IP addresses. All the names for equipment in the San Diego lab look like `thing.sandiego.openresearch.institute`, where `thing` is a memorable name for the equipment, usually its model number for test equipment or the host name for computers and virtual machines. If you're running on one of the lab computers, you can abbreviate these names to just `thing` (because they're listed in _/etc/hosts_ or _C:\Windows\System32\drivers\etc\hosts_ as applicable). VMs on the lab PC can support the same shortcut. Likewise, names in the Little Rock lab look like `thing.littlerock.openresearch.institute` and have similar abbreviations. The idea here is that a test script can be written using the abbreviated names, and that script can run without modification in either lab.

The XS708T Ethernet switch in San Diego is capable of being set up to monitor packets flowing through it by copying those packets to another port for capture. Check with the lab managers [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) if you need this capability. It is also capable of creating virtual LANs within the lab.

The Wireguard VPN has been designed to make it possible to operate equipment in both labs as part of the same setup, bandwidth permitting. A device in the San Diego lab can talk directly to a device in the Little Rock lab through the VPN. Instruments that exist in both labs are given special shortcut names for convenience. For example, the oscilloscope in San Diego, `ds1104.sandiego.openresearch.institute`, known as simply `ds1104` on the San Diego LAN, may be accessed from the Little Rock LAN as `ds1104.sd`. Likewise, `ds1104.littlerock.openresearch.institute` is known as `ds1104` in Little Rock, but `ds1104.lr` in San Diego.

## Preparations for SSH Access

First, you will need to have an SSH client program on your computer. If you're on a Mac or Linux or anything like that, or on a version of Windows 10 newer than April 2020, you already have an SSH client. On older Windows machines, download and install [PuTTY](https://www.putty.org).

Next, you need an SSH key pair. I recommend you generate a fresh key pair to use just for the ORI lab, but an existing key pair will also work. 

To generate a fresh key pair, type in a terminal:
```
ssh-keygen -f ~/.ssh/id_rsa_ori -N ""
```
(or run PuTTYgen if you're using PuTTY). If you need more help with any of this, try searching for "SSH login without password" on the web.

If you need access from multiple computers, you can either copy the key pair to all your computers, or set up a separate key pair on each.

Then, email your **public** key (not your private key!) to [remote-labs@openresearch.institute](mailto:remote-labs@openresearch.institute) and request SSH access, specifying your callsign (preferably) or other username you want to use. If you followed the procedure above, the file to send is `~/.ssh/id_rsa_ori.pub`. Your request will be processed as soon as we can. If you need to set up multiple keys, please request them all at once. They will all access the same user account, unless you specify otherwise.

Once your login is set up, you will be able to use your SSH client to access the system. You need to give it your user name (usually your callsign), the name of the private key file corresponding to the public key file you sent in (unless it's the default one), and the non-standard SSH port number we use, 7322. Exact procedures will vary for GUI SSH clients. The following are the procedures for standard command line SSH clients.

You can put that all on one long command line if you don't mind the typing:
```
ssh -p 7322 -i ~/.ssh/id_rsa_ori w1abc@sandiego.openresearch.institute
```
where you'll replace `w1abc` with your own callsign or username.

Better, take the time now to configure your SSH client to provide all that info automatically. Edit or create a `~/.ssh/config` file (on Windows that's `%HOMEDRIVE%%HOMEPATH%\.ssh\config`), and add a stanza to it with all the settings you use for each kind of connection you usually make. You can assign a memorable nickname to each connection. Here's a good example to start with, substituting your username and private key file name as above.
```
# Connect directly to the remote lab's Raspberry Pi in San Diego.
# This stanza also enables the Host entries below with ProxyJump settings.
Host ori-west
    HostName sandiego.openresearch.institute
    User w1abc
    IdentityFile ~/.ssh/id_rsa_ori
    Port 7322

# Connect directly to the remote lab's Raspberry Pi in Little Rock.
# This stanza also enables the Host entries below with ProxyJump settings.
Host ori-south
	HostName littlerock.openresearch.institute
	User w1abc
	IdentityFile ~/.ssh/id_rsa_ori
	Port 7322

# Connect to the FPGA development Linux VPN. Works for terminal or VNC.
Host chococat
    HostName chococat.sandiego.openresearch.institute
    User w1abc
    IdentityFile ~/.ssh/id_rsa_ori
    Port 22
	ProxyJump ori-west
#	LocalForward 5973 chococat:59xx # uncomment and set xx to use VNC

# Connect to the general purpose Linux VPN. Works for terminal or VNC.
Host chonc-a
    HostName chonc-a.sandiego.openresearch.institute
    User w1abc
    IdentityFile ~/.ssh/id_rsa_ori
    Port 22
	ProxyJump ori-west
#	LocalForward 5973 chonc-a:59xx # uncomment and set xx to use VNC

# Connect to the Windows VM with the GPU. Works for terminal or RDP.
Host chonc-win10
    HostName chonc-win10.sandiego.openresearch.institute
    User w1abc
    IdentityFile ~/.ssh/id_rsa_ori
    Port 22
    ProxyJump ori-west
    LocalForward 13389 chonc-win10:3389

# Connect to the Windows machine Aperture. Works for terminal or RDP.
Host aperture
    HostName aperture.sandiego.openresearch.institute
    User w1abc
    IdentityFile ~/.ssh/id_rsa_ori
    Port 22
    ProxyJump ori-west
	LocalForward 23389 aperture:3389
```

With that in the config file, your command line is much easier, like this:
```
ssh ori-west
```
or
```
ssh chococat
```
etc.

You can use whatever name you find memorable on the Host line, and use that name when you issue the ssh command.

You'll end up in a standard login shell (bash by default on Linux, CMD on Windows).

Now that you're connected to a machine on the private LAN, what to do next is mostly beyond the scope of this document. As a simple _"hello, world"_ demo, try connecting to ori-west and typing
```
nc eez-bb3.sandiego.openresearch.institute 5025
```
This will connect you to the [SCPI interface](https://www.envox.hr/eez/eez-bench-box-3/bb3-scpi-reference-manual/bb3-scpi-introduction.html) of the [EEZ Bench Box 3](https://www.crowdsupply.com/envox/eez-bb3) on the lab bench. If you then type
```
*IDN?
```
and hit return, it should respond with its identification information, like this:
```
Envox,EEZ BB3 (STM32),002C002C3338510738323535,1.0
```
Hit Control-C to exit.

We will need to work out a way to ensure that lab users don't interfere with each other. For now, that is also beyond the scope of this document. Coordinate in the `remote_labs` channel on Slack.

## Preparations for Wireguard VPN Access

This method is probably optional. The baseline method of access is through SSH, described in the previous section.

To make the equipment in the lab act like part of your own network, you first need to install the Wireguard client program on your computer. See [Wireguard Installation](https://www.wireguard.com/install/) for more info on this. It's easy to install on almost any kind of computer.

Wireguard has a command line interface on Linux. On Windows, it has a GUI (graphical user interface) program, which also installs command line tools. Install from the Microsoft Store. On macOS, you can install either the GUI or the command line tools or both. The macOS command line tools can be installed from either [Homebrew](https://brew.sh) or [MacPorts](https://www.macports.org), and the GUI is available on the Mac App Store. Users on macOS should note that the command line tools do not share configuration information with the GUI version, so you should probably pick one and stick with it.

Typically you will want to install Wireguard on the computer you'll use to develop and run tests using the lab equipment. If you can't or don't wish to install Wireguard on the computer you want to use, it's also possible to use a Raspberry Pi (or other small computer) to handle the networking and serve as a gateway between your network and the private lab network. Contact the lab managers if you need details on this.

### Command Line Procedures (Linux or macOS)

If you plan to use the Wireguard GUI on macOS, please skip to the next section.

Next, you will need to generate a public/private key pair, Wireguard style. Open a terminal (Linux or macOS) or a Command Prompt (not PowerShell) on Windows. Then do this:
```
wg genkey > private_key  
wg pubkey < private_key > public_key
```

Then, email your **public** key (not your private key!) to [remote-labs@openresearch.institute](mailto:remote-labs@openresearch.institute) and request Wireguard access. Your request will be processed as soon as we can. If you need to set up multiple keys, please request them all at once.

We will send you a configuration file, `oriremote.conf`, which is set up to connect you to both labs simultaneously. It will look something like this:

```
[Interface]  
Address = 10.73.0.N/24  
PrivateKey = put-your-private-key-here  

[Peer]  
PublicKey = G9JLSEV6hu+RW1mMFSWB6O9iIn27HvoiyDic+kDzhQA=  
Endpoint = sandiego.openresearch.institute:51900  
AllowedIPs = 10.73.0.1/32, 10.73.1.0/24  
PersistentKeepalive = 25  

[Peer]  
PublicKey = yroEStqN6hDNeKImAeVhC9pY0MB3er9JO6UZBjNAdXI=
Endpoint = littlerock.openresearch.institute:51900  
AllowedIPs = 10.73.0.250/32, 10.73.2.0/24  
PersistentKeepalive = 25  
```

You will need to change two things in this file. First, we will assign you a unique IP address in the VPN block of 10.73.0.x, so you'll need to change the **10.73.0.N** on the Address line to your own unique IP address. Second, you'll need to replace **put-your-private-key-here** with the private key you generated above.

If you only want to use one lab or the other, you can delete the [Peer] stanza for the lab you don't want. You can keep multiple config files around if you use different configurations at different times.

Place the modified config file in the proper directory. On Linux:
```
sudo cp oriremote.conf /etc/wireguard
```
Do not be alarmed by a warning about "writing to a world accessible file" and suggesting a umask setting. We'll take care of that with the next command:
```
sudo chmod 600 /etc/wireguard/oriremote.conf
```
On macOS (if you use the command line procedures):
```
sudo mkdir /usr/local/etc/wireguard  
sudo cp oriremote.conf /usr/local/etc/wireguard  
sudo chmod 600 /usr/local/etc/wireguard
```
On Windows:
```
copy oriremote.conf C:\Windows\System32\config\systemprofile\AppData\Local\WireGuard\Configurations\
```

You'll want to be careful with oriremote.conf and with your private_key file. You don't want to lose the private key, and you also don't want anybody else to get a copy of it. If your private key should leak out beyond your control, please notify the lab managers so we can disable it and set you up with a fresh one.

Then when you want to activate the VPN to access the lab network, you'll say
```
wg-quick up oriremote
```

Likewise, to deactivate the VPN on Linux or the macOS command line, it's
```
wg-quick down oriremote
```

You can substitute whatever .conf file name you want in place of oriremote in these commands. Leave off the .conf part.

You should now have access to the test equipment. You can do a very simple check like this:
```
ping eez-bb3.sandiego.openresearch.institute
```
You should get responses something like this:
```
PING eez-bb3.sandiego.openresearch.institute (10.73.1.3): 56 data bytes
64 bytes from 10.73.1.3: icmp_seq=0 ttl=254 time=128.255 ms
64 bytes from 10.73.1.3: icmp_seq=1 ttl=254 time=85.934 ms
64 bytes from 10.73.1.3: icmp_seq=2 ttl=254 time=74.540 ms
```
You can also do the same experiment as suggested in the SSH section above, but on your local machine (if it has nc for netcat):
```
nc eez-bb3.sandiego.openresearch.institute 5025
```
This will connect you to the [SCPI interface](https://www.envox.hr/eez/eez-bench-box-3/bb3-scpi-reference-manual/bb3-scpi-introduction.html) of the [EEZ Bench Box 3](https://www.crowdsupply.com/envox/eez-bb3) on the lab bench. If you then type
```
*IDN?
```
and hit return, it should respond with its identification information, like this:
```
Envox,EEZ BB3 (STM32),002C002C3338510738323535,1.0
```
Hit Control-C to exit.

### GUI Procedures (macOS or Windows)

If you're using the command line Wireguard on macOS, please skip this section.

Run the WireGuard program installed from the Mac App Store or from [WireGuard.com](https://www.wireguard.com/install/).

At the bottom left, look for a plus sign button or drop-down arrow and click it, then select *Add Empty Tunnel...*. Type in a distinctive name for this tunnel, such as **ori_remote**. Copy the Public Key value from the screen. Click Save.

Paste this **public key** into an email to [remote-labs@openresearch.institute](mailto:remote-labs@openresearch.institute) and request Wireguard access. Your request will be processed as soon as we can. If you need to set up multiple keys, please request them all at once.

We will send you a configuration file, ```oriremote.conf```, which is set up to connect you to both labs simultaneously. It will look something like this:
```
[Interface]  
Address = 10.73.0.N/24  
PrivateKey = put-your-private-key-here  

[Peer]  
PublicKey = G9JLSEV6hu+RW1mMFSWB6O9iIn27HvoiyDic+kDzhQA=  
Endpoint = sandiego.openresearch.institute:51900  
AllowedIPs = 10.73.0.1/32, 10.73.1.0/24  
PersistentKeepalive = 25  

[Peer]  
PublicKey = yroEStqN6hDNeKImAeVhC9pY0MB3er9JO6UZBjNAdXI=
Endpoint = littlerock.openresearch.institute:51900  
AllowedIPs = 10.73.0.250/32, 10.73.2.0/24  
PersistentKeepalive = 25
```

You will need to change two things in this file. First, we will assign you a unique IP address in the VPN block of 10.73.0.x, so you'll need to change the **10.73.0.N** on the Address line to your assigned IP address. Second, you'll need to replace **put_your_private_key_here** with the private key the GUI program generated for you. Here's one way to do that:

Get back into the WireGuard GUI. If there's a WireGuard icon in the menu bar (macOS) or with the notification icons (Windows), you can just click it. If not, run the WireGuard program as usual. Make sure the right tunnel is selected in the left column, and click on Edit.

Now open `oriremote.conf` from the email you received in a text editor, select the entire thing and copy it.  Go back to the WireGuard window and paste the copied text into the big text area, after the text that's already there.

You'll have two copies of the `[Interface]` line and the `PrivateKey` line. Keep the `[Interface]` line at the very top, and the `PrivateKey` line that has your generated private key on it. Delete the extra `[Interface]` line and the `PrivateKey` with the dummy value.

Click Save. You're all set up!

If you only want to use one lab at a time, you can create another tunnel using the same procedures. Just delete [Peer] stanza for the lab you don't need.

Then when you want to activate the VPN to access the lab network, you'll find the WireGuard icon in the menu bar (macOS) or with the notification icons (Windows), right click it, and select the name of the tunnel you want to activate. Repeat the same procedure to deactivate the tunnel.

With the tunnel activated, you should now have access to the test equipment. You can do a very simple check in a terminal or Command Prompt like this:
```
ping eez-bb3.sandiego.openresearch.institute
```
You should get responses something like this:
```
PING eez-bb3.sandiego.openresearch.institute (10.73.1.3): 56 data bytes  
64 bytes from 10.73.1.3: icmp_seq=0 ttl=254 time=128.255 ms  
64 bytes from 10.73.1.3: icmp_seq=1 ttl=254 time=85.934 ms  
64 bytes from 10.73.1.3: icmp_seq=2 ttl=254 time=74.540 ms
```
You can also do the same experiment as suggested in the SSH section above, but on your local machine (if it has nc for netcat):
```
nc eez-bb3.sandiego.openresearch.institute 5025
```
This will connect you to the [SCPI interface](https://www.envox.hr/eez/eez-bench-box-3/bb3-scpi-reference-manual/bb3-scpi-introduction.html) of the [EEZ Bench Box 3](https://www.crowdsupply.com/envox/eez-bb3) on the lab bench. If you then type
```
*IDN?
```
and hit return, it should respond with its identification information, like this:
```
Envox,EEZ BB3 (STM32),002C002C3338510738323535,1.0
```
Hit Control-C to exit.

## Advanced Wireguard Configurations

Depending on your network, you might not need the keepalive that's enabled in the configuration file we provide. Try it and see, if you like. Just delete the **PersistentKeepalive** line from the configuration file (or set it to 0), deactivate the tunnel, and reactivate it. If you find that your VPN connection isn't staying up without the keepalive, put that line back in.

If you have network-capable test equipment in your own lab and wish to integrate it with the equipment in the ORI lab(s), that's certainly possible. We can help you with Wireguard configurations to get the job done.

## Windows Remote Desktop Access

If you prefer to use the Windows GUI on Aperture or Chonc-Win10, you can do that
using a Windows Remote Desktop client through either SSH or Wireguard. See the following sections for setup details.

Microsoft has Remote Desktop clients for Windows, macOS, iOS, and Android. There
are multiple third-party open source clients for Linux. We've had success with
[Vinagre](https://wiki.gnome.org/Apps/Vinagre), but any Remote Desktop client
ought to work.

You'll be prompted to enter your username and password to log into the
remote desktop. This is the username you specified to us (perhaps your
callsign) and the password we sent back to you (unless you've changed it).

Only one user at a time can be connected this way. If the Remote Desktop client
warns you that another user is already connected, you can find out who by
opening an SSH command line session to the Windows machine and typing
```
query user
```
You can then try to coordinate with them on the Slack `remote_labs` channel. If you can't contact them, you can go ahead and connect (which will disconnect them). Windows will try to ask for permission on their remote screen. Just wait a minute and it will let you in, even if they don't answer.

### Remote Desktop via SSH

Use one of the settings you configured in your SSH config file with an entry for `LocalForward`. The example config settings that appeared earlier in this
document include settings for Aperture and Chonc-Win10. If you want to use the
desktop on Chonc-Win10, just type:
```
ssh chonc-win10
```

Then configure your Remote Desktop client to connect to `localhost:13389` or
`127.0.0.1:13389`. The number after the colon must match the number after
`LocalForward` in the config file, so 13389 for Chonc-Win10 or 23389 for
Aperture. These port numbers can be anything, but it's best to avoid the
standard Remote Desktop port 3389.

Bring up the SSH session first, then start the Remote Desktop session. After
you're done with the remote desktop, you will probably want to log out of
Windows (in the GUI). Whether or not you log out, please disconnect cleanly from within the
Remote Desktop client program. Then you may exit the SSH session.


### Remote Desktop via Wireguard

Configure your Remote Desktop client to connect to
`aperture.sandiego.openresearch.institute` or `chonc-win10.sandiego.openresearch.institute`.

You don't need to do anything with SSH or use any special port numbers. Bring up
the Wireguard connection first, if you don't leave it up all the time, and then
start the Remote Desktop session. After you're done with the remote desktop, you
will probably want to log out of Windows (in the GUI). Whether or not you log out, please
disconnect cleanly from within the Remote desktop client program, then you may
deactivate the Wireguard connection (or leave it up).


## Linux Screen Sharing with VNC

If you prefer to use a GUI on a Linux VM, you can do that using VNC through either SSH or Wireguard. You have to run a VNC server on the VM, and then run a VNC client on your local machine.

The client finds the server through the VM's IP address (10.73.1.xx) and a port number. Port numbers start at 5900 and go up, 5901, 5902, etc. Unfortunately, two VNC servers on the same (virtual) machine cannot use the same port number. If they try, the second VNC server to be started will fail to start. To avoid that, we need each user to choose a different port number. Each remote lab user already has a unique number assignment, the last number in their Wireguard IP address. So if your Wireguard IP address is 10.73.0.23, you should set up your VNC server to use port 5923.

Access to screen sharing through VNC can be controlled by a password. This is a separate password, distinct from your login password on the VM. You can choose your own password when you set up your VNC server. We recommend that you do use a password, though, as some VNC clients refuse to connect to a server that doesn't require a password.

When you're done using the screen sharing, you can choose to disconnect or log out. If you disconnect the VNC client, the session will continue to run on the VM, and when you return with a new screen sharing session, you can resume where you left off. If you log out, your session ends, and when you return you'll need to log in again. You may also have the option to restart the virtual machine. You can do that if you're the only one using the VM. You may even be able to shut down or power off the machine. Please don't do that, because then a remote lab admin will have to restart it.


### Choosing a VNC Client Program

In theory, any VNC client ought to work. In practice, there are some problems.

If your local machine runs Linux and does not have a GUI desktop, you'll need to install the GUI parts of Linux before VNC can work. Search the web for information on how to do that.

On Linux, we've had success with a VNC client called Remmina.
```
sudo apt install remmina
```
If you use a different VNC client, try it and see. It'll probably be fine.

If your local machine is a Mac, there's a built-in VNC client that works well. It's called `Screen Sharing`, and it's a little bit hidden. The easiest way to find it is to use Spotlight search (command-spacebar) and type "Screen Sharing". Another good choice on the Mac is VNC Viewer from RealVNC.

If your local machine runs Windows, we've had success with VNC Viewer from RealVNC.

### Running the VNC Server

We use TigerVNC server on the Ubuntu Linux VMs in the remote lab. It's probably already installed on your VM. If not, it can be installed by anyone with sudo permission by
```
sudo apt update && sudo apt install tigervnc-standalone-server
```

Set up a startup file named `~/.vnc/xstartup` and put this in it to start with:
```
#!/bin/sh 
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
vncconfig -iconic &
gnome-terminal --working-directory=~ &
dbus-launch --exit-with-session gnome-session &
```
That tells the VNC server how to start up your desktop for the VNC session. You can change what programs are run at startup by editing this file.

To set up your VNC password, type:
```
vncpasswd
```
and enter the password when prompted (twice).

That completes the initial setup.

Now whenever you want to use VNC, you'll use the program `vncserver`. It can be used in several ways, including:
```
vncserver -list
```
to see what VNC servers might already be running (in your account).
```
vncserver -kill :23
```
to stop the VNC server on display `:23` (that is, port 5923). Anybody currently using that VNC server will lose their session. (Use your own unique number, not 23.)
```
vncserver -localhost no :23
```
to start a new VNC server on display `:23` (that is, port 5923). The `-localhost no` tells the VNC server to accept connections from other machines on the network. (Use your own unique number, not 23.)

The above command will create a VNC server that works with screen resolutions up to 1920x1200 pixels. If you have a larger screen and sufficient network bandwidth to handle it, you may wish to run VNC at a higher resolution. For example, the following will set up a VNC server capable of filling the screen on a 4K monitor:
```
vncserver -localhost no -geometry 3840x2160 -depth 24 :23
```
You may have to right-click the VNC desktop and choose Display Settings in order to select the new resolution.
### VNC using Wireguard

Run the VNC client of your choice. Choose a connection type of VNC (if necessary) and enter the domain name of the VM you wish to connect to, a colon, and the unique port number you use. Here's an example:
```
chococat.sandiego.openresearch.institute:5923
```
The first time (or every time in some VNC clients) you will be prompted to enter your VNC password. This is the one you set with vncpasswd, not the one you use to log in to the VM.

You should see a graphical desktop. If you left a session running, it should appear. If not, you will be at the system login screen. You might have to hit Enter to wake it up. Log in with your username and password for the VM.

You might find that the colors are crazy. In that case, look for a setting to set the color mode to 24 bits. In VNC Viewer from RealVNC, you can click on the slim white bar at the top of the screen, choose the gear icon, and on the Options tab change the "Picture Quality" from "Automatic" to "High" and click "OK". Some simple VNC clients only have automatic mode. For those clients, click around a little, maybe move a window or bring up a menu, and eventually it should sync up to high quality mode.

You might see an error about an invalid message type. Try the "Picture Quality" setting described in the previous paragraph. I know, that doesn't make any sense, but I've found it works sometimes.


### VNC using SSH

Some VNC programs can handle tunneling over SSH by themselves. Others will require you to set up the SSH tunnel manually.

Remmina is one that can handle the SSH tunneling for you, if you use a "connection profile" instead of just entering the info in the Quick Connect bar. Add a connection profile using the icon in the top left corner. Give it a memorable name, perhaps the short name of the VM you're connecting to. Set the Protocol to "Remmina VNC Plugin". Under the Basic tab, set the server to the domain name of the VM you wish to connect to, a colon, and the unique port number you use. Here's an example:
```
chococat.sandiego.openresearch.institute:5923
```
Set the Color depth to "True Color (32 bpp)". Set the Quality to what you want, I suggest "Best (slowest)" unless your Internet connection is slow.

Now go to the "SSH Tunnel" tab. Click "Enable SSH tunnel" and choose "Custom". Next to Custom enter `sandiego.openresearch.institute:7322` or `littlerock.openresearch.institute:7322`, whichever is applicable. Under "SSH Authentication", fill in your remote lab user name (maybe your callsign) for Username, and select "Public key (automatic)".

Save the profile.

You should now be able to double-click the profile and get connected to VNC. The rest of the procedures are just like those detailed for Wireguard above.

If you're using some other VNC client program that can handle SSH tunneling for you, the settings should be similar.

If your VNC client can't handle SSH tunneling, then you'll need to edit the `LocalForward` line in the settings for the remote host in your SSH config file. It should look like this:
```
#    LocalForward 5973 chococat.sandiego.openresearch.institute:59xx
```

Remove the `#` to uncomment the line. Change 59xx on the above line to your port number.

Then in your VNC client, set the server to `127.0.0.1:5973`. Start an SSH session with the modified settings, then connect the VNC client. The SSH session will need to stay open as long as you're using the VNC connection. The rest of the procedures are just like those detailed for Wireguard above.

## Linux Screen Sharing with X11

Not recommended. If you insist, details can be found in [Setting Up for X11 Forwarding](https://github.com/phase4ground/documents/blob/master/Remote_Labs/ORI-Lab-X11-Setup.md)

## Support

You can always email the lab managers at [remote-labs@openresearch.institute](mailto:remote-labs@openresearch.institute) with any questions or suggestions. You can also find us, more often than not, in the **Phase 4 Ground** Slack in the **remote_labs** channel.
