#!/usr/bin/python3
#
# Get a screen image from the DS1104Z Oscilloscope
# Open Research Institute -- Remote Lab West
#
# https://github.com/phase4ground/documents
#
import pyvisa as visa

rm = visa.ResourceManager('@py')
oscope = rm.open_resource('TCPIP::ds1104.sandiego.openresearch.institute::INSTR')
print(oscope.query('*IDN?'))
oscope.write(':STOP; *WAI')
screen_data = oscope.query_binary_values(':DISP:DATA? ON,OFF,JPEG', datatype='s', container=bytes)
with open('os_screen.jpg', 'wb') as f:
    f.write(screen_data)
print('os_screen.jpg written')
