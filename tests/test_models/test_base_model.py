#!/usr/bin/python3

"""This module defines a class BaseModel"""

import uuid
import models
import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def setUp(self):
        """Sets up the class"""
        self.base_model = BaseModel()

    def test_init(self):
        """Tests the __init__ method"""
        self.assertTrue(isinstance(self.base_model, BaseModel))

    def test_id_attribute(self):
        """Tests the id attribute"""
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertEqual(type(self.base_model.id), str)

    def test_created_at_attribute(self):
        """Tests the created_at attribute"""
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertEqual(type(self.base_model.created_at), datetime)

    def test_updated_at_attribute(self):
        """Tests the updated_at attribute"""
        self.assertTrue(hasattr(self.base_model, "updated_at"))
        self.assertEqual(type(self.base_model.updated_at), datetime)

    def test_save_method(self):
        """Tests the save method"""
        initial_created_at = self.base_model.created_at
        sleep(0.05)
        self.base_model = BaseModel()
        self.base_model.save()
        self.assertNotEqual(initial_created_at, self.base_model.created_at)

    def test_str_representation(self):
        """Tests the __str__ method"""
        self.base_model.id = "123456"
        self.base_model.created_at = datetime.now() - timedelta(days=1)
        self.base_model.updated_at = datetime.now()
        expected_str = f"[BaseModel] (123456) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_method(self):
        """Tests the to_dict method"""
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertEqual(base_model_dict["id"], self.base_model.id)
        self.assertEqual(base_model_dict["created_at"],
                         self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"],
                         self.base_model.updated_at.isoformat())

    def test_constructor_with_kwargs_without_attributes(self):
        """Tests the constructor with kwargs without attributes"""
        kwargs = {}
        new_base_model = BaseModel(**kwargs)
        self.assertTrue(hasattr(new_base_model, "id"))
        self.assertTrue(hasattr(new_base_model, "created_at"))
        self.assertTrue(hasattr(new_base_model, "updated_at"))

    def test_str_representation(self):
        """Tests the __str__ method"""
        self.base_model.id = "123456"
        self.base_model.created_at = datetime.now() - timedelta(days=1)
        self.base_model.updated_at = datetime.now()
        expected_str = f"[BaseModel] (123456) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_constructor_without_args(self):
        """Tests the constructor without args"""
        new_base_model = BaseModel()
        self.assertTrue(isinstance(new_base_model.id, str))
        self.assertTrue(isinstance(new_base_model.created_at, datetime))
        self.assertTrue(isinstance(new_base_model.updated_at, datetime))

    def test_constructor_with_args(self):
        """Tests the constructor with args"""
        new_base_model = BaseModel()
        self.assertEqual(type(new_base_model.id), str)
        self.assertTrue(isinstance(new_base_model.created_at, datetime))
        self.assertTrue(isinstance(new_base_model.updated_at, datetime))

    def test_attribute_initialization(self):
        """Tests the initialization of the attributes"""
        self.assertTrue(isinstance(self.base_model.id, str))
        self.assertTrue(isinstance(self.base_model.created_at, datetime))
        self.assertTrue(isinstance(self.base_model.updated_at, datetime))

    def test_save_updates_updated_at(self):
        """Tests that save updates the updated_at attribute"""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_include_class_name(self):
        """Tests that to_dict includes the class key"""
        base_model_dict = self.base_model.to_dict()
        self.assertTrue("__class__" in base_model_dict)


if __name__ == "__main__":
    unittest.main()
