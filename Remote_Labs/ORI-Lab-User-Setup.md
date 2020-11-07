# Setting Up for Remote Access to ORI Labs

DRAFT 2020-11-05 kb5mu

As we start to set up the ORI remote lab in San Diego, we currently have a Raspberry Pi running Raspbian and two other pieces of equipment on the private LAN for the lab bench. There will eventually be many more pieces of equipment on the bench, and probably a more powerful computer in addition to the Raspberry Pi.

Presently there are two ways to access the lab equipment:

1. Use SSH to log in to the Raspberry Pi, and access the equipment on the LAN exclusively from the Raspberry Pi.

2. Use Wireguard to establish a VPN connection to the private LAN, and operate the equipment on the LAN directly from your own computer.

You can use either or both methods. In both cases there will be some things you need to set up on your own computer, and also some things the lab managers will have to set up on your behalf to authorize access.

## Description of the Network

The Raspberry Pi and all the network-capable test equipment in the lab are connected to a gigabit Ethernet switch, a TP-Link TL-SG108PE, and assigned static IP addresses in the 10.73.1.x block. These addresses are not directly routable on the Internet. All access to the private LAN from outside the lab is mediated by the Raspberry Pi, which is known by the domain name ```sandiego.openresearch.institute``` (which goes through a dynamic IP provider).

