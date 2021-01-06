#!/usr/bin/env python3
#
# Get a screen image from every instrument
# Open Research Institute -- Remote Lab West
#
# Requires convert from ImageMagick, apt get imagemagick
# Requires image viewer feh, apt get feh
#
# https://github.com/phase4ground/documents
#
import os

os.system("./bb3_screen.py")
os.system("./os_screen.py")
os.system("./ps_screen.py")
os.system("./sa_screen.py")
os.system("./sg_screen.py")

# make PNGs to shrink large BMP files
os.system("convert -quiet ps_screen.bmp ps_screen.png")
os.system("convert -quiet sa_screen.bmp sa_screen.png")
os.system("convert -quiet sg_screen.bmp sg_screen.png")

# if we have X11, display all the screenshots as clickable thumbnails
if "DISPLAY" in os.environ:
    os.system("feh -t bb3_screen.jpg os_screen.jpg ps_screen.png sa_screen.png sg_screen.png &")
else:
    os.system("zip -q all_screen.zip bb3_screen.jpg os_screen.jpg ps_screen.png sa_screen.png sg_screen.png")
    print("Graphics not available. Fetch all_screen.zip for local viewing.")


