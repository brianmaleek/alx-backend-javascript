#!/usr/bin/python3
""" This module defines a command interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter class """
    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file)
        and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            from models.base_model import BaseModel
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

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
