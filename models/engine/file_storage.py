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
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes objects to the JSON file"""
        # Convert datetime objects to json serializable str
        stor_dict = {}
        for key, value in self.__objects.items():
            stor_dict[key] = value.to_dict()

        # Saves dict obj to file
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(stor_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        import models.city
        import models.user
        import models.place
        import models.state
        import models.review
        import models.amenity
        import models.base_model

        cls_lst = {
                "City": models.city.City,
                "User": models.user.User,
                "Place": models.place.Place,
                "State": models.state.State,
                "Review": models.review.Review,
                "Amenity": models.amenity.Amenity,
                "BaseModel": models.base_model.BaseModel
        }

        try:
            with open(self.__file_path, encoding="utf-8") as file:
                for objs_dict in json.load(file).values():
                    cls = objs_dict["__class__"]
                    self.new(cls_lst[cls](**objs_dict))

        except FileNotFoundError:
            pass

    def reset(self):
        """Resets class's __objects attribute"""
        # Added for testing class functionalities
        self.__objects = {}
