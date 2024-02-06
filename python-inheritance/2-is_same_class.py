#!/usr/bin/python3

"""
    The ``2. Exact same object`` module
"""


def is_same_class(obj, a_class):
    """ Checks the class is same or not. """
    if type(obj) is a_class:
        return True
    return False
