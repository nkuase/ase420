from abstract_display import AbstractDisplay

class CharDisplay(AbstractDisplay):
  def __init__(self, ch: str):
    if len(ch) != 1:
      raise ValueError("CharDisplay requires exactly one character")
    self._ch = ch
  
  def open(self) -> None:
    print("<<", end="")
  
  def print(self) -> None:
    print(self._ch, end="")
  
  def close(self) -> None:
    print(">>")
  
  def get_character(self) -> str:
    return self._ch
  
  def __str__(self) -> str:
    return f"CharDisplay('{self._ch}')"
