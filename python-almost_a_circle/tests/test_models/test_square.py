#!/usr/bin/python3
"""Module for Square unit tests."""
import unittest
import os
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Tests for Square class."""

    def setUp(self):
        """Resets nb_objects."""
        Base._Base__nb_objects = 0

    def test_square_1(self):
        """Test Square(1)."""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2(self):
        """Test Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        """Test Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_1_2_3_4(self):
        """Test Square(1, 2, 3, 4)."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_size_str(self):
        """Test Square("1")."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_square_x_str(self):
        """Test Square(1, "2")."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_y_str(self):
        """Test Square(1, 2, "3")."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_square_size_neg(self):
        """Test Square(-1)."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_square_size_zero(self):
        """Test Square(0)."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_x_neg(self):
        """Test Square(1, -2)."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_square_y_neg(self):
        """Test Square(1, 2, -3)."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_square_str(self):
        """Test __str__() for Square."""
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_square_to_dictionary(self):
        """Test to_dictionary() in Square."""
        s = Square(10, 2, 1, 1)
        d = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s.to_dictionary(), d)

    def test_square_update(self):
        """Test update() in Square."""
        s = Square(1, 1, 1, 1)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.y, 4)
        s.update(**{'id': 70, 'size': 5})
        self.assertEqual(s.size, 5)

    def test_square_create_id(self):
        """Test Square.create(**{'id': 89})."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_square_create_size(self):
        """Test Square.create(**{'id': 89, 'size': 1})."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_square_create_x(self):
        """Test Square.create(**{'id': 89, 'size': 1, 'x': 2})."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_square_create_y(self):
        """Test Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_square_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_empty(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_list(self):
        """Test Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_square_load_from_file_no_file(self):
        """Test Square.load_from_file() no file."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_file_exists(self):
        """Test Square.load_from_file() exists."""
        Square.save_to_file([Square(1)])
        self.assertEqual(len(Square.load_from_file()), 1)
