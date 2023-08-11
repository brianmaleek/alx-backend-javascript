#!/usr/bin/python3
""" This module defines a command interpreter """

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
import re

class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """
    prompt = '(hbnb) '

    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place","Review"]
        
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file)
        and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            x = eval(arg + "()")
            print(x.id)
            x.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            for k, v in storage.all().items():
                if k == key:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):

        """ Deletes instance based on class name and id """   
        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            for k, v in storage.all().items():
                if k == key:
                    del storage.all()[k]
                    storage.save()
                    return
            print("** no instance found **")       

    def do_all(self, arg):

        """ Prints all string representation of all instances """

        if not arg:
            for k, v in storage.all().items():
                print(v)
        elif arg in HBNBCommand.classes:
            for k, v in storage.all().items():
                if arg in k:
                    print(v)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
    
        """ Updates an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
        elif arg.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        elif len(arg.split()) < 3:
            print("** attribute name missing **")
        elif len(arg.split()) < 4:
            print("** value missing **")
        else:
            key = arg.split()[0] + "." + arg.split()[1]
            for k, v in storage.all().items():
                if k == key:
                    setattr(v, arg.split()[2], arg.split()[3])
                    storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print()
        return True

    def emptyline(self):
        """ Empty line + ENTER shouldn’t execute anything """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
