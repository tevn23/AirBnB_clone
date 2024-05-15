#!/usr/bin/env python3
"""Contains test cases on the base_model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel"""

    def setUp(self):
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def test_init(self):
        # Test Cases of the id attributes
        self.assertIsNotNone(self.base1.id)
        self.assertIsNotNone(self.base2.id)
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertIsInstance(self.base1.id, str)

        # Test cases for created_at and updated_at attributes
        self.assertIsNotNone(self.base1.created_at)
        self.assertIsNotNone(self.base2.created_at)
        self.assertIsNotNone(self.base1.updated_at)
        self.assertIsNotNone(self.base2.updated_at)
        self.assertIsInstance(self.base1.created_at, datetime)
        self.assertIsInstance(self.base1.updated_at, datetime)

        with self.assertRaises(TypeError):
            base1 = BaseModel("s")

    def test_str_method(self):
        
        s_exp = f"[BaseModel] ({self.base1.id}) {self.base1.__dict__}"
        self.assertEqual(str(self.base1), s_exp)

    def test_save(self):

        before_save = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(before_save, self.base1.updated_at)
        self.assertGreater(self.base1.updated_at, before_save)


    def test_to_dict(self):
        
        isofmt = self.base1.created_at.isoformat()
        isofmt2 = self.base1.updated_at.isoformat()
        dict_return = self.base1.to_dict()
       

        self.assertIsInstance(dict_return, dict)
        self.assertIn("id", dict_return)
        self.assertIn("updated_at", dict_return)
        self.assertIn("created_at", dict_return)
        self.assertIn("__class__", dict_return)

        self.assertEqual(dict_return["created_at"], isofmt)
        self.assertEqual(dict_return["updated_at"], isofmt2)
        self.assertIsInstance(dict_return["created_at"], str)
        self.assertIsInstance(dict_return["updated_at"], str)
        self.assertEqual(dict_return["__class__"], "BaseModel")
