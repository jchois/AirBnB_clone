#!/usr/bin/python3
"""base_model module"""
import uuid
from datetime import *
import models


class BaseModel():
    """
    Defines all common attributes/methods for other class
    """

    def __init__(self, *args, **kwargs):
        """Constructor
        Arguments:
            *args: won’t be used
            **kwargs: is not empty"""

        fd = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at":
                    self.created_at = datetime.strptime(v, fd)
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v, fd)
                elif k == "__class__":
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
        """Return a String that contains the class name, \
        the ID and dictionary
        """
        str = "[{}] ({}) {}"
        return (str.format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all \
        keys/values of __dict__ of the instance"""

        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()

        return (dic)
