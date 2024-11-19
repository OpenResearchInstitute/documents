# ORI Remote Labs: Spectrum Analyzer Video

## You Probably Don't Need Video Streaming Anymore

As of firmware version 00.03.06 of the RSA5065N Spectrum Analyzer, there is a much better way to remotely access the instrument. It now supports an internal web page that not only displays the screen in real time, but also allows full control of the instrument through the browser. If you already have Wireguard set up, you can just access http://rsa5065n.sandiego.openresearch.institute and go. (Note: http not https)

One special trick you need: in order to access functions that would require pressing physical buttons on the front panel of the spectrum analyzer, use the on-screen button in the top row that looks like four buttons.

Now that you can control the spectrum analyzer and not just view its screen, there is a possibility that you might interfere with other users. Please be aware of this possibility and coordinate on Slack if in doubt.

That said, the video stream from `labvideo.sandiego.openresearch.institute` remains available and you can still use that if you prefer. Read on for more details.

## Original Introduction

Of all the instruments in the lab, the RSA5065N Spectrum Analyzer has the largest and richest screen display. The size of the display makes screenshots slow. Moreover, for many lab purposes it's quite revealing to see the spectrum display changing in real time, and not really satisfactory to get only a still screenshot.

The RSA5065N has an HDMI video output port. We have an inexpensive HDMI capture device connected between that HDMI output and a USB port on a Raspberry Pi. With just a little extra setup, you can use this to get a live view of the spectrum analyzer's screen. It won't be quite as quick as the instrument's actual front panel, but will still be far more useful than static screenshots.

Unfortunately, none of the other instruments has a video output port, so this only works on the spectrum analyzer.

## Previous Versions of This Document

Previous versions of this document described how to access the video by running VLC remotely on the main Raspberry Pi in the lab. That method has been replaced by a more reliable and efficient method. We've also moved the video capture device from the main Raspberry Pi to a dedicated one, named `labvideo.sandiego.openresearch.institute`.

## Streaming Video Access

We split the job of displaying the captured video into two parts. The first part runs on the dedicated Raspberry Pi `labvideo`. It uses the program `ffmpeg` to convert the captured HDMI video data into a unicast UDP video stream, which it sends over the Wireguard network to your local computer. The second part runs on your local computer. It uses the companion program `ffplay` to receive the UDP stream and display it. This way, only the video data itself travels across the network, and error recovery is built in to the ffmpeg programs.

To make this two-stage process as convenient as possible, we use a little shell script to bring up both parts. One version of the script works on Linux and on macOS. A separate version is for Windows PowerShell. Download the script that matches your system, and put it somewhere convenient. On Linux or macOS, you will need to make it executable:

```bash
chmod +x video.sh
```

### `video.sh` Script for Linux or macOS

This script was developed on Ubuntu 20.04 and macOS Sonoma 14.0. Some of the trickier bits may not be entirely portable across different versions. Let us know if you run into any such problems.

```bash
#!/usr/bin/env bash

# You must be connected to remote lab West using Wireguard.
# See Remote_Labs/ORI-Lab-User-Setup.md for more info.

# You must have a ~/.ssh/config entry for host labvideo:
# Host labvideo
#     HostName labvideo.sandiego.openresearch.institute
#     User labvideo
#     Port 22

# You must have ffplay available on the path.
# sudo apt install ffmpeg


if [[ $OSTYPE == 'linux'* ]]; then
  myip=$(ip route get 10.73.1.1 | sed -n '/src/{s/.*src *\([^ ]*\).*/\1/p;q}')
elif [[ $OSTYPE == 'darwin'* ]]; then
  interface=$(route get 10.73.1.1 | grep interface: | sed s/"interface: "//)
  myip=$(ifconfig $interface | grep --only-matching "10\\.73\\.\\d\\+\\.\\d\\+ --" | awk '{print $1}')
else
  myip=10.73.0.N	# replace N with your unique number!
fi
myport=57373

# make sure the IP address is plausible
if [[ ! $myip =~ ^10.73.0.[0-9]+$ ]]; then
	echo "Implausible IP address $myip -- is Wireguard up?"
	exit 1
fi

ssh -f labvideo ffmpeg -hide_banner -loglevel error -s 1280x720 -i /dev/video0 -f mpegts udp://${myip}:${myport}
echo Sending video to ${myip}:${myport}, type q into video window to quit \(or ^C here\).
ffplay -hide_banner -nostats -loglevel fatal -i udp://localhost:${myport}
ssh labvideo pkill -e -f "ffmpeg.*udp://${myip}:${myport}"
wait
```

