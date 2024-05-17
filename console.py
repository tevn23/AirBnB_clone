#!/usr/bin/env python3
"""
Contains the command interpreter for the Airbnb clone
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter for the Airbnb"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_quit(self, arg):
        """Quits command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
