#!/usr/bin/python3

"""Unittest for FileStorage class"""

import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class TestFileStorageDocs(unittest.TestCase):
    """Test for the file storage docs"""

    def test_class_doc(self):
        """Test for the existence of class doc"""
        self.assertTrue(len(models.storage.__doc__) > 0)

    def test_method_docs(self):
        """Test for the existence of method doc"""
        for func in dir(models.storage):
            self.assertTrue(len(func.__doc__) > 0)


class TestFileStorageInstance(unittest.TestCase):
    """Test for the file storage class instance creation"""

    def test_instance(self):
        """Test for the creation of a FileStorage class instance"""
        self.assertIsInstance(models.storage, FileStorage)

    def test_instantiation(self):
        """Test with no args passed into instantiation"""
        self.assertEqual(type(FileStorage()), FileStorage)

        """Test for passing an argument to the FileStorage instance"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path(self):
        """Test for the file path attribute"""
        self.assertEqual(type(models.storage._FileStorage__file_path), str)

    def test_objects(self):
        """Test for the objects attribute"""
        self.assertEqual(type(models.storage._FileStorage__objects), dict)


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test methods"""
        self.storage = models.storage
        self.file_path = models.storage._FileStorage__file_path

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.storage.all(), dict)

        """Test all with arguments"""
        with self.assertRaises(TypeError):
            self.storage.all(1, 2)

    def test_new(self):
        """Test new method"""
        self.storage.new(User())
        self.storage.new(State())
        self.storage.new(City())
        self.storage.new(Amenity())
        self.storage.new(Place())
        self.storage.new(Review())
        self.storage.new(BaseModel())
        self.storage.save()

        self.assertIn("User." + User().id, models.storage.all().keys())
        self.assertIn(User(), models.storage.all().values())
        self.assertIn("State." + State().id, models.storage.all().keys())
        self.assertIn("City." + City().id, models.storage.all().keys())
        self.assertIn("Amenity." + Amenity().id, models.storage.all().keys())
        self.assertIn("Place." + Place().id, models.storage.all().keys())
        self.assertIn("Review." + Review().id, models.storage.all().keys())
        self.assertIn("BaseModel." + BaseModel().id, models.storage.all()
                      .keys())
        """Test new method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.new(1, 2)

    def test_save(self):
        """Test save method"""
        models.storage.new(User())
        models.storage.new(State())
        models.storage.new(City())
        models.storage.new(Amenity())
        models.storage.new(Place())
        models.storage.new(Review())
        models.storage.new(BaseModel())
        models.storage.save()
        text_saved = ""
        with open("file.json", 'r') as f:
            text_saved = f.read()
        self.assertTrue(len(text_saved) > 0)

        """Test save method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.save(1, 2)

    def test_reload(self):
        """Test reload method"""
        self.storage.reload()
        self.assertIsInstance(self.storage.all(), dict)

        """Test reload method with arguments"""
        with self.assertRaises(TypeError):
            self.storage.reload(1, 2)
