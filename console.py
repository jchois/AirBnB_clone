#!/usr/bin/python3
"""Console"""
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'Quit command to exit the program\n'
        return True

    def do_create(self, line):
        'Creates a new instance of BaseModel\n'
        #self.base_model = BaseModel()
        #r = self.base_model.to_dict()
        #print(r)
        cls ={'BaseModel': BaseModel}
        arg = line.split() # ['create', 'BaseModel']

        if len(line) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in cls: # [arg[0] = 'BaseModel']
            print("** class doesn't exist **")
            return
        else:
            new_instance = eval(arg[0])(self)
            new_instance.save()
            print(new_instance.id)
            return


    def do_show(self, line):
        'Prints the string representation of an instance based on \
the class name and id'
        self.base_model = BaseModel()
        r = self.base_model.to_dict()
        cls = {'BaseModel' : BaseModel}
        print(r)
        arg = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in cls:
            print("** class doesn't exist **")
            return
        elif len(line) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                new_instance = models.storage.all()
                keyID = "{}.{}".format(arg[0], arg[1])
                if keyID in new_instance:
                    print(new_instance[keyID])
            except Exception:
                print("** no instance found **")
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
