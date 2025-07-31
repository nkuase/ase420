"""
StringDisplay class for Template Method Pattern Example

This concrete class extends AbstractDisplay and implements the abstract methods
to display a string with decorative borders. It demonstrates how the same
template method can produce different outputs based on different implementations.

This is a "Concrete Class" in the Template Method pattern.
"""

from abstract_display import AbstractDisplay


class StringDisplay(AbstractDisplay):
    """
    Concrete implementation of AbstractDisplay for displaying a string with borders.
    
    This class implements the abstract methods to create a bordered
    display format for a string.
    """
    
    def __init__(self, string: str):
        """
        Initialize StringDisplay with a string to display.
        
        Args:
            string (str): The string to be displayed
        """
        self._string = string
        self._width = len(string)
    
    def open(self) -> None:
        """
        Implementation of abstract open method.
        Displays the top border line.
        """
        self._print_line()
    
    def print(self) -> None:
        """
        Implementation of abstract print method.
        Displays the string surrounded by vertical bars.
        """
        print(f"|{self._string}|")
    
    def close(self) -> None:
        """
        Implementation of abstract close method.
        Displays the bottom border line.
        """
        self._print_line()
    
    def _print_line(self) -> None:
        """
        Private helper method to print horizontal border lines.
        Prints a line like "+----+" where the number of dashes
        matches the string width.
        """
        print("+", end="")
        for i in range(self._width):
            print("-", end="")
        print("+")
    
    def get_string(self) -> str:
        """
        Get the string being displayed.
        
        Returns:
            str: The string being displayed
        """
        return self._string
    
    def get_width(self) -> int:
        """
        Get the width of the string.
        
        Returns:
            int: The width (length) of the string
        """
        return self._width
    
    def __str__(self) -> str:
        """String representation of StringDisplay."""
        return f"StringDisplay('{self._string}')"
