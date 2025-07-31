from display_impl import DisplayImpl


class Display:
  
  def __init__(self, impl):
    self.impl = impl
  
  def open(self):
    self.impl.raw_open()
  
  def print(self):
    self.impl.raw_print()
  
  def close(self):
    self.impl.raw_close()
  
  def display(self):
    self.open()
    self.print()
    self.close()
