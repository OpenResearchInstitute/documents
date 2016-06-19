#Protocol Data Unit
class PDU:
	def __init__(self):
		self.data = [0,0,0,0,0,0,0,0,0,0,0,0]
		#demo data [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]

#Encapsulated Packet Unit = GSE Packet
class EPU:
	def __init__(self):
		self.data = [0,0,0,0,0,0,0,0,0,0,0,0]
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
	
class AF_queue:
	
class BE_queue:
	
class ACM_updater:
	
class Priority_solver:
	
class Timeout_scheduler:
	
class Priority_scheduler: