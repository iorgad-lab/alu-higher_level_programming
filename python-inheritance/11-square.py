#!/usr/bin/python3
"""Module that defines a Square class with custom string output."""
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

    def __str__(self):
        """Return the string representation of the square."""
        w = self._Rectangle__width
        h = self._Rectangle__height
        return "[Square] {}/{}".format(w, h)
