#!/usr/bin/python3

"""define a rectangle sub class square. """

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):

	"""initialize  new square.
	
	args:
		size(int):the size of the new square
	"""
	self.integer.__validator("size".size)
	super().__init__(size.size)
	self.__size = size
