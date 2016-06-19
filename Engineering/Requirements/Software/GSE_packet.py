from struct import *
import binascii


##Crash course in struct:
#>>> from struct import *
#>>> pack('hhl', 1, 2, 3)
#'\x00\x01\x00\x02\x00\x00\x00\x03'
#>>> unpack('hhl', '\x00\x01\x00\x02\x00\x00\x00\x03')
#(1, 2, 3)
#>>> calcsize('hhl')
#8
#>>> pack('!bbb', 1, 2, 3)
#'\x01\x02\x10'

##GSE header
#Start indicator one bit
#End indicator one bit
#label type indicator two bits
#there's GSE-length, which is 12 bits
#16 bits is two bytes
#so the possible combinations?
#11101111 is 15, 16

#if start indicator == 0 and end indicator == 0 and label type indicator == 0
# then there are four padding bits, and padding bytes?


#Protocol Data Units are the things we want to encapsulate
PDU_default_data = pack('!2b', 15, 16)
print "PDU_default_data is", PDU_default_data

class PDU:
	def __init__(self):
		self.data = PDU_default_data
		self.size = (calcsize('2b'))

#Encapsulated Packet Unit = GSE Packet
class EPU:
	def __init__(self):
		self.data = pack('!bb', 0xe, 0xf)
		self.size = calcsize('!bb')
		#demo data [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]
	

#Baseband frame
class BBF:
	def __init__(self):
		self.data = [0,0,0,0,0,0,0,0,0,0,0,0]
		#demo data [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]

#one of two topmost units that make GSE packets
class PDU_manager:
	def __init__(self):
		self.data = [0,0,0]
		#for example

#one of two topmost units that make GSE packets
class EPU_manager:
	def __init__(self):
		self.data = [0,0,0]
		#for example
		
#stores received PDU packets 
#Provides QoS and ACM support
#ACM FIFO queues
#three priority levels
#each priority level has a different ACM mode
class Scheduler_queue:
	def __init__(self):
		self.data = [0,0,0]
		#for example

class EF_queue:
	def __init__(self):
		self.data = [0,0,0]
		#for example
	
class AF_queue:
	def __init__(self):
		self.data = [0,0,0]
		#for example

	
class BE_queue:
	def __init__(self):
		self.data = [0,0,0]
		#for example
	
class ACM_updater:
	def __init__(self):
		self.data = [0,0,0]
		#for example
	
class Priority_solver:
	def __init__(self):
		self.data = [0,0,0]
		#for example

	
class Timeout_scheduler:
	def __init__(self):
		self.data = [0,0,0]
		#for example

	
class Priority_scheduler:
	def __init__(self):
		self.data = [0,0,0]
		#for example
		
a = PDU()
print "PDU data is", a.data
print "PDU data size in bytes is", a.size

b = EPU()
print "EPU data is", b.data
print "EPU data size in bytes is", b.size