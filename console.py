#!/usr/bin/python3
"""
Created by:
    Samuel Ezeh
    Mercy Korir
2022-10-26
"""


from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.user import User
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = "(hbnb)"
    classes = ["BaseModel", "User", "Place", "Review", "State", "City", "Amenity", "Place"]  # noqa

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit(1)

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Create command to create new instance"""
        args = line.split()
        status = self.check_class(line)
        if status is True:
            new_instance = eval(args[0] + "()")
            if isinstance(new_instance, BaseModel):
                new_instance.save()
            print(new_instance.id)

    def do_destroy(self, line):
        """Delete command deletes an instance based on the class name and id"""
        if HBNBCommand.check_class(line):
            if HBNBCommand.check_id(line):
                args = line.split()
                instance_keys = "{}.{}".format(args[0], args[1])
                objects = models.storage.all()
                if instance_keys in objects.keys():
                    print("Found", instance_keys)
                    del objects[instance_keys]
                    print("Successfully deleted")
                    models.storage.save()

    def do_all(self, line):
        """All command to print all string representation of all instances"""
        args = line.split()
        list_objs = []
        objects = models.storage.all()
        if len(args) <= 0:
            for values in objects.values():
                list_objs.append(str(values))
        elif len(args) >= 1 and HBNBCommand.check_class(line):
            for keys, values in objects.items():
                if args[0] in keys:
                    list_objs.append(str(values))
        if len(list_objs) > 0:
            print(list_objs)

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
            if args[2] in storage.all()["{}.{}".format(args[0], args[1])].__class__.__dict__.keys():  # noqa
                attribute_type = type(storage.all()["{}.{}".format(args[0], args[1])].__class__.__dict__[args[2]])  # noqa
                storage.all()["{}.{}".format(args[0], args[1])].__dict__[args[2]] = attribute_type(args[3])  # noqa
            else:
                storage.all()["{}.{}".format(args[0], args[1])].__dict__[args[2]] = args[3]  # noqa
        storage.save()

    @staticmethod
    def check_id(line):
        """Verifies the instance id entered"""
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
        args = line.split()
        if len(args) <= 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
