#this is what I used first
from struct import *
import binascii

#this is what was recommended by mossman
from bitstring import BitArray, BitStream


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
#maybe these are a bitstream? Probably not? 

default_start = '0b1'
default_stop = '0b1'
default_label_type = '0b11'
#00 6-byte label is present and shall be used for filtering
#01 3-byte label is present and shall be used for filtering
#10 Broadcast. No label field present. All Rx shall process this packet.
#   This combination shall be used also in non-broadcast systems when 
#   no filtering is applied at Layer 2, but IP header processing is utilized.
#11 Label re-use. No label field is present. All Rx shall reuse the label 
#   that was present in the previous Start or Complete GSE Packet of the 
#   same Base Band frame. This method is used for transmitting a sequence 
#   of GSE packets with the same label without repeating the label field. 
#   This value shall not be used for the first GSE packet in the frame. 

default_GSE_length = '0b000000000000'


default_fragment_ID = '0b11111111'

default_total_length = '0b0000000011111111'

default_protocol_type = '0b0000000011111111'

#default_label presence and length depends on the label type
if default_label_type == '0b00':
	default_label = '0b000000001111111100000000111111110000000011111111'
elif default_label_type == '0b01':
	default_label = '0b000000001111111100000000'
else:
	default_label = None



zero_prefix = '0b00000'
H_LEN = '0b111'
#001 optional extension header length of 2 bytes
#010 optional extension header length of 4 bytes
#011 optional extension header length of 6 bytes
#100 optional extension header length of 8 bytes
#101 optional extension header length of 10 bytes
H_TYPE = '0b11111111'
#represents either one of 256 Mandatory Extension Headers or
#represents one of 256 Optional Extension Headers
default_extension_header_1 = zero_prefix+H_LEN+H_TYPE


#default_extension_header_2 =

class PDU:
	def __init__(self):
		start = BitArray(default_start)
		stop = BitArray(default_stop)
		label_type = BitArray(default_label_type)
		
		if start == '0b1' && end == '0b0' && label_type == '0b00':

#N1 is the number of bytes until the end of the Base Band frame.
		Padding_bits
		for(i=0;i<N1;i++) {
		Padding_bytes
		

		}
		
		
		GSE_length = BitArray(default_GSE_length)

		fixed_header = start+stop+label_type+GSE_length
		label = BitArray(default_label)

		self.data = fixed_header+label
		self.size = len(self.data)

#Encapsulated Packet Unit = GSE Packet
class EPU:
	def __init__(self):
		self.data = pack('!bb', 0xe, 0xf)
	

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
print "PDU data size is", a.size