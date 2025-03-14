#!/usr/bin/env python3
#
# Control the DSG821A Signal Generator: increment frequency by 1 Hz
# Open Research Institute -- Remote Lab West
#
# https://github.com/phase4ground/documents
#
import pyvisa as visa

rm = visa.ResourceManager('@py')
sg = rm.open_resource('TCPIP::dsg821a.sandiego.openresearch.institute::INSTR')
print(sg.query('*IDN?').strip())

freq = float(sg.query(':FREQ?'))
freq += 1.0
sg.write(f'FREQ {freq}')
print(sg.query(':FREQ?'))
