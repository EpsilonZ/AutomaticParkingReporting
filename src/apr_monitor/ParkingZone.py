import os
import json
import Position

class ParkingZone:

	def __init__ (self, parkingzoneid, boundingBox, topLeftLimit, bottomRightLimit):
		self.boundingBox = boundingBox
		self.parkingzoneid = parkingzoneid
		self.topLeftLimit = topLeftLimit
		self.bottomRightLimit = bottomRightLimit

	def __str__(self):
		return str(self.__class__) + ": " + str(self.boundingBox)

	def get_bbox(self):
		return self.boundingBox
