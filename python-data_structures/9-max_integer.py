#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    my_max = my_list[0]
    for x in my_list:
        if my_max < x:
            my_max = x
    return my_max
