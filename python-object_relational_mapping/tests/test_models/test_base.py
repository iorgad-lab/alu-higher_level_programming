import unittest
from models.base import Base
import os


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_none(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        b3 = Base(100)
        self.assertEqual(b3.id, 100)

    def test_id_mixed(self):
        b4 = Base()
        b5 = Base(200)
        b6 = Base()
        self.assertEqual(b4.id, 1)
        self.assertEqual(b5.id, 200)
        self.assertEqual(b6.id, 2)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_list_of_dicts(self):
        dictionary = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        json_string = Base.to_json_string([dictionary])
        self.assertTrue(type(json_string) is str)
        expected = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(json_string, expected)

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_json_string(self):
        json_string = "[{\"id\": 89, \"width\": 10, \"height\": 4}]"
        list_output = Base.from_json_string(json_string)
        self.assertEqual(list_output, [{'id': 89, 'width': 10, 'height': 4}])

    def test_create_rectangle(self):
        from models.rectangle import Rectangle
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        from models.square import Square
        s1 = Square(5, 1, 0, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_save_to_file_none(self):
        from models.rectangle import Rectangle
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        from models.rectangle import Rectangle
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangle(self):
        from models.rectangle import Rectangle
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertIn('"id": 1', content)
            self.assertIn('"width": 10', content)
            self.assertIn('"id": 2', content)

    def test_save_to_file_square(self):
        from models.square import Square
        s1 = Square(5, 1, 0, 1)
        s2 = Square(7, 9, 1, 2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertIn('"id": 1', content)
            self.assertIn('"size": 5', content)
            self.assertIn('"id": 2', content)

    def test_load_from_file_no_file(self):
        from models.rectangle import Rectangle
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        from models.rectangle import Rectangle
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(str(list_rectangles_output[0]), str(r1))
        self.assertEqual(str(list_rectangles_output[1]), str(r2))

    def test_load_from_file_square(self):
        from models.square import Square
        s1 = Square(5, 1, 0, 1)
        s2 = Square(7, 9, 1, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(len(list_squares_output), 2)
        self.assertEqual(str(list_squares_output[0]), str(s1))
        self.assertEqual(str(list_squares_output[1]), str(s2))
