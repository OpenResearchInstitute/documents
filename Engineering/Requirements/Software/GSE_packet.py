#this is what was recommended by mossman
from bitstring import BitArray, BitStream



#Baseband frame information
#should this be an object?
#N1 is the number of bytes until the end of the Base Band frame.
N1 = 10


#if start indicator == 0 and end indicator == 0 and label type indicator == 0
# then there are four padding bits, and padding bytes?


#Protocol Data Units are the things we want to encapsulate
#maybe these are a bitstream? Probably not? 
#How about making it a random value every time we run the code?

default_start = '0b1'
default_stop = '0b0'
default_label_type = '0b01'
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

default_GSE_length = '0b101010101010'

default_fragment_ID = '0b01010101'

default_total_length = '0b1110111011101110'

default_protocol_type = '0b00100010001000100010'

#default_label presence and length depends on the label type
if default_label_type == '0b00':
	print "label type is 00"
	default_label = '0b101011010101010110101101010101011010110101010101'
	print "Six byte label"
elif default_label_type == '0b01':
	print "label type is 01"
	default_label = '0b101011010101010101010101'
	print "three byte label"
else:
	default_label = None
	print "label type was not 00 or 01. That means no label."



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
		print "start is ", start
		stop = BitArray(default_stop)
		print "stop is ", stop
		label_type = BitArray(default_label_type)
		print "label type is", label_type



		#they have to exist before we can use them
		padding = BitArray()
		fragment_ID = BitArray()
		total_length = BitArray()	
		protocol_type = BitArray()	
		label = BitArray()


		
		if start == '0b0' and stop == '0b0' and label_type == '0b00':
			print "padding condition has been met"

#N1 is the number of bytes until the end of the Base Band frame.
#how do we get N1? Keep track of it with calculations.
			for x in range(0, N1-1):{
			padding.append('0b00000000')
			}
			
		
		GSE_length = BitArray(default_GSE_length)
		
		
		if start == '0b0' and stop == '0b0':
			fragment_ID = BitArray(default_fragment_ID)
			print "fragment ID condition has been met and fragment ID value is", fragment_ID
		
		if start == '0b1' and stop == '0b0':
			total_length = BitArray(default_total_length)
			print "total length field condition has been met and total length value is", total_length
		
		if start == '0b1':
			protocol_type = BitArray(default_protocol_type)
			print "protocol type field condition has been met and protocol type value is", protocol_type
			if label_type == '0b00':
				label = BitArray(default_label)
				print "six byte label condition has been met and the label is", label
			elif label_type == '0b01':
				label = BitArray(default_label)
				print "three byte label condition has been met and the label is", label


		fixed_header = start+stop+label_type+GSE_length

		self.data = fixed_header+padding+fragment_ID+total_length+protocol_type+label
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