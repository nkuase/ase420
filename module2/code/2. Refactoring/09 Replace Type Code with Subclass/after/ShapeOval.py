from Shape import Shape

class ShapeOval(Shape):
    """Oval shape implementation"""
    
    def __init__(self, startx: int, starty: int, endx: int, endy: int):
        super().__init__(startx, starty, endx, endy)
        
    def get_typecode(self) -> int:
        return Shape.TYPECODE_OVAL
        
    def get_name(self) -> str:
        return "OVAL"
        
    def draw(self):
        self._draw_oval()
        
    def _draw_oval(self):
        print(f"drawOval: {self}")
