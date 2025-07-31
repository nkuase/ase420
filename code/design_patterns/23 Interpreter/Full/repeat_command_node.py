"""
Interpreter Pattern - Repeat Command Node
This node represents repeat commands that execute a command list multiple times.
Grammar: <repeat command> ::= repeat <number> <command list>
"""

from typing import TYPE_CHECKING
from node import Node

if TYPE_CHECKING:
    from context import Context


class RepeatCommandNode(Node):
    """
    Concrete node that represents repeat commands.
    A repeat command executes a command list a specified number of times.
    """
    
    def __init__(self):
        """Initialize the repeat command node."""
        self.number: int = 0
        self.command_list_node: Node = None
    
    def parse(self, context: 'Context'):
        """
        Parse a repeat command: 'repeat' <number> <command list>
        
        Args:
            context (Context): The parsing context
        """
        from command_list_node import CommandListNode
        
        context.skip_token("repeat")
        self.number = context.current_number()
        context.next_token()
        self.command_list_node = CommandListNode()
        self.command_list_node.parse(context)
    
    def get_number(self) -> int:
        """
        Get the repeat count.
        
        Returns:
            int: Number of times to repeat the command list
        """
        return self.number
    
    def get_command_list(self) -> Node:
        """
        Get the command list to be repeated.
        
        Returns:
            Node: The command list node
        """
        return self.command_list_node
    
    def __str__(self) -> str:
        """String representation of the repeat command node."""
        return f"[repeat {self.number} {self.command_list_node}]"
