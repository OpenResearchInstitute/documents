#!/usr/bin/python3
#
# Get a screen image from the DSG821A Signal Generator
# Open Research Institute -- Remote Lab West
#
# https://github.com/phase4ground/documents
#
import pyvisa as visa

rm = visa.ResourceManager('@py')
sg = rm.open_resource('TCPIP::dsg821a::INSTR')
print(sg.query('*IDN?').strip())

screen_data = sg.query_binary_values(':PRIV:SNAP? BMP',datatype='B',container=bytearray,delay=0.2)
with open('sg_screen.bmp', 'wb') as f:
    f.write(screen_data)
print('sg_screen.bmp written')
