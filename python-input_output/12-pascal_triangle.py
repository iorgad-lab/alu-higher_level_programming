#!/usr/bin/python3
"""Module that generates Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's Triangle.

    Args:
        n (int): the number of rows of the triangle.

    Returns:
        list: an empty list if n <= 0, otherwise the triangle rows.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)
    return triangle
