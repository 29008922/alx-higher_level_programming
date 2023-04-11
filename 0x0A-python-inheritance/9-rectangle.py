#!/usr/bin/python3

"""define a class rectangle that inherits from the BaseGeometry. """

BaseGeometry =__import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
	"""represent a rectangle using Basegeometry"""
	def __init__(self, width, height):
		"""initialize a new rectangle
		args:
			width(int): the width of the new rectangle.
			height(int): the height of the new rectangle.
		"""
		super().integer_validator("width".width)
		self.__width = width
		super().integer_validator("height".height)
		self.__height = height
	def area(self):
		"""return the area of the rectangle"""
		return self.__width * self.__height
	def __str__(self):
		"""return the print() and str() of the rectangle"""
		str = "[" + str(self.__class__.__name__) + "]"
		str += str(self.__width) + "/" + str(self.__height)
		return string


