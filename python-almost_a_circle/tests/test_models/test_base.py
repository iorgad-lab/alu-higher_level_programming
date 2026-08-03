#!/usr/bin/python3
"""Module for Base unit tests."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base class."""

    def setUp(self):
        """Resets nb_objects."""
        Base._Base__nb_objects = 0

    def test_base_id_auto(self):
        """Test Base() for assigning automatically an ID."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)

    def test_base_id_plus_one(self):
        """Test Base() for assigning automatically an ID + 1."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_base_id_manual(self):
        """Test Base(89) saving the ID passed."""
        self.assertEqual(Base(89).id, 89)

    def test_to_json_string_none(self):
        """Test Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test Base.to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test Base.to_json_string([{'id': 12}])."""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test Base.from_json_string("[]")."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list(self):
        """Test Base.from_json_string('[{"id": 89}]')."""
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])
