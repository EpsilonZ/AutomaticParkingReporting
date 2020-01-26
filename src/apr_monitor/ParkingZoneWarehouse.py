import os
import json
from ParkingZone import ParkingZone

class ParkingZoneWarehouse:

	def __init__(self, bboxes_file_path):
		#still to see if array is the best
		self.parkingZonesArray = [] 
		self.bboxes = self.__parse_parking_zones_from_config_specified_osm(os.environ.get('ACR_HOME') + '/' + bboxes_file_path)	

	def get_parking_zones(self):
		return self.parkingZonesArray

	def __parse_parking_zones_from_config_specified_osm(self, bboxes_file_path):

		with open(bboxes_file_path) as bboxes_file:

			first = False
			for street in bboxes_file:
				#street line in file follows this structure
				#streetName @@@ lat1 lon1 lat2 lon2 lat3 lon3 ... latn lonn where all the lat,lon make the bounding box of the street


				first_part_splitted = street.split("@@@")
				street_name = first_part_splitted[0][:-1] #le quitamos el espacio del final al nombre
				street_bbox = first_part_splitted[1].split(" ")

				#we delete the space that's before the first lattitude
				street_bbox.pop(0)
				#we delete the \n at the end of the line
				street_bbox = street_bbox[:-2]
				#We convert string type that's comming from the file to float 
				street_bbox= list(map(float,street_bbox))

				#We group by pairs (lat,lon) each gps position that forms the bounding box
				n = 2
				street_bbox= [ street_bbox[i:i+n] for i in range(0, len(street_bbox), n) ]

				max_lat = street_bbox[0][0]
				min_lat = street_bbox[0][0]
				max_lon = street_bbox[0][1]
				min_lon = street_bbox[0][1]

				#we look for top,left coordinates of the bounding box
				#we look for bottom,right coordinates of the bounding box
				for i in range(len(street_bbox)):
					if(street_bbox[i][0] > max_lat):
						max_lat = street_bbox[i][0]
					if(street_bbox[i][0] < min_lat):
						min_lat = street_bbox[i][0]
					if(street_bbox[i][1] > max_lon):
						max_lon = street_bbox[i][1]
					if(street_bbox[i][1] < min_lon):
						min_lon = street_bbox[i][1]

				#A little bit of bounding box definition with GPS coordinates (each x represents a point in a map)
				#
				#	    max lat,min lon
				#				x					x
				#
				#
				#
				#
				#				x					x
				#							min lat, max lon
				#required params (parkingzoneid, boundingBox, topLeftLimit, bottomRightLimit)
				parkingZone = ParkingZone(street_name, street_bbox, [max_lat,min_lon], [min_lat,max_lon])
				self.parkingZonesArray.append(parkingZone)


