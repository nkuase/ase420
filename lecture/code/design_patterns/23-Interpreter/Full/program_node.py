"""
Interpreter Pattern - Program Node
This node represents the top-level program grammar rule.
Grammar: <program> ::= program <command list>
"""

from typing import TYPE_CHECKING
from node import Node

if TYPE_CHECKING:
    from context import Context


class ProgramNode(Node):
    """
    Concrete node that represents a complete program.
    A program starts with the keyword 'program' followed by a command list.
    """
    
    def __init__(self):
        """Initialize the program node."""
        self.command_list_node: Node = None
    
    def parse(self, context: 'Context'):
        """
        Parse a program: 'program' <command list>
        
        Args:
            context (Context): The parsing context
        """
        from command_list_node import CommandListNode
        
        context.skip_token("program")
        self.command_list_node = CommandListNode()
        self.command_list_node.parse(context)
    
    def __str__(self) -> str:
        """String representation of the program node."""
        return f"[program {self.command_list_node}]"
