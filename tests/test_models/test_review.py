#!/usr/bin/env python3

"""Unittest for Review class """

import unittest
import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Defines tests for class Review """

    def setUp(self):
        """ Set up Review instance for all tests """
        self.review = Review()

    def test_init(self):
        """ Test that Review is an instance of BaseModel """
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """ Test that Review has expected attributes """
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_attribute_type(self):
        """ Test that Review attributes are the correct type """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_attribute_values(self):
        """ Test that Review attributes are set to empty strings """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_assignment(self):
        """ Test that Review attributes can be assigned """
        self.review.place_id = "123456"
        self.review.user_id = "123456"
        self.review.text = "This is a review"

        self.assertEqual(self.review.place_id, "123456")
        self.assertEqual(self.review.user_id, "123456")
        self.assertEqual(self.review.text, "This is a review")

    def test_to_dict(self):
        """ Test to_dict method"""
        self.review.place_id = "123456"
        self.review.user_id = "123456"
        self.review.text = "This is a review"

        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["place_id"], "123456")
        self.assertEqual(review_dict["user_id"], "123456")
        self.assertEqual(review_dict["text"], "This is a review")
        self.assertTrue('__class__' in review_dict)
        self.assertTrue('created_at' in review_dict)
        self.assertTrue('updated_at' in review_dict)

    def test_inheritance(self):
        """ Test that Review inherits from BaseModel """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_docstring(self):
        """ Test that Review has a docstring """
        self.assertIsNotNone(Review.__doc__)

    def test_str(self):
        """ Test that str method returns a string """
        self.assertIsInstance(str(self.review), str)

    def test_save(self):
        """ Test that save() adds updated_at attribute """
        self.review.save()
        self.assertIsInstance(self.review.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
