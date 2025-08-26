class Position:
    """Position class with x, y coordinates"""
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def relative_move(self, dx: int, dy: int):
        """Move relative to current position"""
        self.x += dx
        self.y += dy
