# Setting Up for Remote Access to ORI Labs

DRAFT 2021-02-12 kb5mu

The ORI remote lab in San Diego consists of two computers and an array of test
equipment, all sharing an isolated local area network (LAN).

A Raspberry Pi 4 running Raspbian, with an extra Ethernet port provided by a USB
dongle, is responsible for all connections to and from the Internet. It, in turn,
is isolated from other network hosts in the building by means of VLAN routing in
an Ethernet switch. The Pi's local host name is `ori-west` and it also has the
domain name `sandiego.openresearch.institute`. 

A decently powerful Windows machine named `Aperture` is connected only to the LAN.
It has an installation of Xilinx Vivado, and is enabled for Remote Desktop access.
There are plans to replace this machine with one with more storage and bandwidth,
matched to our predicted needs for the P4XT project, and also matched to the
machine in use at ORI-East. The intention is that the Windows machine will host
a number of Linux virtual machines, and that tests will be run primarily from
inside these VMs.

Equipment on the LAN is not directly accessible from the Internet, but each item
has a domain name that resolves to its local address on the LAN. For example, the
Windows machine Aperture is `aperture.sandiego.openresearch.institute`, and this
resolves to the non-routable IPv4 address 10.73.1.73. All the instruments on the LAN
have domain names that follow the same pattern. Their host names are generally the
model number of the particular instrument.

Presently there are two ways to access the LAN:

1. Use SSH to log in securely to the Raspberry Pi. While running on the Pi, you have
direct access to everything on the LAN. You can also use SSH to set up tunnels from
your local machine to specific addresses on the LAN. In particular, you can run SSH
again from the Raspberry Pi to log into Aperture and operate Windows and/or the
Linux VMs from their command lines.

2. Use Wireguard to establish a VPN connection to the private LAN, and operate the
equipment on the LAN directly from your own computer. The Raspberry Pi serves as
endpoint for Wireguard, but you might not log into the Raspberry Pi or run anything
on it. You can choose to operate test equipment directly from programs running on
your own computer, which may be handy in certain circumstances. You can also use
the VPN to connect to Aperture using Microsoft Remote Desktop, which would allow
you to operate Aperture through the familiar Windows GUI instead of (or in addition
to) its command line. Microsoft has Remote Desktop clients for Windows, macOS, iOS,
and Android. There are multiple third-party open source clients for Linux.

You can mix and match any of these methods. In each case there will be some things you need to set up on your own computer, and also some things the lab managers will have to set up on your behalf to authorize access.

You can set up tunnels with SSH, but you'll find that you cannot operate most of the equipment directly through that kind of static tunnel. The VXI-11 protocol underlying the VISA instrument control protocol requires access to arbitrary TCP ports. You can get that access by being on the LAN yourself (logged in over SSH to the Raspberry Pi or to a VM on the lab computer), or by having the Wireguard VPN active, but not with SSH tunnels alone.

## Description of the Network

The Raspberry Pi, the Windows PC Aperture, and all the network-capable test equipment in the lab are connected to an Ethernet switch (currently a TP-Link TL-SG108PE, to be upgraded to a DLink DGS-1250-28X) and assigned static IP addresses in the 10.73.1.x block. These addresses are not directly routable on the Internet. All access to the private LAN from outside the lab is mediated by the Raspberry Pi, which is known by the domain name `sandiego.openresearch.institute` (which goes through a dynamic IP provider).

