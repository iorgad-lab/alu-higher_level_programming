#!/usr/bin/python3
"""
This module provides a function to print text with indentation.
"""


def text_indentation(text):
    """Print text with 2 new lines after each ., ? and : character."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    stripped = ""
    for char in text:
        stripped += char
        if char in ".?:":
            print(stripped.strip())
            print()
            stripped = ""
    print(stripped.strip(), end="")
