from abc import ABC
from display import Display


class Border(Display, ABC):
  
  def __init__(self, display):
    if not isinstance(display, Display):
      raise TypeError("Border can only decorate Display objects")
    
    self._display = display
  
  def get_wrapped_display(self):
    return self._display
  
  def unwrap(self):
    current = self._display
    while isinstance(current, Border):
      current = current._display
    return current
  
  def get_decoration_depth(self):
    depth = 1
    if isinstance(self._display, Border):
      depth += self._display.get_decoration_depth()
    return depth
  
  def __str__(self):
    return self.get_all_text()
  
  def __repr__(self):
    return f"{self.__class__.__name__}({repr(self._display)})"
