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

 