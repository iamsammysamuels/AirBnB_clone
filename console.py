#!/usr/bin/env python3
"""
Created by:
    Samuel Ezeh
    Mercy Korir
2022-10-26
"""


from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
import models
import cmd


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = "(hbnb)"
    intro = "*** Welcome to Airbnb console clone ***"
    classes = ["BaseModel", "User", "Place", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit (1)

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Create command to create new instance"""
        args = line.split()
        status = self.check_class(args)
        if status == True:
            new_instance = eval(args[0] + "()")
            if isinstance(new_instance, BaseModel):
                new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Print id with respective class"""
        args = line.split()
        if line is None or len(args) <= 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_update(self, line):
        """Update instance based on class name and id
        by adding or updating attribute"""
        args = line.split()
        if line is None or len(args) <= 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) > 4:
            args = args[:4]
        else:
            if args[2] in storage.all()["{}.{}".format(args[0], args[1])].__class__.__dict__.keys():
                attribute_type = type(storage.all()["{}.{}".format(args[0], args[1])].__class__.__dict__[args[2]])
                storage.all()["{}.{}".format(args[0], args[1])].__dict__[args[2]] = attribute_type(args[3])
            else:
                storage.all()["{}.{}".format(args[0], args[1])].__dict__[args[2]] = args[3]
        storage.save()

    @staticmethod
    def check_id(line):
	    args = line.split()
	    if len(args) < 2:
		    print("** instance id missing **")
		    return False
	    instance_key = "{}.{}".format(args[0], args[1])
	    instances = models.storage.all()
	    if instance_key not in instances.keys():
		    print("** no instance found **")
		    return False 
	    return True

    @staticmethod
    def check_class(line):
        """Checks if a class was passed"""
        if line is None or len(line) <= 0:
            print("** class name missing **")
            return False
        elif line[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
