#!/usr/bin/python3
"""Module that defines a list subclass with a sorted print method."""


class MyList(list):
    """A list that can print itself in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
