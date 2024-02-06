#!/usr/bin/python3

"""
    The ``1. Write to a file`` module
"""


def write_file(filename="", text=""):
    """
        write_file - a function that writes a string to
        a text file (UTF8) and returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    return count
