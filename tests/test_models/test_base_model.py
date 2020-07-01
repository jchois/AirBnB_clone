#!/usr/bin/python3
"""Test for BaseModel class"""
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime
import pep8


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    b1 = BaseModel()
    b2 = BaseModel()

    def test_docstring_module(self):
        """Documentation"""
        self.assertGreater(len(BaseModel.__doc__), 1)

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""

        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

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

    def test_kwarg_creation(self):
        """Tests when passing attribute value"""

        b3 = BaseModel(id="1234")
        self.assertEqual(b3.id, "1234")

    def test_file_save(self):
        """Test that info is saved to file"""
        b3 = BaseModel()
        b3.save()
        with open("file.json", 'r') as f:
            self.assertIn(b3.id, f.read())

    def test_create_at(self):
        """check created_at is of the datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(self.b1.created_at))
        self.assertEqual(datetime, type(self.b2.created_at))

    def test_update_at(self):
        """check update_at is of the datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))
        self.assertEqual(datetime, type(self.b1.updated_at))
        self.assertEqual(datetime, type(self.b2.updated_at))

    def test_to_dict_contens(self):
        """check to_dict"""
        self.assertIn("created_at", self.b1.to_dict())
        self.assertIn("updated_at", self.b1.to_dict())
        self.assertIn("__class__", self.b1.to_dict())
        self.assertIn("name", self.b1.to_dict())
        self.b1.name = "Juliana"
        self.assertIn('name', self.b1.to_dict())

    def test_docstrings(self):
        """docsting of each function"""

        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(hasattr(BaseModel, '__str__'))
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(hasattr(BaseModel, 'save'))
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(hasattr(BaseModel, 'to_dict'))
        self.assertTrue(BaseModel.to_dict.__doc__)


if __name__ == '__main__':
    unittest.main()
