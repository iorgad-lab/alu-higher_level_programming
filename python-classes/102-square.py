#!/usr/bin/python3
"""Module for Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check equality based on area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check inequality based on area"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check greater than based on area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check greater or equal based on area"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check less than based on area"""
        return self.area() < other.area()

    def __le__(self, other):
        """Check less or equal based on area"""
        return self.area() <= other.area()
