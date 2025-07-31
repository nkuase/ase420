from abc import ABC, abstractmethod

class AbstractDisplay(ABC):
  @abstractmethod    
  def open(self): pass
  @abstractmethod
  def print(self): pass
  @abstractmethod
  def close(self): pass
  def display(self):
    self.open()
    for i in range(5):
        self.print()
    self.close()
  def __str__(self) -> str:
    return f"{self.__class__.__name__} (Template Method Pattern)"
