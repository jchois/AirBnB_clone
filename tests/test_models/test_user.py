#!/usr/bin/python3
"""Test User class"""
import unittest
from models.user import User
import pep8


class TestUser(unittest.TestCase):
    """class"""

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_type_users(self):
        """Test the type"""
        u = User()
        self.assertEqual(type(u.email), str)
        self.assertEqual(type(u.password), str)
        self.assertEqual(type(u.first_name), str)
        self.assertEqual(type(u.last_name), str)

    def test_instance(self):
        """Test instance"""
        u = User()
        self.assertIsInstance(u, User)

    def test_docstring(self):
        """Test documentation"""
        u = User.__doc__
        self.assertGreater(len(u), 1)
