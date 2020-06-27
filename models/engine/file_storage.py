#!/usr/bin/python3
"""file_storage module"""
from os import path
import models
import json


class FileStorage():
    """"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """"""
        return (dict(FileStorage.__objects))

    def new(self, obj):
        """"""
        if obj:
            key="{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """"""
        tmp={}
        for k, v in FileStorage.__objects.items():
            tmp[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(tmp, f)

    def reload(self):
        """"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dic = json.load(f)
            tmp={}
            for k, v in dic.items():
                tmp[k] = self.__class__.name
            FileStorage.__objects = tmp.__dict__
        except Exception:
            print("File No Exists")
