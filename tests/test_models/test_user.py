#!/usr/bin/python3
"""Test User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """class"""

    def test_type_users(self):
        """Test the type"""
        u = User()
        self.assertEqual(type(u.email), str)
        self.assertEqual(type(u.password), str)
        self.assertEqual(type(u.first_name), str)
        self.assertEqual(type(u.last_name), str)
