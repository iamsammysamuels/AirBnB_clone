#!/usr/bin/env python3
"""
Created by Samuel Ezeh
2022-10-25
"""


from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


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
        if obj is None:
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
                if "BaseModel" in key:
                    new_instance = BaseModel(**value)
                elif "User" in key:
                    new_instance = User(**value)
                elif "Amenity" in key:
                    new_instance = Amenity(**value)
                elif "Place" in key:
                    new_instance = Place(**value)
                elif "State" in key:
                    new_instance = State(**value)
                elif "City" in key:
                    new_instance = City(**value)
                elif "Review" in key:
                    new_instance = Review(**value)
                self.new(new_instance)
        except Exception:
            pass
