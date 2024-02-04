#!/usr/bin/python3
"""
    The ``4. Text indentation`` module
    This module contains text_indentation function.
"""


def text_indentation(text):
    """
        text_indentation - seperate text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")
    print(text)
