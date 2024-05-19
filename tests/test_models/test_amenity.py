#!/usr/bin/env python3
"""
Contains Amenity class test cases
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestCase(unittest.TestCase):
    """Amenity class test case"""
    def test_amenity(self):
        """Amenity instantiation test"""
        amenity1 = Amenity()

        self.assertTrue(issubclass(type(amenity1), BaseModel))
        self.assertIsInstance(amenity1, Amenity)
        self.assertIsNotNone(amenity1.name)
