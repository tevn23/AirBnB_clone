#!/usr/bin/env python3
"""
Test cases for the file_storage module
"""
import unittest
from .engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage module"""

    @classmethod
    def setUpClass(cls):
        """Sets up shared test environment"""
        storage = FileStorage()

    def test_all(self):
        """Tests for the all method"""
