#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    for i in range(x):
        value = my_list[i]
        try:
            print("{:d}".format(value), end="")
            nb_print += 1
        except Exception:
            pass
    print()
    return nb_print
