import cv2
import time
import numpy as np
from os import walk
import os
import string
import sys
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)


class DDPS(object):

	def __init__(self):

		# save images stuff
		self.nums = []
		self.alph = string.ascii_lowercase
		for i in range(10):
			self.nums.append(i)

		# camera initiation
		self.cap = cv2.VideoCapture(0)
		self.ret, self.frame = None, None
		
		file_path = os.path.dirname(__file__)
		image_path = os.path.join(file_path, 'images')
		os.makedirs(image_path, exist_ok=True)
		self.image_path = image_path

        #set GPIO Pins
		self.GPIO_ECHO = 11
		self.GPIO_TRIGGER = 7
		GPIO.setup(self.GPIO_ECHO, GPIO.IN)
		GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)

		config = {}

		config['general'] = {}
		config['ultrasonic'] = {}
		config['camera'] = {}

		self.config = config

		pass


	def manager(self):

		# get reading from ultrasonic sensor (uss)
		is_car = self.get_reading_from_ultrasonic_sensor_and_search_car()

		if is_car:  # if there is a car

			# get picture
			img = self.get_picture_from_camera()
			self.save_image()

			# read rfid
			is_rfid = self.get_reading_from_rfid()

			if not is_rfid: # if rfid is False

				# turn on leds
				success = self.turn_on_leds()
				# turn on buzzer
				success = self.turn_on_buzzer()

				# for X minutes, try to read rfid and uss


					# if no car, or handicapped car

						# turn off leds
						# turn off buzzer

					# else

						# concat someone

						# send picture

		pass
    
	def distance(self):
    # set Trigger to HIGH
		GPIO.output(self.GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
		time.sleep(0.00001)
		GPIO.output(self.GPIO_TRIGGER, False)
 
		StartTime = time.time()
		StopTime = time.time()
 
    # save StartTime
		while GPIO.input(self.GPIO_ECHO) == 0:
			StartTime = time.time()
 
    # save time of arrival
		while GPIO.input(self.GPIO_ECHO) == 1:
			StopTime = time.time()
 
    # time difference between start and arrival
		TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
		distance = (TimeElapsed * 34300) / 2
 
		return distance
    
	def get_reading_from_ultrasonic_sensor_and_search_car(self):

		# return is_car (bool)
		pass

	def get_picture_from_camera(self):

		self.ret, self.frame = self.cap.read()
		print(self.frame)
		pass

	def get_reading_from_rfid(self):

		# return is_rfid (bool)
		pass

	def turn_on_leds(self):

		# return success (bool)
		pass

	def turn_on_buzzer(self):

		# return success (bool)
		pass

	def save_image(self):
		image = self.frame
		times = time.time()

		#cv2.imshow('finished pic', image)
		#if cv2.waitKey(0) & 0xFF == ord('s'):
		cv2.imwrite(os.path.join(self.image_path, f'{times}.jpg'), image)
		# cv2.destroyAllWindows()
		pass


ddps = DDPS()

ddps.get_picture_from_camera()
ddps.save_image()
for i in range(10):
    print(ddps.distance())
