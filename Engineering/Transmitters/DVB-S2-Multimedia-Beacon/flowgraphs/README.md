# Flowgraphs for DVB-S2 Multimedia Beacon Demos

These are GNU Radio Companion flowgraphs used to demonstrate prototype
DVB-S2 multimedia beacons.

The parameters used, unless noted otherwise:
- 5,000,000 symbols per second
- 16APSK modulation
- rate 9/10 coding
- pilots on

That produces a nominal bit rate of 17,413,400 bits/second in a bandwidth
of 5 MHz. These parameters were chosen by W6RZ to make a nice video demo.
W6RZ also prepared the MPEG transport stream file.

## Preparation

- [dvbs2_tx_rec.grc](hellokitti/dvbs2_tx_rec.grc) converts the TS file
containing the MPEG transport stream into a file full of samples ready
to play back through an SDR.

## Road Show October-November 2021

These were run on _Hello Kitti_ (a pink minitower computer running Ubuntu 20.04.3
on an Intel Core i7-4770 CPU at 3.40 GHz with 16GB RAM)
for demonstrations at:
- San Bernardino Microwave Society (2021-10-07)
- DC 858/619 local DEFCON Meetup (2021-10-13)
- San Diego Microwave Society (2021-10-18)
- Palomar Amateur Radio Club (2021-11-03) (virtual)

These were demonstrated using a BladeRF 2 Mini (xA9 type), but the flowgraphs
also contain (disabled) sink blocks for USRP and HackRF.

- [playback.grc](hellokitti/playback.grc) merely plays back a file full of
samples, pre-built by the flowgraph above.
- [dvbs2_tx_demo1.grc](hellokitti/dvbs2_tx_demo1.grc) does the conversion of
the TS file containing the MPEG transport stream on the fly and sends it to
the SDR.
- [dvbs2_tx_demo2_namedpipe.grc](hellokitti/dvbs2_tx_demo2_namedpipe.grc)
takes an MPEG transport stream from a
named pipe, converts it on the fly, and sends it to the SDR. The named pipe
was fed using the script [runvideo.sh](../runvideo.sh), which uses `ffmpeg`
to transcode the video from a Linux webcam and then pad it out to the
necessary bit rate corresponding to the symbol rate and MODCOD in use.

## Experiments Using Raspberry Pi

During the road show we were asked about using a less powerful computer
to run the transmit flowgraphs, so we some experiments with _Kevin Beacon_, a
Raspberry Pi 4B version 1.4 with 8GB RAM running Raspbian 10 Buster.

- [playback-10GHz.grc](kevin/playback-10GHz.grc) plays back the file full of
precomputed samples. This keeps all four cores about 30% busy.
- [fromts-10GHz.grc](kevin/fromts-10GHz.grc) does the conversion of the TS file
on the fly and sends it to the SDR. This flowgraph is challenging for Kevin
to run. It runs fine with nothing extra going on, but with the GNU Radio
Companion flowgraph window displayed, and a terminal window running `htop`,
the CPU can't keep up.
- [webcam-10GHz.grc](kevin/webcam-10GHz.grc) takes an MPEG transport stream
from a named pipe, converts it on the fly, and sends it to the SDR. The named pipe
was fed using the script [runvideo.sh](../runvideo.sh), which transcodes the
video from a Linux webcam and then pads it out to the necessary bit rate
corresponding to the symbol rate and MODCOD in use. This flowgraph *does not work*
on the Raspberry Pi, apparently because the CPU just isn't fast enough.
- [webcam-10GHz-2msym-qpsk35.grc](kevin/webcam-10GHz-2msys-qpsk35.grc) is a
modified version of the above flowgraph that uses different parameters,
chosen to support an adequate bit rate for the webcam at 640x480 resolution:
2,000,000 symbols/sec, QPSK modulation, and rate 3/5 coding. This required
a modified version of the `ffmpeg` command with `-muxrate 2320054`, and worked
reliably on Kevin with CPU utilization around 45% on all four cores.

## Etc.

- [dvbs2_tx_vcm.grc](hellokitti/dvbs2_tx_vcm.grc) transmits a VCM (variable
coding and modulation) transmission composed of three different MODCODs.
We do not yet have a receive setup that can handle this. With MiniTioune
you can see evidence of the various modulations in the constellation diagram.
