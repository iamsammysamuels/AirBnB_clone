#!/usr/bin/env python3
"""Uittests for the base_model module"""


from models.base_model import BaseModel
import pep8
import unittest
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel its instances,
    attributes, instance attributes and methods"""

    def setUp(self):
        """Creates an instance for each function"""
        self.obj = BaseModel()

    def test_pep8_conformation_for_base_model(self):
        """Tests that base_model module is pycodestyled"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        pep8_result = result.total_errors
        self.assertEqual(pep8_result, 0, "Found code style errors (and warnings).")  # noqa

    def test_pep8_conformation_for_test_base_model(self):
        """Tests that test_base_model file is pycodestyled"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_base_model.py"])  # noqa
        pep8_result = result.total_errors
        self.assertEqual(pep8_result, 0, "Found code style errors (and warnings).")  # noqa

    def test_Class_docstring(self):
        """Tests whether the modeule contains docstring"""
        docstring = BaseModel.__doc__
        self.assertTrue(len(docstring) >= 1)

    def test_docstring_for_functions(self):
        """Tests that instance methods have docstrings"""
        docstring = self.obj.__str__.__doc__
        self.assertTrue(len(docstring) >= 1)
        docstring = self.obj.to_dict.__doc__
        self.assertTrue(len(docstring) >= 1)
        docstring = self.obj.save.__doc__
        self.assertTrue(len(docstring) >= 1)

    def test_instance_attributes(self):
        """Test that instances are assigned attributes"""
        self.obj.first_name = "Samuel"
        self.obj.second_name = "Korir"
        self.assertEqual(self.obj.first_name, "Samuel")
        self.assertEqual(self.obj.second_name, "Korir")

    def test_instance_types(self):
        """Tests that instances are objects of the class"""
        self.assertIsInstance(self.obj, BaseModel)
        status = type(self.obj)
        self.assertTrue(status is BaseModel)

    def test_that_id_is_unique(self):
        """Tests that each instance has a unique id"""
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        self.assertNotEqual(obj_1.id, self.obj.id)
        self.assertNotEqual(obj_2.id, self.obj.id)
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_str(self):
        """Tests the __str__ function"""
        test_string = "[{}] ({}) {}".format(self.obj.__class__.__name__, self.obj.id, self.obj.__dict__)  # noqa
        i_string = str(self.obj)
        self.assertEqual(test_string, i_string)
        self.assertTrue("created_at" in i_string)
        self.assertTrue("updated_at" in i_string)
        self.assertTrue("datetime" in i_string)

    def test_to_dict(self):
        """Tests the to_dict method"""
        obj_created_at = self.obj.created_at.isoformat()
        obj_dict = self.obj.to_dict()
        self.assertEqual(obj_dict["created_at"], obj_created_at)
        self.assertTrue(type(obj_dict["created_at"]) is str)
        self.assertTrue("__class__" in obj_dict.keys())
        self.assertEqual(obj_dict["__class__"], self.obj.__class__.__name__)

    def test_from_dict(self):
        """tests initialisation of instance with dict"""
        obj_dict = self.obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(new_obj.created_at, self.obj.created_at)
        self.assertEqual(new_obj.updated_at, self.obj.updated_at)
        self.assertEqual(new_obj.id, self.obj.id)
        self.assertIsInstance(new_obj.created_at, datetime)

    def test_update(self):
        """Tests that instances are updated correctly"""
        update_1 = self.obj.updated_at
        self.obj.save()
        update_2 = self.obj.updated_at
        self.assertNotEqual(update_1, update_2)


if __name__ == "__main__":
    unittest.main()
