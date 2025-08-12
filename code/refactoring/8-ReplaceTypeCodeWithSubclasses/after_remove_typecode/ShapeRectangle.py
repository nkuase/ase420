from Shape import Shape

class ShapeRectangle(Shape):
    @staticmethod
    def create(startx: int, starty: int, endx: int, endy: int) -> 'Shape':
        return ShapeRectangle(startx, starty, endx, endy)        
    
    def __init__(self, startx: int, starty: int, endx: int, endy: int):
        super().__init__(startx, starty, endx, endy)
        
    def get_name(self) -> str:
        return "RECTANGLE"
        
    def draw(self):
        self._draw_rectangle()
        
    def _draw_rectangle(self):
        print(f"drawRectangle: {self}")
