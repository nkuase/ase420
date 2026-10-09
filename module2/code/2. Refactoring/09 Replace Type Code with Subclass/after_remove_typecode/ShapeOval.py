from Shape import Shape

class ShapeOval(Shape):
    @staticmethod
    def create(startx: int, starty: int, endx: int, endy: int) -> 'Shape':
        return ShapeOval(startx, starty, endx, endy)    
    
    def get_name(self) -> str:
        return "OVAL"
        
    def draw(self):
        self._draw_oval()
        
    def _draw_oval(self):
        print(f"drawOval: {self}")
