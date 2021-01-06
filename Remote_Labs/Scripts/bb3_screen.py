#!/usr/bin/python3
#
# Get a screen image from the EEZ-BB3 Power Supply
# Open Research Institute -- Remote Lab West
# (instrument on loan from KB5MU)
#
# https://github.com/phase4ground/documents
#
import pyvisa as visa

rm = visa.ResourceManager('@py')
ps = rm.open_resource('TCPIP::eez-bb3.sandiego.openresearch.institute::5025::SOCKET')
ps.read_termination = '\r'
print(ps.query('*IDN?'))
screen_data = ps.query_binary_values(':DISP:DATA?', datatype='s', container=bytes)
with open('bb3_screen.jpg', 'wb') as f:
    f.write(screen_data)
print('bb3_screen.jpg written')
