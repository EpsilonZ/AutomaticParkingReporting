 #!/usr/bin/python
#encoding:utf-8

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import threading

class Ultrasonic:

	def __init__(self, model, trigPin, echoPin):
		self.model = "JSN SR04T"
		self.trigPin = trigPin
		self.echoPin = echoPin

		self.ultrasonic_shots_array = []

		self.ultrasonic_thread_id = None

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.trigPin, GPIO.OUT)
		GPIO.setup(self.echoPin, GPIO.IN)

	def start_ultrasonic_shoting(self):

		self.record_thread_id = threading.Thread(target=self.__get_sensor_readings, daemon=True)
		self.record_thread_id.start()

	def stop_ultrasonic_shoting(self):
		self.record_thread_id.do_run = False

	def get_ultrasonic_shots():

		arrayToReturn = self.ultrasonic_shots_array
		self.ultrasonic_shots_array.clear()
		return arrayToReturn

	def __get_sensor_readings(self):

		t = threading.currentThread()

		while getattr(t, "do_run", True):

			GPIO.output(self.trigPin, False)                 #Set TRIG as LOW
			#print ("Waiting For Sensor To Settle")
			time.sleep(0.2)                            #Delay of 2 seconds

			GPIO.output(self.trigPin, True)                  #Set TRIG as HIGH
			time.sleep(0.00001)                      #Delay of 0.00001 seconds
			GPIO.output(self.trigPin, False)                 #Set TRIG as LOW

			while GPIO.input(self.echoPin)==0:               #Check if Echo is LOW
				pulse_start = time.time()              #Time of the last  LOW pulse

			while GPIO.input(self.echoPin)==1:               #Check whether Echo is HIGH
				pulse_end = time.time()                #Time of the last HIGH pulse 

			pulse_duration = pulse_end - pulse_start #pulse duration to a variable

			distance = pulse_duration * 17150        #Calculate distance
			distance = round(distance, 2)            #Round to two decimal points


			if distance > 20 and distance < 400:
				print ("u:" + str(distance - 0.5) + " cm")  #Distance with calibration
			else:
				print("u:out of range") #out of range

			self.ultrasonic_shots_array.append(distance-0.5)
