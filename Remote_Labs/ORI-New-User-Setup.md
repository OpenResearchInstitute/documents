# ORI Remote Lab (West) New User Setup Procedures for Lab Managers

## 1. User Requests SSH Access

They should provide a public key and a username, which might be their callsign. There might be multiple keys, but they will all apply to a single username unless the user makes a special request. If this isn't clear from the email, reply and refer them to ```ORI-Lab-User-Setup.md```.

### Log in to the Raspberry Pi as pi

```
ssh ori-west.local
su pi
```
from a local host. Or, if out and about,
```
ssh -p 7322 sandiego.openresearch.institute
su pi
```
Note that the host you log in from will need to have certificate credentials for SSH; password logins are disabled. You can use your own username (if you can ```sudo```) instead of pi. You may have to add ```-i path/to/credentials``` if the defaults aren't right.

### Create a new user on the Raspberry Pi
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
```

### Set up SSH for outgoing connections
We will make outgoing connections to Aperture, so we need a key pair for the
new account on the Raspberry Pi.
```
ssh-keygen
cat ~/.ssh/id_rsa.pub
exit
```
Now you're back in pi's shell on the Raspberry Pi. Later, we will copy and paste
the public key you looked at with `cat`, so keep this terminal window around.

### Grant access to video capture

One more thing to take care of: grant the user access to the video capture device(s).

```
sudo usermod -a -G video callsign
exit
```
Now you're back in your own shell on the Raspberry Pi.

### Log in to Aperture
We need to be the Administrator for this.
```
ssh Glados@aperture
```

### Create user account on Aperture

Make up a temporary password for the user.

```
net user callsign tmppassword /add /fullname:"First Last CALL"
```

### Complete User Creation

The user account created above doesn't fully exist until the user
has logged in to Windows. We can simulate that by using PsExec (from
the PSTools package) to run a command as the new user.

```
C:\PSTools\PsExec64.exe -u callsign -p tmppassword cmd /c
```

### Authorize the Account for Remote Desktop
```
net localgroup "Remote Desktop Users" callsign /add
```

### Install the public key

```
mkdir ..\callsign\.ssh
copy con ..\callsign\.ssh\authorized_keys
```
Go back to where you displayed `id_rsa.pub` and copy the output (one long line).
Paste the public key here, and end with ^Z and return.

Now we need to adjust permissions on `authorized_keys`. SSH requires that the file
permissions be explicit and not inherited, and that there are exactly two: one for
SYSTEM and one for the user. Any other permissions must be removed.

Start by converting all the inherited permissions to explicit ones:
```
icacls c:\users\callsign\.ssh\authorized_keys /inheritance:d
```

Next, list the current permissions:
```
icacls c:\users\callsign\.ssh\authorized_keys
```

The output will look something like this:
```
c:\users\callsign\.ssh\authorized_keys NT AUTHORITY\SYSTEM:(F)
                                       BUILTIN\Administrators:(F)
                                       APERTURE\callsign:(F)
                                       APERTURE\kb5mu:(F)

Successfully processed 1 files; Failed processing 0 files
```
If you see `(I)` in any of the listings, the `inheritance` switch didn't work.

We want to modify this to look like so:
```
c:\users\callsign\.ssh\authorized_keys NT AUTHORITY\SYSTEM:(F)
                                       APERTURE\callsign:(F)

Successfully processed 1 files; Failed processing 0 files
```
by removing the extra entries. In this case:
```
icacls c:\users\callsign\.ssh\authorized_keys /remove:g Administrators
icacls c:\users\callsign\.ssh\authorized_keys /remove:g kb5mu
```

If you find that the user's own permission is missing, add it:
```
icacls c:\users\callsign\.ssh\authorized_keys /grant callsign:F
```

Make sure the command that removes YOUR permission is last. You won't be able
to access the file's permissions after you remove your own permission, unless
you're the Administrator.

```
exit
```

### Test SSH Access from Raspberry Pi to Aperture

From your session on the Raspberry Pi, switch to the new user account
```
su pi
```
When prompted, enter pi's password.
```
sudo su callsign
```
If prompted, enter pi's password again.

Now attempt an SSH session to Aperture:
```
ssh aperture
```
Say `yes` to accept the host fingerprint, if prompted. Then, you should
see a Windows command prompt.
```
exit
exit
exit
```

### (Can't) Test SSH Access from Outside

Unfortunately there's no good way to test this, since you don't have the private key. Password login by SSH is disabled, so you can't even test that.

### Test Remote Desktop Access
#### Wireguard procedure
Enable the Wireguard VPN on your local machine.

Run a Microsoft Remote Desktop client to host `aperture.sandiego.openresearch.institute` with user name callsign and password tmppassword. Disregard the security warning.

#### SSH Tunnel procedure
```
ssh -L 3389:localhost:3389 sandiego.openresearch.institute
```

Run a Microsoft Remote Desktop client to host `localhost` with user name callsign
and password tmppassword. Disregard the security warning.

### Finish Windows Setup

Windows will ask for permission to do a bunch of spying; turn off all the options and
save. Windows will ask to set up the Edge browser; go ahead and let it. Then exit the
browser window and log off.

### Repeat for Chonc-Win10

Repeat all the Windows setup procedures above on the Chonc-Win10 VM.

### Linux VM Access

If the user requests access to specific Linux VMs, on each VM:

```
sudo adduser callsign
```

It prompts for a password. Make up a random one and paste it in, hit return. It prompts for the password again. Paste it in again, hit return. You can now discard the password, it won't be used (unless the new user will be using ```sudo```).

Enter the user's Full Name. Leave the other fields blank.

```
sudo su callsign
cd /home/callsign
ssh-keygen
cd .ssh
cat >authorized_keys
```

Paste in the public key for this user's account on the Raspberry Pi. Hit ^D to end.

```
chmod 600 authorized_keys
exit
sudo usermod -a -G dialout callsign
```

Test that the user can log in without password from the Raspberry Pi to the VM.

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