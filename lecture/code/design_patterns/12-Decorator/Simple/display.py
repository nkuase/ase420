from abc import ABC, abstractmethod


class Display(ABC):
  
  @abstractmethod
  def get_columns(self):
    pass
  
  @abstractmethod
  def get_rows(self):
    pass
  
  @abstractmethod
  def get_row_text(self, row):
    pass
  
  def show(self):
    for i in range(self.get_rows()):
      print(self.get_row_text(i))
  
  def get_all_text(self):
    lines = []
    for i in range(self.get_rows()):
      lines.append(self.get_row_text(i))
    return '\n'.join(lines)
  
  def __str__(self):
    return self.get_all_text()
  
  def __repr__(self):
    return f"{self.__class__.__name__}({self.get_columns()}x{self.get_rows()})"
