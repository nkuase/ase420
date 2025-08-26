"""
WinningStrategy class for Strategy Pattern Example

This concrete strategy implements a simple "winning strategy":
- If the previous hand won, use it again
- If the previous hand lost or this is the first game, choose randomly

This demonstrates a basic concrete strategy in the Strategy pattern.
"""

import random
from typing import Optional
from strategy import Strategy
from hand import Hand


class WinningStrategy(Strategy):
    """
    A simple strategy that reuses winning hands.
    
    This strategy remembers the previous hand and whether it won.
    If the previous hand won, it plays the same hand again.
    If the previous hand lost or it's the first move, it chooses randomly.
    """
    
    def __init__(self, seed: int):
        """
        Initialize the WinningStrategy with a random seed.
        
        Args:
            seed (int): Seed for the random number generator to ensure reproducible results
        """
        self._random = random.Random(seed)
        self._won = False
        self._prev_hand: Optional[Hand] = None
    
    def next_hand(self) -> Hand:
        """
        Determine the next hand using the winning strategy logic.
        
        Strategy:
        - If we didn't win last time (or it's the first game), choose randomly
        - If we won last time, use the same hand again
        
        Returns:
            Hand: The next hand to play
        """
        if not self._won:
            # Choose a new random hand if we lost or it's the first game
            self._prev_hand = Hand.get_hand(self._random.randint(0, 2))
        
        # Return the same hand if we won, or the new random hand if we lost
        return self._prev_hand
    
    def study(self, win: bool) -> None:
        """
        Learn from the game result.
        
        This simple strategy only remembers whether the last game was won.
        
        Args:
            win (bool): True if we won the last game, False if we lost
        """
        self._won = win
    
    def get_win_status(self) -> bool:
        """
        Get the current win status.
        
        Returns:
            bool: True if the last game was won, False otherwise
        """
        return self._won
    
    def get_previous_hand(self) -> Optional[Hand]:
        """
        Get the previous hand played.
        
        Returns:
            Optional[Hand]: The previous hand, or None if no hand has been played yet
        """
        return self._prev_hand
    
    def __str__(self) -> str:
        """String representation of the strategy."""
        return f"WinningStrategy(won_last={self._won}, prev_hand={self._prev_hand})"
