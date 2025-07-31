from node import Node
from parse_exception import ParseException

class PrimitiveCommandNode(Node):
  VALID_COMMANDS = {"go", "right", "left"}
  
  def __init__(self):
    self.name = ""
  
  def parse(self, context):
    current_token = context.current_token()
    
    if current_token is None:
      raise ParseException("Error: Missing <primitive command>")
    elif current_token not in self.VALID_COMMANDS:
      raise ParseException(f"Error: Unknown <primitive command>: '{current_token}'")
    
    self.name = current_token
    context.skip_token(current_token)
  
  def get_name(self):
    return self.name
  
  def __str__(self):
    return self.name
