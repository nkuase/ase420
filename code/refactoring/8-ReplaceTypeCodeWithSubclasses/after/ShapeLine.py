from Shape import Shape

class ShapeLine(Shape):
    """Line shape implementation"""
    
    def __init__(self, startx: int, starty: int, endx: int, endy: int):
        super().__init__(startx, starty, endx, endy)
        
    def get_typecode(self) -> int:
        return Shape.TYPECODE_LINE
        
    def get_name(self) -> str:
        return "LINE"
        
    def draw(self):
        self._draw_line()
        
    def _draw_line(self):
        print(f"drawLine: {self}")
