#!/usr/bin/python3
"""
This module provides a simple integer addition function.

It defines add_integer, validates arguments, returns their sum.
"""


def add_integer(a, b=98):
    """Add a and b, casting floats to int.

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
