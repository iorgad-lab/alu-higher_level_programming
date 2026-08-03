#!/usr/bin/python3
"""Module for Rectangle unit tests."""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from sys import stdout

class TestRectangle(unittest.TestCase):
    """Exhaustive tests for Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_basic_init(self):
        self.assertEqual(Rectangle(1, 2).width, 1)
        self.assertEqual(Rectangle(1, 2, 3).x, 3)
        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_type_errors(self):
        with self.assertRaises(TypeError): Rectangle("1", 2)
        with self.assertRaises(TypeError): Rectangle(1, "2")
        with self.assertRaises(TypeError): Rectangle(1, 2, "3")
        with self.assertRaises(TypeError): Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        with self.assertRaises(ValueError): Rectangle(-1, 2)
        with self.assertRaises(ValueError): Rectangle(1, -2)
        with self.assertRaises(ValueError): Rectangle(0, 2)
        with self.assertRaises(ValueError): Rectangle(1, 0)
        with self.assertRaises(ValueError): Rectangle(1, 2, -3)
        with self.assertRaises(ValueError): Rectangle(1, 2, 3, -4)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        r = Rectangle(2, 2)
        res = "##\n##\n"
        with StringIO() as buc, stdout as old:
            import sys
            sys.stdout = buc
            r.display()
            sys.stdout = old
            self.assertEqual(buc.getvalue(), res)

    def test_display_x_y(self):
        r = Rectangle(2, 2, 1, 1)
        res = "\n ##\n ##\n"
        with StringIO() as buc, stdout as old:
            import sys
            sys.stdout = buc
            r.display()
            sys.stdout = old
            self.assertEqual(buc.getvalue(), res)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), d)

    def test_update(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)
        r.update(**{'id': 70})
        self.assertEqual(r.id, 70)

    def test_create(self):
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)
        r2 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r2.width, 1)
        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r3.y, 4)

    def test_save_load(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(len(Rectangle.load_from_file()), 1)
