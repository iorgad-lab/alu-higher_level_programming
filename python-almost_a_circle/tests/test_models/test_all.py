import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import json

class TestEverything(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(89).id, 89)

    def test_json(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])

    def test_rect_init(self):
        self.assertEqual(Rectangle(1, 2).width, 1)
        self.assertEqual(Rectangle(1, 2, 3).x, 3)
        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)
        with self.assertRaises(TypeError): Rectangle("1", 2)
        with self.assertRaises(ValueError): Rectangle(-1, 2)
        with self.assertRaises(ValueError): Rectangle(0, 2)

    def test_rect_area_str(self):
        r = Rectangle(3, 2, 1, 1, 12)
        self.assertEqual(r.area(), 6)
        self.assertEqual(str(r), "[Rectangle] (12) 1/1 - 3/2")

    def test_rect_update(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        r.update(**{'id': 90, 'width': 10})
        self.assertEqual(r.id, 90)
        self.assertEqual(r.width, 10)

    def test_square_init(self):
        self.assertEqual(Square(5).size, 5)
        self.assertEqual(Square(5, 2, 3).x, 2)
        with self.assertRaises(TypeError): Square("1")
        with self.assertRaises(ValueError): Square(-1)

    def test_square_update(self):
        s = Square(1, 1, 1, 1)
        s.update(89, 2, 3, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        s.update(**{'id': 90, 'size': 10})
        self.assertEqual(s.id, 90)
        self.assertEqual(s.size, 10)
