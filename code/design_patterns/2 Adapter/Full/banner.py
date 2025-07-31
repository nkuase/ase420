"""
Banner class for Adapter Pattern Example

This class represents an existing functionality that we want to adapt.
It has its own interface with specific method names (showWithParen, showWithAster)
that don't match what our client code expects.

This is the "Adaptee" in the Adapter pattern.
"""


class Banner:
    """Existing class with its own interface that needs to be adapted."""
    
    def __init__(self, string: str):
        """
        Initialize the Banner with a string to display.
        
        Args:
            string (str): The text to be displayed in the banner
        """
        self._string = string
    
    def show_with_paren(self) -> None:
        """
        Display the string surrounded by parentheses.
        This is an existing method with its own naming convention.
        """
        print(f"({self._string})")
    
    def show_with_aster(self) -> None:
        """
        Display the string surrounded by asterisks.
        This is an existing method with its own naming convention.
        """
        print(f"*{self._string}*")
    
    def __str__(self) -> str:
        """String representation of the Banner."""
        return f"Banner('{self._string}')"
