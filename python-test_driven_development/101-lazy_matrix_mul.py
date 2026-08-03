#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices m_a and m_b using NumPy."""
    if type(m_a) is not list or type(m_b) is not list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    for row in m_a:
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("invalid data type for einsum")
    for row in m_b:
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("invalid data type for einsum")

    return np.dot(m_a, m_b)
