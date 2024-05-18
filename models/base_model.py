#!/usr/bin/env python3
"""
This module contains BaseModel implementation
"""
import uuid
from models.__init__ import storage
from datetime import datetime


class BaseModel:
    """Represents a BaseModel with basic attributes/methods"""
    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instances"""
        self.id = kwargs.get("id", str(uuid.uuid4()))
        self.created_at = kwargs.get("created_at", datetime.now())
        self.updated_at = kwargs.get("updated_at", self.created_at)

        fmt_str = "%Y-%m-%dT%H:%M:%S.%f"

        if "created_at" in kwargs:
            self.created_at = datetime.strptime(kwargs["created_at"], fmt_str)
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(kwargs["updated_at"], fmt_str)

        if not kwargs:
            storage.new(self)  # Removed storage for each instantiation

    def __str__(self):
        """Returns formatted string of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the `updated_at` timestamp"""
        self.updated_at = datetime.utcnow()

        # Updates the timestamp on saved instance before saving to file
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of BaseModel instance"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }
