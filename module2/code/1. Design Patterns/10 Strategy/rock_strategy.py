"""
Always Rock Strategy - Always chooses Rock
==========================================
Simple concrete strategy that always plays Rock.
"""

from base_classes import Strategy, ROCK


class AlwaysRockStrategy(Strategy):
    """Strategy that always chooses Rock"""
    
    def choose_hand(self):
        return ROCK
    
    def __str__(self):
        return "AlwaysRockStrategy"
