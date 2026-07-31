#!/usr/bin/python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append text to the end of a UTF8 file, creating it if needed.

    Returns:
        int: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
