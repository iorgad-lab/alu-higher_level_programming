#!/usr/bin/python3
"""My class module."""


class MyClass:
    """My class."""

    def __init__(self, name):
        """Initialize MyClass with a name."""
        self.name = name
        self.number = 0

    def __str__(self):
        """Return the string representation of MyClass."""
        return "[MyClass] {} - {:d}".format(self.name, self.number)
