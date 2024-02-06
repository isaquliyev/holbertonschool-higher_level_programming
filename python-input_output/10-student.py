#!/usr/bin/python3

"""
    The ``9. Student to JSON`` module
"""


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ initialize attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation of a Student instance
        """
        new_dict = {}
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            for i in attrs:
                try:
                    new_dict[i] = self.__dict__[i]
                except KeyError:
                    pass
            return new_dict
        return self.__dict__
