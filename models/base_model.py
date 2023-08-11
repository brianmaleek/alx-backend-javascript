#!/usr/bin/python3
""" This module defines BaseModel Class for our hbnb clone """
import uuid
from datetime import datetime
import models


date_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Base class for hbnb models """
    def __init__(self, *args, **kwargs):
        """ Constructor method for BaseModel class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, date_time))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ String representation of an instance of BaseModel class """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ Updates the public instance attribute updated_at with the current
            datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the
            instance
        """
        obj_dic = self.__dict__.copy()
        obj_dic['__class__'] = self.__class__.__name__
        obj_dic['created_at'] = self.created_at.isoformat()
        obj_dic['updated_at'] = self.updated_at.isoformat()
        return obj_dic
