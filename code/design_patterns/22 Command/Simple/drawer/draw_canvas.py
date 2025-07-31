import tkinter as tk
from drawer.drawable import Drawable
from command.macro_command import MacroCommand

class DrawCanvas(tk.Canvas, Drawable):
  def __init__(self, parent, width, height, history):
    super().__init__(parent, width=width, height=height, bg='white')
    self.width = width
    self.height = height
    self.history = history
    self.color = 'red'
    self.radius = 6
    
    self.bind('<B1-Motion>', self._on_mouse_drag)
    self.bind('<Button-1>', self._on_mouse_click)
    
    self.focus_set()
  
  def draw(self, x, y):
    x1 = x - self.radius
    y1 = y - self.radius
    x2 = x + self.radius
    y2 = y + self.radius
    
    self.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
  
  def _on_mouse_click(self, event):
    from drawer.draw_command import DrawCommand
    
    cmd = DrawCommand(self, event.x, event.y)
    self.history.append(cmd)
    cmd.execute()
  
  def _on_mouse_drag(self, event):
    from drawer.draw_command import DrawCommand
    
    cmd = DrawCommand(self, event.x, event.y)
    self.history.append(cmd)
    cmd.execute()
  
  def repaint(self):
    self.delete("all")
    self.history.execute()
  
  def set_color(self, color):
    self.color = color
  
  def set_radius(self, radius):
    self.radius = radius
  
  def get_drawing_info(self):
    return {
      'color': self.color,
      'radius': self.radius,
      'commands': self.history.size()
    }
