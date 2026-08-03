import unittest
from models.square import Square
from models.base import Base
import io
import sys


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(2, 2, 2, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 2)

    def test_size_type_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")

    def test_size_value_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_x_type_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "1")

    def test_x_value_error(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -1)

    def test_y_type_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 1, "1")

    def test_y_value_error(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 1, -1)

    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2, 2, 12)
        self.assertEqual(s2.area(), 4)

    def test_display_no_offset(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s = Square(2)
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        s = Square(3, 1, 3)
        s.display()
        sys.stdout = sys.__stdout__
        expected = "\n\n\n ###\n ###\n ###\n"
        self.assertEqual(captured_output.getvalue(), expected)

    def test_str(self):
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s2 = Square(2, 2, 2, 12)
        self.assertEqual(str(s2), "[Square] (12) 2/2 - 2")

    def test_update_args(self):
        s = Square(10, 10, 10, 1)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/10 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 1)
        s.update(size=1)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 1")
        s.update(x=2, y=3)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 1")
        s.update(id=89, size=7, y=1)
        self.assertEqual(str(s), "[Square] (89) 2/1 - 7")

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 1)
        s.update(89, 2, y=3)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 2")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected_dict = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s_dict, expected_dict)
        self.assertEqual(type(s_dict), dict)
