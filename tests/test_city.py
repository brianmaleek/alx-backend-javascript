#!/usr/bin/env python3
"""Unittest for City class """

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Defines tests for class City """

    def setUp(self):
        """ Set up City instance for all tests """
        self.city = City()

    def test_init(self):
        """ Test that City is an instance of BaseModel """
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """ Test that City inherits from BaseModel """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """ Test that City has expected attributes """
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_attribute_type(self):
        """ Test that City attributes are the correct type """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_default_attribute_values(self):
        """ Test that City attributes are set to empty strings """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_attribute_assignment(self):
        """ Test that City attributes can be assigned """
        self.city.state_id = "123456"
        self.city.name = "San Francisco"

        self.assertEqual(self.city.state_id, "123456")
        self.assertEqual(self.city.name, "San Francisco")

    def test_to_dict(self):
        """ Test to_dict method"""
        self.city.state_id = "123456"
        self.city.name = "San Francisco"

        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["state_id"], "123456")
        self.assertEqual(city_dict["name"], "San Francisco")
        self.assertTrue('__class__' in city_dict)
        self.assertTrue('created_at' in city_dict)
        self.assertTrue('updated_at' in city_dict)

    def test_str_representation(self):
        """ Test __str__ representation of City """
        self.city.state_id = "123456"
        self.city.name = "San Francisco"
        self.city.id = "654321"

        expected_str = (
            f"[City] ({self.city.id}) {self.city.__dict__}"
        )
        self.assertEqual(str(self.city), expected_str)


if __name__ == '__main__':
    unittest.main()
