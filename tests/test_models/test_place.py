#!/usr/bin/env python3
"""Test module for Place"""

import unittest
import pep8
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    class for testing Place class' methods
    """

    def test_pep8_conformance_Place(self):
        """
        Test that place.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")  # noqa

    def test_pep8_conformance_test_place(self):
        """
        Test that test_place.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")  # noqa
 
    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def setUp(self):
        """set up method for place class
        """
        self.P = Place()

    def tearDown(self):
        """initialized method for place
        """
        self.P = None

    def test_type(self):
        """test method for type testing of place
        """
        self.assertIsInstance(self.P, Place)
        self.assertEqual(type(self.P), Place)
        self.assertEqual(issubclass(self.P.__class__, Place), True)
        self.assertEqual(isinstance(self.P, Place), True)

    def test_city_id_type(self):
        """tests the city_id class attributes type for Place
        """
        self.assertEqual(type(Place.city_id), str)

    def test_user_id_type(self):
        """tests the user_id class attributes type for Place
        """
        self.assertEqual(type(Place.user_id), str)

    def test_name_type(self):
        """tests the name class attributes type for Place
        """
        self.assertEqual(type(Place.name), str)

    def test_description_type(self):
        """tests the description class attributes type for Place
        """
        self.assertEqual(type(Place.description), str)

    def test_number_rooms_type(self):
        """tests the number_rooms class attributes type for Place
        """
        self.assertEqual(type(Place.number_rooms), int)

    def test_number_bathrooms_type(self):
        """tests the number_bathrooms class attributes type for Place
        """
        self.assertEqual(type(Place.number_bathrooms), int)

    def test_max_guest_type(self):
        """tests the max_guest class attributes type for Place
        """
        self.assertEqual(type(Place.max_guest), int)

    def test_price_by_night_type(self):
        """tests the price_by_night class attributes type for Place
        """
        self.assertEqual(type(Place.price_by_night), int)

    def test_latitude_type(self):
        """tests the latitude class attributes type for Place
        """
        self.assertEqual(type(Place.latitude), float)

    def test_longitude_type(self):
        """tests the longitude class attributes type for Place
        """
        self.assertEqual(type(Place.longitude), float)

    def test_basic_attribute_set(self):
        """test method for basic attribute assignment
        """
        self.P.first_name = 'Sammy'
        self.P.last_name = 'Samuels'
        self.assertEqual(self.P.first_name, 'Sammy')
        self.assertEqual(self.P.last_name, 'Samuels')

