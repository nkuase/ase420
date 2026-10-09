"""
Always Paper Strategy - Always chooses Paper
============================================
Simple concrete strategy that always plays Paper.
"""

from base_classes import Strategy, PAPER


class AlwaysPaperStrategy(Strategy):
    """Strategy that always chooses Paper"""
    
    def choose_hand(self):
        return PAPER
    
    def __str__(self):
        return "AlwaysPaperStrategy"