Even though the equipment is not directly accessible on the Internet, each item has a DNS host name so you don't need to know the individual IP addresses. All the names for equipment in the San Diego lab look like `thing.sandiego.openresearch.institute`, where `thing` is a memorable name for the equipment, usually its model number. If you're running on the Raspberry Pi or on Aperture, you can abbreviate these names to just `thing` (because they're listed in _/etc/hosts_ or _C:\Windows\System32\drivers\etc_ respectively). VMs on the lab PC will support the same shortcut.

The Ethernet switch is capable of being set up to monitor packets flowing through it by copying those packets to another port for capture. Check with the lab managers [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) if you need this capability. The DLink switch, when it's in place, will also be capable of creating virtual LANs within the lab.

We expect the Eastern lab to have a similar setup. The Wireguard VPN has been designed to make it possible to operate equipment in both labs as part of the same setup, bandwidth permitting. A device in the Western lab could talk directly to a device in the Eastern lab through the VPN.

## Preparations for SSH Access

First, you will need to have an SSH client program on your computer. If you're on a Mac or Linux or anything like that, or on a version of Windows 10 newer than April 2010, you already have an SSH client. On older Windows machines, download and install [PuTTY](https://www.putty.org).

Next, you need an SSH key pair. I recommend you generate a fresh key pair to use just for the ORI lab, but an existing key pair will also work. 

To generate a fresh key pair, type in a terminal:
```
ssh-keygen -f ~/.ssh/id_rsa_ori_west -N ""
```
(or run PuTTYgen if you're using PuTTY). If you need more help with any of this, try searching for "SSH login without password" on the web.

If you need access from multiple computers, you can either copy the key pair to all your computers, or set up a separate key pair on each.

Then, email your **public** key (not your private key!) to [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) and request SSH access, specifying your callsign (preferably) or other username you want to use. If you followed the procedure above, the file to send is `~/.ssh/id_rsa_ori_west.pub`. Your request will be processed as soon as we can. If you need to set up multiple keys, please request them all at once. They will all access the same user account, unless you specify otherwise.

Once your login is set up, you will be able to use your SSH client to access the system. You need to give it your user name (usually your callsign), the name of the private key file corresponding to the public key file you sent in (unless it's the default one), and the non-standard SSH port number we use, 7322. Exact procedures will vary for GUI SSH clients. The following are the procedures for standard command line SSH clients.

You can put that all on one long command line if you don't mind the typing:
```
ssh -p 7322 -i ~/.ssh/id_rsa_ori_west w1abc@sandiego.openresearch.institute
```
where you'll replace `w1abc` with your own callsign or username.

Better, take the time now to configure your SSH client to provide all that info automatically. Add a stanza like this one to your `~/.ssh/config` file, creating a new file if there isn't one already, and substituting your username and private key file name as above.
```
Host ori-west  
    HostName sandiego.openresearch.institute  
    User w1abc  
    IdentityFile ~/.ssh/id_rsa_ori_west  
    Port 7322
```

With that stanza in the config file, your command line is much easier:
```
ssh ori-west
```
You can use whatever name you find memorable in place of `ori-west` above.

You'll end up in a standard login shell (bash by default). What to do next is mostly beyond the scope of this document. As a simple _"hello, world"_ demo, try typing
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

You're automatically set up to SSH from the Raspberry Pi to Aperture using a
unique key pair (with the default name, `id_rsa`). Test your SSH access to Aperture
by typing:
```
ssh aperture
```
You should find yourself at a Windows command prompt. If you prefer the latest
PowerShell, you can type
```
pwsh
```
or if you like the old PowerShell,
```
powershell
```
To back out,
```
exit
```

The procedure for gaining access to VMs on the main PC are expected to be similar, but remain TBD for now.

## Preparations for Wireguard VPN Access

This method is probably optional. The baseline method of access is through SSH, described in the previous section.

To make the equipment in the lab act like part of your own network, you first need to install the Wireguard client program on your computer. See [Wireguard Installation](https://www.wireguard.com/install/) for more info on this. It's easy to install on almost any kind of computer.

Wireguard has a command line interface on Linux. On Windows, it has a GUI (graphical user interface) program, which also installs command line tools. Install from the Microsoft Store. On macOS, you can install either the GUI or the command line tools or both. The macOS command line tools can be installed from either [Homebrew](https://brew.sh) or [MacPorts](https://www.macports.org), and the GUI is available on the Mac App Store.

Typically you will want to install Wireguard on the computer you'll use to develop and run tests using the lab equipment. If you can't or don't wish to install Wireguard on the computer you want to use, it's also possible to use a Raspberry Pi (or other small computer) to handle the networking and serve as a gateway between your network and the private lab network. Contact the lab managers if you need details on this.

### Command Line Procedures (Linux or macOS)

Next, you will need to generate a public/private key pair, Wireguard style. Open a terminal (Linux or macOS) or a Command Prompt (not PowerShell) on Windows. Then do this:
```
wg genkey > private_key  
wg pubkey < private_key > public_key
```

Then, email your **public** key (not your private key!) to [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) and request Wireguard access. Your request will be processed as soon as we can. If you need to set up multiple keys, please request them all at once.

We will send you a configuration file, `sandiego.conf`. It will look something like this:

```
[Interface]  
Address = 10.73.0.N/24  
PrivateKey = put-your-private-key-here  

[Peer]  
PublicKey = G9JLSEV6hu+RW1mMFSWB6O9iIn27HvoiyDic+kDzhQA=  
Endpoint = sandiego.openresearch.institute:51900  
AllowedIPs = 10.73.0.1/32, 10.73.1.0/24  
PersistentKeepalive = 25  
```

You will need to change two things in this file. First, we will assign you a unique IP address in the VPN block of 10.73.0.x, so you'll need to change the **10.73.0.N** on the Address line to your own unique IP address. Second, you'll need to replace **put-your-private-key-here** with the private key you generated above.

Place the modified config file in the proper directory. On Linux:
```
sudo cp sandiego.conf /etc/wireguard
```
Do not be alarmed by a warning about "writing to a world accessible file" and suggesting a umask setting. We'll take care of that with the next command:
```
sudo chmod 600 /etc/wireguard/sandiego.conf
```
On macOS:
```
sudo mkdir /usr/local/etc/wireguard  
sudo cp sandiego.conf /usr/local/etc/wireguard  
sudo chmod 600 /usr/local/etc/wireguard
```
On Windows:
```
copy sandiego.conf C:\Windows\System32\config\systemprofile\AppData\Local\WireGuard\Configurations\
```

You'll want to be careful with sandiego.conf and with your private_key file. You don't want to lose the private key, and you also don't want anybody else to get a copy of it. If your private key should leak out beyond your control, please notify the lab managers so we can disable it and set you up with a fresh one.

Then when you want to activate the VPN to access the lab network, you'll say
```
wg-quick up sandiego
```

Likewise, to deactivate the VPN on Linux or the macOS command line, it's
```
wg-quick down sandiego
```

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
You can also do the same experiment as suggested in the SSH section above, but on your local machine:
```
nc eez-bb3.sandiego.openresearch.institute 5025
```

### GUI Procedures (macOS or Windows)

Run the WireGuard program installed from the store.

At the bottom left, look for a plus sign button and click it, then select *Add Empty Tunnel...*. Type in a distinctive name for this tunnel, such as **ori_west**. Click Save.

Make sure your tunnel is selected in the left column, and then copy the Public Key value from the right part of the screen.

Paste this **public key** into an email to [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) and request Wireguard access. Your request will be processed as soon as we can. If you need to set up multiple keys, please request them all at once.

We will send you a configuration file, ```sandiego.conf```. It will look something like this:
```
[Interface]
Address = 10.73.0.N/24
PrivateKey = put_your_private_key_here

[Peer]
PublicKey = G9JLSEV6hu+RW1mMFSWB6O9iIn27HvoiyDic+kDzhQA=
Endpoint = sandiego.openresearch.institute:51900
AllowedIPs = 10.73.0.1/32, 10.73.1.0/24
PersistentKeepalive = 25
```

You will need to change two things in this file. First, we will assign you a unique IP address in the VPN block of 10.73.0.x, so you'll need to change the **10.73.0.N** on the Address line to your assigned IP address. Second, you'll need to replace **put_your_private_key_here** with the private key the GUI program generated for you. Here's one way to do that:

Get back into the WireGuard GUI. If there's a WireGuard icon in the menu bar (macOS) or with the notification icons (Windows), you can just click it. If not, run the WireGuard program as usual. Make sure the right tunnel is selected in the left column, and click on Edit.

Now open `sandiego.conf` from the email you received in a text editor, select the entire thing and copy it.  Go back to the WireGuard window and paste the copied text into the big text area, after the text that's already there.

You'll have two copies of the `[Interface]` line and the `PrivateKey` line. Keep the `[Interface]` line at the very top, and the `PrivateKey` line that has your generated private key on it. Delete the extra `[Interface]` line and the `PrivateKey` with the dummy value.

Click Save. You're all set up!

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
On macOS (or on Windows if you install a version of netcat), you can do the same experiment as suggested in the SSH section above, but on your local machine:
```
nc eez-bb3.sandiego.openresearch.institute 5025
```

## Advanced Wireguard Configurations

Depending on your network, you might not need the keepalive that's enabled in the configuration file we provide. Try it and see, if you like. Just delete the **PersistentKeepalive** line from the configuration file (or set it to 0), deactivate the tunnel, and reactivate it. If you find that your VPN connection isn't staying up without the keepalive, put that line back in.

If you need to use both labs, you can set up a Wireguard configuration for each, exactly as described above. You can activate one tunnel or the other. You can even activate both at the same time, except on Windows where that is not currently supported.

If you need equipment in one lab to talk directly to equipment in the other, let us know and we can enable a tunnel to do that.

If you have network-capable test equipment in your own lab and wish to integrate it with the equipment in the ORI lab(s), that's certainly possible. We can help you with Wireguard configurations to get the job done.

## Windows Remote Desktop Access

If you prefer to use the Windows GUI, you can do that using a Windows
Remote Desktop client through either SSH or Wireguard. Only one user at a time
can be connected this way. If the Remote Desktop client warns you that another
user is already connected, you can find out who by opening an SSH command
line session to Aperture and typing
```
query user
```
You can then coordinate with that user on the remote_labs Slack channel.

On Windows or the Mac, you probably want to use Microsoft's standard
Remote Desktop Client. On Linux, we've had success with
[Vinagre](https://wiki.gnome.org/Apps/Vinagre), but any Remote Desktop
client ought to work.

You'll be prompted to enter your username and password to log into the
remote desktop. This is the username you specified to us (perhaps your
callsign) and the password we sent back to you.

### Remote Desktop via SSH

From the command line of your local computer, you can say
```
ssh -p 7322 -i ~/.ssh/id_rsa_ori_west -L 3389:aperture:3389 w1abc@sandiego.openresearch.institute
```
where you'll replace `w1abc` with your own callsign or username. This sets
up a tunnel for port 3389, which is the standard port for Remote Desktop.
You'll end up with a terminal session to the Raspberry Pi, which needs to
stay open while you're using the remote desktop.

Better, add a second stanza like this one to your `~/.ssh/config` file:
```
Host aperture-rdp
    HostName sandiego.openresearch.institute  
    User w1abc  
    IdentityFile ~/.ssh/id_rsa_ori_west  
    Port 7322
    LocalForward 3389 aperture:3389
```

With that stanza in the config file, your command line is much easier:
```
ssh aperture-rdp
```
You can use whatever name you find memorable in place of `aperture-rdp` above.

Then configure your Remote Desktop client to connect to `localhost:3389` or
`127.0.0.1:3389`. Bring up the SSH session first, then start the remote desktop
session. After you're done with the remote desktop, disconnect cleanly from
within the remote desktop client, then you may exit the SSH session.

If you get an error message that you "already have a console session in
progress", try using a different local port. That is,
```
ssh -p 7322 -i ~/.ssh/id_rsa_ori_west -L 3390:aperture:3389 w1abc@sandiego.openresearch.institute
```
from the command line, or a stanza like this:
```
Host aperture-rdp
    HostName sandiego.openresearch.institute  
    User w1abc  
    IdentityFile ~/.ssh/id_rsa_ori_west  
    Port 7322
    LocalForward 3390 aperture:3389
```
and then connect to `localhost:3390` or `127.0.0.1:3390`. This solved the
problem in two known cases where the local computer was running Windows 10
and the standard Remote Desktop Connection that comes built-in.

### Remote Desktop via Wireguard

Configure your Remote Desktop client to connect to
`aperture.sandiego.openresearch.institute`. Bring up the Wireguard
connection first, then start the remote desktop session. After you're
done with the remote desktop, disconnect cleanly from within the remote
desktop client, then you may deactivate the Wireguard connection.

## Support

You can always email the lab managers at [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) with any questions or suggestions. You can also find us, more often than not, in the **Phase 4 Ground** Slack in the **remote_labs** channel.
