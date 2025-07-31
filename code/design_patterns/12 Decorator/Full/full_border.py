"""
FullBorder class for Decorator Pattern Example

This class represents a concrete decorator that adds a complete border
around a display (top, bottom, left, and right).

This is a "Concrete Decorator" in the Decorator pattern.
"""

from border import Border
from display import Display


class FullBorder(Border):
    """
    Concrete decorator that adds a complete border around a display.
    
    This decorator adds:
    - Top and bottom borders using '+' and '-' characters
    - Left and right borders using '|' characters
    - Corner characters using '+'
    """
    
    def __init__(self, display: Display):
        """
        Initialize the full border decorator.
        
        Args:
            display (Display): The display component to decorate
        """
        super().__init__(display)
    
    def get_columns(self) -> int:
        """
        Get the number of columns including the full border.
        
        The width is the original width plus 2 (one character on each side).
        
        Returns:
            int: The width including side borders
        """
        return 1 + self._display.get_columns() + 1
    
    def get_rows(self) -> int:
        """
        Get the number of rows including the full border.
        
        The height is the original height plus 2 (top and bottom borders).
        
        Returns:
            int: The height including top and bottom borders
        """
        return 1 + self._display.get_rows() + 1
    
    def get_row_text(self, row: int) -> str:
        """
        Get the text for a specific row with full border.
        
        - Row 0: Top border ("+---+")
        - Last row: Bottom border ("+---+")
        - Middle rows: Original content with side borders ("|content|")
        
        Args:
            row (int): The row number
            
        Returns:
            str: The row text with appropriate border
            
        Raises:
            IndexError: If row is out of bounds
        """
        total_rows = self.get_rows()
        
        if row < 0 or row >= total_rows:
            raise IndexError(f"Row {row} is out of bounds (0-{total_rows-1})")
        
        if row == 0:
            # Top border
            return "+" + self._make_line('-', self._display.get_columns()) + "+"
        elif row == self._display.get_rows() + 1:
            # Bottom border
            return "+" + self._make_line('-', self._display.get_columns()) + "+"
        else:
            # Middle rows with side borders
            original_row = row - 1  # Adjust for the top border
            original_text = self._display.get_row_text(original_row)
            return "|" + original_text + "|"
    
    def _make_line(self, char: str, count: int) -> str:
        """
        Create a line of repeated characters.
        
        Args:
            char (str): The character to repeat
            count (int): The number of times to repeat the character
            
        Returns:
            str: A string with the character repeated count times
        """
        return char * count
    
    def get_inner_content_area(self) -> tuple[int, int]:
        """
        Get the dimensions of the inner content area (excluding borders).
        
        Returns:
            tuple[int, int]: (width, height) of the inner content
        """
        return (self._display.get_columns(), self._display.get_rows())
    
    def get_border_thickness(self) -> int:
        """
        Get the thickness of the border.
        
        For FullBorder, this is always 1.
        
        Returns:
            int: The border thickness (always 1)
        """
        return 1
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        
        Returns:
            str: Representation showing wrapped display
        """
        return f"FullBorder({repr(self._display)})"


class CustomBorder(Border):
    """
    A more flexible border decorator that allows customization of border characters.
    
    This extends the concept of FullBorder to allow different characters
    for different parts of the border.
    """
    
    def __init__(self, display: Display, 
                 horizontal: str = '-', 
                 vertical: str = '|', 
                 corner: str = '+'):
        """
        Initialize a custom border decorator.
        
        Args:
            display (Display): The display component to decorate
            horizontal (str): Character for top and bottom borders
            vertical (str): Character for left and right borders
            corner (str): Character for corners
        """
        super().__init__(display)
        self._horizontal = horizontal
        self._vertical = vertical
        self._corner = corner
    
    def get_columns(self) -> int:
        """Get the number of columns including the border."""
        return 1 + self._display.get_columns() + 1
    
    def get_rows(self) -> int:
        """Get the number of rows including the border."""
        return 1 + self._display.get_rows() + 1
    
    def get_row_text(self, row: int) -> str:
        """Get the text for a specific row with custom border."""
        total_rows = self.get_rows()
        
        if row < 0 or row >= total_rows:
            raise IndexError(f"Row {row} is out of bounds (0-{total_rows-1})")
        
        if row == 0:
            # Top border
            return (self._corner + 
                   self._horizontal * self._display.get_columns() + 
                   self._corner)
        elif row == self._display.get_rows() + 1:
            # Bottom border
            return (self._corner + 
                   self._horizontal * self._display.get_columns() + 
                   self._corner)
        else:
            # Middle rows with side borders
            original_row = row - 1
            original_text = self._display.get_row_text(original_row)
            return self._vertical + original_text + self._vertical
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"CustomBorder({repr(self._display)}, "
                f"h='{self._horizontal}', v='{self._vertical}', c='{self._corner}')")
