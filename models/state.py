#!/usr/bin/env python3
"""Definition of state"""


from models.base_model import BaseModel


class State(BaseModel):
	"""A class state that inherits from BaseModel class

	Attributes:
		name (str, public): A class attribute name
	"""
	name = ""
