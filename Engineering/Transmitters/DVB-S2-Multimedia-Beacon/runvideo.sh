#!/bin/sh
ffmpeg -i /dev/video0 -vcodec libx264 -preset ultrafast -tune zerolatency -acodec copy -muxrate 17413400 -f mpegts pipe:1 > ~/Documents/test.ts

