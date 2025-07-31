import random

class Dice(random.Random):
    """Dice class using inheritance (before refactoring)"""
    
    def __init__(self, seed=314159):
        super().__init__(seed)
        
    def randint(self, a, b):
        """Override to only support dice rolling"""
        if a != 1 or b != 6:
            raise UnsupportedError("Dice only supports 1-6 range")
        return super().randint(1, 6)
        
    def next_int(self):
        """Get next dice roll (1-6)"""
        return super().randint(1, 6)

class UnsupportedError(Exception):
    """Exception for unsupported operations"""
    pass
