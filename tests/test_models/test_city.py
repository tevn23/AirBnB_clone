#!/usr/bin/env python3
"""
Contains City class testcases
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCase(unittest.TestCase):
    """City class test cases"""

    def test_city(self):
        """Testing instantiation"""
        city1 = City()

        self.assertIsNotNone(city1.name)
        self.assertIsNotNone(city1.state_id)
        self.assertIsInstance(city1, BaseModel)
        self.assertTrue(issubclass(type(city1), BaseModel))
