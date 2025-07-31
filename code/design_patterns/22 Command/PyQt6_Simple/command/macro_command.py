from collections import deque
from command.command import Command

class MacroCommand(Command):
    """
    MacroCommand implements the Composite pattern within the Command pattern.
    
    This class can contain multiple commands and execute them as a single unit.
    It demonstrates how the Command pattern can be combined with the Composite
    pattern to create complex command structures.
    
    Use Cases:
    - Group related operations together
    - Create transaction-like behavior (all-or-nothing execution)
    - Build command history for undo/redo functionality
    - Create macro recordings in applications
    """
    
    def __init__(self):
        """Initialize an empty macro command"""
        self.commands = deque()
    
    def execute(self):
        """
        Execute all commands in the macro in order.
        
        This demonstrates the Composite pattern - a MacroCommand can be treated
        the same way as a single Command, but it actually executes multiple commands.
        """
        for cmd in self.commands:
            cmd.execute()
    
    def append(self, cmd):
        """
        Add a command to the end of the macro.
        
        Args:
            cmd (Command): The command to add to the macro
            
        Raises:
            ValueError: If trying to add the macro command to itself (infinite loop prevention)
        """
        if cmd is self:
            raise ValueError("Cannot append macro command to itself - would cause infinite loop")
        
        if not isinstance(cmd, Command):
            raise TypeError(f"Expected Command instance, got {type(cmd).__name__}")
        
        self.commands.append(cmd)
        print(f"Added {type(cmd).__name__} to macro (total commands: {len(self.commands)})")
    
    def undo(self):
        """
        Remove the last command from the macro.
        
        This implements a simple undo mechanism by removing the most recently
        added command. In a more sophisticated implementation, you might
        want to implement an actual undo operation that reverses the effect
        of the last command.
        """
        if self.commands:
            removed = self.commands.pop()
            print(f"Undid command: {type(removed).__name__}")
            return removed
        else:
            print("No commands to undo")
            return None
    
    def clear(self):
        """
        Remove all commands from the macro.
        
        This is useful for resetting the command history or clearing
        a drawing canvas.
        """
        count = len(self.commands)
        self.commands.clear()
        print(f"Cleared {count} commands from history")
    
    def size(self):
        """
        Get the number of commands in the macro.
        
        Returns:
            int: Number of commands currently in the macro
        """
        return len(self.commands)
    
    def is_empty(self):
        """
        Check if the macro contains any commands.
        
        Returns:
            bool: True if the macro is empty, False otherwise
        """
        return len(self.commands) == 0
    
    def get_commands(self):
        """
        Get a copy of the commands list for inspection.
        
        Returns:
            list: A copy of the commands in the macro
        """
        return list(self.commands)
    
    def insert(self, index, cmd):
        """
        Insert a command at a specific position in the macro.
        
        Args:
            index (int): The position to insert the command
            cmd (Command): The command to insert
        """
        if cmd is self:
            raise ValueError("Cannot insert macro command into itself - would cause infinite loop")
        
        if not isinstance(cmd, Command):
            raise TypeError(f"Expected Command instance, got {type(cmd).__name__}")
        
        self.commands.insert(index, cmd)
        print(f"Inserted {type(cmd).__name__} at position {index}")
    
    def remove_at(self, index):
        """
        Remove a command at a specific position.
        
        Args:
            index (int): The position of the command to remove
            
        Returns:
            Command: The removed command
            
        Raises:
            IndexError: If the index is out of range
        """
        if 0 <= index < len(self.commands):
            removed = self.commands[index]
            del self.commands[index]
            print(f"Removed {type(removed).__name__} from position {index}")
            return removed
        else:
            raise IndexError(f"Index {index} out of range (macro has {len(self.commands)} commands)")
    
    def __str__(self):
        """String representation of the macro command"""
        return f"MacroCommand(commands={len(self.commands)})"
    
    def __len__(self):
        """Allow len() to be called on MacroCommand"""
        return len(self.commands)
    
    def __iter__(self):
        """Allow iteration over the commands in the macro"""
        return iter(self.commands)
