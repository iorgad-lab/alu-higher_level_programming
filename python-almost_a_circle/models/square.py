#!/usr/bin/python3
"""This module defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a special case of Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
            x (int): the x coordinate of the square.
            y (int): the y coordinate of the square.
            id (int): the identity of the new instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes via no-keyword or key-worded arguments."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
