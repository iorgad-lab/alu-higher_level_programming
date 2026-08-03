#!/usr/bin/python3
"""Module for Square unit tests."""
import unittest
import os
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """Exhaustive tests for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_basic_init(self):
        self.assertEqual(Square(1).size, 1)
        self.assertEqual(Square(1, 2).x, 2)
        self.assertEqual(Square(1, 2, 3).y, 3)
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_type_errors(self):
        with self.assertRaises(TypeError): Square("1")
        with self.assertRaises(TypeError): Square(1, "2")
        with self.assertRaises(TypeError): Square(1, 2, "3")

    def test_value_errors(self):
        with self.assertRaises(ValueError): Square(-1)
        with self.assertRaises(ValueError): Square(0)
        with self.assertRaises(ValueError): Square(1, -2)
        with self.assertRaises(ValueError): Square(1, 2, -3)

    def test_str(self):
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s.to_dictionary(), d)

    def test_update(self):
        s = Square(1, 1, 1, 1)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)
        s.update(**{'id': 70, 'size': 5})
        self.assertEqual(s.size, 5)

    def test_create(self):
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)
        s2 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s2.y, 3)

    def test_save_load(self):
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        Square.save_to_file([])
        Square.save_to_file([Square(1)])
        self.assertEqual(len(Square.load_from_file()), 1)
