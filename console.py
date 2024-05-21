#!/usr/bin/env python3
"""
Contains the command interpreter for the Airbnb clone
"""
import ast
import cmd
import shlex
from models import storage
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Interpreter for the Airbnb"""
    intro = "The Command Interpreter for the Airbnb"
    prompt = "(hbnb) "

    class_list = {
            "City": City,
            "User": User,
            "Place": Place,
            "State": State,
            "Review": Review,
            "Amenity": Amenity,
            "BaseModel": BaseModel
    }

    CLASS_LIST = list(class_list)

    def do_create(self, arg):
        """Creates and saves a new instance of BaseModel"""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")

        elif len(args) == 1:
            if args[0] in self.class_list:
                cls = self.class_list[args[0]]
                inst = cls()
                inst.save()
                print(inst.id)

            else:
                print("** class doesn't exist **")
        else:
            print("Usage: create <class name>")

    def do_show(self, arg):
        """Prints an instance string representation"""
        args = shlex.split(arg)

        if args:
            if args[0] in self.class_list:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    stored_dict = storage.all()

                    if key in stored_dict:
                        print(stored_dict[key])

                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance"""
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")

        elif args[0] in self.class_list:
            if len(args) == 1:
                print("** instance id missing **")

            else:
                key = f"{args[0]}.{args[1]}"
                stored_dict = storage.all()

                if key in stored_dict:
                    del stored_dict[key]
                    storage.save()

                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)

        class_dict = []
        stored_dict = storage.all()

        if not args:
            for key in stored_dict:
                class_dict.append(str(stored_dict[key]))
            print(class_dict)

        else:
            if args[0] in self.class_list:
                for key, val in stored_dict.items():
                    if args[0] == val.__class__.__name__:
                        class_dict.append(str(val))
                print(class_dict)

            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance"""
        # Handles dict interpretation
        arg = arg.replace("'", '"')
        arg = arg.replace('{', "'{")
        arg = arg.replace('}', "}'")

        args = shlex.split(arg)

        if not args:
            print("** class name missing **")

        elif args[0] in self.class_list:
            if len(args) == 1:
                print("** instance id missing **")

            else:
                key = f"{args[0]}.{args[1]}"
                stored_dict = storage.all()

                if key in stored_dict:
                    if len(args) == 2:
                        print("** attribute name missing **")

                    else:
                        # safe evaluation of str argument
                        try:
                            args[2] = ast.literal_eval(args[2])
                        except (ValueError, SyntaxError):
                            print("An error occured")

                        if len(args) == 3 and not isinstance(args[2], dict):
                            print("** value missing **")

                        elif isinstance(args[2], dict):
                            for ky, val in args[2].items():
                                setattr(stored_dict[key], ky, val)
                        else:
                            setattr(stored_dict[key], args[2], args[3])
                            stored_dict[key].save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = shlex.split(arg)

        count = 0
        stored_dict = storage.all()

        if not args:
            print(len(stored_dict))

        else:
            if args[0] in self.class_list:
                for key, val in stored_dict.items():
                    if args[0] == val.__class__.__name__:
                        count += 1
                print(count)

            else:
                print("** class doesn't exist **")

    def complete_command(self, text, line, begidx, endidx, command):
        """Common completion method for class-based commands"""
        if not text:
            completions = self.CLASS_LIST[:]
        else:
            completions = [cls + ' ' for cls in self.CLASS_LIST
                           if cls.startswith(text)]
        return completions

    def complete_create(self, text, line, begidx, endidx):
        return self.complete_command(text, line, begidx, endidx, 'create')

    def complete_destroy(self, text, line, begidx, endidx):
        return self.complete_command(text, line, begidx, endidx, 'destroy')

    def complete_show(self, text, line, begidx, endidx):
        return self.complete_command(text, line, begidx, endidx, 'show')

    def complete_all(self, text, line, begidx, endidx):
        return self.complete_command(text, line, begidx, endidx, 'all')

    def complete_update(self, text, line, begidx, endidx):
        return self.complete_command(text, line, begidx, endidx, 'update')

    def complete_count(self, text, line, begidx, endidx):
        return self.complete_command(text, line, begidx, endidx, 'count')

    def do_quit(self, arg):
        """Quits command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) command to exit the program"""
        return True

    # Quit the interpreter using exit
    do_exit = do_quit

    def precmd(self, arg):
        """Calls commands using <class_name>.command()"""
        if '.' in arg:
            # Extract command and arguments
            parts = arg.split('.')
            cls_name, cmd_parts = parts[0], parts[1].split('(')
            cmd = cmd_parts[0]
            # Processing for dictionary arguments
            if '{' in cmd_parts[1]:
                cmd_args = cmd_parts[1].split('{')
                id_arg = cmd_args[0].strip()
                id_arg = id_arg.rstrip(',')
                dict_arg = '{' + cmd_args[1].rstrip(')')

                rebuilt_arg = f"{cmd} {cls_name} {id_arg} {dict_arg}"

                return rebuilt_arg

            # Extract the argument from within parentheses (if present)
            if len(cmd_parts) > 1:
                # Remove trailing parenthesis
                raw_args = cmd_parts[1].rstrip(')')

                # Process raw string args to remove delimiters like ','
                list(raw_args)
                args = "".join(char for char in raw_args if char != ',')

            else:
                args = None

            # Rebuild the command and return it for processing
            if args:
                rebuilt_cmd = f"{cmd} {cls_name} {args}"
            else:
                rebuilt_cmd = f"{cmd} {cls_name}"

            return rebuilt_cmd

        else:
            return arg  # Return original argument

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
