#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with methods area and integer_validator"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer > 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
