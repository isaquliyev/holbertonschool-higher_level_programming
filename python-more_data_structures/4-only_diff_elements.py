#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = set()
    for i in set_1:
        od_set.add(i)
    for j in set_2:
        od_set.add(j)
    od_set = list(set(od_set))
    od_set = set(od_set)
    return od_set
