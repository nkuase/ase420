"""
Visitor Pattern - Concrete Element (File)
This class represents a file in the file system.
"""

from entry import Entry
from visitor import Visitor


class File(Entry):
    """
    Concrete implementation of Entry representing a file.
    A file has a name and size, and can accept visitors.
    """
    
    def __init__(self, name: str, size: int):
        """
        Initialize a file with name and size.
        
        Args:
            name (str): The name of the file
            size (int): The size of the file
        """
        self.name = name
        self.size = size
    
    def get_name(self) -> str:
        """
        Get the name of this file.
        
        Returns:
            str: The name of the file
        """
        return self.name
    
    def get_size(self) -> int:
        """
        Get the size of this file.
        
        Returns:
            int: The size of the file
        """
        return self.size
    
    def accept(self, visitor: Visitor):
        """
        Accept a visitor and let it visit this file.
        
        Args:
            visitor (Visitor): The visitor to accept
        """
        visitor.visit_file(self)
