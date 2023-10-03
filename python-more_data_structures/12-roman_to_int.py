#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    roman_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    value = 0
    for i in range(len(roman_string) - 1):
        if roman_num[roman_string[i]] < roman_num[roman_string[i + 1]]:
            value -= roman_num[roman_string[i]]
        else:
            value += roman_num[roman_string[i]]
    value += roman_num[roman_string[-1]]
    return value
