#!/usr/bin/python3

"""
    The ``4. Only sub class of`` module.
"""


def inherits_from(obj, a_class):
    """ find obj inherits from a_class or not """
    return not type(obj) is a_class and isinstance(obj, a_class)
