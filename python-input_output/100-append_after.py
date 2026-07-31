#!/usr/bin/python3
"""Module that inserts a line after every line containing a string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line containing search_string.

    Args:
        filename (str): the file to modify.
        search_string (str): the string to search for in each line.
        new_string (str): the string to insert after matching lines.
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
