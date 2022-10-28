#!/usr/bin/env python3
"""Definition of the class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
	"""A class that inherits from BaseModel
	
	Attributes:
		name (str, public): Class attribute name
	"""
	name = ""
