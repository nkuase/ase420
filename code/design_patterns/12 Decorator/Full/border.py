"""
Border abstract class for Decorator Pattern Example

This abstract class represents the base decorator in the Decorator pattern.
It maintains a reference to a Display object and extends the Display interface.

This is the "Decorator" in the Decorator pattern.
"""

from abc import ABC
from display import Display


class Border(Display, ABC):
    """
    Abstract base class for all border decorators.
    
    This class serves as the base for all concrete decorators.
    It maintains a reference to the component being decorated
    and implements the same interface as the component.
    """
    
    def __init__(self, display: Display):
        """
        Initialize the border decorator with a display component.
        
        Args:
            display (Display): The component to be decorated
            
        Raises:
            TypeError: If display is not a Display instance
        """
        if not isinstance(display, Display):
            raise TypeError("Border can only decorate Display objects")
        
        self._display = display
    
    def get_wrapped_display(self) -> Display:
        """
        Get the wrapped display component.
        
        This method allows access to the decorated component,
        which can be useful for debugging or introspection.
        
        Returns:
            Display: The wrapped display component
        """
        return self._display
    
    def unwrap(self) -> Display:
        """
        Get the innermost display component by unwrapping all decorators.
        
        This method recursively unwraps decorators until it finds
        the original component.
        
        Returns:
            Display: The innermost display component
        """
        current = self._display
        while isinstance(current, Border):
            current = current._display
        return current
    
    def get_decoration_depth(self) -> int:
        """
        Get the depth of decoration (how many decorators are stacked).
        
        Returns:
            int: The number of decorator layers
        """
        depth = 1  # This decorator
        if isinstance(self._display, Border):
            depth += self._display.get_decoration_depth()
        return depth
    
    def __str__(self) -> str:
        """
        String representation showing decorator information.
        
        Returns:
            str: The decorated display content
        """
        return self.get_all_text()
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation showing decoration structure.
        
        Returns:
            str: Representation showing decorator hierarchy
        """
        return f"{self.__class__.__name__}({repr(self._display)})"
