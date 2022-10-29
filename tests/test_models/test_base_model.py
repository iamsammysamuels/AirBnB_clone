#!/usr/bin/env python3
"""Uittests for the base_model module"""


from models.base_model import BaseModel
import pep8
import unittest
from models import base_model


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
        docstring = self.obj.__str__().__doc__
        self.assertTrue(len(docstring) >= 1)
        docstring = self.obj.to_dict().__doc__
        self.assertTrue(len(docstring) >= 1)
        docstring = self.obj.save().__doc__

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


if __name__ == "__main__":
    unittest.main()
