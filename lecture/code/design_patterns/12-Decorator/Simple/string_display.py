from display import Display


class StringDisplay(Display):
  
  def __init__(self, string):
    self._string = string
  
  def get_columns(self):
    return len(self._string)
  
  def get_rows(self):
    return 1
  
  def get_row_text(self, row):
    if row != 0:
      raise IndexError(f"StringDisplay only has 1 row, but row {row} was requested")
    return self._string
  
  def get_string(self):
    return self._string
  
  def set_string(self, string):
    self._string = string
  
  def __eq__(self, other):
    if not isinstance(other, StringDisplay):
      return False
    return self._string == other._string
  
  def __hash__(self):
    return hash(self._string)
