#!/usr/bin/env python3
"""
Contains place test cases
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestCase(unittest.TestCase):
    """Place class test cases"""
    def test_place(self):
        """Testing place class instantiation"""
        place1 = Place()

        self.assertTrue(issubclass(type(place1), BaseModel))
        self.assertIsInstance(place1, Place)

        self.assertIsNotNone(place1.city_id)
        self.assertIsInstance(place1.city_id, str)

        self.assertIsNotNone(place1.user_id)
        self.assertIsInstance(place1.user_id, str)

        self.assertIsNotNone(place1.name)
        self.assertIsInstance(place1.name, str)

        self.assertIsNotNone(place1.description)
        self.assertIsInstance(place1.description, str)

        self.assertIsNotNone(place1.number_rooms)
        self.assertIsInstance(place1.number_rooms, int)

        self.assertIsNotNone(place1.number_bathrooms)
        self.assertIsInstance(place1.number_bathrooms, int)

        self.assertIsNotNone(place1.max_guest)
        self.assertIsInstance(place1.max_guest, int)

        self.assertIsNotNone(place1.price_by_night)
        self.assertIsInstance(place1.price_by_night, int)

        self.assertIsNotNone(place1.latitude)
        self.assertIsInstance(place1.latitude, float)

        self.assertIsNotNone(place1.longitude)
        self.assertIsInstance(place1.longitude, float)

        self.assertIsNotNone(place1.amenity_ids)
        self.assertIsInstance(place1.amenity_ids, list)
