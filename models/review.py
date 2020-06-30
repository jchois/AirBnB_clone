#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """[Public class attributes]

    Args:
        BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
