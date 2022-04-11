import cv2
import time
import numpy as np
from os import walk
import string
import sys



class DDPS(object):

	def __init__(self):

		# save images stuff
		self.nums = []
		self.alph = string.ascii_lowercase
		for i in range(10):
			self.nums.append(i)

		# camera initiation
		self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
		self.ret, self.frame = None, None


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

	def get_reading_from_ultrasonic_sensor_and_search_car(self):

		# return is_car (bool)
		pass

	def get_picture_from_camera(self):

		self.ret, self.frame = self.cap.read()
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
		f = []
		image = self.frame
		letter = None
		num = None
		for (dirpath, dirnames, filenames) in walk("saveimages\\"):
			f.extend(filenames)
			break
		if f:
			for i in range(len(self.alph)):
				if f[-1][0] == self.alph[i]:
					if int(f[-1][-5]) == self.nums[-1]:
						letter, num = self.alph[i + 1], self.nums[0]
					else:
						letter, num = self.alph[i], self.nums[self.nums.index(int(f[-1][-5])) + 1]
		else:
			letter, num = self.alph[0], 0

		# cv2.imshow('finished pic', image)
		# if cv2.waitKey(0) & 0xFF == ord('s'):
		cv2.imwrite(f'saveimages\\{letter}{num}.jpg', image)
		# cv2.destroyAllWindows()
		pass



