#!/usr/bin/python3

"""
    The ``8. Class to JSON`` module
"""


import json


def class_to_json(obj):
    """
        class_to_json - Function that returns the dictionary description
        with simple data structure.
    """
    return json.dumps(obj.__dict__)
