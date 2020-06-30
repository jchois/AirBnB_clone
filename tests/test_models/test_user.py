#!/usr/bin/python3
"""Test User class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """class"""

    def test_email_user(self):
        """Test email user"""
        self.assertEqual(type(User.email), str)

    def test_pass_user(self):
        """Test password user"""
        self.assertEqual(type(User.password), str)

    def test_first_name(self):
        """Test first_name"""
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        """Test first_name"""
        self.assertEqual(type(User.last_name), str)
