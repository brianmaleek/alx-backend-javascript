#!/usr/bin/python3
"""" Class FileStorage """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """
    class that serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        n_dict = FileStorage.__objects
        o_dict = {obj: n_dict[obj].to_dict() for obj in n_dict.keys()}
        with open(self.__file_path, "w") as write_file:
            json.dump(o_dict, write_file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as read_file:
                n_dict = json.load(read_file)
            for obj in n_dict.keys():
                FileStorage.__objects[obj] = eval(n_dict[obj]["__class__"])(**n_dict[obj])
        except FileNotFoundError:
            pass
