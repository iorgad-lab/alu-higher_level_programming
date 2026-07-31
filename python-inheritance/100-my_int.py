#!/usr/bin/python3
"""Module that defines an int subclass with inverted comparisons."""


class MyInt(int):
    """An int whose == and != operators are inverted."""

    def __eq__(self, other):
        """Return True if self is NOT equal to other."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return True if self IS equal to other."""
        return int(self) == int(other)
