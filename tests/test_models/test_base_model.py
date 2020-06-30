#!/usr/bin/python3
"""Test for BaseModel class"""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    b1 = BaseModel()
    b2 = BaseModel()

    def test_docstring_module(self):
        """Documentation"""
        self.assertGreater(len(BaseModel.__doc__), 1)

    def test_create(self):
        """test the creation of a BaseModel"""

        self.assertTrue(self.b1)
        self.assertTrue(self.b2)

    def test_file(self):
        """check if the file exists and delete it"""

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_check_id(self):
        """check id of each object"""

        self.assertNotEqual(self.b1, self.b2)

    def test_attr_test(self):
        """checks for user data created attributes"""

        self.b1.name = "Juliana"
        self.b2.name = "Adrian"
        self.assertEqual(self.b1.name, "Juliana")
        self.assertEqual(self.b2.name, "Adrian")
        self.assertNotEqual(self.b1.name, self.b2.name)

    def test_update_name(self):
        """checks for update user name attributes"""

        self.b1.name = "Juliana"
        self.b2.name = "Adrian"
        self.b1.name = "Julianita"
        self.assertTrue(self.b1.name, "Julianita")
        self.assertTrue(self.b2.name, "Adrian")
