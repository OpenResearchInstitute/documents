# Scripts for ORI Remote Labs

This directory includes scripts for controlling the instruments in the ORI Remote Labs. These scripts are useful on their own, but are meant primarily to be starting points for your own programs to control the instruments.

The instruments are connected to the Remote Lab local area network. They can be accessed from any host or virtual host on the network, and also from any host connected to Wireguard. See [ORI Lab User Setup](../ORI-Lab-User-Setup.md) for information on how to connect to the Remote Lab LAN.

Most of the instruments are controlled using [SCPI](https://en.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments) commands via [VISA](https://en.wikipedia.org/wiki/Virtual_instrument_software_architecture). See [Getting Screenshots](../Getting%20Screenshots.md) for an introduction to SCPI/VISA programming for Remote Lab instruments. See also the [Test Equipment Documentation](../Test_Equipment) for information on the commands available for each instrument. Most instruments have a separate "programming manual", rather than including the remote control details in the main user manual.

## Prerequisites for all scripts

* Python 3
* pip3 install pyvisa pyvisa-py
* a connection to the Remote Lab LAN

## Screen Shot Scripts

__A note about screen images:__ not all of these instruments have documented procedures for obtaining a screenshot, but they all implement that function. Unfortunately, not all in the same way. We've gathered up lore from various sources to implement working screen shot scripts for all the instruments. There is no guarantee that the methods used here are the best available methods, or that they will continue to work with other firmware versions in the instruments.

### `bb3_screen.py`
Get a screen image from the EEZ-BB3 Power Supply.  Writes a 480x272 pixel JPEG file named `bb3_screen.jpg` to the current directory.

### `os_screen.py`
Get a screen image from the DS1104Z Oscilloscope.  Writes a 800x480 pixel JPEG file named `bb3_screen.jpg` to the current directory.

### `ps_screen.py`
Get a screen image from the DP832 Power Supply. Writes a 320x240 pixel BMP file named `ps_screen.bmp` to the current directory.

### `sa_screen.py`
Get a screen image from the RSA5065N Spectrum Analyzer. Writes a 1024x600 pixel BMP file named `sa_screen.bmp` to the current directory. Note that the spectrum analyzer also has a [Web Control](http://rsa5065n.sandiego.openresearch.institute) interface that gives the remote user total control over the instrument, almost as if sitting in front of it. It's faster and easier to make a screen shot using Web Control, unless you need it to be automated. Surprisingly, you can run this script even while Web Control is running.

### `sg_screen.py`
Get a screen image from the DSG821A Signal Generator. Writes a 320x240 pixel BMP file named `sg_screen.bmp` to the current directory.

### `all_screen.py`
Get a screen image from each of the instruments, which it places in a new subdirectory of the current directory named with the date and time, like this: `20250206-125959`. It converts the bulky BMP files into smaller PNG files. Then, if the terminal connection supports X11, it attempts to open the image viewer `feh` to display all the images. If X11 is not supported, it combines all the images into a zip file named `all_screen.zip` and leaves the zip file for you download.

This script requires that ImageMagick be installed, and all the individual script files above must be in the current directory.

### `mod_all_screen.py`
Like `all_screen.py` except it doesn't use a subdirectory.

## Other Scripts

### `sa_peak.py`
Reads the frequency of a peak value from the RSA5065N Spectrum Analyzer. Manually set up the spectrum analyzer to focus on a single peak, such as the local oscillator leakage from a connected SDR device. The signal of interest must be consistently the strongest peak on the spectrum analyzer display. For most precise results, use the narrowest practical frequency span and resolution bandwidth settings. Modify the settings at the top of the script to set the nominal frequency of the peak and to control the number of measurements recorded, then run the script. If no errors occur, the script will output the number of lines you specified. Each line will contain a timestamp (in decimal seconds since the Unix epoch) and the difference between the measured peak frequency and the nominal frequency. You can then graph these results or analyze them in any other way.
