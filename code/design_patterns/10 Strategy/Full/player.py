"""
Player class for Strategy Pattern Example

This class represents a player in the Rock-Paper-Scissors game.
It demonstrates the Context in the Strategy pattern - it uses a Strategy
to determine its moves but doesn't know the details of the strategy implementation.

This is the "Context" in the Strategy pattern.
"""

from strategy import Strategy
from hand import Hand


class Player:
    """
    A player in the Rock-Paper-Scissors game.
    
    The Player class delegates the decision-making to a Strategy object.
    This demonstrates the Strategy pattern where the algorithm (strategy)
    can be changed independently of the client (player) that uses it.
    """
    
    def __init__(self, name: str, strategy: Strategy):
        """
        Initialize a player with a name and strategy.
        
        Args:
            name (str): The player's name
            strategy (Strategy): The strategy this player will use
        """
        self._name = name
        self._strategy = strategy
        self._win_count = 0
        self._lose_count = 0
        self._game_count = 0
    
    def next_hand(self) -> Hand:
        """
        Get the next hand from the strategy.
        
        The player delegates the decision to its strategy.
        This is the key aspect of the Strategy pattern.
        
        Returns:
            Hand: The next hand to play
        """
        return self._strategy.next_hand()
    
    def win(self) -> None:
        """
        Record a win and inform the strategy.
        
        Updates statistics and tells the strategy about the win
        so it can learn and adapt.
        """
        self._strategy.study(True)
        self._win_count += 1
        self._game_count += 1
    
    def lose(self) -> None:
        """
        Record a loss and inform the strategy.
        
        Updates statistics and tells the strategy about the loss
        so it can learn and adapt.
        """
        self._strategy.study(False)
        self._lose_count += 1
        self._game_count += 1
    
    def even(self) -> None:
        """
        Record a tie game.
        
        Updates game count but doesn't inform strategy since
        ties don't provide learning information.
        """
        self._game_count += 1
    
    def get_name(self) -> str:
        """Get the player's name."""
        return self._name
    
    def get_strategy(self) -> Strategy:
        """Get the player's strategy (useful for analysis)."""
        return self._strategy
    
    def get_win_count(self) -> int:
        """Get the number of wins."""
        return self._win_count
    
    def get_lose_count(self) -> int:
        """Get the number of losses."""
        return self._lose_count
    
    def get_game_count(self) -> int:
        """Get the total number of games played."""
        return self._game_count
    
    def get_tie_count(self) -> int:
        """Get the number of tie games."""
        return self._game_count - self._win_count - self._lose_count
    
    def get_win_rate(self) -> float:
        """
        Calculate the win rate.
        
        Returns:
            float: Win rate as a percentage (0.0 to 100.0)
        """
        if self._game_count == 0:
            return 0.0
        return (self._win_count / self._game_count) * 100.0
    
    def reset_stats(self) -> None:
        """Reset all game statistics."""
        self._win_count = 0
        self._lose_count = 0
        self._game_count = 0
    
    def __str__(self) -> str:
        """
        String representation showing player stats.
        
        Format matches the Java version for consistency.
        """
        return (f"[{self._name}:"
                f"{self._game_count} games, "
                f"{self._win_count} win, "
                f"{self._lose_count} lose]")
    
    def detailed_stats(self) -> str:
        """
        Get detailed statistics including win rate and ties.
        
        Returns:
            str: Detailed statistics string
        """
        tie_count = self.get_tie_count()
        win_rate = self.get_win_rate()
        
        return (f"Player: {self._name}\n"
                f"  Total games: {self._game_count}\n"
                f"  Wins: {self._win_count}\n"
                f"  Losses: {self._lose_count}\n"
                f"  Ties: {tie_count}\n"
                f"  Win rate: {win_rate:.1f}%\n"
                f"  Strategy: {type(self._strategy).__name__}")
