from command.command import Command
from drawer.drawable import Drawable

class DrawCommand(Command):
  def __init__(self, drawable, x, y):
    self.drawable = drawable
    self.x = x
    self.y = y
  
  def execute(self):
    self.drawable.draw(self.x, self.y)
  
  def get_position(self):
    return (self.x, self.y)
  
  def __str__(self):
    return f"DrawCommand(x={self.x}, y={self.y})"
