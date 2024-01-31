#!/usr/bin/python3
def raise_exception():
    txt = "Hello, World!"
    try:
        number = int(txt)
    except:
        raise TypeError
