"""
StringDisplay class for Decorator Pattern Example

This class represents a concrete component in the Decorator pattern.
It provides basic string display functionality that can be enhanced
by decorators.

This is a "Concrete Component" in the Decorator pattern.
"""

from display import Display


class StringDisplay(Display):
    """
    Concrete implementation of Display for simple string display.
    
    This class represents the basic object to which additional
    responsibilities can be added using decorators.
    """
    
    def __init__(self, string: str):
        """
        Initialize with a string to display.
        
        Args:
            string (str): The string to be displayed
        """
        self._string = string
    
    def get_columns(self) -> int:
        """
        Get the number of columns (width) of the string.
        
        For a simple string, this is just the length of the string.
        
        Returns:
            int: The width in characters
        """
        return len(self._string)
    
    def get_rows(self) -> int:
        """
        Get the number of rows (height) of the display.
        
        For a simple string, this is always 1 row.
        
        Returns:
            int: Always returns 1
        """
        return 1
    
    def get_row_text(self, row: int) -> str:
        """
        Get the text for a specific row.
        
        For a simple string display, only row 0 is valid.
        
        Args:
            row (int): The row number (must be 0)
            
        Returns:
            str: The string content
            
        Raises:
            IndexError: If row is not 0
        """
        if row != 0:
            raise IndexError(f"StringDisplay only has 1 row, but row {row} was requested")
        return self._string
    
    def get_string(self) -> str:
        """
        Get the original string content.
        
        Returns:
            str: The original string
        """
        return self._string
    
    def set_string(self, string: str) -> None:
        """
        Update the string content.
        
        Args:
            string (str): The new string content
        """
        self._string = string
    
    def __eq__(self, other) -> bool:
        """
        Check equality with another StringDisplay.
        
        Args:
            other: Another object to compare with
            
        Returns:
            bool: True if both have the same string content
        """
        if not isinstance(other, StringDisplay):
            return False
        return self._string == other._string
    
    def __hash__(self) -> int:
        """
        Hash function for using StringDisplay in sets and dictionaries.
        
        Returns:
            int: Hash value based on the string content
        """
        return hash(self._string)
