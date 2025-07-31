"""
Interpreter Pattern - Abstract Node
This abstract class defines the interface for all nodes in the abstract syntax tree.
Each node represents a grammar rule in the mini language.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from context import Context


class Node(ABC):
    """
    Abstract base class for all nodes in the language syntax tree.
    Each concrete node implements a specific grammar rule.
    """
    
    @abstractmethod
    def parse(self, context: 'Context'):
        """
        Parse the input according to this node's grammar rule.
        
        Args:
            context (Context): The parsing context containing tokens
            
        Raises:
            ParseException: If parsing fails
        """
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """
        String representation of the parsed node.
        
        Returns:
            str: String representation of the node structure
        """
        pass
