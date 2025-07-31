"""
Chain of Responsibility Pattern - Concrete Handler (NoSupport)
This handler never resolves any troubles and always passes them on.
"""

from support import Support
from trouble import Trouble


class NoSupport(Support):
    """
    Concrete handler that doesn't resolve any troubles.
    Always passes requests to the next handler in the chain.
    """
    
    def __init__(self, name: str):
        """
        Initialize the no-support handler.
        
        Args:
            name (str): The name of this handler
        """
        super().__init__(name)
    
    def resolve(self, trouble: Trouble) -> bool:
        """
        This handler doesn't resolve any troubles.
        
        Args:
            trouble (Trouble): The trouble (ignored)
            
        Returns:
            bool: Always False - never resolves anything
        """
        return False
