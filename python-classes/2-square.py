#!/usr/bin/python3
"""This file contains Square class inside."""


class Square():
    """Documentation for Square class"""
    def __init__(self, size = 0):
        """Init block of Square Class"""
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