### `video.ps1` Script for Windows PowerShell

This script was developed on Windows 11 with PowerShell 7.3.9.

```powershell
# for PowerShell

# You must be connected to remote lab West using Wireguard.

# You must have a ~/.ssh/config entry for host labvideo:
# Host labvideo
#     HostName labvideo.sandiego.openresearch.institute
#     User labvideo
#     Port 22

# You must have the program ffplay.exe installed on the PATH.

$myip = Get-NetIPAddress | Where-Object { ($_.IPAddress.Length -Ge 9) -and ($_.IPAddress.SubString(0,8) -Eq "10.73.0.") } | select -ExpandProperty IPAddress
$myport = 57373

# make sure the IP address is plausible
$last_octet = [int]($myip -Split "\.",4)[3]
if ( ($last_octet -lt 1) -or ($last_octet -ge 255))
{
	echo "Implausible IP address $myip -- is Wireguard up?"
	return
}

Start-Process -FilePath "ssh" -ArgumentList "labvideo ffmpeg -hide_banner -loglevel error -s 1280x720 -i /dev/video0 -f mpegts udp://${myip}:${myport}" -WindowStyle Hidden

echo "Sending video to ${myip}:${myport}, type q into video window to quit"

& 'ffplay.exe' -hide_banner -nostats -loglevel fatal -i udp://labvideo.sandiego.openresearch.institute:${myport}
 
ssh labvideo pkill -e -f "ffmpeg.*udp://${myip}:${myport}"
```


### Prerequisites

* Your computer must be connected to the San Diego remote lab over Wireguard. If not, check out [Setting Up for Remote Access to ORI Labs](ORI-Lab-User-Setup.md) for some guidance.

