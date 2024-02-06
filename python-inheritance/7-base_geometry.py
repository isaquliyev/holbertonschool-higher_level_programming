#!/usr/bin/python3

"""
    The ``Geometry`` module.
"""


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Area of geometry. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
