#!/usr/bin/python3
"""Module that adds all unique integers in a list."""


def uniq_add(my_list=[]):
    """Return the sum of unique integers in my_list."""
    return sum(set(my_list))
