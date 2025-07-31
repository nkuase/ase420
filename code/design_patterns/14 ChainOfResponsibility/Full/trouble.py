"""
Chain of Responsibility Pattern - Trouble Class
This class represents a trouble or problem that needs to be resolved.
"""


class Trouble:
    """
    Represents a trouble with a specific number.
    This is the request object that gets passed along the chain.
    """
    
    def __init__(self, number: int):
        """
        Initialize a trouble with a number.
        
        Args:
            number (int): The trouble number/identifier
        """
        self.number = number
    
    def get_number(self) -> int:
        """
        Get the trouble number.
        
        Returns:
            int: The trouble number
        """
        return self.number
    
    def __str__(self) -> str:
        """
        String representation of the trouble.
        
        Returns:
            str: String representation showing trouble number
        """
        return f"[Trouble {self.number}]"
