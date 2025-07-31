"""
Command Pattern - Drawable Interface
This interface defines the contract for objects that can be drawn on.
It represents the receiver in the Command pattern.
"""

from abc import ABC, abstractmethod


class Drawable(ABC):
    """
    Abstract interface for drawable objects.
    This is the receiver interface that commands will operate on.
    """
    
    @abstractmethod
    def draw(self, x: int, y: int):
        """
        Draw at the specified coordinates.
        
        Args:
            x (int): X coordinate
            y (int): Y coordinate
        """
        pass