* Your computer must have `ffplay` installed and on the path. On Linux or macOS, `ffplay` is usually part of the `ffmpeg` package, which will be available from your usual package manager. On macOS, that would be [Homebrew](https://brew.sh). On Windows, download from one of the providers listed on [ffmpeg.org](https://ffmpeg.org/download.html), extract, and copy `ffplay.exe` to a directory on the path (or add the `bin` directory where you extracted the files to the path).

* Your computer must be able to `ssh` in to `labvideo` as user `labvideo` with no password (and no public key pair, either). This is accomplished by putting an entry into your `~/.ssh/config` file, like this one:

```
Host labvideo
    HostName labvideo.sandiego.openresearch.institute
    User labvideo
    Port 22
```

* If your computer runs Linux or macOS, the bash script `video.sh` above should take care of everything. If your computer runs Windows, the PowerShell script `video.ps1` above should take care of everything. If your computer runs something else, we haven't yet worked out the details for you.

### Script Walkthrough

The script starts with some warnings about the prerequisites. Then it spends a few lines trying to find out your computer's IP address on the remote lab Wireguard LAN. I couldn't find a way that worked on both Linux and macOS, so these two cases are handled separately in the bash script. There's a third case in the bash script where you just type the IP address into the script, replacing N with your assigned unique number as described in [Setting Up for Remote Access to ORI Labs](ORI-Lab-User-Setup.md).

Next, the script uses an `ssh` connection to run the program `ffmpeg` on the Raspberry Pi `labvideo` in the remote lab.
* `-hide_banner -loglevel error` suppress some unnecessary output from `ffmpeg`.
* `-s 1280x720` sets the video resolution of the stream. 1280x720 pixels is the native size of the spectrum analyzer's screen, so it results in the sharpest output. You can use a lower resolution if you need to save some network bandwidth.
* `-i /dev/video0` tells `ffmpeg` where to get its input: from the video capture device.
* `-f mpegts` tells `ffmpeg` what format of video stream to create.
* `udp://${myip}:${myport}` tells `ffmpeg` where to send the video stream and how. It will send using the protocol `UDP`, to the specified port on the Wireguard IP address of your computer.

The script outputs a message to let you know what's happening.

Then the script runs `ffplay` on your local computer.
* `-hide_banner -nostats -loglevel fatal` suppress some unnecessary output from `ffplay`. The loglevel filter is set very high, so that only fatal error messages come out, because otherwise it's very typical to have a steady stream of non-fatal errors. You can't do much about those errors, so there's no point in seeing them. You will probably see some noisy artifacts on the screen from time to time, due to these errors.
* `-i udp://localhost:${myport}` tells `ffplay` how and where to receive the video stream. It comes in using the protocol `UDP`, directly to your computer's IP address, on the specified port. In the PowerShell script, we have to put the Raspberry Pi's address there instead of `localhost`.

At this point, after a short delay, the video window should pop up and begin displaying the spectrum analyzer's screen. Leave the terminal window open, and go about your business. When you're done with the spectrum analyzer display, you can end the session by selecting the video window and pressing `q` for quit. Or, you can type control-C on the original terminal window (on Linux or macOS) or close the original terminal window (on Windows).

Lastly, the script uses another `ssh` connection to stop the `ffmpeg` program running on `labvideo`. It uses the program `pkill` with a matching expression that will only kill programs matching your IP address and port number. This prevents your shutdown from disrupting any other instances of `ffmpeg` that may be running.

### Multiple Simultaneous Users Not Supported

Unfortunately, the Raspberry Pi's video system only allows one program to use the video capture device at a time, so we don't support multiple users on the spectrum analyzer video. Supporting several users would be possible with some trickery, but we haven't tried to implement that. If the need arises, we can look into it. Since the spectrum analyzer has to be hooked up and configured for each user's needs, we expect that one remote video user at a time will be sufficient.

If someone is already using the remote video when you run the script, it will say
```
/dev/video0: Device or resource busy
```

and hang. It won't automatically recover when the other session ends. You will have hit control-C in the terminal window to shut it down (or close the terminal window on Windows). You can try again any time; it doesn't disrupt the other user's session at all.

Try to coordinate with the other user to work out a time sharing arrangement. If the other user is not available to shut down their video session, you can force quit their open session like this:
```bash
ssh labvideo killall ffmpeg
```

The other user will see their video freeze, since the UDP stream has ended. They can recover by typing `q` for quit into the frozen video window, or Control-C into the terminal window on Linux or macOS, or closing the terminal window on Windows.

### Remote Video on Other Platforms

If you would like to access the remote video using a device other than Linux, macOS, or Windows, it may be possible, but we haven't worked out the details yet.

If you run [WSL2](https://learn.microsoft.com/en-us/windows/wsl/about) on a Windows machine, the instructions for Linux above will probably work for you. Note that your Wireguard installation will need to be inside the WSL machine in order for the networking to work. The remote lab LAN IP address does not pass through from Windows to WSL.

## Security Note

The Raspberry Pi `labvideo` is configured to accept a login without any password or public key for the username `labvideo`. This is generally terrible security practice, but since this machine is only available over the Wireguard LAN, and access to that is controlled, and the `labvideo` machine doesn't host anything else, we consider this configuration acceptable. It makes setting up your access to stream the spectrum analyzer video easier than a more conventional locked-down configuration.
