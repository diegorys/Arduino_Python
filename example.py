# -- coding: utf-8 --
#__requires__ = ['arduino']

"""
 Example of use.

 Diego de los Reyes Rodríguez.
 v0.1 Oct 2015    - Created.
 v0.2 Dec 2016	- Send and receive message.
"""

from arduino.boardmanager import BoardManager

boardManager = BoardManager()

print "Searching for boards..."
boards = boardManager.search()

print len(boards),"boards found"

for board in boards:
	print board.toString()
	message = ""
	while message != "bye":
		message = raw_input("Send message: ")
		receive = False
		if message == "on":
			board.sendMessage("101")
			receive = True
		elif message == "off":
			board.sendMessage("100")
			receive = True
		elif message == "bye":
			print "Bye!"
		else:
			print "Unknown message"

		if receive:
			result = board.receiveMessage()
			if result != "":
				print "Result:",result
			else:
				print "Board is not responding"