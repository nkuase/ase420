"""
Flyweight Pattern - BigString (Context)
This class uses BigChar flyweights to represent a string of big characters.
It demonstrates how flyweights can be used in different contexts.
"""

from typing import List
from big_char import BigChar
from big_char_factory import BigCharFactory


class BigString:
    """
    Context class that uses BigChar flyweights to represent a string.
    This class holds references to flyweights but doesn't duplicate their intrinsic state.
    """
    
    def __init__(self, string: str):
        """
        Initialize a big string by getting flyweight instances for each character.
        
        Args:
            string (str): The string to represent with big characters
        """
        self.string = string
        factory = BigCharFactory.get_instance()
        
        # Get flyweight instances for each character
        self.bigchars: List[BigChar] = []
        for char in string:
            big_char = factory.get_big_char(char)
            self.bigchars.append(big_char)
    
    def print(self):
        """
        Print the big string by delegating to each BigChar flyweight.
        This demonstrates how extrinsic state (position in string) is handled
        while intrinsic state (font data) is shared.
        """
        # For ASCII art, we need to print line by line
        lines = self._get_lines()
        for line in lines:
            print(line)
    
    def _get_lines(self) -> List[str]:
        """
        Get the lines of the big string by combining font data from all characters.
        
        Returns:
            List[str]: List of lines that make up the complete big string
        """
        if not self.bigchars:
            return []
        
        # Split each character's font data into lines
        char_lines = []
        for big_char in self.bigchars:
            fontdata = big_char.get_fontdata()
            lines = fontdata.split('\n')
            char_lines.append(lines)
        
        # Find the maximum number of lines
        max_lines = max(len(lines) for lines in char_lines) if char_lines else 0
        
        # Combine lines horizontally
        result_lines = []
        for line_num in range(max_lines):
            combined_line = ""
            for char_line_list in char_lines:
                if line_num < len(char_line_list):
                    combined_line += char_line_list[line_num]
                else:
                    # Pad with spaces if character has fewer lines
                    combined_line += " " * 16  # Assuming each char is 16 wide
            result_lines.append(combined_line.rstrip())
        
        return result_lines
    
    def get_string(self) -> str:
        """
        Get the original string.
        
        Returns:
            str: The original string
        """
        return self.string
    
    def get_char_count(self) -> int:
        """
        Get the number of characters in this big string.
        
        Returns:
            int: Number of characters
        """
        return len(self.bigchars)
    
    def __str__(self) -> str:
        """String representation of the big string."""
        return f"BigString('{self.string}')"
