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
                    del objects[instance_keys]
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

    def default(self, args):
        """Default method that is called when the inputted command starts
        with a class name.
        Attributes:
            args (str): The inputted line string
        """
        line = args.strip('()').split(".")
        if len(line) < 2:
            print('** missing attribute **')
            return
        objects = models.storage.all()
        class_name = line[0].capitalize()
        cmd_name = line[1].lower()
        split2 = cmd_name.strip(')').split('(')
        cmd_name = split2[0]
        if cmd_name == 'all':
            HBNBCommand.do_all(self, class_name)
        elif cmd_name == 'count':
            count = 0
            for k in objects.keys():
                key = k.split('.')
                if class_name == key[0]:
                    count += 1
            print(count)
        elif cmd_name == 'show':
            if len(split2) < 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_show(self, class_name + ' ' + split2[1])
        elif cmd_name == 'destroy':
            if len(split2) < 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_destroy(self, class_name + ' ' + split2[1])
        elif cmd_name == 'update':
            split3 = split2[1].split(', ')
            if len(split3) == 0:
                print('** no instance found **')
            elif len(split3) == 1 and type(split3[1]) == dict:
                for k, v in split[1].items():
                    HBNBCommand.do_update(self, class_name + ' ' + split3[0] +
                                          ' ' + k + ' ' + v)
            elif len(split3) == 1 and type(split3[1]) != dict:
                print('** no instance found **')
            elif len(split3) == 2:
                print('** no instance found **')
            else:
                HBNBCommand.do_update(self, class_name + ' ' + split3[0] +
                                      ' ' + split3[1] + ' ' + split3[2])

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
