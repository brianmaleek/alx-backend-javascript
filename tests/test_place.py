#!/usr/bin/env python3
"""Unittest for Place class """

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def setUp(self):
        """ Set up Place instance for all tests """
        self.place = Place()

    def test_init(self):
        """ Test that Place is an instance of BaseModel """
        self.assertIsInstance(self.place, Place)

    def test_inheritance(self):
        """ Test that Place inherits from BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """ Test that Place has expected attributes """
        attributes = [
            "city_id", "user_id", "name", "description",
            "number_rooms", "number_bathrooms", "max_guest",
            "price_by_night", "latitude", "longitude",
            "amenity_ids"
        ]
        for attribute in attributes:
            self.assertTrue(hasattr(self.place, attribute))

    def test_attribute_types(self):
        """ Test that Place attributes are the correct type """
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_attribute_values(self):
        """ Test that Place attributes are set to empty strings """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_assignment(self):
        """ Test that Place attributes can be assigned """
        self.place.city_id = "123456"
        self.place.user_id = "123456"
        self.place.name = "My Place"
        self.place.description = "My House"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 2
        self.place.max_guest = 2
        self.place.price_by_night = 100
        self.place.latitude = 36.789987
        self.place.longitude = -123.456278
        self.place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(self.place.city_id, "123456")
        self.assertEqual(self.place.user_id, "123456")
        self.assertEqual(self.place.name, "My Place")
        self.assertEqual(self.place.description, "My House")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 2)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 36.789987)
        self.assertEqual(self.place.longitude, -123.456278)
        self.assertEqual(self.place.amenity_ids, ["amenity1", "amenity2"])

    def test_to_dict(self):
        """ Test that to_dict method """
        self.place.city_id = "654321"
        self.place.user_id = "654321"
        self.place.name = "Cottage Apartment"
        self.place.description = "Contemporary Cottage Apartment"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 2
        self.place.max_guest = 2
        self.place.price_by_night = 100
        self.place.latitude = 63.789987
        self.place.longitude = -132.456278
        self.place.amenity_ids = ["amenity3", "amenity4"]

        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["city_id"], "654321")
        self.assertEqual(place_dict["user_id"], "654321")
        self.assertEqual(place_dict["name"], "Cottage Apartment")
        self.assertEqual(place_dict["description"],
                         "Contemporary Cottage Apartment")
        self.assertEqual(place_dict["number_rooms"], 2)
        self.assertEqual(place_dict["number_bathrooms"], 2)
        self.assertEqual(place_dict["max_guest"], 2)
        self.assertEqual(place_dict["price_by_night"], 100)
        self.assertEqual(place_dict["latitude"], 63.789987)
        self.assertEqual(place_dict["longitude"], -132.456278)
        self.assertEqual(place_dict["amenity_ids"], ["amenity3", "amenity4"])
        self.assertTrue("__class__" in place_dict)
        self.assertTrue("created_at" in place_dict)
        self.assertTrue("updated_at" in place_dict)

    def test_str_representation(self):
        """ Test that the str method has the correct output """
        self.place.id = "1234356"
        self.place.name = "My Place"

        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)

    def test_save(self):
        """ Test that save method updates updated_at """
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_save_to_file(self):
        """ Test that save_to_file method saves to file.json """
        self.place.save()
        with open("file.json", "r") as file:
            self.assertIn(self.place.id, file.read())


if __name__ == "__main__":
    unittest.main()
