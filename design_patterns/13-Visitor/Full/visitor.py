"""
Visitor Pattern - Abstract Visitor
This abstract class defines the interface for visitors that can operate on elements.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from file import File
    from directory import Directory


class Visitor(ABC):
    """
    Abstract visitor class that defines the interface for visiting different types of elements.
    Concrete visitors must implement visit methods for each type of element.
    """
    
    @abstractmethod
    def visit_file(self, file: 'File'):
        """
        Visit a File element.
        
        Args:
            file (File): The file element to visit
        """
        pass
    
    @abstractmethod
    def visit_directory(self, directory: 'Directory'):
        """
        Visit a Directory element.
        
        Args:
            directory (Directory): The directory element to visit
        """
        pass
