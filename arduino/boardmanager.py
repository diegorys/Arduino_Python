# -- coding: utf-8 --

"""
 Manage boards.

 Diego de los Reyes Rodríguez.
 v0.1 Oct 2015	- Created.
"""

from board import Board
import serial.tools.list_ports

class BoardManager:

	def __init__(self):
		print "Init"

	def search(self):
		print "Searching for boards..."
		self.boards = {}

		ports = list(serial.tools.list_ports.comports())

		for p in ports:
			if "Arduino" in p[1]:
				board = Board(p[0].strip(), p[1].strip(), p[2].strip())
				print "\nFound board connected to :",board.port
				if board.isAvailable():
					self.boards[board.port] = board

		print len(self.boards),"boards found"

		return self.boards

	def getBoards(self):
		return self.boards