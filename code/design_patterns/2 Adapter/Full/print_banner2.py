"""
PrintBanner class for Adapter Pattern Example (Composition Version)

This class serves as an Adapter that makes the Banner class compatible
with the Print abstract class. It uses composition to adapt the Banner class.

This demonstrates the "Object Adapter" pattern using composition.
"""

from banner import Banner
from print_class import Print


class PrintBanner(Print):
    """
    Adapter class that extends Print and contains a Banner instance.
    
    This is the "Adapter" in the Adapter pattern. It translates calls from
    the Print interface to the Banner class methods using composition.
    
    This version uses composition (object adapter pattern):
    - Extends Print abstract class to provide expected interface
    - Contains Banner instance as a member (composition)
    - Delegates calls to the Banner instance
    """
    
    def __init__(self, string: str):
        """
        Initialize the PrintBanner adapter.
        
        Args:
            string (str): The text to be displayed
        """
        # Create a Banner instance (composition)
        self._banner = Banner(string)
    
    def print_weak(self) -> None:
        """
        Implement Print class's abstract print_weak method.
        
        This method adapts/translates the call to Banner's show_with_paren method
        by delegating to the contained Banner instance.
        """
        self._banner.show_with_paren()
    
    def print_strong(self) -> None:
        """
        Implement Print class's abstract print_strong method.
        
        This method adapts/translates the call to Banner's show_with_aster method
        by delegating to the contained Banner instance.
        """
        self._banner.show_with_aster()
    
    def get_banner(self) -> Banner:
        """
        Get access to the contained Banner instance.
        This method demonstrates the composition relationship.
        
        Returns:
            Banner: The contained Banner instance
        """
        return self._banner
    
    def __str__(self) -> str:
        """String representation of the PrintBanner adapter."""
        return f"PrintBanner containing {self._banner}"
