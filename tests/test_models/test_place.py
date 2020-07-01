#!/usr/bin/python3
"""Test Place class"""
import unittest
from models.place import Place
import pep8


class TestPlace(unittest.TestCase):
    """Test for Place class"""

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_instance(self):
        """Test instance"""
        p = Place()
        self.assertIsInstance(p, Place)

    def test_type_place(self):
        """ Testing type of attr"""
        p = Place()
        self.assertEqual(type(p.city_id), str)
        self.assertEqual(type(p.user_id), str)
        self.assertEqual(type(p.name), str)
        self.assertEqual(type(p.description), str)
        self.assertEqual(type(p.number_rooms), int)
        self.assertEqual(type(p.number_bathrooms), int)
        self.assertEqual(type(p.max_guest), int)
        self.assertEqual(type(p.price_by_night), int)
        self.assertEqual(type(p.latitude), float)
        self.assertEqual(type(p.longitude), float)
        self.assertEqual(type(p.amenity_ids), list)

    def test_docstring(self):
        """Test documentation"""
        p = Place.__doc__
        self.assertGreater(len(p), 1)
