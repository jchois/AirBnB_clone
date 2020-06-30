#!/usr/bin/python3
"""User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """[Public class attributes]

    Args:
        BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
