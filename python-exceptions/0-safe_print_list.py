#!/usr/bin/python3
"""Module for safe_print_list"""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list"""
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except (IndexError, TypeError):
        pass
    print()
    return count
