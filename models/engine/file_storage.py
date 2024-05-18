#!/usr/bin/env python3
"""
Contains file storage functionality
"""
import json


class FileStorage:
    """Handles instance file storage in json format"""
    __file_path = "data.json"
    __objects = {}

    def all(self):
        """Return all instances dict representation"""
        return self.__objects

    def new(self, obj):
        """adds an object dict representation for storage"""
        key = f"<{obj.__class__.__name__}>.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes objects to the JSON file"""
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass

    def reset(self):
        """Resets class's __objects attribute"""
        # Added for testing class functionalities
        self.__objects = {}
