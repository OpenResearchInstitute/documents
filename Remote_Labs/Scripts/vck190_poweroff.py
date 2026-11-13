#!/usr/bin/python3
# Use pexpect to interact with the EZmation.com USB power switch
# to turn the power off.

import pexpect
import sys
import time
from pathlib import Path

power_switch_serial_number = 'A5XK3RJT' # set this to match your power switch

# This is an alias to the USB serial device with the specified serial number,
# automatically created by the operating system when the device is enumerated.
power_switch_path = f'/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_{power_switch_serial_number}-if00-port0'

def report_status():
   child.sendline('?')
   i = child.expect(['ON\r\n', 'OFF\r\n'], timeout=1)
   if i == 0:
      print('Power is on.')
   elif i==1:
      print('Power is off.')
   else:
      print('Can\'t get the current power status!')

# First, check if the serial port to the power switch exists.
if not Path(power_switch_path).is_char_device():
   print('The USB power switch is not connected!');
   sys.exit(1)

# Now, check to see if the serial port to the power switch is already in use
(fuser_output, fuser_exitstatus) = pexpect.run(
      f'fuser -u {power_switch_path}',
      withexitstatus=True
)
if fuser_exitstatus == 0:
   print('Power switch serial port is already in use!')
   print('Here is the port name, the process ID, and the user name:')
   print(fuser_output.decode())
   sys.exit(1)

child = pexpect.spawn(f'screen {power_switch_path} 115200')
child.expect('\x1b\[2J', timeout=5)	# clear terminal screen at screen startup
child.expect('\x1b\[2J', timeout=1)	# screen sends two screen clears

child.sendline('?')			# get current power switch status
try:
   i = child.expect(['ON\r\n', 'OFF\r\n', 'invalid command\r\n',  pexpect.EOF, pexpect.TIMEOUT], timeout=1)
   if i==0:
      print('Power is on; turning it off now.')
      child.sendline('OFF')
      report_status()
   elif i==1:
      print('Power switch is already off.')
   elif i==2:
      print('Power switch reports an invalid command\n')
   elif i==3:
      print('Could not open the power switch serial port.')
      print('Are you in the dialout group?')
   elif i==4:
      print('Nothing happened for 5 seconds!\n')
   else:
      print('screen reported some unexplained value!\n')
finally:
   child.send('\01ky')	# Ctrl-A k y is screen's command to exit
   child.expect(pexpect.EOF, timeout=1)
