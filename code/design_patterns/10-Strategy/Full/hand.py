"""
Hand class for Strategy Pattern Example

This class represents a hand in Rock-Paper-Scissors game.
It encapsulates the logic for comparing hands and determining winners.
Python doesn't have enums in the same way as Java, but we can use
the enum module or create a class with class constants.
"""

from enum import Enum
from typing import Optional


class Hand(Enum):
    """
    Enum representing Rock-Paper-Scissors hands.
    
    Each hand has a Korean name and a numeric value for comparison logic.
    """
    
    ROCK = ("바위", 0)
    SCISSORS = ("가위", 1) 
    PAPER = ("보", 2)
    
    def __init__(self, name: str, hand_value: int):
        """
        Initialize a Hand with name and value.
        
        Args:
            name (str): Korean name of the hand
            hand_value (int): Numeric value (0=Rock, 1=Scissors, 2=Paper)
        """
        self.name = name
        self.hand_value = hand_value
    
    @classmethod
    def get_hand(cls, hand_value: int) -> 'Hand':
        """
        Get Hand enum by numeric value.
        
        Args:
            hand_value (int): The numeric value (0, 1, or 2)
            
        Returns:
            Hand: The corresponding Hand enum
            
        Raises:
            ValueError: If hand_value is not 0, 1, or 2
        """
        hands = [cls.ROCK, cls.SCISSORS, cls.PAPER]
        if 0 <= hand_value <= 2:
            return hands[hand_value]
        else:
            raise ValueError(f"Invalid hand value: {hand_value}. Must be 0, 1, or 2.")
    
    def is_stronger_than(self, other: 'Hand') -> bool:
        """
        Check if this hand is stronger than the other hand.
        
        Args:
            other (Hand): The other hand to compare against
            
        Returns:
            bool: True if this hand wins, False otherwise
        """
        return self._fight(other) == 1
    
    def is_weaker_than(self, other: 'Hand') -> bool:
        """
        Check if this hand is weaker than the other hand.
        
        Args:
            other (Hand): The other hand to compare against
            
        Returns:
            bool: True if this hand loses, False otherwise
        """
        return self._fight(other) == -1
    
    def _fight(self, other: 'Hand') -> int:
        """
        Compare this hand with another hand.
        
        Rock-Paper-Scissors rules:
        - Rock (0) beats Scissors (1)
        - Scissors (1) beats Paper (2)  
        - Paper (2) beats Rock (0)
        
        Args:
            other (Hand): The other hand to fight against
            
        Returns:
            int: 0 for tie, 1 if this hand wins, -1 if this hand loses
        """
        if self == other:
            return 0  # Tie
        elif (self.hand_value + 1) % 3 == other.hand_value:
            return 1  # This hand wins
        else:
            return -1  # This hand loses
    
    def __str__(self) -> str:
        """String representation showing the Korean name."""
        return self.name
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Hand.{self.name}({self.name}, {self.hand_value})"


# Alternative implementation without Enum (more similar to Java)
class HandAlternative:
    """Alternative implementation that more closely mirrors the Java version."""
    
    # Class constants
    ROCK_VALUE = 0
    SCISSORS_VALUE = 1
    PAPER_VALUE = 2
    
    def __init__(self, name: str, hand_value: int):
        self._name = name
        self._hand_value = hand_value
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def hand_value(self) -> int:
        return self._hand_value
    
    @classmethod
    def get_hand(cls, hand_value: int):
        """Factory method to create Hand instances."""
        hands = [
            cls("바위", 0),
            cls("가위", 1),
            cls("보", 2)
        ]
        if 0 <= hand_value <= 2:
            return hands[hand_value]
        else:
            raise ValueError(f"Invalid hand value: {hand_value}")
    
    def is_stronger_than(self, other) -> bool:
        return self._fight(other) == 1
    
    def is_weaker_than(self, other) -> bool:
        return self._fight(other) == -1
    
    def _fight(self, other) -> int:
        if self._hand_value == other._hand_value:
            return 0
        elif (self._hand_value + 1) % 3 == other._hand_value:
            return 1
        else:
            return -1
    
    def __str__(self) -> str:
        return self._name
    
    def __eq__(self, other) -> bool:
        return isinstance(other, HandAlternative) and self._hand_value == other._hand_value
