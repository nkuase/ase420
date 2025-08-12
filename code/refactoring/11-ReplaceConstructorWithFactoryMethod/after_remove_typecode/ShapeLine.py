from Shape import Shape

class ShapeLine(Shape):
    """Line shape implementation"""
    
    def __init__(self, startx: int, starty: int, endx: int, endy: int):
        super().__init__(startx, starty, endx, endy)
        
    def get_name(self) -> str:
        return "LINE"
        
    def draw(self):
        print(f"drawLine: {self}")
