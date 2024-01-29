#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    items = sorted(a_dictionary.items())
    for key, value in items:
        print("{}: {}".format(key, value))
