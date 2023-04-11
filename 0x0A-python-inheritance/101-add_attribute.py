#!/usr/bin/python3
"""define a function that add attribute to an object"""


def add_attribute(obj, att, value):
	"""add attribute to an object if possible

	args:
		obj(any):the object to add attribute to.
		att(str):the name of attribute to add to obj.
		value(any):the value of attr
	Raises:
		TypeError:if the attribute cannot be added.

	"""
	if not hasattr(obj. "__dic__"):
		raise TypeError("can't add new attribute")
	setattr(obj, att, value)
