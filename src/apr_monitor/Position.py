import os
import json

class Position:

	def __init__(self, gpsPosition):
		self.gpsPosition = gpsPosition

	def get_gps(self):
		return self.gpsPosition

	def update_gps(self, newGPSPosition):
		self.gpsPosition = newGPSPosition

	def get_lat(self):
		return self.gpsPosition[0]

	def get_lon(self):
		return self.gpsPosition[1]

	def __str__(self):
		return str(self.get_lat())+","+str(self.get_lon())

