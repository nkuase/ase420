from border import Border
from display import Display


class SideBorder(Border):
  
  def __init__(self, display, border_char = '|'):
    super().__init__(display)
    
    if len(border_char) != 1:
      raise ValueError("Border character must be exactly one character")
    
    self._border_char = border_char
  
  def get_columns(self):
    return 1 + self._display.get_columns() + 1
  
  def get_rows(self):
    return self._display.get_rows()
  
  def get_row_text(self, row):
    original_text = self._display.get_row_text(row)
    return self._border_char + original_text + self._border_char
  
  def get_border_char(self):
    return self._border_char
  
  def set_border_char(self, border_char):
    if len(border_char) != 1:
      raise ValueError("Border character must be exactly one character")
    self._border_char = border_char
  
  def __repr__(self):
    return f"SideBorder('{self._border_char}', {repr(self._display)})"