Even though the equipment is not directly accessible on the Internet, each item has a DNS host name so you don't need to know the individual IP addresses. All the names for equipment in the San Diego lab look like ```thing.sandiego.openresearch.institute```, where ```thing``` is a memorable name for the equipment, usually its model number. If you're running on the Raspberry Pi, you can abbreviate these names to just ```thing``` (because they're listed in _/etc/hosts_).

The Ethernet switch is capable of being set up to monitor packets flowing through it by copying those packets to another port for capture. Check with the lab managers [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) if you need this capability.

We expect the Eastern lab to have a similar setup. The Wireguard VPN has been designed to make it possible to operate equipment in both labs as part of the same setup, bandwidth permitting. A device in the Western lab could talk directly to a device in the Eastern lab through the VPN.

## Preparations for SSH Access

First, you will need to have an SSH client program on your computer. If you're on a Mac or Linux or anything like that, or on a version of Windows 10 newer than April 2010, you already have an SSH client. On older Windows machines, download and install PuTTY.

Next, you need an SSH key pair. I recommend you generate a fresh key pair to use just for the ORI lab, but an existing key pair will also work. 

To generate a fresh key pair, type:
```
ssh-keygen -f ~/.ssh/id_rsa_ori_west -N ""
```
(or run PuTTYgen if you're using PuTTY). If you need more help with any of this, try searching for "SSH login without password" on the web.

If you need access from multiple computers, you can either copy the key pair to all your computers, or set up a separate key pair on each.

Then, email your **public** key (not your private key!) to [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) and request SSH access, specifying your callsign (preferably) or other username you want to use. If you followed the procedure above, the file to send is ```~/.ssh/id_rsa_ori_west.pub```. Your request will be processed as soon as we can. If you need to set up multiple keys, please request them all at once. They will all access the same user account, unless you specify otherwise.

Once your login is set up, you will be able to use your SSH client to access the system. You need to give it your user name (usually your callsign), the name of the private key file corresponding to the public key file you sent in (unless it's the default one), and the non-standard SSH port number we use, 7322. Exact procedures will vary for GUI SSH clients. The following are the procedures for standard command line SSH clients.

You can put that all on one long command line if you don't mind the typing:
```
ssh -p 7322 -i ~/.ssh/your_private_key_file w1abc@sandiego.openresearch.institute
```
where you'll replace ```w1abc``` with your own callsign or username, and ```your_private_key_file``` with the name of the file where you stored the private key.

Better, take the time now to configure your SSH client to provide all that info automatically. Add a stanza like this one to your ```~/.ssh/config``` file, creating a new file if there isn't one already, and substituting your username and private key file name as above.
```
Host ori-west
    HostName sandiego.openresearch.institute
    User w1abc
    IdentityFile ~/.ssh/your_private_key_file
    Port 7322
```

With that stanza in the config file, your command line is much easier:
```
ssh ori-west
```
You can use whatever name you find memorable in place of ```ori-west``` above.

You'll end up in a standard login shell. What to do next is mostly beyond the scope of this document. As a simple _"hello, world"_ demo, try typing
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

We will need to work out a way to ensure that lab users don't interfere with each other. For now, that is also beyond the scope of this document.

## Preparations for Wireguard VPN Access

To make the equipment in the lab act like part of your own network, you first need to install the Wireguard client program on your computer. See [Wireguard Installation](https://www.wireguard.com/install/) for more info on this. It's easy to install on almost any kind of computer.

If you install on macOS, you want the Basic CLI installation using [Homebrew](https://brew.sh) or [MacPorts](https://www.macports.org), shown near the bottom of the Wireguard Installation web page. The Mac App Store program is a optional GUI that helps with managing tunnels, but doesn't provide the tools to set them up from scratch.

Typically you will want to install Wireguard on the computer you'll use to develop and run tests using the lab equipment.

If you can't or don't wish to install Wireguard on the computer you want to use, it's also possible to use a Raspberry Pi (or other small computer) to handle the networking and serve as a gateway between your network and the private lab network. Contact the lab managers if you need details on this.

Next, you will need to generate a public/private key pair, Wireguard style. If you're on a Linux or similar system, or macOS, just do this:
```
wg genkey > private_key
wg pubkey < private_key > public_key
```
On Windows, do this in *Command Prompt* (not PowerShell):
```
wg genkey > private_key
wg pubkey < private_key > public_key
```

Then, email your **public** key (not your private key!) to [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) and request Wireguard access. Your request will be processed as soon as we can. If you need to set up multiple keys, please request them all at once.

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

You will need to change two things in this file. First, we will assign you a unique IP address in the VPN block of 10.73.0.x, so you'll need to change the **10.73.0.N** on the Address line to your own unique IP address. Second, you'll need to replace **put_your_private_key_here** with the private key you generated above.

On Linux, place the modified file in the proper directory:
```
sudo cp sandiego.conf /etc/wireguard
sudo chmod 600 /etc/wireguard/sandiego.conf
```
On Windows, you have a somewhat fancier interface that lets you "import" a tunnel from a file. Just feed your modified sandiego.conf file to that part of the Wireguard program. I think that works.

On macOS, you can import sandiego.conf through the App Store program, if you installed it. If you didn't, then the command line procedure works too:
```
cd /usr/local/etc
mkdir -m 700 wireguard
cp sandiego.conf wireguard
chmod 600 wireguard/sandiego.conf
```

You'll want to be careful with sandiego.conf and with your private_key file. You don't want to lose the private key, and you also don't want anybody else to get a copy of it.

Then when you want to activate the VPN to access the lab network, on Linux or the macOS command line, you'll say
```
wg-quick up sandiego
```
and on Windows (or macOS App Store app if you installed it) there's a fairly obvious GUI to activate the **sandiego** tunnel.

Likewise, to deactivate the VPN on Linux or the macOS command line, it's
```
wg-quick down sandiego
```
and on Windows (or macOS App Store app if you installed it) just follow your nose in the GUI.

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
On Linux or macOS, you can do the same experiment as suggested in the SSH section above:
```
nc eez-bb3.sandiego.openresearch.institute 5025
```

## Advanced Wireguard Configurations

Depending on your network, you might not need the keepalive that's enabled in the configuration file we provide. Try it and see. Just delete the **PersistentKeepalive** line from the configuration file (or set it to 0), deactivate the tunnel, and reactivate it. If you find that your VPN connection isn't staying up without the keepalive, put that line back in.

If you need to use both labs, you can set up a Wireguard configuration for each, exactly as described above. You can activate one tunnel or the other, or both at the same time. If you need equipment in one lab to talk directly to equipment in the other, let us know and we can enable a tunnel to do that.

If you have network-capable test equipment in your own lab and wish to integrate it with the equipment in the ORI lab(s), that's certainly possible. We can help you with Wireguard configurations to get the job done.

## Support

You can always email the lab managers at [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) with any questions or suggestions. You can also find us, more often than not, in the **Phase 4 Ground** Slack in the **remote_labs** channel.
