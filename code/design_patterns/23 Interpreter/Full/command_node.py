"""
Interpreter Pattern - Command Node
This node represents a single command which can be either a repeat command or primitive command.
Grammar: <command> ::= <repeat command> | <primitive command>
"""

from typing import TYPE_CHECKING
from node import Node

if TYPE_CHECKING:
    from context import Context


class CommandNode(Node):
    """
    Concrete node that represents a single command.
    A command can be either a repeat command or a primitive command.
    """
    
    def __init__(self):
        """Initialize the command node."""
        self.node: Node = None
    
    def parse(self, context: 'Context'):
        """
        Parse a command: <repeat command> | <primitive command>
        
        Args:
            context (Context): The parsing context
        """
        from repeat_command_node import RepeatCommandNode
        from primitive_command_node import PrimitiveCommandNode
        
        current_token = context.current_token()
        
        if current_token == "repeat":
            self.node = RepeatCommandNode()
            self.node.parse(context)
        else:
            self.node = PrimitiveCommandNode()
            self.node.parse(context)
    
    def get_node(self) -> Node:
        """
        Get the underlying node (repeat or primitive command).
        
        Returns:
            Node: The parsed command node
        """
        return self.node
    
    def __str__(self) -> str:
        """String representation of the command node."""
        return str(self.node)
