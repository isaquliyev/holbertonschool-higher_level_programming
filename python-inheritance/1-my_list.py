#!/usr/bin/python3

"""
    The ``MyList`` module
"""


class MyList(list):
    """ MyList class """
    def print_sorted(self):
        print(sorted(self))
