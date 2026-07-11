#!/usr/bin/python3
"""Module that returns the key with the biggest integer value."""


def best_score(a_dictionary):
    """Return the key with the highest value in a_dictionary."""
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
