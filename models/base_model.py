#!/usr/bin/env python3
"""
This module contains BaseModel implementation
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """Represents a BaseModel with basic attributes/methods"""
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instances"""
        if kwargs:
            exed = ["created_at", "updated_at"]

            for key, value in kwargs.items():
                if key in exed and isinstance(value, str):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns formatted string of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the `updated_at` timestamp"""
        self.updated_at = datetime.now()

        # Updates the timestamp on saved instance before saving to file
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of BaseModel instance"""
        re_dict = self.__dict__.copy()
        re_dict["created_at"] = self.created_at.isoformat()
        re_dict["updated_at"] = self.updated_at.isoformat()
        re_dict["__class__"] = self.__class__.__name__

        return re_dict
