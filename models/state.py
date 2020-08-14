#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
#from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """Asociete cities and states"""
        return type(self).cities
        """dict_cities = models.storage.all(City)
        _list = []
        for city in dict_cities.values():
            if city.states.id == self.id:
                _list.append(city)
        return _list"""
