#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Test a list already in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list not in any particular order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test a list in descending order."""
        self.assertEqual(max_integer([9, 5, 3, 1]), 9)

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        self.assertEqual(max_integer([-5, -1, -10]), -1)

    def test_mixed_sign_numbers(self):
        """Test a list of mixed positive and negative numbers."""
        self.assertEqual(max_integer([-5, 3, -1, 10, 2]), 10)

    def test_duplicate_max(self):
        """Test a list where the max value appears more than once."""
        self.assertEqual(max_integer([4, 7, 7, 2]), 7)

    def test_default_argument(self):
        """Test calling with no arguments uses the default empty list."""
        self.assertEqual(max_integer(), None)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
