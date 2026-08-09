#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for Rectangle instantiation and attribute assignment."""

    def test_is_base_instance(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)

    def test_width_height(self):
        """Test width and height are assigned correctly."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_all_args(self):
        """Test full instantiation with all arguments."""
        r = Rectangle(10, 2, 1, 3, 12)
        actual = (r.width, r.height, r.x, r.y, r.id)
        self.assertEqual(actual, (10, 2, 1, 3, 12))

    def test_id_auto_assigned(self):
        """Test that id is auto-assigned when not given."""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.id, r1.id + 1)


class TestRectangleValidation(unittest.TestCase):
    """Tests for Rectangle attribute validation."""

    def test_width_not_int(self):
        """Test TypeError for non-integer width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_not_int(self):
        """Test TypeError for non-integer height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_x_not_int(self):
        """Test TypeError for non-integer x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_y_not_int(self):
        """Test TypeError for non-integer y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, [])

    def test_width_zero(self):
        """Test ValueError for width of 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        """Test ValueError for negative width."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_zero(self):
        """Test ValueError for height of 0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_x_negative(self):
        """Test ValueError for negative x."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_y_negative(self):
        """Test ValueError for negative y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_setter_validation(self):
        """Test setter validation after instantiation."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area."""

    def test_area_basic(self):
        """Test basic area calculation."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_with_position(self):
        """Test area is unaffected by x/y."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for Rectangle.display."""

    def test_display_basic(self, ):
        """Test basic display output."""
        import io
        import sys
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        """Test display output respects x and y offsets."""
        import io
        import sys
        r = Rectangle(3, 2, 1, 0)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ###\n ###\n")


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__."""

    def test_str(self):
        """Test the string representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for Rectangle.update with *args."""

    def test_update_id(self):
        """Test updating only the id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_all(self):
        """Test updating all attributes via args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        actual = (r.id, r.width, r.height, r.x, r.y)
        self.assertEqual(actual, (89, 2, 3, 4, 5))


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for Rectangle.update with **kwargs."""

    def test_update_kwargs(self):
        """Test updating via keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_kwargs_multiple(self):
        """Test updating multiple attributes via keywords."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual((r.id, r.width, r.x, r.y), (89, 2, 3, 1))

    def test_kwargs_skipped_if_args(self):
        """Test that kwargs are ignored if args are given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(1, height=99)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.height, 10)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def test_to_dictionary_keys(self):
        """Test that all expected keys are present."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "width", "height", "x", "y"})

    def test_to_dictionary_values(self):
        """Test that dictionary values match the instance."""
        r = Rectangle(10, 2, 1, 9, 99)
        d = r.to_dictionary()
        expected = {"id": 99, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(d, expected)

    def test_to_dictionary_round_trip(self):
        """Test that a rectangle rebuilt from its dict is equal."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
