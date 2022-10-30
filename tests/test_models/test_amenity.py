#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Test modele for Amenity
"""
import unittest
import pep8
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    class for testing Amenity class' methods
    """

    def test_pep8_conformance_Amenity(self):
        """
        Test that amenity.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_pep8_conformance_test_Amenity(self):
        """
        Test that test_amenity.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])  # noqa
        self.assertEqual(result.total_errors, 1, "Found code style errors (and warnings).")  # noqa

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def setUp(self):
        """Set up method for amenity class
        """
        self.A = Amenity()

    def tearDown(self):
        """Initialized method for class Amenity
        """
        self.A = None

    def test_type(self):
        """test method for type testing of amenity
        """
        self.assertIsInstance(self.A, Amenity)
        self.assertEqual(type(self.A), Amenity)
        self.assertEqual(issubclass(self.A.__class__, Amenity), True)
        self.assertEqual(isinstance(self.A, Amenity), True)

    def test_name_type(self):
        """tests the name type of attribute
        """
        self.assertEqual(type(Amenity.name), str)

