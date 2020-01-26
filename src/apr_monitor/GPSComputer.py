import threading
import geopy.distance
from Position import Position

class GPSComputer:

	def __init__(self, gpsfrec):
		self.gpsfrec = gpsfrec

	def compute_gps_points_in_ultrasonic_shots(self, numberOfShots, originPosition, destinationPosition):

		array_gps_points_in_ultrasonic_shots = []

		originLat = originPosition.get_lat()
		originLon = originPosition.get_lon()

		destinationLat = destinationPosition.get_lat()
		destinationLon = destinationPosition.get_lon()

		latDiff = abs(destinationLat - originLat)
		lonDiff = abs(destinationLon - originLon)

		interval_X = latDiff / (numberOfShots + 1)
		interval_Y = lonDiff / (numberOfShots + 1)

		k=1

		while (k<=puntosIntermedios):

			interPointLat = puntoAX+interval_X*k	
			interPointLon = puntoAY+interval_Y*k 

			array_gps_points_in_ultrasonic_shots.append([interPointLat, interPointLon])

			k+=1

		return array_gps_points_in_ultrasonic_shots

	def distance_between_points(self, originPosition, destinationPosition):

			return (geopy.distance.distance(originPosition, destionationPosition).km*1000)
