#!/usr/bin/env python3
"""Uittests for the base_model module"""


from models.base_model import BaseModel
import pep8
import unittest


class TestBaseModel(unittest.TestCase):
	"""Tests for BaseModel its instances,\
			attributes, instance attributes and methods"""
	
	def test_pep8_conformation_for_base_model(self):
		"""Tests for the pep8 conformation of base_model module"""
		pep8style = pep8.StyleGuide(quiet=True)
		result = pep8style.check_files(["models/base_model.py"])
		self.assertEqual(result.total_errors, 0,\
				"Found code style errors (and warnings).")

if __name__ == "__main__":
	unittest.main()
