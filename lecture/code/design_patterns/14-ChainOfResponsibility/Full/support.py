"""
Chain of Responsibility Pattern - Abstract Handler (Support)
This abstract class defines the interface for handling requests in the chain.
"""

from abc import ABC, abstractmethod
from typing import Optional
from trouble import Trouble


class Support(ABC):
    """
    Abstract base class for support handlers in the chain of responsibility.
    Each handler can either resolve a trouble or pass it to the next handler.
    """
    
    def __init__(self, name: str):
        """
        Initialize the support handler with a name.
        
        Args:
            name (str): The name of this support handler
        """
        self.name = name
        self.next: Optional['Support'] = None
    
    def set_next(self, next_support: 'Support') -> 'Support':
        """
        Set the next handler in the chain.
        
        Args:
            next_support (Support): The next handler to pass requests to
            
        Returns:
            Support: The next handler (for method chaining)
        """
        self.next = next_support
        return next_support
    
    def support(self, trouble: Trouble):
        """
        Handle a trouble request. This implements the chain logic.
        
        Args:
            trouble (Trouble): The trouble to resolve
        """
        if self.resolve(trouble):
            self.done(trouble)
        elif self.next is not None:
            self.next.support(trouble)
        else:
            self.fail(trouble)
    
    def __str__(self) -> str:
        """
        String representation of the support handler.
        
        Returns:
            str: Handler name in brackets
        """
        return f"[{self.name}]"
    
    @abstractmethod
    def resolve(self, trouble: Trouble) -> bool:
        """
        Attempt to resolve the trouble.
        This method must be implemented by concrete handlers.
        
        Args:
            trouble (Trouble): The trouble to resolve
            
        Returns:
            bool: True if the trouble was resolved, False otherwise
        """
        pass
    
    def done(self, trouble: Trouble):
        """
        Called when the trouble is successfully resolved.
        
        Args:
            trouble (Trouble): The resolved trouble
        """
        print(f"{trouble} is resolved by {self}.")
    
    def fail(self, trouble: Trouble):
        """
        Called when no handler in the chain could resolve the trouble.
        
        Args:
            trouble (Trouble): The unresolved trouble
        """
        print(f"{trouble} cannot be resolved.")
