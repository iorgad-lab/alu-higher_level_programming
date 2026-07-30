#!/usr/bin/python3
"""Module that defines a base geometry class with an area method."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raise an exception since area() is not implemented here."""
        raise Exception("area() is not implemented")
