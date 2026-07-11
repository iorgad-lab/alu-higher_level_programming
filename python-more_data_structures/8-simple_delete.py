#!/usr/bin/python3
"""Module that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Delete key from a_dictionary if it exists."""
    a_dictionary.pop(key, None)
    return a_dictionary
