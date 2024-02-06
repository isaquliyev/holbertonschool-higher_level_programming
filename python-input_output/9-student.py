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

    def to_json(self):
        """
            retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
