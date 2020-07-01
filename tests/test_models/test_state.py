#!/usr/bin/python3
"""State class"""
import unittest
from models.state import State
import pep8


class TestState(unittest.TestCase):
    """Test for State class"""

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """Testing docstring documentation"""
        s = State.__doc__
        self.assertGreater(len(s), 1)

    def test_hasattr(self):
        """Test if has an attr"""
        s = State()
        self.assertTrue(hasattr(s, "name"))

    def test_instance(self):
        """testing if is instance"""
        s = State()
        self.assertIsInstance(s, State)

    def test_type_name(self):
        """Testing type of attr"""
        s = State()
        self.assertEqual(type(s.name), str)
