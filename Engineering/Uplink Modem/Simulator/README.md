# M17 Uplink Simulations

The baseline Phase 4 voice uplink is a bunch of M17 channels. In order to enable testing of a multichannel receiver implementation, we're working on building an offline simulator that generates a massively multichannel uplink. Here's what we've made so far.

[m17-upsim-1-stream.grc](m17-upsim-1-stream.grc) is a GNU Radio flowgraph that transmits a single M17 stream, taken from a symbol stream file created by `m17-mod -b` from the [m17-cxx-demod](https://github.com/mobilinkd/m17-cxx-demod) reference implementation. This is identical to what we demonstrated at a PARC/IEEE meeting on May 4, 2022. The audio source is an episode of [Amateur Radi Newsline](https://www.arnewsline.org).

[m17-upsim-3-identical-streams.grc](m17-upsim-3-identical-streams.grc) is a GNU Radio flowgraph that transmits a single M17 stream, taken from a premodulated stream file created by `m17-mod` without the `-b` flag, on three adjacent channels, using the *Frequency Shift* block. The audio source is a story taken from [Librivox](https://librivox.org), an archive of free public domain audiobooks.

[m17-upsim-3-distinct-streams.grc](m17-upsim-3-distinct-streams.grc) is a GNU Radio flowgraph that transmits three distinct M17 streams, each taken from a premodulated stream file created by `m17-mod`, on three adjacent channels, using the *Frequency Shift* block. The audio sources are stories taken from [Librivox](https://librivox.org), an archive of free public domain audiobooks.

## Build Notes

Steps to build `m17-mod` and friends on Ubuntu 20.04.4 (on the Chonc-A virtual machine in the ORI remote lab):

```sudo apt install sox ffmpeg libcodec2-dev libboost-program-options1.67-dev libgtest-dev
git clone https://github.com/mobilinkd/m17-cxx-demod
cd m17-cxx-demod
mkdir build
cd build
cmake ..
make
make test
sudo make install
```

## Audio File Conversion

We will need lots of speech audio files, so we downloaded some from [Librivox](https://librivox.org), an archive of free public domain audiobooks. These files were in MP3 format. Since `m17-mod` requires a different format, these files needed converting. There are many tools that can do this conversion. We used [ffmpeg](https://ffmpeg.org).

```
ffmpeg -i somefile.mp3 -f s16le -acodec pcm_s16le -ac 1 -ar 8000 somefile.wav
```
The output .wav file is 16-bit signed integer values, single channel, at a sample rate of 8000 Hz. There's no header, so this file won't be playable by most audio players. If you have [SoX](http://sox.sourceforge.net) installed, it can be played like so:
```
play -q -b 16 -r 8000 -c1 -t s16 somefile.wav
```

Then, to make pre-modulated M17 files,

```
cat somefile.wav | m17-mod -S KB5MU >somefile.bin
```

This file is at 48 kHz and again 16-bit single-channel, but is not fully modulated. It is the input to an FM modulator. For now, the FM modulation is provided by the flowgraph.

If you want to check the modulated M17 file, you can convert it to a playable WAV file, like so:

```
cat somefile.bin | m17-demod -l -d >somefile-check.wav
```

## Receiving the Multichannel Uplink

For initial testing of these multichannel uplink flowgraphs, we have been using an [OpenWebRX](https://www.openwebrx.de) consisting of a Raspberry Pi 4 and an [SDRplay RSPdx](https://www.sdrplay.com/rspdx/). The OpenWebRX software has M17 demodulation built in, and provides a nice visualization of the frequency spectrum.

## Next Steps

These are just the first prototypes on the way to a multichannel uplink simulation.
