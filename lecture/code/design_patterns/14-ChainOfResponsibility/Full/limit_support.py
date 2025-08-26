"""
Chain of Responsibility Pattern - Concrete Handler (LimitSupport)
This handler resolves troubles below a certain limit.
"""

from support import Support
from trouble import Trouble


class LimitSupport(Support):
    """
    Concrete handler that resolves troubles with numbers below a specified limit.
    """
    
    def __init__(self, name: str, limit: int):
        """
        Initialize the limit support handler.
        
        Args:
            name (str): The name of this handler
            limit (int): The upper limit for troubles this handler can resolve
        """
        super().__init__(name)
        self.limit = limit
    
    def resolve(self, trouble: Trouble) -> bool:
        """
        Resolve troubles with numbers below the limit.
        
        Args:
            trouble (Trouble): The trouble to resolve
            
        Returns:
            bool: True if trouble number is below limit, False otherwise
        """
        return trouble.get_number() < self.limit
