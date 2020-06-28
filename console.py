#!/usr/bin/python3
"""Console"""
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """entry point of the command interpreter"""
    prompt = "(hbnb) "
    cls = {'BaseModel' : BaseModel}

    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'Quit command to exit the program\n'
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        'Creates a new instance of BaseModel\n'
        # cls ={'BaseModel': BaseModel}
        arg = line.split() # ['create', 'BaseModel']

        if len(line) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in self.cls: # [arg[0] = 'BaseModel']
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
        #self.base_model = BaseModel()
        #r = self.base_model.to_dict()
        #print(r)
        #print('========================================================')
        arg = line.split()

        if len(line) == 0: # show -> line[0], line[1], line[2]
            print("** class name missing **")
            return
        elif arg[0] not in self.cls: # [show 'BaseModel']
            print("** class doesn't exist **")
            return
        elif len(arg) == 1: # show BaseModel
            print("** instance id missing **")
            return
        else:
                new_instance = models.storage.all() # storage variable global
                keyID = "{}.{}".format(arg[0], arg[1])
                if keyID in new_instance:
                    print(new_instance[keyID])
                else:
                    print("** no instance found **")
        return

    def do_all(self, line):
        """Prints all string representation of all instances based or \
not on the class name"""
        arg = line.split()
        lis = []
        # if len(line) == 0:
        #    print("** class name missing **")
        if arg[0] not in self.cls:
            print("** class doesn't exist **")
        else:
            instance = models.storage.all()
            for value in instance.values():
                lis.append(value.__str__())
            print(lis)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
