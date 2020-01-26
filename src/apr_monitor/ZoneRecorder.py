from Recorder import Recorder
import os
import time
import pathlib
from ParkingZoneWarehouse import ParkingZoneWarehouse

class ZoneRecorder:

	def __init__(self, camera_map, parkingZoneWarehouse, verboseEnabled):
		self.camera_map = camera_map
		self.recorder_map = {}
		#not used but will be in the future
		self.parkingZoneWarehouse = parkingZoneWarehouse
		#helpful for debug
		self.verboseEnabled = verboseEnabled

	def start_recording(self):
		recorded_videos_dir = "../recorded_videos/{}".format(int(time.time()))
		pathlib.Path(recorded_videos_dir).mkdir(parents=True, exist_ok=True)
		print (self.camera_map)
		for camera_id in self.camera_map:
			camera_OS_index = self.camera_map[camera_id]["camera_os_index"]
			self.recorder_map[camera_id] = Recorder(camera_OS_index, self.verboseEnabled, self.camera_map[camera_id]["camera_fps"])
			self.recorder_map[camera_id].start_recording(recorded_videos_dir+"/{}".format(str(camera_id)))

	def stop_recording(self):
		for recorder_id in self.recorder_map:
			print(recorder_id)
			self.recorder_map[recorder_id].stop_recording()
		self.recorder_map = {}
