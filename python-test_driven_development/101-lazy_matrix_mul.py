#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices m_a and m_b using NumPy."""
    def validate(m, name):
        if not isinstance(m, list):
            raise TypeError("{} must be a list".format(name))
        if not all(isinstance(row, list) for row in m):
            raise TypeError("{} must be a list of lists".format(name))
        if m == [] or m == [[]]:
            raise ValueError("{} can't be empty".format(name))
        for row in m:
            for item in row:
                if not isinstance(item, (int, float)) or \
                        isinstance(item, bool):
                    raise TypeError(
                        "{} should contain only integers or floats"
                        .format(name))
        row_len = len(m[0])
        if not all(len(row) == row_len for row in m):
            raise TypeError(
                "each row of {} must be of the same size".format(name))

    validate(m_a, "m_a")
    validate(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
