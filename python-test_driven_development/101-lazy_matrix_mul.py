#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices m_a and m_b using NumPy."""
    return np.matmul(m_a, m_b)
