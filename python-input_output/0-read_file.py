#!/usr/bin/python3

"""
    The ``0. Read file`` module
"""


def read_file(filename=""):
    """
        read_file - a function that reads a text file (UTF8)
        and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
    f.close()
