#!/usr/bin/python3
"""Model Unittest → Place
"""

import unittest
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class test
    """

    def setUp(self):
        """ setUp init for tests"""
        self.my_model = Place()
        self.my_model2 = Place()
        self.my_model.name = "Vale"
        self.my_model.age = 28

    def test_pep8_conformance_Place(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings(self):
        """Test docstrings"""
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)
        self.assertIsNotNone(Place.__str__.__doc__)
        self.assertIsNotNone(Place.save.__doc__)
        self.assertIsNotNone(Place.to_dict.__doc__)

    def test_base(self):
        """Test for Place
        """
        self.assertIsInstance(self.my_model, Place)
        self.assertEqual(self.my_model.name, "Vale")
        self.assertEqual(self.my_model.age, 28)
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))
        self.assertTrue(hasattr(self.my_model, "__class__"))
        model1 = self.my_model.created_at
        model2 = self.my_model2.created_at
        self.assertTrue(model1 != model2)
        model1 = self.my_model.id
        model2 = self.my_model2.id
        self.assertNotEqual(model1, model2)

    def test_to_dict(self):
        """test_to_dict - test the return of a dict containing
            all the key/values of __dict__"""

        dict_json = self.my_model.to_dict()
        self.assertEqual(type(dict_json), dict)
        self.assertTrue(type(dict_json['created_at']) is str)
        self.assertTrue(type(dict_json['updated_at']) is str)

    def test_save(self):
        """Test for save method
        """
        previous_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(previous_update, self.my_model.updated_at)

    def test_str(self):
        """Test for __str__ method
        """
        self.assertEqual(str(self.my_model), "[Place] ({}) {}".
                         format(self.my_model.id, self.my_model.__dict__))
        self.assertEqual(self.my_model.__str__(), "[Place] ({}) {}".
                         format(self.my_model.id, self.my_model.__dict__))

    def test_kwargs(self):
        """Test for recreate instance from a instance old
        """
        dict_json = self.my_model.to_dict()
        my_model2 = Place(**dict_json)
        self.assertFalse(my_model2 is self.my_model)
        self.assertEqual(self.my_model.id, my_model2.id)
        self.assertEqual(self.my_model.created_at, my_model2.created_at)
        self.assertEqual(self.my_model.updated_at, my_model2.updated_at)


if __name__ == '__main__':
    unittest.main()
