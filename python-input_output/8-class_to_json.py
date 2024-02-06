#!/usr/bin/python3

"""
    The ``8. Class to JSON`` module
"""


def class_to_json(obj):
    """
        class_to_json - Function that returns the dictionary description
        with simple data structure.
    """
    return obj.__dict__
