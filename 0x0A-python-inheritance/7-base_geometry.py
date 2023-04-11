#!/usr/bin/python3
"""base geometry is a bsegeometry class."""

class BaseGeometry:
	"""rep base geometry."""
	def area(self):
		"""not yet implemented."""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""validate a parameter as an integer.

		args:
			name(str): the name of the parameter.
			value(int):the parameter to validate.
		raises:
			TypeError: if a value is not an integer.
			ValueError: if the value is <= 0
		"""

		if type(value) != int:
			raise TypeError("{} must be an integer".format(name))
		if value <= 0:
			raise ValueError("{} must be greater than 0".format(name))

