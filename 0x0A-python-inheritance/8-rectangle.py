#!/usr/bin/python3
"""class rectangle inherit from basegeometry."""

Basegeometry = __import__("7-base_geometry.py").Basegeometry

class Rectangle(BaseGeometry):
	"""represent a rectangle using BaseGeometry """
	

	def __init__(self, width, height):
		"""initialize the new triangle.
		args:
			width(int):width of the new rectangle.
			height(int):the height of the new rectangle.
		"""
	 	self.integer_validator("width".width)
		self.__width = width
		self.interger_validator("height".height)
		self.__height = height
