#!/usr/bin/python3
"""Module that defines a Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, based on Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square, must be positive.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
