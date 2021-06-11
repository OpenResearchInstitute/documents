# Setting Up for X11 Forwarding

Revised 2021-06-10 kb5mu

This is a supplement to [Setting Up for Remote Access to ORI Labs](https://github.com/phase4ground/documents/blob/master/Remote_Labs/ORI-Lab-User-Setup.md). Read and follow that document first.

That document discusses ways to operate lab computers in a text terminal session, and describes how to use their GUI desktops via VNC screen sharing. Those are the recommended methods. In some cases, however, it may turn out to be preferable to run GUI programs without sharing the entire screen. This can be done by running an X11 server on your local machine and using X11 forwarding via SSH. This document explains how to do that.

Be sure you have a good reason to use X11 forwarding. VNC screen sharing is more compatible and generally faster, too.

* [Installing an X11 Server](#installing-an-x11-server)
* [Preparations for SSH Access](#preparations-for-ssh-access)
* [About Wireguard VPN Access](#about-wireguard-vpn-access)
* [Using X11 Sharing](using-x11-sharing)
* [Support](#support)


## Installing an X11 Server

You need to run an X11 server on your local machine.

If you're on a Linux machine with a GUI desktop, that's already done. If you're on a Linux machine that only has the command line, you may be able to install desktop support.

If your local machine is a Mac, you will need to install an X11 server program. The one to get is called Xquartz, but unfortunately it is not fully compatible with everything you will want to do. For instance, most of Vivado works fine, but you can't even launch the documentation viewer. Mac users who need to use GUI programs like Vivado remotely should probably just use VNC and forget about forwarding X11. Alternatively, you might consider installing a virtual machine host on your Mac and running a Linux virtual machine. 

If your local machine runs Windows, you can install an X11 server program such as `Xming`. I have not yet tested X11 servers on Windows. Let me know what works for you and I'll add it here. Alternatively, you might consider installing a virtual machine host and running a Linux virtual machine. (Windows Subsystem for Linux does not currently solve the graphics problem, so you'll need a true VM environment like Parallels Desktop. That may change soon according to rumors from Microsoft.)


## Preparations for SSH Access

You already have a `~/.ssh/config` file (on Windows that's `%HOMEDRIVE%%HOMEPATH%\.ssh\config`) with several stanzas for your various connections. In order to forward X11 along with the connection, add these lines to the stanza for the desired connection and to the master entry for ori-west:
```
    ForwardX11 yes
    ForwardX11Trusted yes
    ForwardX11Timeout 100h
```


## About Wireguard VPN Access

It's perfectly possible to use Wireguard instead of SSH tunnels to run X11. You'd have to set up the DISPLAY environment variable manually (or use extra command line flags each time you run an X11 program), and configure your X11 server to accept connections from the remote machine. Generally this is more trouble than it's worth. Even if you use Wireguard, you should use X11 forwarding over SSH.

You can use exactly the same setup as detailed above for SSH access. That takes an unnecessary relay through the Raspberry Pi, but that should be fine. If you want to skip the extra hop, you can create a different stanza (with a different name) in the SSH config file that omits the ProxyJump command and add the ForwardX11... commands to that one.


## Using X11 Sharing

Set up an SSH terminal session to the VM where you want to run a GUI program, by typing
```
ssh hostname
```
for the hostname you used in the SSH config file stanza. Watch out for error messages here. If there's a problem with port forwarding, you'll need to fix it before proceeding.

You'll end up in a terminal window on the lab VM. The X11 forwarding is in effect, but invisible so far. You can check that it knows where to find your X11 server by typing
```
echo $DISPLAY
```
It should respond with something like this:
```
localhost:10.0
```
If it replies with just a blank line, the X11 forwarding didn't work.

To test it, run a simple GUI program like `glxgears` from the command line in your remote terminal window. If everything is working, a little window should pop up on your local screen with a colorful picture of spinning gears. In the terminal window, you'll get an estimate of the GUI performance every few seconds. If this all works with no error messages, your X11 forwarding is working.

Now you can start whatever GUI programs you want to use. Type the program name and any arguments into the terminal session. You can make more terminals, if you like. On our default Ubuntu VMs, `gnome-terminal` will start a new terminal window.


## Support

You can always email the lab managers at [sandiego-lab@openresearch.institute](mailto:sandiego-lab@openresearch.institute) with any questions or suggestions. You can also find us, more often than not, in the **Phase 4 Ground** Slack in the **remote_labs** channel.
