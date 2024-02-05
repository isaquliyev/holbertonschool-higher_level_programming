#!/usr/bin/python3
"""
    This file contains Rectangle class.
"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """initialize parameters"""
        self.width = width
        self.height = height

    @property
    def width(self):
        # Get the value width
        return self.__width

    @width.setter
    def width(self, value):
        # Set the value width
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        # Get the value height
        return self.__height

    @height.setter
    def height(self, value):
        # Set the value height
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        # Area of Rectangle
        return self.__height * self.__width

    def perimeter(self):
        # Perimeter of Rectangle
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        # Returns rectangle using # signs
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result[:-1]
