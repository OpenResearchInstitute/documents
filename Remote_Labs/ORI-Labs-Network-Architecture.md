# ORI Remote Labs Network Architecture

DRAFT 2020-11-06 kb5mu

ORI is setting up two labs for remote operation. This document describes the network connectivity between these labs and their users.

## Basic Requirement

The labs are in homes in California and Florida. The users may be anywhere in the world. The goal is to enable any user(s) to control the test equipment in either lab at will.

Remote users are not able to see or interact with the physical front panels of the test equipment in the lab. We've chosen test equipment capable of being remotely controlled by TCP/IP, so that it is possible, if not necessarily very convenient, to operate the equipment remotely as long as there is appropriate network connectivity.

The Internet provides the required connectivity, but also some extra challenges. We can't do much about limitations of bandwidth and latency between the various sites. We can try to make the connections as logically transparent as possible, and we absolutely must control access to prevent Internet shenanigans from ruining everything.

Many of the devices participating in the lab network are off the shelf test equipment. We have limited or no flexibility to change the network stack in such devices. The test equipment expects to be plugged in to an ordinary Ethernet LAN running an ordinary TCP/IP protocol stack, and that's what we must provide at each lab. Remote connectivity must be provided by some sort of computer serving as a gateway to the Internet.

## Remote Operation Models

There are two familiar models for this sort of operation, which we will refer to as thin-client and VPN (virtual private network). Our proposal here supports both models, including hybrid approaches.

### The Thin-Client Model

In the thin-client model, the user remotely operates a computer at the lab, and the lab computer controls all the test equipment. The user's computer (the thin client) provides only a remote screen and keyboard (etc.) needed to operate the lab computer. This may be a plain text terminal interface such as an SSH session, or it may be a remote graphical interface such as an X11 server, or it may be a full screen sharing system such as VNC or Remote Desktop.

The common thread for our purposes here is that the user's computer only needs to connect to the lab computer, and only in standard ways that can rely on off-the-shelf software for remote operation. This is such a common scenario that a variety of software is readily available.

A big advantage of this model is that the lab PC is local to the test equipment, so it will be able to run tests that require high bandwidths and/or low latencies that are not possible (or not reliable) over the remote connection.

Another potential advantage of this model is that the lab PC can be provisioned with licenses for expensive specialized software and/or high-powered hardware that might be impractical for each user to obtain. 

The primary limitation with this model is that the lab computer has to be configured to run every possibly tool in every possible scenario for all the things any user wants to do with the test equipment. For any given test, that's no problem. If we could identify a fixed set of tests to support, it would probably be possible to arrange a computer configuration that would serve them all. The flexibility of this model can be extended by cooperative use of tools such as environment managers (like Python's venv), containers (like Docker), and virtual machines, at some considerable cost in training and consensus-building.

### The VPN Model

In the VPN model, the user's computer is enabled to talk directly to every piece of test equipment in the lab. The user is free to configure their computer in any way that seems convenient, from the choice of operating system all the way to the detailed setup of software tools used to communicate with test equipment.

There are two big limitations to this model. The user's PC is on the wrong end of the slow internet connection, so it can only perform tests that don't require extreme bandwidth or very low latency.

Perhaps worse, each user would be primarily responsible for every aspect of setting up their system to operate the lab's test equipment. This is great for flexibility, but means a lot of duplicated effort getting things working from each computer.

### Hybrid Models

There's no particular reason to choose only one of these two models. By supporting both, we enable users to make their own tradeoffs and do whatever works best for their needs.

If the user needs to run a test that requires high bandwidth signal capture but also requires control software that won't run on the lab PC (for whatever reason), they can do the high bandwidth operation on the lab PC and still run the control plane from home.

## Internet Access at the Lab

Each lab is located in a home where reasonably broadband internet connectivity is already available. The home network router blocks direct incoming access to all hosts and ports inside the home, except where specific entries are made in the router's port forwarding table. Port forwarding entries to the gateway host will be limited to the minimum possible set.

Residential ISPs typically do not offer fixed IP addresses, at least not without charge. Each home network will use a dynamic DNS provider (updated automatically) to register a fixed domain name that will always work. An ORI domain name will also be assigned to each, with a CNAME record pointing to the dynamic DNS provider. For example, the home network for the West lab has dynamic DNS at ```ptw.dyndns.org``` and is also reachable at ```sandiego.openresearch.institute```.

