import random

class Dice:
    """Dice class using delegation (after refactoring)"""
    
    def __init__(self, seed=314159):
        self._random = random.Random(seed)
        
    def next_int(self):
        """Get next dice roll (1-6)"""
        return self._random.randint(1, 6)
        
    def set_seed(self, seed):
        """Set the random seed"""
        self._random.seed(seed)
