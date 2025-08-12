from display import Display
from display_impl import DisplayImpl


class CountDisplay(Display):
  
  def __init__(self, impl):
    super().__init__(impl)
  
  def multi_display(self, times):
    self.open()
    for i in range(times):
      self.print()
    self.close()
