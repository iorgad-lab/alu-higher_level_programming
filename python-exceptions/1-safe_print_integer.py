#!/usr/bin/python3
"""Module for safe_print_integer"""


def safe_print_integer(value):
    """Print an integer safely"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
