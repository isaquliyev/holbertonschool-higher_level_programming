#!/usr/bin/python3
def best_score(a_dictionary):
    try:
        values = sorted(a_dictionary.values())
        for key in a_dictionary.keys():
             if a_dictionary[key] == values[-1]:
                 return key
    except:
        return None
