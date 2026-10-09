"""
Strategy Pattern - Core Classes  
===============================
Simple classes for demonstrating Strategy pattern with Rock-Paper-Scissors.
No ABC, no complex logic, just the essential concept.
"""

class Hand:
    """Simple hand representation"""
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name


# Pre-made hands for easy use
ROCK = Hand("Rock")
PAPER = Hand("Paper") 
SCISSORS = Hand("Scissors")


class Player:
    """Context class - uses strategy to choose hands"""
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy
    
    def play(self):
        """Ask strategy to choose a hand"""
        return self.strategy.choose_hand()
    
    def set_strategy(self, strategy):
        """Change strategy at runtime"""
        self.strategy = strategy
    
    def get_strategy_name(self):
        return self.strategy.__class__.__name__


class Strategy:
    """Base strategy class"""
    def choose_hand(self):
        """Choose a hand - implemented by concrete strategies"""
        pass
