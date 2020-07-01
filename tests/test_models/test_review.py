#!/usr/bin/python3
"""TestCase Review module"""
import unittest
import os
import pep8
from models.review import Review
from datetime import datetime


class TestCasesReview(unittest.TestCase):
    """"""

    r1 = Review()
    r2 = Review()

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_module(self):
        """Check for the DocString"""

        self.assertGreater(len(Review.__doc__), 1)

    def test_create(self):
        """Check for the objects"""

        self.assertTrue(self.r1)
        self.assertTrue(self.r2)

    def test_file(self):
        """Check for the file is create"""

        r3 = Review()
        r3.save()
        with open('file.json', 'r') as f:
            self.assertIn(r3.id, f.read())

    def test_file_exists(self):
        """Check for the file Exists"""

        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_attr_test(self):
        """Check for user data created attributes"""

        self.r1.name = "Good"
        self.r2.name = "More or Less"
        self.assertEqual(self.r1.name, "Good")
        self.assertEqual(self.r2.name, "More or Less")

    def test_update_name(self):
        """Check for update user name attributes"""

        self.r1.name = "Good"
        self.r2.name = "More or Less"
        self.r1.name = "Fine"
        self.assertEqual(self.r1.name, "Fine")
        self.assertEqual(self.r2.name, "More or Less")

    def test_created_at(self):
        """Check created_at is of the datetime"""

        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(self.r1.created_at))
        self.assertEqual(datetime, type(self.r2.created_at))

    def test_update_at(self):
        """check update_at is of the datetime"""

        self.assertEqual(datetime, type(Review().updated_at))
        self.assertEqual(datetime, type(self.r1.updated_at))
        self.assertEqual(datetime, type(self.r2.updated_at))


if __name__ == '__main__':
    unittest.main()
