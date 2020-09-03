#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            if "updated_at" in kwargs and "updated_at" in kwargs\
                    and "__class__" in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                del kwargs['__class__']
            else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            for k, v in kwargs.items():
                setattr(self, k, v)
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at=datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict=dict(self.__dict__)
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        my_dict["__class__"]=str(type(self).__name__)
        my_dict["created_at"]=self.created_at.isoformat()
        my_dict["updated_at"]=self.updated_at.isoformat()
        return my_dict

    def delete(self):
        """ delete the current instance from the storage (models.storage)"""
        models.storage.delete(self)
