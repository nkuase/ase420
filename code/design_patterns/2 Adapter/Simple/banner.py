class Banner:
  def __init__(self, string: str):
      self._string = string
  
  def show_with_paren(self):
      print(f"({self._string})")
  
  def show_with_aster(self):
      print(f"*{self._string}*")
  
  def __str__(self) -> str:
    return f"Banner('{self._string}')"
