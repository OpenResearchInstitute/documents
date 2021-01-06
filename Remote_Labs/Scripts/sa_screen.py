#!/usr/bin/env python3
#
# Get a screen image from the RSA5065N Spectrum Analyzer
# Open Research Institute -- Remote Lab West
#
# https://github.com/phase4ground/documents
#
import pyvisa as visa

rm = visa.ResourceManager('@py')
sa = rm.open_resource('TCPIP::rsa5065n.sandiego.openresearch.institute::INSTR')
print(sa.query('*IDN?'))
screen_data = sa.query_binary_values(':PRIV:SNAP? BMP', datatype='s', container=bytes)
with open('sa_screen.bmp', 'wb') as f:
    f.write(screen_data)
print('sa_screen.bmp written')
