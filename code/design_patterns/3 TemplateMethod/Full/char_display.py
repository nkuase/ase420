"""
CharDisplay class for Template Method Pattern Example

This concrete class extends AbstractDisplay and implements the abstract methods
to display a single character. It demonstrates how different subclasses can
provide different implementations of the same algorithm steps.

This is a "Concrete Class" in the Template Method pattern.
"""

from abstract_display import AbstractDisplay


class CharDisplay(AbstractDisplay):
    """
    Concrete implementation of AbstractDisplay for displaying a single character.
    
    This class implements the abstract methods to create a specific
    display format for a character.
    """
    
    def __init__(self, ch: str):
        """
        Initialize CharDisplay with a character to display.
        
        Args:
            ch (str): The character to be displayed (should be single character)
        """
        if len(ch) != 1:
            raise ValueError("CharDisplay requires exactly one character")
        self._ch = ch
    
    def open(self) -> None:
        """
        Implementation of abstract open method.
        Displays the opening characters "<<".
        """
        print("<<", end="")
    
    def print(self) -> None:
        """
        Implementation of abstract print method.
        Displays the stored character once.
        """
        print(self._ch, end="")
    
    def close(self) -> None:
        """
        Implementation of abstract close method.
        Displays the closing characters ">>" and a newline.
        """
        print(">>")
    
    def get_character(self) -> str:
        """
        Get the character being displayed.
        
        Returns:
            str: The character being displayed
        """
        return self._ch
    
    def __str__(self) -> str:
        """String representation of CharDisplay."""
        return f"CharDisplay('{self._ch}')"
