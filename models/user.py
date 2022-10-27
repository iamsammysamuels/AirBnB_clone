#!/usr/bin/python3
"""Definition of class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Declaration of public class attributes

    Attributes:
        email (str): email of User
        password (str): password of User's email
        first_name (str): first name of User
        last_name (str): last name of User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
