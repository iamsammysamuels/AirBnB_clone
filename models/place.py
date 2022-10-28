#!/usr/bin/python3
"""Definition of class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Declaration of public class attributes

    Attributes:
        city_id (str): City id
        user_id (str): User id
        name (str): Name of Place
        description (str): description of Place
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): price at night
        latitude (float): latitude of the place
        longitude (float): longitude of Place
        amenity_ids (list): ids of amenity
    """

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
