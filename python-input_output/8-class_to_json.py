#!/usr/bin/python3
"""Module that converts an object's attributes to a JSON-ready dict."""


def class_to_json(obj):
    """Return the dictionary description of an object's attributes."""
    return obj.__dict__
