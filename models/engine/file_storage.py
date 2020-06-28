#!/usr/bin/python3
"""file_storage module"""

from models.base_model import BaseModel
import json


class FileStorage():
    """
    class that serializes instances to a JSON file and\
 deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary"""

        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""

        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        tmp = {}
        for key, value in self.__objects.items():
            tmp[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(tmp, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path, 'r') as f:
                # dic = json.load(f)
                for key, value in json.load(f).items():
                    tmp = eval(value['__class__'])(**value)
                    self.__objects[key] = tmp
        except Exception:
            pass
