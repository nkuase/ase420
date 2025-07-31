from abstract_display import AbstractDisplay

class StringDisplay(AbstractDisplay):
  def __init__(self, string: str):
    self._string = string
    self._width = len(string)
  
  def open(self):
    self._print_line()
  
  def print(self):
    print(f"|{self._string}|")
  
  def close(self):
    self._print_line()
  
  def _print_line(self):
    print("+", end="")
    for i in range(self._width):
      print("-", end="")
    print("+")
  
  def get_string(self):
    return self._string
  
  def get_width(self):
    return self._width
  
  def __str__(self):
    return f"StringDisplay('{self._string}')"
