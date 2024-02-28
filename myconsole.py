#!/usr/bin/env python3

import cmd
class command(cmd.Cmd):
 # constructor method for the class
    
    def do_greet(self, line):
        """Say hello to someone"""
        print("Hello World")

    def do_EOF(self, line):
        print()
        return True

    def default(self, line):
        print("Unknown command: {line}")
        return super().default(line)
    
if __name__ == "__main__":
    command().cmdloop()