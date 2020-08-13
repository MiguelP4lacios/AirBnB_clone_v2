#!/usr/bin/env python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade="all, delete, delete-orphan")

    @property
    def cities(sefl):
        """Asociete cities and states"""
        dict_cities = models.storage.all(City)
        _list = []
        for city in dict_cities.values():
            if city.states.id == sefl.id:
                _list.append(city)
        return _list
