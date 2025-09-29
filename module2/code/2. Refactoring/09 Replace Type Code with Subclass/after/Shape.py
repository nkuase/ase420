from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract shape class (after refactoring)"""
    
    TYPECODE_LINE = 0
    TYPECODE_RECTANGLE = 1
    TYPECODE_OVAL = 2
    
    @staticmethod
    def create_shape(typecode: int, startx: int, starty: int, endx: int, endy: int) -> 'Shape':
        """Factory method to create shapes"""
        if typecode == Shape.TYPECODE_LINE:
            from ShapeLine import ShapeLine
            return ShapeLine(startx, starty, endx, endy)
        elif typecode == Shape.TYPECODE_RECTANGLE:
            from ShapeRectangle import ShapeRectangle
            return ShapeRectangle(startx, starty, endx, endy)
        elif typecode == Shape.TYPECODE_OVAL:
            from ShapeOval import ShapeOval
            return ShapeOval(startx, starty, endx, endy)
        else:
            raise ValueError(f"typecode = {typecode}")
    
    def __init__(self, startx: int, starty: int, endx: int, endy: int):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        
    @abstractmethod
    def get_typecode(self) -> int:
        """Get the type code for this shape"""
        pass
        
    @abstractmethod
    def get_name(self) -> str:
        """Get the name of this shape"""
        pass
        
    def __str__(self):
        return (f"[ {self.get_name()}, "
                f"({self.startx}, {self.starty})-"
                f"({self.endx}, {self.endy}) ]")
                
    @abstractmethod
    def draw(self):
        """Draw this shape"""
        pass
