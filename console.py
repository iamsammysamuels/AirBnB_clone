#!/usr/bin/env python3
"""
Created by Samuel Ezeh
2022-10-26
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
	"""The entry point of the command interpreter"""

	prompt = "(hbnb)"
	intro = "*** Welcome to Airbnb console clone ***"
	classes = ["BaseModel"]

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
