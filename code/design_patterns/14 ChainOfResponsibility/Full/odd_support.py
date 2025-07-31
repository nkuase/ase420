"""
Chain of Responsibility Pattern - Concrete Handler (OddSupport)
This handler resolves troubles with odd numbers.
"""

from support import Support
from trouble import Trouble


class OddSupport(Support):
    """
    Concrete handler that resolves troubles with odd numbers only.
    """
    
    def __init__(self, name: str):
        """
        Initialize the odd support handler.
        
        Args:
            name (str): The name of this handler
        """
        super().__init__(name)
    
    def resolve(self, trouble: Trouble) -> bool:
        """
        Resolve troubles with odd numbers.
        
        Args:
            trouble (Trouble): The trouble to resolve
            
        Returns:
            bool: True if trouble number is odd, False otherwise
        """
        return trouble.get_number() % 2 == 1
