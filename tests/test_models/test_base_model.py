#!/usr/bin/env python3
"""
Contains test cases on the base_model
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest.mock import patch, mock_open
from models.__init__ import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel"""
    def setUp(self):
        """Sets up testing environment"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """cleans up the test environment"""
        del self.base1
        del self.base2
        storage.reset()

    @patch("models.__init__.storage.new")
    def test_init(self, mock_new):
        """Test cases for the __init__ method"""
        base = BaseModel()

        # Test Cases of the id attributes
        self.assertIsNotNone(self.base1.id)
        self.assertIsNotNone(self.base2.id)
        self.assertIsInstance(self.base1.id, str)
        self.assertNotEqual(self.base1.id, self.base2.id)

        # Test cases for created_at and updated_at attributes
        self.assertIsNotNone(self.base1.created_at)
        self.assertIsNotNone(self.base2.created_at)
        self.assertIsNotNone(self.base1.updated_at)
        self.assertIsNotNone(self.base2.updated_at)
        self.assertIsInstance(self.base1.created_at, datetime)
        self.assertIsInstance(self.base1.updated_at, datetime)

        # Verify that storage.new() was called once with the new instance
        mock_new.assert_called_once_with(base)

    def test_recreate(self):
        """Test case for objects re-creation"""
        obj_dict = self.base1.to_dict()
        self.base3 = BaseModel(**obj_dict)

        self.assertIsNotNone(self.base3.id)
        self.assertIsInstance(self.base3.id, str)
        self.assertIsNotNone(self.base3.created_at)
        self.assertIsNotNone(self.base3.updated_at)
        self.assertIsInstance(self.base3.created_at, datetime)
        self.assertIsInstance(self.base3.updated_at, datetime)

    def test_empty_dict(self):
        """Empty dict re-creation error case"""
        self.base4 = BaseModel(**{})

        self.assertIsNotNone(self.base4.id)
        self.assertIsInstance(self.base4.id, str)
        self.assertIsNotNone(self.base4.created_at)
        self.assertIsNotNone(self.base4.updated_at)
        self.assertIsInstance(self.base4.created_at, datetime)
        self.assertIsInstance(self.base4.updated_at, datetime)

    def test_str_method(self):
        """Test cases for the __str__ method"""
        s_exp = f"[BaseModel] ({self.base1.id}) {self.base1.__dict__}"
        self.assertEqual(str(self.base1), s_exp)

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save_base_model(self, mock_json_dump, mock_file_open):
        """Test cases for the save method"""
        before_save = self.base1.updated_at
        self.base1.save()
        self.assertNotEqual(before_save, self.base1.updated_at)
        self.assertGreater(self.base1.updated_at, before_save)

        # Checks if open was called with the right arguments
        mock_file_open.assert_called_once_with("data.json",
                                               'w', encoding="utf-8")

        # Indicates expected data by json.dump via storage's save()
        # by instance save()
        key = f"<BaseModel>.{self.base1.id}"
        key2 = f"<BaseModel>.{self.base2.id}"

        r_dict = self.base1.to_dict()
        r_dict2 = self.base2.to_dict()

        # Although save is called on just self.base1
        # self.base2 was added to storage during initialization
        # and is thus saved
        expected_data = {
                key: r_dict,
                key2: r_dict2
        }

        # Checks if json.dump was called with the right arguments
        mock_json_dump.assert_called_once_with(expected_data, mock_file_open())

    def test_to_dict(self):
        """Test cases for the to_dict method"""
        date = self.base1.created_at.isoformat()
        date2 = self.base1.updated_at.isoformat()
        dict_return = self.base1.to_dict()

        self.assertIn("id", dict_return)
        self.assertIn("__class__", dict_return)
        self.assertIn("updated_at", dict_return)
        self.assertIn("created_at", dict_return)
        self.assertIsInstance(dict_return, dict)

        self.assertEqual(dict_return["created_at"], date)
        self.assertEqual(dict_return["updated_at"], date2)
        self.assertEqual(dict_return["__class__"], "BaseModel")
        self.assertIsInstance(dict_return["created_at"], str)
        self.assertIsInstance(dict_return["updated_at"], str)
