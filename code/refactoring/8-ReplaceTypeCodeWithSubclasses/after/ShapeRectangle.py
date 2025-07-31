from Shape import Shape

class ShapeRectangle(Shape):
    """Rectangle shape implementation"""
    
    def __init__(self, startx: int, starty: int, endx: int, endy: int):
        super().__init__(startx, starty, endx, endy)
        
    def get_typecode(self) -> int:
        return Shape.TYPECODE_RECTANGLE
        
    def get_name(self) -> str:
        return "RECTANGLE"
        
    def draw(self):
        self._draw_rectangle()
        
    def _draw_rectangle(self):
        print(f"drawRectangle: {self}")
