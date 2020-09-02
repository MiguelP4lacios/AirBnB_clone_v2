#!/usr/bin/env python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Asociete cities and states"""
            """return type(self).cities"""
            cities_dict = models.storage.all(City)
            cities_list = []
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
