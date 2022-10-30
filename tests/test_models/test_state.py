#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests the State class"""

import unittest
import pep8
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """class TestCase"""

    def test_pep8_conformance_State(self):
        """
        Test that state.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")  # noqa

    def test_pep8_conformance_test_state(self):
        """
        Test that test_state.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")  # noqa

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(State.__doc__) >= 1)

    def setUp(self):
        """set up method for State class
        """
        self.S = State()

    def tearDown(self):
        """initialized method for State class
        """
        self.S = None

    def test_type(self):
        """test method for type testing of state
        """
        self.assertIsInstance(self.S, State)
        self.assertEqual(type(self.S), State)
        self.assertEqual(issubclass(self.S.__class__, State), True)
        self.assertEqual(isinstance(self.S, State), True)

    def test_name_type(self):
        """tests the type of state attribute
        """
        self.assertEqual(type(State.name), str)

    def test_string_return(self):
        """tests the string method
        """
        string = str(self.S)
        test_str = "[{}] ({})".format(self.S.__class__.__name__, self.S.id)  # noqa
        self.assertTrue(test_str in string)
        self.assertTrue("updated_at" in string)
        self.assertTrue("created_at" in string)
        self.assertTrue("datetime.datetime" in string)
