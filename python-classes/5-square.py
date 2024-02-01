#!/usr/bin/python3
"""This file contains Square class inside."""


class Square():
    """Documentation for Square class"""
    def __init__(self, size=0):
        """Init block of Square Class"""
        self.__size = size

    @property
    def size(self):
        """size function that returns private size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size function for set value for size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area mothod that calculates area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints area using # sign"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
