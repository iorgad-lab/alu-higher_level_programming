#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Tests for Base's id-management behavior."""

    def test_id_assigned(self):
        """Test that a given id is assigned directly."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_auto_increment(self):
        """Test that ids auto-increment when not provided."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_none_explicit(self):
        """Test that passing id=None still auto-increments."""
        b1 = Base(None)
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)


class TestBaseToJSONString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none(self):
        """Test that None returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """Test that an empty list returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """Test conversion of a list of dictionaries."""
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, '[{"id": 1}]')

    def test_return_type(self):
        """Test that the return type is str."""
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)


class TestBaseFromJSONString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none(self):
        """Test that None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """Test that an empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        """Test parsing a valid JSON string."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(result, [{"id": 1}])

    def test_return_type(self):
        """Test that the return type is list."""
        self.assertIsInstance(Base.from_json_string('[{"id": 1}]'), list)


class TestBaseSaveLoadFile(unittest.TestCase):
    """Tests for Base.save_to_file and Base.load_from_file."""

    def tearDown(self):
        """Remove any files created during the tests."""
        for f in ("Rectangle.json", "Square.json"):
            if os.path.exists(f):
                os.remove(f)

    def test_save_to_file_creates_file(self):
        """Test that save_to_file creates the expected JSON file."""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        """Test that save_to_file(None) writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file_no_file(self):
        """Test that load_from_file returns [] if no file exists."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_and_load_round_trip(self):
        """Test that saved and reloaded instances match originals."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_save_and_load_square(self):
        """Test round-tripping Square instances."""
        s1 = Square(5)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle(self):
        """Test creating a Rectangle from a dictionary."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test creating a Square from a dictionary."""
        s1 = Square(5, 1, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
