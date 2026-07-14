#!/usr/bin/python3
"""Module for magic_calculation"""


def magic_calculation(a, b):
    """Perform magic calculation based on bytecode logic"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
