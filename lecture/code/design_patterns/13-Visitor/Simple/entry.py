from abc import ABC, abstractmethod
from element import Element


class Entry(Element, ABC):
  
  @abstractmethod
  def get_name(self):
    pass
  
  @abstractmethod
  def get_size(self):
    pass
  
  def __str__(self):
    return f"{self.get_name()} ({self.get_size()})"
