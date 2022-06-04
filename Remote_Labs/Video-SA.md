# ORI Remote Labs: Spectrum Analyzer Video

Of all the instruments in the lab, the RSA5065N Spectrum Analyzer has the largest and richest screen display. The size of the display makes screenshots slow. Moreover, for many lab purposes it's quite revealing to see the spectrum display changing in real time, and not really satisfactory to get only a still screenshot.

The RSA5065N has an HDMI video output port. We have an inexpensive HDMI capture device connected between that HDMI output and a USB port on the Raspberry Pi. With just a little extra setup, you can use this to get a live view of the spectrum analyzer's screen. It won't be quite as quick as the instrument's actual front panel, but will still be more useful than static screenshots.

Unfortunately, none of the other instruments has a video output port, so this only works on the spectrum analyzer.

## Access via X11 Forwarding

One way to get access to the spectrum analyzer video feed is to run a video viewer on the Raspberry Pi. A plain SSH session only gives you access to a text terminal, though. The solution is to forward the Pi's GUI through your SSH session to your local screen. There are two steps: run an X11 server on your local machine, and forward X11 through SSH.

Go ahead and set this up now, even if you're not excited about looking at the spectrum analyzer video feed. There will be other cases where you want GUI access to the remote lab computers.

### Running X11 on Your Local Machine

If your local machine is running Linux with a GUI desktop, congratulations! You're almost done with this step. Edit `/etc/ssh/sshd_config` and look for (or add) a line for `X11Forwarding`. Set it to `yes` and save the file.

If your local machine is running macOS, you need to install
[Xquartz](https://www.xquartz.org/) (unless you already have). Edit `/etc/ssh/sshd_config` and look for (or add) a line for `X11Forwarding`. Set it to `yes` and save the file. Depending on macOS version and probably Xquartz version, you may need to manually start Xquartz before starting your SSH session.

If your local machine is running Windows, you need to install an X11 server such as
[Xming](https://sourceforge.net/projects/xming/). You will need to manually start the server before starting your SSH session.

### Forwarding X11 over SSH

I'm going to assume you're already running SSH and able to access the Raspberry Pi in the remote lab. If not, check out [Setting Up for Remote Access to ORI Labs](ORI-Lab-User-Setup.md) for some guidance.

If you invoke SSH from the command line (Linux, macOS), just add `-X` to the command line. It will look something like this:
```
ssh -X ori-west
```

If you invoke SSH from a GUI (PuTTY on Windows), enable X forwarding in new or saved SSH sessions by selecting Enable X11 forwarding in the "PuTTY Configuration" window (Connection > SSH > X11).

### Simple Test of X11 Forwarding

I like to verify that X11 forwarding is working in the simplest way possible, before jumping into something fancy. One way to do this is to run the toy program `xeyes`.

Open an SSH session to the Raspberry Pi with X11 forwarding enabled.

Type `xeyes` at the command prompt.

Immediately you should see a new window pop up on your local screen. The window background should be transparent, and there should be two large cartoon eyeballs. If you move the mouse around, the pupils in these eyeballs should follow the mouse cursor around. This works all the time on Linux (where the whole GUI is in X11) but only while an X11 window has focus on other systems.

If that didn't work, nothing else is likely to work with X11, so take the time to debug it.

When you're done with Xeyes, you can exit it by hitting Ctrl-C in the terminal.

### Viewing the Video

Now that we're set up to run GUI programs, we can view the spectrum analyzer video.

One way to do that is to use the program `vlc` to view video from the capture device:

```
vlc v4l2:///dev/video0:width=1280:height=720 &
```

In that command line, `v4l2` means _Video for Linux version 2_ and identifies the type of stream to open. `/dev/video0` is the name of the device. If you don't specify the width and height to capture, you'll get an upscaled 1080p version of the video. 1280x720 is the native size of the video from the spectrum analyzer. If you choose some other size, you'll get the closest match that the capture device supports.

The ampersand at the end of the command line is optional. It tells the shell to run VLC in the background, freeing up your terminal for other work.

#### What if it's taking forever?

Under some circumstances we don't fully understand yet, forwarding X11 over SSH doesn't really work with VLC capturing video. In that case, skip ahead to the section on running video capture on a VNC screen instead.

#### v4l2 stream error: cannot select input 0: Device or resource busy

If you get a message from VLC saying *Device or resource busy*, the video capture device is probably in use by some other user. Only one user at a time can capture live video from the spectrum analyzer. You can find out who has it busy by running
```
ps aux | grep video0
```
on ori-west and looking at the first column in the response. Try to coordinate with them to share the video capture facility. If you can't contact them, you can `sudo kill -9 #####`, where ##### is the process number found in the second column in the response above. This forcibly disconnects them from the video capture device.

#### "cannot open device '/dev/video0'"

If the device `/dev/video0` cannot be opened, the video capture dongle is probably not plugged in. The device is only present when the dongle is plugged into a USB port on the Raspberry Pi *and* also connected to a video source. If the spectrum analyzer is off, or disconnected from video for some reason, the video device will disappear. Contact the Remote Lab admins (on Slack or by email) and request that the video capture be reconnected.

You will see other devices named `/dev/video10` through `/dev/video16`. These are associated with video features of the Broadcom BCM2835 SoC that is the heart of the Raspberry Pi. They are not able to capture external video, so they are not relevant for our purposes.

#### Disregard These Error Messages

If your SSH client is based on OpenSSH (most are), you'll very likely see a burst of error messages like these:

```
[b3a2f140] xcb generic error: shared memory server-side error: X11 error 10
[b3a2f140] xcb generic error: same error on retry: X11 error 10
[b3a2f140] xcb_x11 generic: using buggy X11 server - SSH proxying?
```

You'll also see some other messages when VLC starts, and possibly again when you shut it down.

The messages on startup may come out after the terminal prompt, so it might at first glance appear that you didn't get back a terminal prompt. You can just hit return to see a fresh prompt.

### Combining SSH and VLC Steps

If you're using X11 forwarding to your local machine, you can skip the step of logging in to the Raspberry Pi interactively. You can start the video playback right from your own machine's command line, like so:

```
ssh -X -f ori-west vlc v4l2:///dev/video0:width=1280:height=720
```

Here the `-f` flag tells SSH to put the program into the background before running the `vlc` command. This releases your local terminal for other tasks. (You don't need an ampersand at the end of the command in this case.)

### Using VLC

VLC will pop up a GUI window with the spectrum analyzer video in it. Everything is more or less self-explanatory.

If you need a still image screenshot for your records or for documentation, you can make one by choosing `Take Snapshot` from the `Video` menu. A screenshot taken this way won't be quite as crisp as one taken digitally over the remote control interface directly on the instrument, but it will be good enough for most purposes.

When you're done with the video, quit VLC in any of the usual ways.

## Access via VNC

If you're already running a GUI session on the Raspberry Pi via VNC for some other reason, you can include the video capture window within that GUI. The command to start capturing video is the same, you'd just run it from a terminal window within the VNC screen:

```
vlc v4l2:///dev/video0:width=1280:height=720 &
```

However, if your VNC screen is already crowded, you can still run the video capture outside of VNC via X11 forwarding, as detailed above. This would be useful if your local machine has two monitors. You might run VNC in full-screen mode on one monitor, and display the video by X11 forwarding in a window on the other monitor.

## Access via Streaming

It would probably use network bandwidth more efficiently if we streamed the spectrum analyzer video from the lab to a program running on your local machine. We don't have that set up yet, but this document will be updated if and when we do.

