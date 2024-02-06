#!/usr/bin/python3

"""
    The ``Geometry`` module.
"""


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Area of geometry. """
        raise Exception("area() is not implemented")
