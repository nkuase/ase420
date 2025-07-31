"""
PrintBanner class for Adapter Pattern Example (Inheritance Version)

This class serves as an Adapter that makes the Banner class compatible
with the Print interface. It uses inheritance to adapt the Banner class.

This demonstrates the "Class Adapter" pattern using inheritance.
"""

from banner import Banner
from print_interface import Print


class PrintBanner(Banner, Print):
    """
    Adapter class that inherits from Banner and implements Print interface.
    
    This is the "Adapter" in the Adapter pattern. It translates calls from
    the Print interface to the Banner class methods.
    
    This version uses multiple inheritance (class adapter pattern):
    - Inherits from Banner to get its functionality
    - Implements Print interface to provide expected interface
    """
    
    def __init__(self, string: str):
        """
        Initialize the PrintBanner adapter.
        
        Args:
            string (str): The text to be displayed
        """
        # Call parent constructor
        super().__init__(string)
    
    def print_weak(self) -> None:
        """
        Implement Print interface's print_weak method.
        
        This method adapts/translates the call to Banner's show_with_paren method.
        The "weak" formatting is mapped to parentheses display.
        """
        self.show_with_paren()
    
    def print_strong(self) -> None:
        """
        Implement Print interface's print_strong method.
        
        This method adapts/translates the call to Banner's show_with_aster method.
        The "strong" formatting is mapped to asterisk display.
        """
        self.show_with_aster()
    
    def __str__(self) -> str:
        """String representation of the PrintBanner adapter."""
        return f"PrintBanner adapting {super().__str__()}"
