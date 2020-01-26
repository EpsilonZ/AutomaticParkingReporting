import os
import json
import argparse
import time
import socket
from GPSReceiver import GPSReceiver
from Position import Position
from Ultrasonic import Ultrasonic
from ParkingZoneWarehouse import ParkingZoneWarehouse
from Config import Config
from ParkingZoneDetector import ParkingZoneDetector

parkingZoneWarehouse = None
parkingZoneDetector = None
ultrasonic = Ultrasonic("JSN-SR04T", 18, 24)
received_gps_positions = []
in_parking_zone = 0

file_parking_zone_tmp_output_file = open("tmp_monitor_output/last_parking_zone_data.txt",'w')

def recvall(self,sock):

	BUFF_SIZE = 1 # 1 KiB
	data = b''
	recv_end = 0
	while recv_end != -1:
		part = sock.recv(BUFF_SIZE)
		data += part
		recv_end = data.decode('utf-8').find('\n')

	return data.decode('utf-8')[:-1]

def process_position_received(position):

	last_parking_zone_detected = parkingZoneDetector.get_last_parking_zone_detected()
	actual_parking_zone = None

	if (last_parking_zone_detected != None and parkingZoneDetector.is_position_in_parking_zone(position, last_parking_zone_detected)):
		actual_parking_zone = last_parking_zone_detected

	else:
		if (is_position_in_any_parking_zone(position)):
			actual_parking_zone_detected = parkingZoneDetector.get_last_parking_zone_detected()

	#if vehicle is in parking zone
	if(actual_parking_zone_detected != None):
		parking_zone_tmp_output_file.write(position)
		if(in_parking_zone):
			print ("WE ENTERED IN A PARKING ZONE!")
			in_parking_zone = 1
			#we get the last ultrasonic shots to clear buffer as they were not in a parking zone and not save them
			cleannedBuffer = ultrasonic.get_ultrasonic_shots()
		else:
			parking_zone_tmp_output_file.write(ultrasonic.get_ultrasonic_shots())
	
	#if actual parking zone is not a parking zone and we were in a parking zone in previous gps received or last parking zone is different than actual
	elif (actual_parking_zone_detected == None and last_parking_zone_detected != None or \
		  actual_parking_zone_detected != None and last_parking_zone_detected != None and actual_parking_zone_detected != last_parking_zone_deteted):

		in_parking_zone = 0

		parking_zone_tmp_output_file.write(ultrasonic.get_ultrasonic_shots())
		parking_zone_tmp_output_file.write(position)

		process_ended_parking_zone()

def process_ended_parking_zone():

	return 0
				

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("json_config", help="city json configuration")
	parser.add_argument("--verbose", help="increase output info for debug purposes", action="store_true")
	args = parser.parse_args()
	if(args.verbose):
		print("Verbose enabled")

	config = Config(args.json_config)
	if(args.verbose):
		print("Config file: " + config.config_file_info())

	parkingZoneWarehouse = ParkingZoneWarehouse(config.get_bboxes_config_file_path())
	if(args.verbose):
		print("Sample parking zone from parking zones warehouse: " + str(parkingZoneWarehouse.get_parking_zones()[0])) 

	parkingZoneDetector = ParkingZoneDetector(parkingZoneWarehouse)


	init_gps_listener = 0
	point_within_parkingZone = 0

	sock = socket.socket(AF_INET, socket.SOCK_STREAM)
	sock.bind(('0.0.0.0',15000))
	sock.listen(1)

	while(True):

		connection, client_addr = sock.accept()

		print ("accepted conn")
		if (init_gps_listener==0):
			print ("starting ultrasonic shoting")
			ultrasonic.start_ultrasonic_shoting()

		data = recvall(connection)
		connection.close()

		lat,lon,speed = data.split(",")
		print ("g:" + str(lat) + "," + str(lon))

		position = Position([float(lat),float(lon)])
		process_position_received(position)
		
if __name__ == "__main__":
	main()
