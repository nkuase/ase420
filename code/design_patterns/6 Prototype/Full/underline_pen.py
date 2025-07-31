"""
Prototype Pattern - Concrete Product (UnderlinePen)
This class creates underlined text output using a specified character.
"""

from framework.product import Product


class UnderlinePen(Product):
    """
    Concrete product that creates underlined text.
    Uses a specified character to draw underlines below text.
    """
    
    def __init__(self, ulchar: str):
        """
        Initialize the underline pen with a specific character.
        
        Args:
            ulchar (str): The character to use for underlining
        """
        self.ulchar = ulchar
    
    def use(self, s: str):
        """
        Display the string with an underline beneath it.
        
        Args:
            s (str): The string to underline
        """
        ulen = len(s)
        print(s)
        print(self.ulchar * ulen)
    
    def __str__(self):
        """String representation for debugging."""
        return f"UnderlinePen('{self.ulchar}')"
