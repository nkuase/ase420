from banner import Banner
from print_interface import Print

class PrintBanner(Banner, Print):
  def __init__(self, string: str):
      super().__init__(string)
  
  def print_weak(self):
      self.show_with_paren()
  
  def print_strong(self):
      self.show_with_aster()
  
  def __str__(self) -> str:
    return f"PrintBanner adapting {super().__str__()}"
