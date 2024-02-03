#!/usr/bin/python3

"""
    The 0. Integers addition Module

    This module contains add_integer function
"""


def add_integer(a, b=98):
    """
    Simple Algorithm that adds two integer and return sum
    """
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not(isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a+b
