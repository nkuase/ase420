from node import Node

class RepeatCommandNode(Node):
  def __init__(self):
    self.number = 0
    self.command_list_node = None
  
  def parse(self, context):
    from command_list_node import CommandListNode
    
    context.skip_token("repeat")
    self.number = context.current_number()
    context.next_token()
    self.command_list_node = CommandListNode()
    self.command_list_node.parse(context)
  
  def get_number(self):
    return self.number
  
  def get_command_list(self):
    return self.command_list_node
  
  def __str__(self):
    return f"[repeat {self.number} {self.command_list_node}]"
