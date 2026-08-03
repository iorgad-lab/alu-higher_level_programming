#!/usr/bin/python3
"""Module for Rectangle unit tests."""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def setUp(self):
        """Resets nb_objects."""
        Base._Base__nb_objects = 0

    def test_rectangle_1_2(self):
        """Test Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_1_2_3(self):
        """Test Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_1_2_3_4(self):
        """Test Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_1_2_3_4_5(self):
        """Test Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_width_str(self):
        """Test Rectangle("1", 2)."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_rectangle_height_str(self):
        """Test Rectangle(1, "2")."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_rectangle_x_str(self):
        """Test Rectangle(1, 2, "3")."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_rectangle_y_str(self):
        """Test Rectangle(1, 2, 3, "4")."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_width_neg(self):
        """Test Rectangle(-1, 2)."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_rectangle_height_neg(self):
        """Test Rectangle(1, -2)."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_rectangle_width_zero(self):
        """Test Rectangle(0, 2)."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_rectangle_height_zero(self):
        """Test Rectangle(1, 0)."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_rectangle_x_neg(self):
        """Test Rectangle(1, 2, -3)."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_rectangle_y_neg(self):
        """Test Rectangle(1, 2, 3, -4)."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        """Test area()."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_rectangle_str(self):
        """Test __str__() for Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_display_no_x_y(self):
        """Test display() without x and y."""
        r = Rectangle(2, 2)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_rectangle_display_no_y(self):
        """Test display() without y."""
        r = Rectangle(2, 2, 1)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_rectangle_display_full(self):
        """Test display()."""
        r = Rectangle(2, 2, 1, 1)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_rectangle_to_dictionary(self):
        """Test to_dictionary() in Rectangle."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), d)

    def test_rectangle_update(self):
        """Test update() in Rectangle."""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)
        r.update(**{'id': 70})
        self.assertEqual(r.id, 70)

    def test_rectangle_create_id(self):
        """Test Rectangle.create(**{'id': 89})."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_rectangle_create_width(self):
        """Test Rectangle.create(**{'id': 89, 'width': 1})."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_rectangle_create_height(self):
        """Test Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_rectangle_create_x(self):
        """Test Rectangle.create(**{'id': 89, 'width': 1, 'x': 3})."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_rectangle_create_y(self):
        """Test create method with all attrs."""
        r = Rectangle.create(**{
            'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4
        })
        self.assertEqual(r.y, 4)

    def test_rectangle_save_to_file_none(self):
        """Test Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_to_file_empty(self):
        """Test Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rectangle_save_to_file_list(self):
        """Test Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_rectangle_load_from_file_no_file(self):
        """Test Rectangle.load_from_file() no file."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_from_file_exists(self):
        """Test Rectangle.load_from_file() exists."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(len(Rectangle.load_from_file()), 1)
