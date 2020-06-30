#!/usr/bin/python3
"""
+=====+
Console
+=====+
"""
import cmd
import models
import shlex
# class
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "
    cls = {'BaseModel': BaseModel,
           'User': User,
           'Place': Place,
           'State': State,
           'City': City,
           'Amenity': Amenity,
           'Review': Review}

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel\n"""

        arg = shlex.split(line)  # ['create', 'BaseModel']
        if len(line) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.cls:  # [arg[0] = 'BaseModel']
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(arg[0])(self)
            new_instance.save()
            print(new_instance.id)
            return

    def do_show(self, line):
        """Prints the string representation of an instance based on \
        the class name and id"""

        arg = shlex.split(line)
        if len(line) == 0:  # show -> line[0], line[1], line[2]
            print("** class name missing **")
            return
        elif arg[0] not in self.cls:  # [show 'BaseModel']
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:  # show BaseModel
            print("** instance id missing **")
            return
        else:
            new_instance = models.storage.all()  # storage variable global
            keyID = "{}.{}".format(arg[0], arg[1])
            if keyID in new_instance:
                print(new_instance[keyID])
            else:
                print("** no instance found **")
            return

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id \
        (save the change into the JSON file)"""

        arg = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.cls:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        else:
            to_del = models.storage.all()
            keyID = "{}.{}".format(arg[0], arg[1])
            # for k, v in to_del.items():
            if keyID in to_del:
                del to_del[keyID]
                models.storage.save()
            else:
                print("** no instance found **")
            return

    def do_all(self, line):
        """Prints all string representation of all instances based or \
not on the class name"""

        arg = shlex.split(line)
        instance = models.storage.all()
        lis = []
        if len(line) == 0:
            for value in instance.values():
                lis.append(value.__str__())
            print(lis)
            return
        if arg[0] not in self.cls:
            print("** class doesn't exist **")
            return
        else:
            for value in instance.values():
                if arg[0] == value.__class__.__name__:
                    lis.append(value.__str__())
            print(lis)
            return

    def do_update(self, line):
        """Update command interpreter"""

        arg = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.cls:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        else:
            instance = models.storage.all()
            keyID = "{}.{}".format(arg[0], arg[1])  # BaseModel and ID
            if keyID in instance:
                for value in instance.values():  # return Values
                    try:
                        tp = type(getattr(value, arg[2]))
                        arg[3] = tp(arg[3])
                    except AttributeError:
                        pass
                    setattr(value, arg[2], arg[3])
                    models.storage.save()
            else:
                print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
