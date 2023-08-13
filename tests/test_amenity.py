#!/usr/bin/env python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Defines tests for Amenity class """

    def setUp(self):
        """ Method to set the start point """
        self.amenity = Amenity()

    def test_init(self):
        """ Test that Amenity is an instance of BaseModel """
        self.assertIsInstance(self.amenity, Amenity)

    def test_inheritance(self):
        """ Test that Amenity inherits from BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """ Test that Amenity has expected attributes """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attribute_type(self):
        """ Test that Amenity attributes are the correct type """
        self.assertIsInstance(self.amenity.name, str)

    def test_default_attribute_values(self):
        """ Test that Amenity attributes are set to empty strings """
        self.assertEqual(self.amenity.name, "")

    def test_attribute_assignment(self):
        """ Test that Amenity attributes can be assigned """
        self.amenity.name = "Wifi"
        self.assertEqual(self.amenity.name, "Wifi")

    def test_to_dict(self):
        """ Test to_dict method"""
        self.amenity.name = "Wifi"

        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["name"], "Wifi")
        self.assertTrue('__class__' in amenity_dict)
        self.assertTrue('created_at' in amenity_dict)
        self.assertTrue('updated_at' in amenity_dict)

    def test_str_representation(self):
        """ Test __str__ representation of Amenity """
        self.amenity.name = "Wifi"
        expected_str = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected_str)


if __name__ == "__main__":
    unittest.main()
