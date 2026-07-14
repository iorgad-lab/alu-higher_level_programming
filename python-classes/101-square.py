#!/usr/bin/python3
"""Module for Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation, same as my_print"""
        if self.__size == 0:
            return ""
        lines = []
        for i in range(self.__position[1]):
            lines.append("")
        for i in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
