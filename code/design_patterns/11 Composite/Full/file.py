"""
File class for Composite Pattern Example

This class represents a leaf node in the Composite pattern.
A file is a simple entry that cannot contain other entries.

This is a "Leaf" in the Composite pattern.
"""

from entry import Entry


class File(Entry):
    """
    Concrete implementation of Entry representing a file.
    
    Files are leaf nodes in the file system hierarchy - they cannot
    contain other entries. They represent the "primitive" objects
    in the Composite pattern.
    """
    
    def __init__(self, name: str, size: int):
        """
        Initialize a file with name and size.
        
        Args:
            name (str): The name of the file
            size (int): The size of the file in bytes
            
        Raises:
            ValueError: If size is negative
        """
        if size < 0:
            raise ValueError("File size cannot be negative")
        
        self._name = name
        self._size = size
    
    def get_name(self) -> str:
        """
        Get the name of this file.
        
        Returns:
            str: The file name
        """
        return self._name
    
    def get_size(self) -> int:
        """
        Get the size of this file.
        
        Returns:
            int: The file size in bytes
        """
        return self._size
    
    def _print_list(self, prefix: str) -> None:
        """
        Print this file in a directory listing format.
        
        Files are displayed with a "/" prefix followed by their string representation.
        
        Args:
            prefix (str): The prefix string for proper indentation
        """
        print(f"{prefix}/{self}")
    
    def set_size(self, size: int) -> None:
        """
        Update the size of this file.
        
        Args:
            size (int): The new size in bytes
            
        Raises:
            ValueError: If size is negative
        """
        if size < 0:
            raise ValueError("File size cannot be negative")
        self._size = size
    
    def get_extension(self) -> str:
        """
        Get the file extension.
        
        Returns:
            str: The file extension (without the dot), or empty string if no extension
        """
        if '.' in self._name:
            return self._name.split('.')[-1]
        return ""
    
    def get_basename(self) -> str:
        """
        Get the file name without extension.
        
        Returns:
            str: The base name of the file
        """
        if '.' in self._name:
            return '.'.join(self._name.split('.')[:-1])
        return self._name
    
    def __eq__(self, other) -> bool:
        """
        Check equality with another File.
        
        Args:
            other: Another object to compare with
            
        Returns:
            bool: True if both files have same name and size
        """
        if not isinstance(other, File):
            return False
        return self._name == other._name and self._size == other._size
    
    def __lt__(self, other) -> bool:
        """
        Compare files for sorting (by name).
        
        Args:
            other: Another File to compare with
            
        Returns:
            bool: True if this file's name is lexicographically smaller
        """
        if not isinstance(other, File):
            return NotImplemented
        return self._name < other._name
    
    def __hash__(self) -> int:
        """
        Hash function for using File in sets and dictionaries.
        
        Returns:
            int: Hash value based on name and size
        """
        return hash((self._name, self._size))
