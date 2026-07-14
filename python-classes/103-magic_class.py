#!/usr/bin/python3
"""Module for MagicClass"""
import math


class MagicClass:
    """Represent a magic class with a radius"""

    def __init__(self, radius=0):
        """Initialize a new MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area based on the radius"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference based on the radius"""
        return 2 * math.pi * self.__radius
