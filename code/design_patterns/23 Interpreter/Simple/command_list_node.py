from node import Node
from parse_exception import ParseException

class CommandListNode(Node):
  def __init__(self):
    self.command_nodes = []
  
  def parse(self, context):
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
  
  def get_commands(self):
    return self.command_nodes.copy()
  
  def __str__(self):
    if not self.command_nodes:
      return "[]"
    
    command_strings = [str(cmd) for cmd in self.command_nodes]
    return "[" + ", ".join(command_strings) + "]"
