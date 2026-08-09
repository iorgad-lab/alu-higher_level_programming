#!/usr/bin/python3
"""Unittest for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquareInstantiation(unittest.TestCase):
    """Tests for Square instantiation."""

    def test_is_rectangle_instance(self):
        """Test that Square inherits from Rectangle."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_size_sets_width_height(self):
        """Test that width and height both equal size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_all_args(self):
        """Test full instantiation with all arguments."""
        s = Square(3, 1, 3, 12)
        actual = (s.width, s.height, s.x, s.y, s.id)
        self.assertEqual(actual, (3, 3, 1, 3, 12))


class TestSquareValidation(unittest.TestCase):
    """Tests that Square inherits Rectangle's validation."""

    def test_size_not_int(self):
        """Test TypeError for non-integer size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_negative(self):
        """Test ValueError for negative size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)


class TestSquareArea(unittest.TestCase):
    """Tests for Square.area."""

    def test_area(self):
        """Test area calculation for a square."""
        self.assertEqual(Square(5).area(), 25)


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__."""

    def test_str(self):
        """Test the string representation."""
        s = Square(3, 1, 3, 12)
        self.assertEqual(str(s), "[Square] (12) 1/3 - 3")


class TestSquareSize(unittest.TestCase):
    """Tests for the Square.size property."""

    def test_size_getter(self):
        """Test that size returns width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test that setting size updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_validation(self):
        """Test that size setter validates like width."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for Square.update with *args."""

    def test_update_size(self):
        """Test updating id and size via args."""
        s = Square(5)
        s.update(1, 2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)

    def test_update_all(self):
        """Test updating all attributes via args."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for Square.update with **kwargs."""

    def test_update_kwargs(self):
        """Test updating via keyword arguments."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def test_to_dictionary_keys(self):
        """Test that all expected keys are present."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_to_dictionary_round_trip(self):
        """Test that a square rebuilt from its dict is equal."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
