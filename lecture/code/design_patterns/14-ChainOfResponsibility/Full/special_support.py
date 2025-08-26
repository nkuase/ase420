"""
Chain of Responsibility Pattern - Concrete Handler (SpecialSupport)
This handler resolves only one specific trouble number.
"""

from support import Support
from trouble import Trouble


class SpecialSupport(Support):
    """
    Concrete handler that resolves only troubles with a specific number.
    """
    
    def __init__(self, name: str, number: int):
        """
        Initialize the special support handler.
        
        Args:
            name (str): The name of this handler
            number (int): The specific trouble number this handler can resolve
        """
        super().__init__(name)
        self.number = number
    
    def resolve(self, trouble: Trouble) -> bool:
        """
        Resolve troubles only if they match the specific number.
        
        Args:
            trouble (Trouble): The trouble to resolve
            
        Returns:
            bool: True if trouble number matches the special number, False otherwise
        """
        return trouble.get_number() == self.number
