#!/usr/bin/python3

"""
    The ``2. Append to a file`` module
"""


def append_write(filename="", text=""):
    """
        append_write -  function that appends a string at the end
        of a text file (UTF8) and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    f.close()
    return count
