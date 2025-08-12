"""
Interpreter Pattern - Context Class
This class manages the tokenization and current state of parsing.
It provides methods for navigating through tokens and extracting values.
"""

from typing import List, Optional
from parse_exception import ParseException


class Context:
    """
    Context class that manages the input text tokenization and parsing state.
    Provides methods for token navigation and validation during parsing.
    """
    
    def __init__(self, text: str):
        """
        Initialize the context with input text.
        
        Args:
            text (str): The input text to be parsed
        """
        self.tokens: List[str] = text.split()
        self.index = 0
        self.last_token: Optional[str] = None
        self.next_token()
    
    def next_token(self) -> Optional[str]:
        """
        Move to the next token in the input.
        
        Returns:
            Optional[str]: The next token, or None if no more tokens
        """
        if self.index < len(self.tokens):
            self.last_token = self.tokens[self.index]
            self.index += 1
        else:
            self.last_token = None
        
        return self.last_token
    
    def current_token(self) -> Optional[str]:
        """
        Get the current token without advancing.
        
        Returns:
            Optional[str]: The current token, or None if no more tokens
        """
        return self.last_token
    
    def skip_token(self, expected_token: str):
        """
        Skip the current token if it matches the expected token.
        
        Args:
            expected_token (str): The token that is expected
            
        Raises:
            ParseException: If the current token doesn't match expected token
        """
        current = self.current_token()
        
        if current is None:
            raise ParseException(f"Error: '{expected_token}' is expected, but no more tokens found.")
        elif current != expected_token:
            raise ParseException(f"Error: '{expected_token}' is expected, but '{current}' is found.")
        
        self.next_token()
    
    def current_number(self) -> int:
        """
        Get the current token as a number.
        
        Returns:
            int: The current token converted to integer
            
        Raises:
            ParseException: If current token is not a valid number
        """
        current = self.current_token()
        
        if current is None:
            raise ParseException("Error: No more tokens.")
        
        try:
            return int(current)
        except ValueError as e:
            raise ParseException(f"Error: Cannot convert '{current}' to number: {e}")
    
    def has_more_tokens(self) -> bool:
        """
        Check if there are more tokens to process.
        
        Returns:
            bool: True if more tokens available, False otherwise
        """
        return self.current_token() is not None
    
    def get_remaining_tokens(self) -> List[str]:
        """
        Get all remaining tokens from current position.
        
        Returns:
            List[str]: List of remaining tokens
        """
        if self.index <= len(self.tokens):
            return self.tokens[self.index-1:]
        return []
    
    def __str__(self) -> str:
        """String representation of the context."""
        remaining = len(self.tokens) - self.index + 1
        return f"Context(current='{self.current_token()}', remaining={remaining})"
