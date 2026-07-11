#!/usr/bin/python3
"""Module that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    """Print each key/value pair sorted alphabetically by key."""
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
