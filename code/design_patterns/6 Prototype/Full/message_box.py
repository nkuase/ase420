"""
Prototype Pattern - Concrete Product (MessageBox)
This class creates boxed text output using a specified decoration character.
"""

from framework.product import Product


class MessageBox(Product):
    """
    Concrete product that creates a decorative box around text.
    Uses a specified character to create borders around the message.
    """
    
    def __init__(self, decochar: str):
        """
        Initialize the message box with a specific decoration character.
        
        Args:
            decochar (str): The character to use for the box decoration
        """
        self.decochar = decochar
    
    def use(self, s: str):
        """
        Display the string inside a decorative box.
        
        Args:
            s (str): The string to display in the box
        """
        decolen = 1 + len(s) + 1  # Border + text + border
        
        # Top border
        print(self.decochar * decolen)
        
        # Middle line with text
        print(f"{self.decochar}{s}{self.decochar}")
        
        # Bottom border
        print(self.decochar * decolen)
    
    def __str__(self):
        """String representation for debugging."""
        return f"MessageBox('{self.decochar}')"
