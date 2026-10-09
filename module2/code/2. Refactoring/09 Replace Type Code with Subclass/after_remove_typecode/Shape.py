from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, startx: int, starty: int, endx: int, endy: int):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        
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
