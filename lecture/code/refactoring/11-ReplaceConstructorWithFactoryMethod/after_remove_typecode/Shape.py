from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract shape class with factory methods for subclasses"""
    
    @staticmethod
    def create_line(startx: int, starty: int, endx: int, endy: int) -> 'Shape':
        """Factory method to create line shapes"""
        from ShapeLine import ShapeLine
        return ShapeLine(startx, starty, endx, endy)
        
    @staticmethod
    def create_rectangle(startx: int, starty: int, endx: int, endy: int) -> 'Shape':
        """Factory method to create rectangle shapes"""
        from ShapeRectangle import ShapeRectangle
        return ShapeRectangle(startx, starty, endx, endy)
        
    @staticmethod
    def create_oval(startx: int, starty: int, endx: int, endy: int) -> 'Shape':
        """Factory method to create oval shapes"""
        from ShapeOval import ShapeOval
        return ShapeOval(startx, starty, endx, endy)
    
    def __init__(self, startx: int, starty: int, endx: int, endy: int):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        
    def __str__(self):
        return (f"[ {self.get_name()}, "
                f"({self.startx}, {self.starty})-"
                f"({self.endx}, {self.endy}) ]")
                
    @abstractmethod
    def get_name(self) -> str:
        """Get the name of this shape"""
        pass
        
    @abstractmethod
    def draw(self):
        """Draw this shape"""
        pass
