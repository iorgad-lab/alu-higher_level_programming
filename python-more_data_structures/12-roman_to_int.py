#!/usr/bin/python3
"""Module that converts a Roman numeral to an integer."""


def roman_to_int(roman_string):
    """Convert a Roman numeral string to an integer."""
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        value = roman_values.get(roman_string[i], 0)
        if i + 1 < length and value < roman_values.get(roman_string[i + 1], 0):
            total -= value
        else:
            total += value

    return total
