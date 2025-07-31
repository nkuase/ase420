"""
SideBorder class for Decorator Pattern Example

This class represents a concrete decorator that adds border characters
to the left and right sides of a display.

This is a "Concrete Decorator" in the Decorator pattern.
"""

from border import Border
from display import Display


class SideBorder(Border):
    """
    Concrete decorator that adds side borders to a display.
    
    This decorator adds the same character to both the left and right
    sides of each row in the wrapped display.
    """
    
    def __init__(self, display: Display, border_char: str = '|'):
        """
        Initialize the side border decorator.
        
        Args:
            display (Display): The display component to decorate
            border_char (str): The character to use for the side borders (default: '|')
            
        Raises:
            ValueError: If border_char is not exactly one character
        """
        super().__init__(display)
        
        if len(border_char) != 1:
            raise ValueError("Border character must be exactly one character")
        
        self._border_char = border_char
    
    def get_columns(self) -> int:
        """
        Get the number of columns including the side borders.
        
        The width is the original width plus 2 (one character on each side).
        
        Returns:
            int: The width including side borders
        """
        return 1 + self._display.get_columns() + 1
    
    def get_rows(self) -> int:
        """
        Get the number of rows.
        
        Side borders don't change the height, so return the original height.
        
        Returns:
            int: The same height as the wrapped display
        """
        return self._display.get_rows()
    
    def get_row_text(self, row: int) -> str:
        """
        Get the text for a specific row with side borders.
        
        Each row is the original row text with border characters
        added to the left and right sides.
        
        Args:
            row (int): The row number
            
        Returns:
            str: The row text with side borders
            
        Raises:
            IndexError: If row is out of bounds
        """
        # Get the original row text and add border characters
        original_text = self._display.get_row_text(row)
        return self._border_char + original_text + self._border_char
    
    def get_border_char(self) -> str:
        """
        Get the border character being used.
        
        Returns:
            str: The border character
        """
        return self._border_char
    
    def set_border_char(self, border_char: str) -> None:
        """
        Change the border character.
        
        Args:
            border_char (str): The new border character
            
        Raises:
            ValueError: If border_char is not exactly one character
        """
        if len(border_char) != 1:
            raise ValueError("Border character must be exactly one character")
        self._border_char = border_char
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        
        Returns:
            str: Representation showing border character and wrapped display
        """
        return f"SideBorder('{self._border_char}', {repr(self._display)})"
