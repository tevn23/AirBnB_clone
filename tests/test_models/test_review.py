#!/usr/bin/env python3
"""
Contains Review class test cases
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class Testcase(unittest.TestCase):
    """Review class test cases"""
    def test_review(self):
        """Testing review class instantiation"""
        review1 = Review()

        self.assertTrue(issubclass(type(review1), BaseModel))
        self.assertIsInstance(review1, Review)

        self.assertIsNotNone(review1.place_id)
        self.assertIsInstance(review1.place_id, str)

        self.assertIsNotNone(review1.user_id)
        self.assertIsInstance(review1.user_id, str)

        self.assertIsNotNone(review1.text)
        self.assertIsInstance(review1.text, str)
