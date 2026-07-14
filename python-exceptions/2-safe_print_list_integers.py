#!/usr/bin/python3
"""Module for safe_print_list_integers"""


def safe_print_list_integers(my_list=[], x=0):
    """Print first x integer elements of a list"""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
