"""
Memento Pattern - Memento Class
This class stores the internal state of the Gamer object.
It provides both narrow and wide interfaces for accessing the stored state.
"""

from typing import List


class Memento:
    """
    Memento class that stores the state of a Gamer.
    Implements both narrow interface (for caretaker) and wide interface (for originator).
    """
    
    def __init__(self, money: int):
        """
        Initialize memento with money amount.
        This constructor has package-level access (wide interface).
        
        Args:
            money (int): The amount of money to store
        """
        self._money = money
        self._fruits: List[str] = []
    
    def get_money(self) -> int:
        """
        Get the stored money amount.
        This is part of the narrow interface - accessible to caretaker.
        
        Returns:
            int: The stored money amount
        """
        return self._money
    
    def _add_fruit(self, fruit: str):
        """
        Add a fruit to the stored state.
        This is part of the wide interface - only accessible to originator.
        
        Args:
            fruit (str): The fruit to add
        """
        self._fruits.append(fruit)
    
    def _get_fruits(self) -> List[str]:
        """
        Get a copy of the stored fruits.
        This is part of the wide interface - only accessible to originator.
        
        Returns:
            List[str]: A copy of the stored fruits list
        """
        return self._fruits.copy()
    
    # In Python, we simulate package-level access by using underscore prefix
    # and providing access methods that the Gamer class can use
    def add_fruit(self, fruit: str):
        """Public method for Gamer to add fruits (simulates package access)."""
        self._add_fruit(fruit)
    
    def get_fruits(self) -> List[str]:
        """Public method for Gamer to get fruits (simulates package access)."""
        return self._get_fruits()
