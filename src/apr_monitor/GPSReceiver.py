import os
import socket
import threading
from Position import Position

class GPSReceiver:

	def __init__(self, deviceIP, devicePort):
		self.deviceIP = deviceIP
		self.devicePort = devicePort
		#we use TCP
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((deviceIP, devicePort))
		#manages thread
		self.receive_gps_thread_id = None
		#array of gps points since last retrieval

	def start_gps_receiver(self):

		self.receive_gps_thread_id = threading.Thread(target=self.__rcv_data_from_gps, daemon=True)
		self.receive_gps_thread_id.start()

	def stop_gps_receiver(self):

		self.receive_gps_thread_id.do_run=False

	def __rcv_data_from_gps(self):

		t = threading.currentThread()
		self.sock.listen(1)

		while getattr(t, "do_run", True):

			connection, client_addr = self.sock.accept()
			print("accepted conn")
			data = self.__recvall(connection)
			lat,lon,speed = data.split(",")
			print ("g:" + str(lat) + "," + str(lon))

			connection.close()

	def __recvall(self,sock):
		BUFF_SIZE = 1 # 4 KiB
		data = b''
		while True:
			part = sock.recv(BUFF_SIZE)
			data += part
			recv_end = data.decode('utf-8').find('\n')
			if recv_end != -1:
				break
		return data.decode('utf-8')[:-1]

