#!/usr/bin/env python3
"""
Created by Samuel Ezeh
2022-10-25
"""

from models.base_model import BaseModel
import json
from models.user import User
from models.place import Place
from models.review import Review

class FileStorage:
	"""
	serializes instances to a JSON file and\
			deserializes JSON file to instances
	
	Attributes:
		fille_path (str, private): Path to the JSON file
		objects (dict, private): Dictionary
	"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""
		 Returns the dictionary __objects

		 Returns:
		 	__objects
		"""
		return FileStorage.__objects

	def new(self, obj):
		"""
		sets in __objects the obj with key <obj class name>.id

		Args:
			obj (instance): The instance to set as value of the key
		"""
		if obj == None:
			return
		key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
		FileStorage.__objects[key] = obj

	def save(self):
		"""
		Serializes __objects to the JSON file
		"""
		new_objects = {}
		for key, value in FileStorage.__objects.items():
			new_objects[key] = value.to_dict()
		with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
			json.dump(new_objects, file)

	def reload(self):
		"""
		Deserializes the JSON file to __objects
		"""
		try:
			with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
				new_dict = json.load(file)
			for key, value in new_dict.items():
				new_instance = BaseModel(**value)
				self.new(new_instance)
		except:
			pass
