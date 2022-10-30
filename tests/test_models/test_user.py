#!/usr/bin/env python3
"""Uittests for user module"""


from models.user import User
from models.base_model import BaseModel
import pep8
import unittest
from datetime import datetime
import uuid


class TestUser(unittest.TestCase):
    """Tests the user class"""

    def setUp(self):
        """ """
        self.user_ = User()

    def tearDown(self):
        """ """
        self.user_ = None

    def test_pep8_connformation_for_user(self):
        """tests that user module is pep8styled"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        pep8_result = result.total_errors
        self.assertEqual(pep8_result, 0, "Found code style errors (and warnings).")  # noqa

    def test_pep8_conformation_for_test_user(self):
        """tests that test_user is pep8styled"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_user.py"])
        pep8_results = result.total_errors
        self.assertEqual(pep8_results, 0, "Found code style errors (and warnings).")  # noqa

    def test_type(self):
        """type checks for user model
        """
        self.assertEqual(issubclass(self.user_.__class__, User), True)
        self.assertEqual(isinstance(self.user_, User), True)
        self.assertEqual(isinstance(self.user_, User), True)
        self.assertEqual(type(self.user_), User)

    def test_basic_attribute_set(self):
        """Basic attribute tests for user model
        """
        self.user_.first_name = 'Meco'
        self.user_.last_name = 'Montes'
        self.assertEqual(self.user_.first_name, 'Meco')
        self.assertEqual(self.user_.last_name, 'Montes')

    def test_email(self):
        """tests the user's email attribute
        """
        self.assertEqual(type(User.email), str)

    def test_password(self):
        """tests the user's password attribute
        """
        self.assertEqual(type(User.password), str)

    def test_first_name(self):
        """tests the user's first_name attribute
        """
        self.assertEqual(type(User.first_name), str)

    def test_last_name(self):
        """tests the user's last_name attribute
        """
        self.assertEqual(type(User.last_name), str)
