#!/usr/bin/python3
"""State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test for State class"""

    s = State()

    def test_docstring(self):
        """Testing docstring documentation"""
        self.assertIsNone(State.__doc__)

    def test_hasattr(self):
        """Test if has an attr"""
        self.assertTrue(hasattr(s, "name"))

    def test_instance(self):
        """testing if is instance"""
        self.assertIsInstance(s, State)

    def test_type_name(self):
        self.assertEqual(type(s.name), str)
