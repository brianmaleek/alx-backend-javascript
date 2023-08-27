#!/usr/bin/python3
"""
Unittest for base.py
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Test cases for Base class'''

    def setUp(self):
        '''
        Setup for each testcase
        import module and instantiates class
        '''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''
        Resets __nb_objects
        '''
        pass

    def test_id(self):
        '''
        Tests id attribute
        '''
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(-10), self.id == -10)
        self.assertTrue(Base(1.5), self.id == 1.5)
        self.assertTrue(Base("string"), self.id == "string")

    def test_no_id(self):
        '''
        Tests id attribute with no id
        '''
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_private(self):
        '''
        Test object is private attribute
        and can be accessed with Base.nb_objects
        '''
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_intialization(self):
        '''
        Tests Base class initialization
        to ensure object is set to 0
        '''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)


    def test__instantiation_with_id(self):
        '''
        Tests Base (12) instantiation
        '''
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(12).__dict__, {"id": 12})

    def test__instantiation_with_negative_id(self):
        '''
        Tests Base (-98) instantiation
        '''
        self.assertEqual(Base(-98).id, -98)
        self.assertEqual(Base(-98).__dict__, {"id": -98})

    def test__instantiation_with_string_id(self):
        '''
        Tests Base ("string") instantiation
        '''
        self.assertEqual(Base("string").id, "string")
        self.assertEqual(Base("string").__dict__, {"id": "string"})

    def test__instantiation_with_float_id(self):
        '''
        Tests Base (98.6) instantiation
        '''
        self.assertEqual(Base(98.6).id, 98.6)
        self.assertEqual(Base(98.6).__dict__, {"id": 98.6})

    def test__instantiation_with_None_id(self):
        '''
        Tests Base (None) instantiation
        '''
        self.assertEqual(Base(None).id, 1)
        self.assertEqual(Base(None).__dict__, {"id": 1})

    def test_constructor(self):
        '''
        Tests Base constructor
        '''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        s = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_args(self):
        '''
        Tests Base constructor with many arguments
        '''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        s = "__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), s)

    def test_invalid_args(self):
        '''
        Tests Base instantiation with invalid arguments
        '''
        with self.assertRaises(TypeError):
            Base(1, 1)
            Base([1, 2, 3])
            Base({"a": 1, "b": 2})
            Base((1, 2))
            Base(True)
            Base(float('nan'))
            Base(float('inf'))
            Base(float('-inf'))

    def test_class(self):
        '''
        Tests Base class
        '''
        self.assertTrue(Base(1), self.__class__ == Base)

    def test_to_json_string(self):
        '''
        Tests to_json_string method
        '''
        d0 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        d1 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        strd01 = Base.to_json_string([d0, d1])
        self.assertTrue(d0 == dict)
        self.assertTrue(d1 == dict)
        self.assertTrue(type(strd01) == str)
        self.assertTrue(strd01, [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                        {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])

    def test_to_json_string_empty(self):
        '''
        Tests to_json_string method with empty list
        '''
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_none(self):
        '''
        Tests to_json_string method with None
        '''
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        '''
        Tests from_json_string method
        '''
        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
                        {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        list_output = [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                        {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]
        self.assertEqual(Base.from_json_string(json_string), list_output)

    def test_from_json_string_empty(self):
        '''
        Tests from_json_string method with empty string
        '''
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_None(self):
        '''
        Tests from_json_string method with None
        '''
        self.assertEqual(Base.from_json_string(None), [])

    def test_create(self):
        '''
        Tests create method
        '''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Square(3, 5, 1)

    def test_empty_none_to_file(self):
        '''
        Tests save_to_file method with empty list
        '''
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file(self):
        '''
        Tests load_from_file method
        '''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(list_rectangles_output[1]), "[Rectangle] (2) 0/0 - 2/4")

    def test_load_from_file_none(self):
        '''
        Tests load_from_file method with None
        '''
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_load_from_file_empty(self):
        '''
        Tests load_from_file method with empty list
        '''
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

if __name__ == '__main__':
    unittest.main()
