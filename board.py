# -- coding: utf-8 --

"""
 Represents a board.

 Diego de los Reyes Rodríguez.
 v0.1 Oct 2015	- Created.
"""
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