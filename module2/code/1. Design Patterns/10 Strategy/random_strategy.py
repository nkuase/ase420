"""
Random Strategy - Randomly chooses Rock, Paper, or Scissors  
============================================================
Simple concrete strategy that randomly selects a hand.
"""

import random
from base_classes import Strategy, ROCK, PAPER, SCISSORS


class RandomStrategy(Strategy):
    """Strategy that randomly chooses a hand"""
    
    def __init__(self):
        self.hands = [ROCK, PAPER, SCISSORS]
    
    def choose_hand(self):
        return random.choice(self.hands)
    
    def __str__(self):
        return "RandomStrategy"
