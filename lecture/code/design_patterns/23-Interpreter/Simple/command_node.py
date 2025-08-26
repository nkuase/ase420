from node import Node

class CommandNode(Node):
  def __init__(self):
    self.node = None
  
  def parse(self, context):
    from repeat_command_node import RepeatCommandNode
    from primitive_command_node import PrimitiveCommandNode
    
    current_token = context.current_token()
    
    if current_token == "repeat":
      self.node = RepeatCommandNode()
      self.node.parse(context)
    else:
      self.node = PrimitiveCommandNode()
      self.node.parse(context)
  
  def get_node(self):
    return self.node
  
  def __str__(self):
    return str(self.node)
