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
