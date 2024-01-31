def safe_print_list(my_list=[], x=0):
    nb_print = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nb_print += 1
        except Exception:
            break
    print()
    return nb_print