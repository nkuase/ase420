"""
Command Pattern - Macro Command (Composite Command)
This class implements a composite command that can contain multiple commands.
It demonstrates how commands can be combined and executed as a group.
"""

from collections import deque
from typing import Deque
from command.command import Command


class MacroCommand(Command):
    """
    Composite command that contains and executes multiple commands.
    This implements the Composite pattern within the Command pattern.
    """
    
    def __init__(self):
        """Initialize an empty macro command."""
        self.commands: Deque[Command] = deque()
    
    def execute(self):
        """
        Execute all commands in the macro in order.
        """
        for cmd in self.commands:
            cmd.execute()
    
    def append(self, cmd: Command):
        """
        Add a command to the macro.
        
        Args:
            cmd (Command): The command to add
            
        Raises:
            ValueError: If trying to add the macro to itself (infinite loop)
        """
        if cmd is self:
            raise ValueError("Cannot append macro command to itself - would cause infinite loop")
        
        self.commands.append(cmd)
    
    def undo(self):
        """
        Remove the last command from the macro.
        This provides a simple undo functionality.
        """
        if self.commands:
            removed = self.commands.pop()
            print(f"Undid command: {type(removed).__name__}")
        else:
            print("No commands to undo")
    
    def clear(self):
        """
        Remove all commands from the macro.
        """
        count = len(self.commands)
        self.commands.clear()
        print(f"Cleared {count} commands from history")
    
    def size(self) -> int:
        """
        Get the number of commands in the macro.
        
        Returns:
            int: Number of commands
        """
        return len(self.commands)
    
    def is_empty(self) -> bool:
        """
        Check if the macro is empty.
        
        Returns:
            bool: True if no commands, False otherwise
        """
        return len(self.commands) == 0
    
    def __str__(self) -> str:
        """String representation of the macro command."""
        return f"MacroCommand(commands={len(self.commands)})"
