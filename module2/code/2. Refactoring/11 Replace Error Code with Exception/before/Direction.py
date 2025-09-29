class Direction:
    """Direction class with x, y components"""
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def set_direction(self, x: int, y: int):
        """Set new direction"""
        self.x = x
        self.y = y
