#!/usr/bin/env python3
"""Definition of city"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class City that inherits from BaseModel

    Attributes:
        state_id (str, public): An attribute of the class city
        name (str, public): An attribute of the class city
    """
    state_id = ""
    name = ""
