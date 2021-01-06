#!/usr/bin/env python3
#
# Get a screen image from the DP832 Power Supply
# Open Research Institute -- Remote Lab West
#
# https://github.com/phase4ground/documents
#
import pyvisa as visa

rm = visa.ResourceManager('@py')
# ps = rm.open_resource('USB0::0x1AB1::0x0E11::DP8C222902347::INSTR')
ps = rm.open_resource('TCPIP::dp832.sandiego.openresearch.institute::INSTR')
print(ps.query('*IDN?').strip())

screen_data = ps.query_binary_values(':SYST:PRINT? BMP',datatype='B',container=bytearray,delay=0.2)
with open('ps_screen.bmp', 'wb') as f:
    f.write(screen_data)
print('ps_screen.bmp written')
