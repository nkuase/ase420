"""Macro command - composite pattern"""
from command import Command

class MacroCommand(Command):
    def __init__(self):
        self.commands = []
    
    def add(self, command):
        self.commands.append(command)
    
    def execute(self):
        for cmd in self.commands:
            cmd.execute()
    
    def undo_last(self):
        if self.commands:
            return self.commands.pop()
