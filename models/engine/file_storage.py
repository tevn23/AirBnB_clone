#!/usr/bin/env python3
"""
Contains file storage functionality
"""
import json
from datetime import datetime
from models import class_mapping

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
        self.__objects[key] = obj

def save(self):
    """serializes objects to the JSON file"""
    objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
    
    with open(self.__file_path, 'w', encoding="utf-8") as file:
        json.dump(objects_dict, file)

def reload(self):
    """deserializes the JSON file to __objects"""
    try:
        with open(self.__file_path, encoding="utf-8") as file:
            objects_dict = json.load(file)
            for key, obj_dict in objects_dict.items():
                class_name = obj_dict["__class__"]
                cls = class_mapping.get(class_name)
                if cls:
                    obj_dict["created_at"] = datetime.fromisoformat(obj_dict["created_at"])
                    obj_dict["updated_at"] = datetime.fromisoformat(obj_dict["updated_at"])
                    self.__objects[key] = cls(**obj_dict)
    except FileNotFoundError:
            pass                  
