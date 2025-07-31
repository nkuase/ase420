"""
Display abstract class for Decorator Pattern Example

This abstract class represents the component in the Decorator pattern.
It defines the interface for objects that can have responsibilities 
added to them dynamically.

This is the "Component" in the Decorator pattern.
"""

from abc import ABC, abstractmethod


class Display(ABC):
    """
    Abstract base class for display objects.
    
    This class defines the interface for objects that can display text
    in various formats. The Decorator pattern allows new display behaviors
    to be added dynamically by wrapping objects with decorator classes.
    """
    
    @abstractmethod
    def get_columns(self) -> int:
        """
        Get the number of columns (width) of the display.
        
        Returns:
            int: The width in characters
        """
        pass
    
    @abstractmethod
    def get_rows(self) -> int:
        """
        Get the number of rows (height) of the display.
        
        Returns:
            int: The height in lines
        """
        pass
    
    @abstractmethod
    def get_row_text(self, row: int) -> str:
        """
        Get the text for a specific row.
        
        Args:
            row (int): The row number (0-based)
            
        Returns:
            str: The text content for the specified row
            
        Raises:
            IndexError: If row is out of bounds
        """
        pass
    
    def show(self) -> None:
        """
        Display all rows of the content.
        
        This method provides a default implementation that iterates
        through all rows and prints each one.
        """
        for i in range(self.get_rows()):
            print(self.get_row_text(i))
    
    def get_all_text(self) -> str:
        """
        Get all text as a single string with newlines.
        
        Returns:
            str: Complete text content with line breaks
        """
        lines = []
        for i in range(self.get_rows()):
            lines.append(self.get_row_text(i))
        return '\n'.join(lines)
    
    def __str__(self) -> str:
        """
        String representation of the display.
        
        Returns:
            str: The complete display content
        """
        return self.get_all_text()
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        
        Returns:
            str: Developer representation showing dimensions
        """
        return f"{self.__class__.__name__}({self.get_columns()}x{self.get_rows()})"
