class Shape:
    """Shape class with type codes (before refactoring)"""
    
    TYPECODE_LINE = 0
    TYPECODE_RECTANGLE = 1
    TYPECODE_OVAL = 2
    
    def __init__(self, typecode: int, startx: int, starty: int, endx: int, endy: int):
        self.typecode = typecode
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        
    def get_typecode(self) -> int:
        return self.typecode
        
    def get_name(self) -> str:
        if self.typecode == Shape.TYPECODE_LINE:
            return "LINE"
        elif self.typecode == Shape.TYPECODE_RECTANGLE:
            return "RECTANGLE"
        elif self.typecode == Shape.TYPECODE_OVAL:
            return "OVAL"
        else:
            return None
            
    def __str__(self):
        return (f"[ {self.get_name()}, "
                f"({self.startx}, {self.starty})-"
                f"({self.endx}, {self.endy}) ]")
                
    def draw(self):
        if self.typecode == Shape.TYPECODE_LINE:
            self._draw_line()
        elif self.typecode == Shape.TYPECODE_RECTANGLE:
            self._draw_rectangle()
        elif self.typecode == Shape.TYPECODE_OVAL:
            self._draw_oval()
            
    def _draw_line(self):
        print(f"drawLine: {self}")
        
    def _draw_rectangle(self):
        print(f"drawRectangle: {self}")
        
    def _draw_oval(self):
        print(f"drawOval: {self}")
