import win32com.client
import pythoncom
import datetime
import time
import os
# import numpy
# from numpy import *
Pwr_sense2 = win32com.client.Dispatch("mcl_pm.USB_PM")
Pwr_sense2.Open_AnySensor()
 
Pwr_sense2.Freq=500000000/1e6
Pout=Pwr_sense2.ReadPower()
print ('%3.2f'%(Pout))
