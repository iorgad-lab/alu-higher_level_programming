#!/usr/bin/python3
"""Module that adds an attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj if obj supports it.

    Args:
        obj: the object to add the attribute to.
        name (str): the attribute name.
        value: the attribute value.

    Raises:
        TypeError: if obj cannot have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
