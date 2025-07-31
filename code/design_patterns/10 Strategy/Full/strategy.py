"""
Strategy interface for Strategy Pattern Example

This interface defines the strategy for playing Rock-Paper-Scissors.
Different strategies can implement this interface to provide different
approaches to the game.

This is the "Strategy" interface in the Strategy pattern.
"""

from abc import ABC, abstractmethod
from hand import Hand


class Strategy(ABC):
    """
    Abstract strategy interface for Rock-Paper-Scissors game strategies.
    
    This interface defines the contract that all concrete strategies must follow.
    The Strategy pattern allows algorithms to be selected at runtime.
    """
    
    @abstractmethod
    def next_hand(self) -> Hand:
        """
        Determine the next hand to play.
        
        This method should implement the strategy's logic for choosing
        the next Rock, Paper, or Scissors move.
        
        Returns:
            Hand: The next hand to play
        """
        pass
    
    @abstractmethod
    def study(self, win: bool) -> None:
        """
        Learn from the result of the previous game.
        
        This method allows the strategy to adapt and learn from
        the outcomes of previous games.
        
        Args:
            win (bool): True if the strategy won the last game, False if lost
        """
        pass
