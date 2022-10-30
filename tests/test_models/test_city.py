#!/usr/bin/env python3

"""Test module for City"""

import unittest
import pep8
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """
    class for testing City class' methods
    """

    def test_pep8_conformance_City(self):
        """
        Test that city.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_City(self):
        """
        Test that test_city.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(City.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(City.__doc__) >= 1)

    def setUp(self):
        """Set up mehtod for city class
        """
        self.C = City()

    def tearDown(self):
        """Initialized City class
        """
        self.C = None

    def test_type(self):
        """test method for type testing of city
        """
        self.assertIsInstance(self.C, City)
        self.assertEqual(type(self.C), City)
        self.assertEqual(issubclass(self.C.__class__, City), True)
        self.assertEqual(isinstance(self.C, City), True)

    def test_state_id_type(self):
        """tests the state_id type attribute
        """
        self.assertEqual(type(City.state_id), str)

    def test_name_type(self):
        """tests the name type of class attribute
        """
        self.assertEqual(type(City.name), str)

    def test_basic_attribute_set(self):
        """test method for basic attribute
        """
        self.C.first_name = 'Sammy'
        self.C.last_name = 'Korir'
        self.assertEqual(self.C.first_name, 'Sammy')
        self.assertEqual(self.C.last_name, 'Korir')
