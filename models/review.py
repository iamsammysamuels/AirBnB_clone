#!/usr/bin/python3
"""Definition of class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes

    Attributes:
        place_id (str): id of the place
        user_id (str): id of the user
        text (str): review text
    """

    place_id = ""
    user_id = ""
    text = ""
