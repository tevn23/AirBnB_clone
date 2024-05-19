#!/usr/bin/env python3
"""
Contains state class test cases
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestCase(unittest.TestCase):
    """State class tests"""
    def test_state(self):
        """testing instantiation"""
        state1 = State()

        self.assertIsInstance(state1, State)
        self.assertTrue(issubclass(type(state1), BaseModel))
        self.assertIsNotNone(state1.name)
