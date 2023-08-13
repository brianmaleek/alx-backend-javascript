#!/usr/bin/env python3
""" Unittest for User class """

import unittest
import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Defines tests for User class """

    def setUp(self):
        """ Set up User instance for all tests """
        self.user = User()

    def test_init(self):
        """ Test that User is an instance of BaseModel """
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """ Test that User has expected attributes """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attribute_type(self):
        """ Test that User attributes are the correct type """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_inheritance(self):
        """ Test that User inherits from BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_docstring(self):
        """ Test that User has a docstring """
        self.assertIsNotNone(User.__doc__)

    def test_save(self):
        """ Test that save() adds updated_at attribute """
        self.user.save()
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_str(self):
        """ Test that str method returns a string """
        self.assertIsInstance(str(self.user), str)

    def test_default_attribute_values(self):
        """ Test that User attributes are set to empty strings """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """ Test to_dict method"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Smith"

        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertEqual(user_dict["password"], "password123")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Smith")
        self.assertTrue('__class__' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)

    def test_attribute_assignment(self):
        """ Test attribute assignment method"""
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Smith"

        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Smith")


if __name__ == "__main__":
    unittest.main()
