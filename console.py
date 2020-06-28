#!/usr/bin/python3
""""""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt='(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program\n'

        print("Bye!!")
        return (True)

    def do_EOF(self, arg):
        'Quit command to exit the program\n'

        print("Bye!! EOF")
        return (True)


def parse(arg):
    return (tuple(map(int, arg.split())))

if __name__=='__main__':
    HBNBCommand().cmdloop()
