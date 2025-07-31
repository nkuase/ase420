from border import Border
from display import Display


class FullBorder(Border):
  
  def __init__(self, display):
    super().__init__(display)
  
  def get_columns(self):
    return 1 + self._display.get_columns() + 1
  
  def get_rows(self):
    return 1 + self._display.get_rows() + 1
  
  def get_row_text(self, row):
    total_rows = self.get_rows()
    
    if row < 0 or row >= total_rows:
      raise IndexError(f"Row {row} is out of bounds (0-{total_rows-1})")
    
    if row == 0:
      return "+" + self._make_line('-', self._display.get_columns()) + "+"
    elif row == self._display.get_rows() + 1:
      return "+" + self._make_line('-', self._display.get_columns()) + "+"
    else:
      original_row = row - 1
      original_text = self._display.get_row_text(original_row)
      return "|" + original_text + "|"
  
  def _make_line(self, char, count):
    return char * count
  
  def get_inner_content_area(self):
    return (self._display.get_columns(), self._display.get_rows())
  
  def get_border_thickness(self):
    return 1
  
  def __repr__(self):
    return f"FullBorder({repr(self._display)})"


class CustomBorder(Border):
  
  def __init__(self, display, horizontal = '-', vertical = '|', corner = '+'):
    super().__init__(display)
    self._horizontal = horizontal
    self._vertical = vertical
    self._corner = corner
  
  def get_columns(self):
    return 1 + self._display.get_columns() + 1
  
  def get_rows(self):
    return 1 + self._display.get_rows() + 1
  
  def get_row_text(self, row):
    total_rows = self.get_rows()
    
    if row < 0 or row >= total_rows:
      raise IndexError(f"Row {row} is out of bounds (0-{total_rows-1})")
    
    if row == 0:
      return (self._corner + 
             self._horizontal * self._display.get_columns() + 
             self._corner)
    elif row == self._display.get_rows() + 1:
      return (self._corner + 
             self._horizontal * self._display.get_columns() + 
             self._corner)
    else:
      original_row = row - 1
      original_text = self._display.get_row_text(original_row)
      return self._vertical + original_text + self._vertical
  
  def __repr__(self):
    return (f"CustomBorder({repr(self._display)}, "
            f"h='{self._horizontal}', v='{self._vertical}', c='{self._corner}')")
