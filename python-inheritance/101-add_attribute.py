#!/usr/bin/python3

"""
    The ``13. Can I?`` module
"""


def add_attribute(obj, attr, value):
    """
        add_attribute - Function that try to add new attribute.
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
