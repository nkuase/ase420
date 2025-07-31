from collections import deque
from command.command import Command

class MacroCommand(Command):
  def __init__(self):
    self.commands = deque()
  
  def execute(self):
    for cmd in self.commands:
      cmd.execute()
  
  def append(self, cmd):
    if cmd is self:
      raise ValueError("Cannot append macro command to itself - would cause infinite loop")
    
    self.commands.append(cmd)
  
  def undo(self):
    if self.commands:
      removed = self.commands.pop()
      print(f"Undid command: {type(removed).__name__}")
    else:
      print("No commands to undo")
  
  def clear(self):
    count = len(self.commands)
    self.commands.clear()
    print(f"Cleared {count} commands from history")
  
  def size(self):
    return len(self.commands)
  
  def is_empty(self):
    return len(self.commands) == 0
  
  def __str__(self):
    return f"MacroCommand(commands={len(self.commands)})"
