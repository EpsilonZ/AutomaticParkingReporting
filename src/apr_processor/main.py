import os
import json
from Config import Config
from ParkingZoneWarehouse import ParkingZoneWarehouse
import argparse
import time
from GPSReceiver import GPSReceiver
from Ultrasonic import Ultrasonic
import socket

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

