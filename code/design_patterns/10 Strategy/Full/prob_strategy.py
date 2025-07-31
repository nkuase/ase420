"""
ProbStrategy class for Strategy Pattern Example

This concrete strategy implements a probabilistic approach based on game history.
It maintains a 3x3 matrix tracking which hands follow which hands, and uses
this history to make probabilistic decisions about the next move.

This demonstrates a more sophisticated concrete strategy in the Strategy pattern.
"""

import random
from typing import List
from strategy import Strategy
from hand import Hand


class ProbStrategy(Strategy):
    """
    A sophisticated strategy that learns from game history.
    
    This strategy maintains a probability matrix of hand transitions:
    - Tracks what hands tend to follow other hands
    - Uses this history to make probabilistic decisions
    - Adapts its behavior based on win/loss outcomes
    """
    
    def __init__(self, seed: int):
        """
        Initialize the ProbStrategy with a random seed.
        
        Args:
            seed (int): Seed for the random number generator
        """
        self._random = random.Random(seed)
        self._prev_hand_value = 0
        self._current_hand_value = 0
        
        # 3x3 history matrix: history[prev][current] = frequency
        # Initialized with 1s to avoid zero probabilities
        self._history: List[List[int]] = [
            [1, 1, 1],
            [1, 1, 1], 
            [1, 1, 1]
        ]
    
    def next_hand(self) -> Hand:
        """
        Determine the next hand using probabilistic strategy.
        
        Uses the history matrix to calculate probabilities and select
        the next hand based on what has been effective previously.
        
        Returns:
            Hand: The next hand to play
        """
        # Generate random number for probabilistic selection
        bet = self._random.randint(0, self._get_sum(self._current_hand_value) - 1)
        
        # Select hand based on accumulated probabilities
        hand_value = 0
        if bet < self._history[self._current_hand_value][0]:
            hand_value = 0  # Rock
        elif bet < (self._history[self._current_hand_value][0] + 
                   self._history[self._current_hand_value][1]):
            hand_value = 1  # Scissors
        else:
            hand_value = 2  # Paper
        
        # Update hand values for next iteration
        self._prev_hand_value = self._current_hand_value
        self._current_hand_value = hand_value
        
        return Hand.get_hand(hand_value)
    
    def _get_sum(self, hand_value: int) -> int:
        """
        Calculate the sum of frequencies for a given hand value.
        
        Args:
            hand_value (int): The hand value to get sum for
            
        Returns:
            int: Sum of all frequencies for the given hand value
        """
        return sum(self._history[hand_value])
    
    def study(self, win: bool) -> None:
        """
        Learn from the game result and update the history matrix.
        
        Strategy for updating:
        - If we won: increase frequency of the winning combination
        - If we lost: increase frequency of the other two combinations
          (the hands that would have beaten our opponent)
        
        Args:
            win (bool): True if we won the last game, False if we lost
        """
        if win:
            # Reinforce the winning combination
            self._history[self._prev_hand_value][self._current_hand_value] += 1
        else:
            # Reinforce the combinations that would have won
            # Increase frequency of the two hands that would have beaten the opponent
            self._history[self._prev_hand_value][(self._current_hand_value + 1) % 3] += 1
            self._history[self._prev_hand_value][(self._current_hand_value + 2) % 3] += 1
    
    def get_history_matrix(self) -> List[List[int]]:
        """
        Get a copy of the current history matrix.
        
        Returns:
            List[List[int]]: Copy of the 3x3 history matrix
        """
        return [row[:] for row in self._history]  # Deep copy
    
    def get_probabilities(self, hand_value: int) -> List[float]:
        """
        Get the current probabilities for the next hand given a current hand.
        
        Args:
            hand_value (int): The current hand value
            
        Returns:
            List[float]: Probabilities for [Rock, Scissors, Paper]
        """
        total = self._get_sum(hand_value)
        return [freq / total for freq in self._history[hand_value]]
    
    def __str__(self) -> str:
        """String representation of the strategy."""
        return f"ProbStrategy(prev={self._prev_hand_value}, current={self._current_hand_value})"
    
    def print_history(self) -> None:
        """Print the current history matrix in a readable format."""
        print("History Matrix (frequency of hand transitions):")
        print("    From\\To  Rock  Scissors  Paper")
        hand_names = ["Rock    ", "Scissors", "Paper   "]
        for i, row in enumerate(self._history):
            print(f"    {hand_names[i]}  {row[0]:4d}  {row[1]:8d}  {row[2]:5d}")
