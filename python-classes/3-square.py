#!/usr/bin/python3
"""Module for Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size
