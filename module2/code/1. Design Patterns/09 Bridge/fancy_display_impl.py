from display_impl import DisplayImpl


class FancyDisplayImpl(DisplayImpl):
  
  def __init__(self, string):
    self.string = string
    self.width = len(string)
  
  def raw_open(self):
    self._print_line()
  
  def raw_print(self):
    print(f"|^^{self.string}^^|")
  
  def raw_close(self):
    self._print_line()
  
  def _print_line(self):
    line = "+" + "-" * (self.width + 4) + "+"
    print(line)
