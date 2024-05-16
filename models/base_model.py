#!/usr/bin/env python3
"""
This module contains BaseModel implementation
"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents a BaseModel with basic attributes/methods"""
    def __init__(self):
        """Initializes BaseModel instances"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns formatted string of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at timestamp"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of BaseModel instance"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": self.__class__.__name__
        }
