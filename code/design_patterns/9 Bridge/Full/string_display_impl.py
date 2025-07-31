"""
Bridge Pattern - Concrete Implementation
This class provides a concrete implementation of DisplayImpl for string display.
It implements the actual display logic using text formatting.
"""

from display_impl import DisplayImpl


class StringDisplayImpl(DisplayImpl):
    """
    Concrete implementation that displays a string with borders.
    This class implements the actual display logic for strings.
    """
    
    def __init__(self, string: str):
        """
        Initialize with the string to display.
        
        Args:
            string (str): The string to be displayed
        """
        self.string = string
        self.width = len(string)
    
    def raw_open(self):
        """Open the display by printing the top border"""
        self._print_line()
    
    def raw_print(self):
        """Print the string content with side borders"""
        print(f"|{self.string}|")
    
    def raw_close(self):
        """Close the display by printing the bottom border"""
        self._print_line()
    
    def _print_line(self):
        """
        Private method to print a horizontal line border.
        This creates the top and bottom borders of the display.
        """
        line = "+" + "-" * self.width + "+"
        print(line)
