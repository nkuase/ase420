"""
Entry abstract class for Composite Pattern Example

This abstract class represents the component in the Composite pattern.
It defines the interface that both leaf objects (files) and composite 
objects (directories) must implement.

This is the "Component" in the Composite pattern.
"""

from abc import ABC, abstractmethod


class Entry(ABC):
    """
    Abstract base class for file system entries.
    
    This class defines the common interface for both files and directories
    in a file system hierarchy. The Composite pattern allows clients to
    treat individual objects (files) and compositions (directories) uniformly.
    """
    
    @abstractmethod
    def get_name(self) -> str:
        """
        Get the name of this entry.
        
        Returns:
            str: The name of the file or directory
        """
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        """
        Get the size of this entry.
        
        For files: returns the file size
        For directories: returns the total size of all contained entries
        
        Returns:
            int: The size in bytes
        """
        pass
    
    def print_list(self, prefix: str = "") -> None:
        """
        Print the directory listing.
        
        This method provides a default implementation that calls
        the protected _print_list method with an empty prefix.
        
        Args:
            prefix (str): The prefix string for indentation (default: "")
        """
        self._print_list(prefix)
    
    @abstractmethod
    def _print_list(self, prefix: str) -> None:
        """
        Protected method to print the directory listing with prefix.
        
        This method must be implemented by concrete classes to define
        how they should be displayed in a directory listing.
        
        Args:
            prefix (str): The prefix string for proper indentation
        """
        pass
    
    def __str__(self) -> str:
        """
        String representation of the entry.
        
        Returns a string showing the name and size of the entry.
        
        Returns:
            str: String representation in format "name (size)"
        """
        return f"{self.get_name()} ({self.get_size()})"
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation of the entry.
        
        Returns:
            str: Developer representation
        """
        return f"{self.__class__.__name__}('{self.get_name()}', size={self.get_size()})"
