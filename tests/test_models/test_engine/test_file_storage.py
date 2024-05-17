#!/usr/bin/env python3
"""
Test cases for the file_storage module
"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Sets up test environment"""
        self.maxDiff = None
        self.storage = FileStorage()
        self.base1 = BaseModel()
        self.test_file = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Cleans up test environment"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_empty(self):
        """Test on empty storage"""
        FileStorage._FileStorage__objects = {}
        self.assertEqual(self.storage.all(), {})
        self.assertIsInstance(self.storage.all(), dict)
        del self.storage

    def test_all_with_content(self):
        """Test with content"""
        key = f"<{self.base1.__class__.__name__}>.{self.base1.id}"
        FileStorage._FileStorage__objects = {}
        self.storage.new(self.base1)
        returned_dict = self.storage.all()
        expected_str = self.base1.to_dict()

        self.assertEqual(returned_dict[key], expected_str)
        self.assertIsInstance(returned_dict, dict)
        del self.storage

    def test_new(self):
        """Tests for the new method"""
        self.storage.new(self.base1)
        key = f"<{self.base1.__class__.__name__}>.{self.base1.id}"
        
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.base1.to_dict())
        del self.storage

    def test_save(self):
        """Test cases for the save method"""
        self.storage.new(self.base1)
        self.storage.save()
        with open(self.test_file, encoding="utf-8") as file:
            content = json.load(file)

        key = f"<{self.base1.__class__.__name__}>.{self.base1.id}"
        self.assertIn(key, content)
        self.assertEqual(content[key], self.base1.to_dict())
        del self.storage

    def test_reload(self):
        """Test cases for the reload method"""
        FileStorage._FileStorage__objects = {}
        # Assert __objects is empty
        self.assertEqual(self.storage.all(), {})
        # Add new instance to __objects 
        self.storage.new(self.base1)
        # Saves __objects to file
        self.storage.save()
        # Delete storage instance to remove __objects attribute
        del self.storage
        # Reinitialize storage instance
        self.storage = FileStorage()
        FileStorage._FileStorage__objects = {}
        # Assert __objects is empty
        self.assertEqual(self.storage.all(), {})
        # Reload _objects content from file
        self.storage.reload()
        # Assert __objects now contains file
        key = f"<{self.base1.__class__.__name__}>.{self.base1.id}"
        self.assertEqual(self.storage.all()[key], self.base1.to_dict())
        del self.storage

