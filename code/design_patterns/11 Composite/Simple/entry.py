from abc import ABC, abstractmethod


class Entry(ABC):
  
  @abstractmethod
  def get_name(self):
    pass
  
  @abstractmethod
  def get_size(self):
    pass
  
  def print_list(self, prefix = ""):
    self._print_list(prefix)
  
  @abstractmethod
  def _print_list(self, prefix):
    pass
  
  def __str__(self):
    return f"{self.get_name()} ({self.get_size()})"
  
  def __repr__(self):
    return f"{self.__class__.__name__}('{self.get_name()}', size={self.get_size()})"
