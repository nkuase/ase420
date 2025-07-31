"""
Proxy Pattern - Subject Interface
This interface defines the common interface for both the real subject and proxy.
"""

from abc import ABC, abstractmethod


class Printable(ABC):
    """
    Abstract interface for printable objects.
    Both the real printer and proxy implement this interface.
    """
    
    @abstractmethod
    def set_printer_name(self, name: str):
        """
        Set the printer name.
        
        Args:
            name (str): The printer name to set
        """
        pass
    
    @abstractmethod
    def get_printer_name(self) -> str:
        """
        Get the printer name.
        
        Returns:
            str: The current printer name
        """
        pass
    
    @abstractmethod
    def print(self, string: str):
        """
        Print a string.
        
        Args:
            string (str): The string to print
        """
        pass
