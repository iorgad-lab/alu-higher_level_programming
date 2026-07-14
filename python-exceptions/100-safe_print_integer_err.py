#!/usr/bin/python3
"""Module for safe_print_integer_err"""
import sys


def safe_print_integer_err(value):
    """Print an integer safely, print exception to stderr on failure"""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
