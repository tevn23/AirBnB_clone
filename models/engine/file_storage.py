#!/usr/bin/env python3
"""
Contains file storage functionality
"""
import json
import copy
from datetime import datetime


class FileStorage:
    """Handles instance file storage in json format"""
    __file_path = "data.json"
    __objects = {}

    def all(self):
        """Return all instances dict representation"""
        return self.__objects

    def new(self, obj):
        """adds an object dict representation for storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """serializes objects to the JSON file"""
        # Convert datetime objects to json serializable str
        stored_objs = copy.deepcopy(self.__objects)
        for key, value in stored_objs.items():
            dt = ["created_at", "updated_at"]
            if dt[0] in value and isinstance(value[dt[0]], datetime):
                value["created_at"] = value["created_at"].isoformat()
            if dt[1] in value and isinstance(value[dt[1]], datetime):
                value["updated_at"] = value["updated_at"].isoformat()

        # Saves dict obj to file
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(stored_objs, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as file:
                try:
                    self.__objects = json.load(file)
                except json.JSONDecodeError:
                    pass
            fmt_str = "%Y-%m-%dT%H:%M:%S.%f"

            # Re-converts str objects to datetime objects
            dt = ["created_at", "updated_at"]
            for key, value in self.__objects.items():
                if "created_at" in value:
                    value[dt[0]] = datetime.strptime(value[dt[0]], fmt_str)
                if "updated_at" in value:
                    value[dt[1]] = datetime.strptime(value[dt[1]], fmt_str)

        except FileNotFoundError:
            pass

    def reset(self):
        """Resets class's __objects attribute"""
        # Added for testing class functionalities
        self.__objects = {}
