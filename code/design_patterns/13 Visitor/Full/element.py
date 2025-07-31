"""
Visitor Pattern - Element Interface
This interface defines the accept method that elements must implement
to allow visitors to operate on them.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from visitor import Visitor


class Element(ABC):
    """
    Abstract interface for elements that can be visited.
    Elements must implement the accept method to allow visitors to operate on them.
    """
    
    @abstractmethod
    def accept(self, visitor: 'Visitor'):
        """
        Accept a visitor and allow it to operate on this element.
        
        Args:
            visitor (Visitor): The visitor that will operate on this element
        """
        pass