## Separate Gateway Host

Each lab will use a dedicated host as a network gateway. The West lab uses a Raspberry Pi 4 equipped with a second Ethernet port (via USB) for this purpose. The East lab gateway computer is TBD. The gateway computer is given a static IP address on the home network, so that it can be the target of port forwarding entries.

The purpose of the dedicated gateway host is to isolate the network connectivity setup from the configuration of the Lab PC or any other equipment on the private lab network. The configuration of the gateway host will be under the control of designated lab managers at each lab.

## SSH for Thin-Client Connectivity

The lab gateway at each lab is configured to accept SSH (secure shell) connections from authorized lab users.

A non-standard port number (7322) is used for SSH, to reduce the load from random password-guessing attacks on the standard SSH port (22). The home router has a port forwarding entry for TCP packets on port 7322 to port 22 on the gateway host.

Password authentication for SSH sessions is disabled, to protect against common password-guessing attacks. Lab users are required to authenticate SSH sessions using the public key method. That means that lab users have to have an account on the gateway host. In order to set up that account, the user emails the lab manager (```sandiego-lab@openresearch.institute``` for the West lab, TBD for the East) and provides their public key and username information. (Users are encouraged, but not required, to use their amateur radio callsign as their username.) The lab manager sets up the account manually. The user procedure for this is set out in tutorial form in [Setting Up for Remote Access to ORI Labs](ORI-Lab-User-Setup.md) and the lab manager procedures are set out in [ORI Remote Lab (West) New User Procedure](ORI-New-User-Setup.md) for the West and TBD for the East.

Users are permitted to log into the gateway host, which may be useful for such things as diagnosing networking problems. For extremely lightweight tests, tests may even be run on the gateway host. However, users are not permitted to modify the configuration of the gateway host. If they have non-trivial needs for local test execution, they use the Lab PC, which is on the private Lab LAN. This can be done with an SSH tunnel, or directly through the VPN.

## Wireguard for VPN Connectivity

The lab gateway at each lab is configured to act as a VPN server using the [Wireguard](https://www.wireguard.com) protocol on port 51900. The home router has a port forwarding entry for UDP packets on port 51900 to port 51900 on the gateway host.

Wireguard uses public keys for authentication, like SSH, but also uses them for routing. To get set up for Wireguard, the user emails the lab manager and provides their Wireguard public key. No username is involved. The lab manager manually installs a tunnel from the Lab LAN to the user's computer. The user installs a tunnel to the Lab LAN. User and lab manager procedures for this are set out in the same documents mentioned in the previous section. Each user is assigned an IP address in the private block 10.73.0.0/24 for Wireguard tunneling purposes.

Every device (PC or test equipment or other) on each lab's LAN is assigned a static IP address. The private block 10.73.1.0/24 is used in the West lab, and 10.73.2.0/24 is used in the East lab. Each device is also given a short name, generally based on the device's model number. That name is also used to create a domain name for the device. For example, an EEZ Bench Box 3 power supply in the West lab might be named ```eez-bb3``` and have the domain name ```eez-bb3.sandiego.openresearch.institute```. Where possible, users (test procedure authors) are strongly encourage to use the domain name instead of the numeric IP address. When running on the gateway (and maybe the Lab PC, TBD) the short name alone can also be used as a domain name, thanks to entries in the local /etc/hosts file. A directory of equipment short names and IP addresses is published at TBD.

To use the lab remotely, the user brings up the tunnel with a simple command, and then has what appears to be direct access to every device on the Lab LAN. When done, the user may disable the tunnel, but it is not a problem if this step is omitted.

If the user has other hosts or devices in their own LAN that need to participate in the network with equipment at the lab, a minor adjustment to the user's config file can set that up. This procedure is set out in TBD.

If a test procedure involves equipment at both ORI labs talking directly to one another, the lab managers can set up a tunnel between the two lab LANs. This procedure is set out in TBD.

## Known Issues

If multiple users try to use the same lab at the same time, there is likely to be trouble. Procedures to coordinate usage times are TBD. It's possible that the network access mechanism could be involved in enforcing limits.

The network can control the test equipment, but it can't readily change how they are interconnected unless remotely-controlled switches are added. There are probably other things that will require hands-on configuration. The on-site lab managers can do that, but changes will have to be scheduled in advance in coordination with user scheduling.

Setup instructions have not been tested on any version of Windows yet.
