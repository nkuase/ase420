"""
Visitor Pattern - Concrete Element (Directory)
This class represents a directory in the file system.
"""

from typing import List, Iterator
from entry import Entry
from visitor import Visitor


class Directory(Entry):
    """
    Concrete implementation of Entry representing a directory.
    A directory can contain other entries (files and subdirectories).
    """
    
    def __init__(self, name: str):
        """
        Initialize a directory with a name.
        
        Args:
            name (str): The name of the directory
        """
        self.name = name
        self.directory: List[Entry] = []
    
    def get_name(self) -> str:
        """
        Get the name of this directory.
        
        Returns:
            str: The name of the directory
        """
        return self.name
    
    def get_size(self) -> int:
        """
        Get the total size of this directory (sum of all entries).
        
        Returns:
            int: The total size of all entries in the directory
        """
        total_size = 0
        for entry in self.directory:
            total_size += entry.get_size()
        return total_size
    
    def add(self, entry: Entry) -> 'Directory':
        """
        Add an entry to this directory.
        
        Args:
            entry (Entry): The entry to add (file or subdirectory)
            
        Returns:
            Directory: This directory (for method chaining)
        """
        self.directory.append(entry)
        return self
    
    def __iter__(self) -> Iterator[Entry]:
        """
        Make directory iterable over its entries.
        
        Returns:
            Iterator[Entry]: Iterator over the entries in this directory
        """
        return iter(self.directory)
    
    def accept(self, visitor: Visitor):
        """
        Accept a visitor and let it visit this directory.
        
        Args:
            visitor (Visitor): The visitor to accept
        """
        visitor.visit_directory(self)
