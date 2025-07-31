"""
Command Pattern - Concrete Command (DrawCommand)
This class encapsulates a drawing operation as a command object.
It stores the receiver (drawable) and the parameters needed for the operation.
"""

from command.command import Command
from drawer.drawable import Drawable


class DrawCommand(Command):
    """
    Concrete command that encapsulates a drawing operation.
    Stores the drawable object (receiver) and the position to draw at.
    """
    
    def __init__(self, drawable: Drawable, x: int, y: int):
        """
        Initialize the draw command with drawable and position.
        
        Args:
            drawable (Drawable): The object to draw on (receiver)
            x (int): X coordinate to draw at
            y (int): Y coordinate to draw at
        """
        self.drawable = drawable
        self.x = x
        self.y = y
    
    def execute(self):
        """
        Execute the drawing command by calling draw on the receiver.
        """
        self.drawable.draw(self.x, self.y)
    
    def get_position(self) -> tuple:
        """
        Get the position this command draws at.
        
        Returns:
            tuple: (x, y) coordinates
        """
        return (self.x, self.y)
    
    def __str__(self) -> str:
        """String representation of the draw command."""
        return f"DrawCommand(x={self.x}, y={self.y})"
