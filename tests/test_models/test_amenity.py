#!/usr/bin/python3
"""TestCases Amenity module"""
import unittest
import os
import pep8
from models.amenity import Amenity
from datetime import datetime


class TestCasesAmenity(unittest.TestCase):
    """TestAmenity class module"""

    a1 = Amenity()
    a2 = Amenity()

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_module(self):
        """Check for the DocString"""

        self.assertGreater(len(Amenity.__doc__), 1)

    def test_create(self):
        """Check for the objects"""

        self.assertTrue(self.a1)
        self.assertTrue(self.a2)

    def test_file(self):
        """Check for the file is create"""

        a3 = Amenity()
        a3.save()
        with open('file.json', 'r') as f:
            self.assertIn(a3.id, f.read())

    def test_file_exists(self):
        """Check for the file Exists"""

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attr_test(self):
        """Check for user data created attributes"""

        self.a1.name = "High"
        self.a2.name = "Normal"
        self.assertEqual(self.a1.name, "High")
        self.assertEqual(self.a2.name, "Normal")

    def test_update_name(self):
        """Check for update user name attributes"""

        self.a1.name = "High"
        self.a2.name = "Normal"
        self.a1.name = "Low"
        self.assertEqual(self.a1.name, "Low")
        self.assertEqual(self.a2.name, "Normal")

    def test_created_at(self):
        """Check created_at is of the datetime"""

        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(self.a1.created_at))
        self.assertEqual(datetime, type(self.a2.created_at))

    def test_update_at(self):
        """check update_at is of the datetime"""

        self.assertEqual(datetime, type(Amenity().updated_at))
        self.assertEqual(datetime, type(self.a1.updated_at))
        self.assertEqual(datetime, type(self.a2.updated_at))


if __name__ == '__main__':
    unittest.main()
