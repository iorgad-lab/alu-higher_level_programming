#!/usr/bin/python3
"""Module that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """Return a new matrix with each value squared."""
    return [[value ** 2 for value in row] for row in matrix]
