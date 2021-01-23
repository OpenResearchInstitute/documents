# ORI Remote Lab (West) New User Setup Procedures for Lab Managers

## 1. User Requests SSH Access

They should provide a public key and a username, which might be their callsign. There might be multiple keys, but they will all apply to a single username unless the user makes a special request. If this isn't clear from the email, reply and refer them to ```ORI-Lab-User-Setup.md```.

### Log in

```
ssh pi@ori-west.local
```
from a local host. Or, if out and about,
```
ssh -p 7322 pi@sandiego.openresearch.institute
```
Note that the host you log in from will need to have certificate credentials for SSH; password logins are disabled. You can use your own username (if you can ```sudo```) instead of pi. You may have to add ```-i path/to/credentials``` if the defaults aren't right.

### Create a new user
Once per user,

```
sudo adduser callsign
```

It prompts for a password. Make up a random one and paste it in, hit return. It prompts for the password again. Paste it in again, hit return. You can now discard the password, it won't be used (unless the new user will be using ```sudo```).

Enter the user's Full Name. Leave the other fields blank.

### Install the public key(s)

```
sudo su callsign
cd /home/callsign
mkdir .ssh
cd .ssh
cat >authorized_keys
```
Paste in the public key(s) for this user from their email. Each is one long line. Hit ^D to end.

```
chmod 600 authorized_keys
exit
```

Now you're back in your own shell. One more thing to take care of: grant the user access to the video capture device(s).

```
sudo usermod -a -G video callsign
exit
```

Now you should be back at your local computer.

### (Can't) Test SSH Access

Unfortunately there's no good way to test this, since you don't have the private key. Password login by SSH is disabled, so you can't even test that.

### Reply to User

Reply to the user's email and tell them that they should now be able to log in to the system by following the instructions in ```ORI-Lab-User-Setup.md``` (aka _Setting Up for Remote Access to ORI Labs_).

## 2. User Requests Wireguard Access

They should provide a Wireguard-style public key. We assign them a sequential IP address from the 10.73.0.x/24 block. There may be multiple keys. Repeat the procedure for each key. If this isn't clear from the email, reply and refer them to ```ORI-Lab-User-Setup.md```.

### Log in

```
ssh pi@ori-west.local
```
from a local host. Or, if out and about,
```
ssh -p 7322 pi@sandiego.openresearch.institute
```
Note that the host you log in from will need to have certificate credentials for SSH; password logins are disabled. You can use your own username (if you can ```sudo```) instead of pi. You may have to add ```-i path/to/credentials``` if the defaults aren't right.

### Stop Wireguard

First, make sure nobody is relying on Wireguard access right now. Detailed procedure, TBD.

```
sudo wg-quick down wg0
```

### No User Creation

Wireguard doesn't require the user to have a local account. All users will probably need to have SSH access, though, so they already do have an account.

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
### Test Wireguard
Make sure Wireguard is still working for you. You did remember to restart Wireguard, right?