# ORI Remote Lab (West) New User Procedure

## 1. User Requests SSH Access

They should provide a public key and a username, which might be their callsign. There might be multiple keys, but they will all apply to a single username unless the user makes a special request.

### Log in

```
ssh pi@ori-west.local
```
from a local host. Or, if out and about,
```
ssh -p 7322 pi@sandiego.openresearch.institute
```
Note that the host you log in from will need to have certificate credentials for SSH; password logins are disabled.

### Create a new user

```
sudo adduser callsign
```
It prompts for a password. Make up a random one and paste it in, hit return. It prompts for the password again. Paste it in again, hit return. You can now discard the password, it won't be used.

Enter the user's Full Name. Leave the other fields blank.

### Install the public key

```
sudo su callsign
cd /home/callsign
mkdir .ssh
cd .ssh
cat >authorized_keys
```
Paste in the (one long line) public key for this user from their email. Hit ^D to end.

```
chmod 600 authorized_keys
exit
exit
```
Now you should be back at your local computer.

### Test SSH Access

Unfortunately there's no good way to test this, since you don't have the private key. Password login by SSH is disabled, so you can't even test that.

### Reply to User

Reply to the user's email and tell them that they should now be able to log in to the system by following the instructions in ORI-Lab-User-Setup.md (aka _Setting Up for Remote Access to ORI Labs_).

## 2. User Requests Wireguard Access

They should provide a Wireguard-style public key. We assign them a sequential IP address from the 10.73.0.x/24 block. There may be multiple keys. Repeat the procedure for each key.

### Log in

```
ssh pi@ori-west.local
```
from a local host. Or, if out and about,
```
ssh -p 7322 pi@sandiego.openresearch.institute
```
Note that the host you log in from will need to have certificate credentials for SSH; password logins are disabled.

### Stop Wireguard

First, make sure nobody is relying on Wireguard access right now. Detailed procedure, TBD.

```
sudo wg-quick down wg0
```

### Edit the Wireguard Configuration

```
sudo su
cd /etc/wireguard
nano wg0.conf
```

Add a new stanza at the bottom of the file, starting with this template:
```
[Peer]
PublicKey = foo
AllowedIPs = 10.73.0.N/32
```

Now replace **foo** with the user-provided public key, and **N** with the next sequential number.

### Record the IP Address Assignment

```
nano tunnel_assignments.txt
```

Add a line with the assigned IP address, corresponding user name, and their email address. This is not used by the software, it's for administrator reference. (Comments in the config file get removed when Wireguard updates it with location information for peers; terrible design.)

### Restart Wireguard
```
sudo wg-quick up wg0
```
Don't forget that step!

### Reply to User

Reply to the user's email and tell them their VPN IP address 10.73.0.whatever_was_assigned. Attach the sample ```sandiego.conf``` file, and refer them back to the procedure in ORI-Lab-User-Setup.md (aka _Setting Up for Remote Access to ORI Labs_).

If multiple keys were set up, include the information about which IP address goes with which key.
