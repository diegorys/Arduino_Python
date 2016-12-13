# -- coding: utf-8 --

"""
 Represents a board.

 Diego de los Reyes Rodríguez.
 v0.1 Oct 2015	- Created.
 v0.2 Dec 2016	- Send and receive message.
"""

import time
import serial
from serial.serialutil import SerialException

class Board:

	port = ''
	description = ''
	serialNumber = ''
	device = ''

	def __init__(self, port, description, serialNumber):
		self.port = port
		self.description = description
		self.serialNumber = serialNumber

	def isAvailable(self):
		try:
			self.device = serial.Serial(self.port, 9600)
			return True
		except SerialException:
			print "\tBOARD IN ",self.port,"IS IN USE BY OTHER PROGRAM OR YOU HAVE NOT PERMISSIONS"
			return False


	def toString(self):
		return self.port+": "+self.description

	def sendMessage(self, message):
		self.device.write(message)

	def receiveMessage(self):
		attempts = 5
		result = ""
		while (result == "" and attempts > 0):
			time.sleep(1)
			while self.device.inWaiting() > 0:
				message = self.device.readline()
				if message:
					result = message
			attempts -= 1
		return result

