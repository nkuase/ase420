"""
Interpreter Pattern - Parse Exception
Custom exception for parsing errors in the mini language.
"""


class ParseException(Exception):
    """
    Custom exception raised when parsing errors occur.
    Provides specific error messages for debugging the mini language.
    """
    
    def __init__(self, message: str):
        """
        Initialize the parse exception.
        
        Args:
            message (str): Error message describing the parsing problem
        """
        super().__init__(message)
        self.message = message
    
    def __str__(self) -> str:
        """String representation of the exception."""
        return f"ParseException: {self.message}"
