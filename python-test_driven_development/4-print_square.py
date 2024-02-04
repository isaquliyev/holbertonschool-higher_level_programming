#!/usr/bin/python3
"""
    The ``3. Print square`` module.
    This module contains print_square function.
"""


def print_square(size):
    """
        print_square - prints square with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
