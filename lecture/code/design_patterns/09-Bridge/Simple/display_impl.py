from abc import ABC, abstractmethod


class DisplayImpl(ABC):
  
  @abstractmethod
  def raw_open(self):
    pass
  
  @abstractmethod
  def raw_print(self):
    pass
  
  @abstractmethod
  def raw_close(self):
    pass
