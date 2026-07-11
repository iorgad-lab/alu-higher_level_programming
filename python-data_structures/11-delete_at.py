#!/usr/bin/python3
"""Module that deletes an item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    """Delete the item at idx, modifying the original list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
