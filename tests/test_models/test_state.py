#!/usr/bin/env python3
"""Unittest for State class """

import unittest
import datetime
from models.state import State
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Defines tests for class State """

    def setUp(self):
        """ Set up State instance for all tests """
        self.state = State()

    def test_init(self):
        """ Test that State is an instance of BaseModel """
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """ Test that State has expected attributes """
        self.assertTrue(hasattr(self.state, "name"))

    def test_attribute_type(self):
        """ Test that State attributes are the correct type """
        self.assertIsInstance(self.state.name, str)

    def test_inheritance(self):
        """ Test that State inherits from BaseModel """
        self.assertTrue(issubclass(State, BaseModel))

    def test_docstring(self):
        """ Test that State has a docstring """
        self.assertIsNotNone(State.__doc__)

    def test_save(self):
        """ Test that save() adds updated_at attribute """
        self.state.save()
        self.assertIsInstance(self.state.updated_at, datetime.datetime)

    def test_str(self):
        """ Test that str method returns a string """
        self.assertIsInstance(str(self.state), str)

    def test_default_attribute_values(self):
        """ Test that State attributes are set to empty strings """
        self.assertEqual(self.state.name, "")

    def test_attribute_assignment(self):
        """ Test that State attributes can be assigned """
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_to_dict(self):
        """ Test to_dict method"""
        self.state.name = "California"

        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["name"], "California")
        self.assertEqual(state_dict["__class__"], "State")
        self.assertTrue('__class__' in state_dict)
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)


if __name__ == "__main__":
    unittest.main()
