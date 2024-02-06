#!/usr/bin/python3

"""
    The ``3. To JSON string`` module
"""


import json


def to_json_string(my_obj):
    """
        to_json_string - function that returns the
        JSON representation of an object.
    """
    return json.dumps(my_obj)
