#!/usr/bin/python3

"""
    The ``Geometry`` module.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle class that inherits BaseGeometry """
    def __init__(self, width, height):
        """ initialize width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
