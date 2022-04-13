# ORI Remote Labs: Working With the AYECKa SR-1

DRAFT 2022-04-12 Paul Williamson KB5MU

The AYECKa SR-1 is a commercial data receiver for DVB-S2 (but not DVB-S2X) and GSE, installed in the Remote Lab in San Diego.

# SR-1 Manual

The manual for the SR-1 is in [Test Equipment](Test_Equipment/SR-1\ DVB-S2\ GSE\ Receiver).

# DVB-S2 Input Connections

The SR-1 has two RF inputs. They can be connected on demand to any source of DVB-S2 signals with frequency in the SR-1's range of 950 - 2150 MHz.

# Management of the SR-1

The SR-1 can be managed through a USB serial port or via Ethernet using Telnet. It uses a somewhat quirky menu interface. The main thing to know is that typing '0' (zero) usually backs up to the previous menu. See the SR-1 manual for an explanation of the menus.

If you have difficulty accessing the management interface, see below for troubleshooting ideas.

## Management through the Serial Port

The USB serial port is connected to the chococat VM, currently at /dev/ttyUSB2, and works at 115200 baud. On chococat, you can connect to it with:
```
screen /dev/ttyUSB2 115200
```
After connecting, you may need to type '0' (zero) once or twice to get the menu to come up. To exit screen, the default keystroke is Ctrl-A k (for kill).

## Ethernet Ports and Domain Names

The SR-1 has two Ethernet ports. Both are connected to the Remote Lab private LAN. The management port is known as `sr1m.sandiego.openresearch.institute`, and the traffic port is known as `sr1t.sandiego.openresearch.institute`. These may be abbreviated as `sr1m` and `sr1t` from hosts on the Remote Lab private LAN.

The management port will respond to pings, but the traffic port will not.

## Management via Telnet

The management menus are available using telnet to the management port. On any Remote Lab host or VM:
```
telnet sr1m
```
or, elsewhere, if you have WireGuard connected,
```
telnet sr1m.sandiego.openresearch.institute
```

Wait for the fake login prompt with username telnet already filled in. The telnet password is empty (just type return).

Your telnet session is on a short timeout. If you leave it alone for a short while, it will disconnect you. There may not be any indication on the screen when that happens.

To exit telnet, the default keystroke is Ctrl-] to get back to the telnet> prompt. Then type `quit`.

## Management Interface Troubleshooting Ideas

The Ethernet ports are configurable for compatibility with the local network. If these settings get changed to wrong values, the Ethernet ports will be inaccessible. Access the management interface via the serial port and change the networking settings back to valid values. The serial port doesn't have any configuration to worry about.

If your telnet session connects and then immediately says `Connection closed by foreign host.` then probably someone else already has a telnet session open to the SR-1. If this session is idle, the SR-1 is supposed to time it out after a short while, so wait a minute and try again. If the session is not idle, then you'd better coordinate with that other user.

The serial port can only be owned by one process at a time. If another process (possibly another user's screen session) has the port open, you will be denied access. Screen will immediately say `Screen is terminating.` without any explanation. You can find out what process has the port open by typing
```
lsof /dev/ttyUSB2
```
Then if you can't get the other user to release the serial port, you can forcibly kill the interfering process with `sudo kill` and the process ID, which you got from the `lsof` command.

The serial port is also disabled when a telnet connection is active. You'll get connected, but it won't show the menu or respond to your keystrokes. For this reason, the SR-1 is set to time out inactive telnet sessions after a short while. Stay connected for a minute or so, and your menu may spring to life when the telnet session is terminated. If not, then you'd better coordinate with that other user.
