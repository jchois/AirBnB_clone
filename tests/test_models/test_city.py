#!/usr/bin/python3
"""TestCases City module"""
import unittest
import os
import pep8
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test User class"""

    c1 = City()
    c2 = City()

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_module(self):
        """Check for the DocString"""

        self.assertGreater(len(City.__doc__), 1)

    def test_create(self):
        """Check for the objects"""

        self.assertTrue(self.c1)
        self.assertTrue(self.c2)

    def test_file(self):
        """Check for the file is create"""

        c3 = City()
        c3.save()
        with open('file.json', 'r') as f:
            self.assertIn(c3.id, f.read())

    def test_file_exists(self):
        """Check for the file Exists"""

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attr_test(self):
        """Check for user data created attributes"""

        self.c1.name = "Barranquilla"
        self.c2.name = "Puerto Colombia"
        self.assertEqual(self.c1.name, "Barranquilla")
        self.assertEqual(self.c2.name, "Puerto Colombia")

    def test_update_name(self):
        """Check for update user name attributes"""

        self.c1.name = "Barranquilla"
        self.c2.name = "Puerto Colombia"
        self.c1.name = "Cartagena"
        self.assertEqual(self.c1.name, "Cartagena")
        self.assertEqual(self.c2.name, "Puerto Colombia")

    def test_created_at(self):
        """Check created_at is of the datetime"""

        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(self.c1.created_at))
        self.assertEqual(datetime, type(self.c2.created_at))

    def test_update_at(self):
        """check update_at is of the datetime"""

        self.assertEqual(datetime, type(City().updated_at))
        self.assertEqual(datetime, type(self.c1.updated_at))
        self.assertEqual(datetime, type(self.c2.updated_at))


if __name__ == '__main__':
    unittest.main()
