import json
import os
from Position import Position
from ParkingZone import ParkingZone

class ParkingZoneDetector:

	def __init__(self, parkingZoneWarehouse):
		self.position_near_or_within_parking_zone = False
		self.parkingZoneWarehouse = parkingZoneWarehouse
		self.last_parking_zone_detected = None

	def is_position_in_any_parking_zone(self, position):

		parkingZones = self.parkingZoneWarehouse.get_parking_zones()
		i = 0
		is_position_within_a_parkingZone = False

		while(i < len(parkingZones) and not is_position_within_a_parkingZone):
			is_position_within_a_parkingZone = self.is_position_in_parking_zone(position, parkingZones[i])
			if(is_position_within_a_parkingZone):
				self.last_zone_detected = parkingZones[i]
			i = i + 1

		return is_position_within_a_parkingZone

	def get_last_parking_zone_detected(self):
		return self.last_parking_zone_detected

	def is_position_in_parking_zone(self, position, parkingZone):
		return self.__check_if_position_is_near_or_within_parking_zone(position, parkingZone)

	def __distance_from_position_to_zone(self, position, boundingBox):
		#todo but in other projects something didn't look it worked out
		return 0

	def __is_position_within_parking_zone_boundingbox(self, position, boundingbox):

		#source code can be found at https://wrf.ecse.rpi.edu//Research/Short_Notes/pnpoly.html

		"""
		x, y -- x and y coordinates of point
		poly -- a list of tuples [(x, y), (x, y), ...]
		"""

		num = len(boundingbox)
		i = 0
		j = num - 1
		c = False

		x = position.get_lat()
		y = position.get_lon()

		for i in range(num):
			if ((boundingbox[i][1] > y) != (boundingbox[j][1] > y)) and \
				    (x < boundingbox[i][0] + (boundingbox[j][0] - boundingbox[i][0]) * (y - boundingbox[i][1]) /
				                      (boundingbox[j][1] - boundingbox[i][1])):
				c = not c
			j = i

		return c


	def __check_if_position_is_near_or_within_parking_zone(self, position, parkingZone):

		#we first check if its within a zone
		is_within_a_zone = self.__is_position_within_parking_zone_boundingbox(position, parkingZone.get_bbox())
		#we check if parkingZone is near enough
		#this is still in test so nothing to do more

		return is_within_a_zone


