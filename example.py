# -- coding: utf-8 --
#__requires__ = ['arduino']

"""
 Example of use.

 Diego de los Reyes Rodríguez.
 v0.1 Oct 2015    - Created
"""

from arduino.boardmanager import BoardManager

boardManager = BoardManager()
boards = boardManager.search()