"""
Visitor Pattern - Abstract Entry
This abstract class represents an entry in a file system that can be visited.
"""

from abc import ABC, abstractmethod
from element import Element


class Entry(Element, ABC):
    """
    Abstract base class for file system entries (files and directories).
    Provides common functionality for getting name and size.
    """
    
    @abstractmethod
    def get_name(self) -> str:
        """
        Get the name of this entry.
        
        Returns:
            str: The name of the entry
        """
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        """
        Get the size of this entry.
        
        Returns:
            int: The size of the entry
        """
        pass
    
    def __str__(self) -> str:
        """
        String representation of the entry.
        
        Returns:
            str: Entry name and size in parentheses
        """
        return f"{self.get_name()} ({self.get_size()})"
