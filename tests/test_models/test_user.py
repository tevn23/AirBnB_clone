#!/usr/bin/env python3
"""
Test cases for the User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestCase(unittest.TestCase):
    """Test case for User class"""

    def test_user(self):
        """Test cases for the user class"""
        user1 = User()

        self.assertIsInstance(user1, User)
        self.assertTrue(issubclass(type(user1), BaseModel))
        self.assertIsNotNone(user1.email)
        self.assertIsNotNone(user1.password)
        self.assertIsNotNone(user1.last_name)
        self.assertIsNotNone(user1.first_name)
