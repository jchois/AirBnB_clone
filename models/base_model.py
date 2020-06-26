#!/usr/bin/python3
""""""
import uuid
from datetime import *
import models


class BaseModel():
    """"""

    def __init__(self):
        """"""
        #dt_string = '2017-06-14T22:31:03.285259'
        self.create_at = datetime.now()
        self.update_at = datetime.now()
        self.id = str(uuid.uuid4())

    def save(self):
        """"""
        self.update_at = datetime.now()

    def to_dict(self):
        """"""
        dic = self.__dict__.copy()
        dic['__class__'] = BaseModel.__name__
        dic['create_at'] = self.create_at.isoformat()
        dic['update_at'] = self.update_at.isoformat()
        return(dic)

    def __str__(self):
        str="[<{}>] (<{}>) <{}>"
        return (str.format(BaseModel.__name__, self.id, self.__dict__))
