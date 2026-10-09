from abc import abstractmethod


class Drawable: # (metaclass=DrawableMetaClass):
    @abstractmethod
    def draw(self, x, y):
        """
        Draw a point or shape at the specified coordinates.
        
        Args:
            x (int): X-coordinate for the drawing operation
            y (int): Y-coordinate for the drawing operation
            
        Note:
            The specific implementation of what gets drawn (point, circle, etc.)
            is left to the concrete classes. This allows flexibility in how
            drawing operations are visualized.
        """
        pass
