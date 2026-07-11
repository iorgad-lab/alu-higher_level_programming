#!/usr/bin/python3
"""Module that replaces all occurrences of an element in a list."""


def search_replace(my_list, search, replace):
    """Return a new list with search replaced by replace."""
    return [replace if item == search else item for item in my_list]
