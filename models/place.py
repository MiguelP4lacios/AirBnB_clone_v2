#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity",
                                 secondary=place_amenity, viewonly=False)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            review_dict = models.storage.all(Review)
            review_list = []
            for review in review_dict.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review

        @property
        def amenities(self):
            amenity_list = []
            for amenity in amenity_ids:
                key = 'Amenity.{}'.format(id)
                if key in self.__objects.keys():
                    amenity_list.append(self.__objects[key])

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
            else:
                pass
