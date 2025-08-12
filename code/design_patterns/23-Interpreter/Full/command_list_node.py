"""
Interpreter Pattern - Command List Node
This node represents a list of commands ending with 'end'.
Grammar: <command list> ::= <command>* end
"""

from typing import List, TYPE_CHECKING
from node import Node
from parse_exception import ParseException

if TYPE_CHECKING:
    from context import Context


class CommandListNode(Node):
    """
    Concrete node that represents a list of commands.
    Commands are executed in sequence until 'end' is encountered.
    """
    
    def __init__(self):
        """Initialize the command list node."""
        self.command_nodes: List[Node] = []
    
    def parse(self, context: 'Context'):
        """
        Parse a command list: <command>* 'end'
        
        Args:
            context (Context): The parsing context
        """
        from command_node import CommandNode
        
        while True:
            current_token = context.current_token()
            
            if current_token is None:
                raise ParseException("Error: Missing 'end'")
            elif current_token == "end":
                context.skip_token("end")
                break
            else:
                command_node = CommandNode()
                command_node.parse(context)
                self.command_nodes.append(command_node)
    
    def get_commands(self) -> List[Node]:
        """
        Get the list of command nodes.
        
        Returns:
            List[Node]: List of parsed command nodes
        """
        return self.command_nodes.copy()
    
    def __str__(self) -> str:
        """String representation of the command list node."""
        if not self.command_nodes:
            return "[]"
        
        command_strings = [str(cmd) for cmd in self.command_nodes]
        return "[" + ", ".join(command_strings) + "]"
