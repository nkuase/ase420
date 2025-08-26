"""
Flyweight Pattern - BigChar (Concrete Flyweight)
This class represents a big character that can be shared among multiple contexts.
The font data is intrinsic state (shared), while position is extrinsic state.
"""

import os


class BigChar:
    """
    Concrete flyweight that represents a big ASCII art character.
    Stores the intrinsic state (font data) that can be shared across instances.
    """
    
    def __init__(self, charname: str):
        """
        Initialize a big character by loading its font data from file.
        
        Args:
            charname (str): The character to load (e.g., '0', '1', '-')
        """
        self.charname = charname
        
        try:
            filename = f"big{charname}.txt"
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    self.fontdata = f.read()
            else:
                # Fallback if file doesn't exist
                self.fontdata = f"{charname}?\n"
        except IOError:
            self.fontdata = f"{charname}?\n"
    
    def print(self):
        """
        Print the big character to console.
        This method uses the intrinsic state (font data) stored in the flyweight.
        """
        print(self.fontdata, end='')
    
    def get_fontdata(self) -> str:
        """
        Get the font data for this character.
        
        Returns:
            str: The ASCII art representation of the character
        """
        return self.fontdata
    
    def __str__(self) -> str:
        """String representation of the big character."""
        return f"BigChar('{self.charname}')"
