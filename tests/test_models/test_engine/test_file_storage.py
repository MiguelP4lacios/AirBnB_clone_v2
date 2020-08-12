#!/usr/bin/python3
"""Test File_storage
"""

import unittest
import pep8
import json
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    """Class to test FileStorage"""

    def test_pep8_conformance_FileStorage(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def setUp(self):
        """Set variables"""
        self.my_model = BaseModel()
        self.storaged = FileStorage()

    def test_file_storage_methods(self):
        """test if the methods exist"""
        self.assertTrue(hasattr(self.storaged, "all"))
        self.assertTrue(hasattr(self.storaged, "new"))
        self.assertTrue(hasattr(self.storaged, "save"))
        self.assertTrue(hasattr(self.storaged, "reload"))

    def test_all_method(self):
        """Test for all method
        """
        dict_tmp = self.storaged.all()
        self.assertEqual(type(dict_tmp), dict)
        self.assertIs(dict_tmp, self.storaged._FileStorage__objects)

    def test_new_method(self):
        """Test for new method
        """
        self.storaged.new(self.my_model)
        key = 'BaseModel.{}'.format(self.my_model.id)
        self.assertIn(key, self.storaged.all())

    def test_attr(self):
        """Test for attributes
        """
        self.assertTrue(isinstance(storage._FileStorage__objects, dict))
        self.assertTrue(isinstance(storage._FileStorage__file_path, str))

    def test_save_method(self):
        """Test for save method
        """
        self.my_model.save()
        key = "BaseModel.{}".format(self.my_model.id)
        self.assertIn(key, self.storaged._FileStorage__objects.keys())

    def test_reload_method(self):
        """Test for reload method
        """
        self.storaged.reload()
        self.assertTrue(len(self.storaged._FileStorage__objects) > 0)
