#!/usr/bin/env python3

"""
BaseModel module.
Created by:
	Samuel Ezeh
	Mercy Korir
25th of oct 2022
"""

from datetime import datetime
import models
import uuid

class BaseModel:
	"""
	Defines all common attributes/methods for other classes
	"""
	def __init__(self, *args, **kwargs):
		"""
		Instantiates the objects

		Args:
		"""
		if kwargs is not None and len(kwargs) != 0:
			for key, value in kwargs.items():
				if key in ["created_at", "updated_at"]:
					value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
				elif key == "__class__":
					continue
				setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)
	
	def __str__(self):
		"""
		Returns the str output of an instance
		"""
		return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""
		Updates updated_at with the current datetime
		"""
		self.updated_at = datetime.now()
		models.storage.save()

	def to_dict(self):
		"""
		Returns a dictionary of the instance

		Returns:
			A dictionary
		"""
		new_dict = {}
		new_dict = self.__dict__.copy()
		new_dict["created_at"] = self.created_at.isoformat()
		new_dict["updated_at"] = self.updated_at.isoformat()
		new_dict["__class__"] = self.__class__.__name__
		return new_dict
