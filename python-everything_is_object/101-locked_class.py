#!/usr/bin/python3
"""Module that defines a class with restricted instance attributes."""


class LockedClass:
    """Class that only allows the 'first_name' instance attribute."""

    __slots__ = ['first_name']
