#!/usr/bin/env python3
"""
Test cases for the file_storage module
"""
import os
import json
import unittest
from unittest.mock import patch, mock_open, call
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Sets up test environment for entire class"""
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Clean up test environment"""
        cls.storage.reset()
        del cls.storage

    def setUp(self):
        """Sets up test environment"""
        self.base1 = BaseModel()
        self.storage.new(self.base1)
        self.key = f"<BaseModel>.{self.base1.id}"
        r_dict = self.base1.to_dict()
        self.expected_data = {self.key: r_dict}

    def tearDown(self):
        """Clean up test environment"""
        self.storage.reset()

    def test_all(self):
        """Test cases for the all method"""
        self.storage.reset()
        r_dict = self.storage.all()
        self.assertEqual(r_dict, {})
        self.assertIsInstance(r_dict, dict)

    def test_new(self):
        """Test cases for the new method"""
        r_dict = self.storage.all()
        key = f"<BaseModel>.{self.base1.id}"
        self.assertIn(key, r_dict)

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.dump")
    def test_save(self, mock_json_dump, mock_file_open):
        """Test cases for the save method"""
        self.storage.save()

        # Checks if open was called with the right arguments
        mock_file_open.assert_called_once_with("data.json",
                                               'w', encoding="utf-8")

        # Checks if json.dump was called with the right arguments
        mock_json_dump.assert_called_once_with(self.expected_data,
                                               mock_file_open())

    @patch("builtins.open", new_callable=mock_open)
    @patch("json.load")
    @patch("json.dump")
    def test_reload(self, mock_json_dump, mock_json_load, mock_file_open):
        """Test cases for the reload method"""
        # mock data for json.dump during save
        mock_json_dump.return_value = None

        # mock json.dump call during save operation
        self.storage.save()

        # Resets storage to ensure it starts empty
        self.storage.reset()
        self.assertEqual(self.storage.all(), {})

        # Mock return value for json.load
        mock_json_load.return_value = self.expected_data

        # Reload storage with mocked data
        self.storage.reload()

        # Assert storage now contains reloaded data
        self.assertIn(self.key, self.storage.all())  # Key check

        r_dict_val = self.storage.all()[self.key]  # Value check
        self.assertEqual(r_dict_val, self.expected_data[self.key])

        # Assert open() was called exactly twice
        mock_file_open.assert_has_calls([
            call("data.json", encoding="utf-8"),
            call("data.json", 'w', encoding="utf-8")
        ], any_order=True)

        # Assert json.load was called exactly once
        mock_json_load.assert_called_once_with(mock_file_open())
