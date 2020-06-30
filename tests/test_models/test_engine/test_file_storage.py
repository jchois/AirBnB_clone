#!/usr/bin/python3
""" Test case FileStorage module"""
import unittest
import os
import contextlib
import pep8

# class
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """"""

    b1 = BaseModel()
    a1 = Amenity()
    c1 = City()
    p1 = Place()
    r1 = Review()
    s1 = State()
    u1 = User()
    storage = FileStorage()

    def test_del_file(self):
        """Check the file.json and delete de objects"""


       # del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_storage_empty(self):
        """check the storage is not empty"""

        self.assertIsNotNone(self.storage.all())

    def test_storage_all_type(self):
        """check the type of storage"""

        self.assertEqual(dict, type(self.storage.all()))

    def test_docstrings(self):
        """Check the docString each function"""

        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertTrue(hasattr(FileStorage, 'reload'))


if __name__ == '__main__':
    unittest.main()
