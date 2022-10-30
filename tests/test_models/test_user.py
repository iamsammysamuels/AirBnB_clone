#!/usr/bin/env python3
"""Uittests for user module"""


from models.base_model import BaseModel
import pep8
import unittest
from datetime import datetime
import uuid

class TestUser(unittest.TestCase):
    """Tests the user class"""

    def setUp(self):
        """ """
        self.user_ = user()

    def tearDown(self):
        """ """
        self.user_ = None

    def test_pep8_connformation_for_user(self):
        """tests that user module is pep8styled"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user"])
        pep8_result = result.total_errors
        self.assertEqual(pep8_result, 0, "Found code style errors (and warnings).")  # noqa

    def test_pep8_conformation_for_test_user(self):
        """tests that test_user is pep8styled"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_user.py"])
        pep8_result = result.total_errors
        self.assertEqual(pep8_result, 0, "Found code style errors (and warnings).")  # noqa
