import json
import os
from ParkingZoneDetector import ParkingZoneDetector
from Position import Position
import cv2
import threading
import numpy as np

class Recorder:

	def __init__(self, camera_id, verboseEnabled, camera_fps):
		self.camera_id = camera_id
		self.parkingZoneDetector = ParkingZoneDetector()
		self.within_recording_zone = False
		self.record_thread_id = None
		self.verboseEnabled = verboseEnabled
		self.camera_fps = camera_fps

	def __record_thread(self, recordFileName):

		t = threading.currentThread()

		cap = cv2.VideoCapture(self.camera_id)
		#if(cap.isOpened() == False):
		#	print("Unable to read camera feed")

		#THIS IS NEEDED SO WE DONT HAVE IMAGES FROM THE PAST!
		cap.set(cv2.CAP_PROP_BUFFERSIZE, 1) #now the opencv buffer just one frame.


		# Default resolutions of the frame are obtained.The default resolutions are system dependent.
		# We convert the resolutions from float to integer.
		frame_width = int(cap.get(3))
		frame_height = int(cap.get(4))

		# Define the codec and create VideoWriter object.The output is stored in 'output.avi' file.
		out = cv2.VideoWriter('{}.avi'.format(recordFileName),cv2.VideoWriter_fourcc('M','J','P','G'), self.camera_fps, (frame_width,frame_height))
		 
		while getattr(t, "do_run", True):

			ret, frame = cap.read()

			if ret == True: 
			 
				# Write the frame into the file 'output.avi'
				out.write(frame)
		 
		# When everything done, release the video capture and video write objects
		cap.release()
		out.release()

	def start_recording(self, recordFileName):

		self.record_thread_id = threading.Thread(target=self.__record_thread, args=(recordFileName,), daemon=True)
		self.record_thread_id.start()
		#start recording on camera_id index
		if(self.verboseEnabled):
			print("Recording started")
		
	def stop_recording(self):
		#stop recording on camera_id index
		if(self.verboseEnabled):
			print("Recording stopped")
		self.record_thread_id.do_run = False

	def is_position_within_recording_zone(self, position):
		
		return self.parkingZoneDetector.is_position_within_recording_zone(position)

	def load_city_characteristics(self):

		return False

	
