"""
Interpreter Pattern - Primitive Command Node
This node represents basic commands in the mini language.
Grammar: <primitive command> ::= go | right | left
"""

from typing import TYPE_CHECKING
from node import Node
from parse_exception import ParseException

if TYPE_CHECKING:
    from context import Context


class PrimitiveCommandNode(Node):
    """
    Concrete node that represents primitive commands.
    Primitive commands are the basic building blocks: go, right, left.
    """
    
    # Valid primitive commands
    VALID_COMMANDS = {"go", "right", "left"}
    
    def __init__(self):
        """Initialize the primitive command node."""
        self.name: str = ""
    
    def parse(self, context: 'Context'):
        """
        Parse a primitive command: 'go' | 'right' | 'left'
        
        Args:
            context (Context): The parsing context
        """
        current_token = context.current_token()
        
        if current_token is None:
            raise ParseException("Error: Missing <primitive command>")
        elif current_token not in self.VALID_COMMANDS:
            raise ParseException(f"Error: Unknown <primitive command>: '{current_token}'")
        
        self.name = current_token
        context.skip_token(current_token)
    
    def get_name(self) -> str:
        """
        Get the name of the primitive command.
        
        Returns:
            str: The command name (go, right, or left)
        """
        return self.name
    
    def __str__(self) -> str:
        """String representation of the primitive command node."""
        return self.name
