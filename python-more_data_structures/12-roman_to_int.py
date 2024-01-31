#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_dict = {"X": 10, "V": 5, "I": 1, "L": 50,
                  "D": 500, "M": 1000, "C": 100}
    number = 0
    number_cmp = 0
    for i in range(len(roman_string)):
        value = roman_dict[roman_string[i]]
        number += value
    for i in range(len(roman_string)):
        value = roman_dict[roman_string[i]]
        if i != len(roman_string) - 1:
            value_next = roman_dict[roman_string[i + 1]]
        if i == len(roman_string) - 1 or value_next <= value:
            number_cmp += value
    result = number - 2 * (number - number_cmp)
    return result
