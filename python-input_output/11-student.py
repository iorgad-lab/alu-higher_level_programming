#!/usr/bin/python3
"""Module that defines a Student class that can reload from JSON."""


class Student:
    """Represents a student with a name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): optional list of attribute names to include.
                If not a list, all attributes are included.
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
