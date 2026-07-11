#!/usr/bin/python3
"""Module that prints integers of a list in reverse."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if my_list is None:
        my_list = []
    for i in reversed(my_list):
        print("{:d}".format(i))
