from node import Node

class ProgramNode(Node):
  def __init__(self):
    self.command_list_node = None
  
  def parse(self, context):
    from command_list_node import CommandListNode
    
    context.skip_token("program")
    self.command_list_node = CommandListNode()
    self.command_list_node.parse(context)
  
  def __str__(self):
    return f"[program {self.command_list_node}]"
