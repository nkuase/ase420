"""
Builder Pattern - Abstract Builder
This abstract class defines the interface for building documents.
Different concrete builders can implement different output formats.
"""

from abc import ABC, abstractmethod
from typing import List


class Builder(ABC):
    """
    Abstract builder class that defines the interface for building documents.
    Concrete builders will implement these methods to create specific formats.
    """
    
    @abstractmethod
    def make_title(self, title: str):
        """
        Create a title for the document.
        
        Args:
            title (str): The title text
        """
        pass
    
    @abstractmethod
    def make_string(self, string: str):
        """
        Add a string section to the document.
        
        Args:
            string (str): The string content
        """
        pass
    
    @abstractmethod
    def make_items(self, items: List[str]):
        """
        Add a list of items to the document.
        
        Args:
            items (List[str]): List of item strings
        """
        pass
    
    @abstractmethod
    def close(self):
        """
        Finalize the document construction.
        """
        pass
