from abc import ABC, abstractmethod

class Printable(ABC):
  @abstractmethod
  def set_printer_name(self, name):
    pass
  
  @abstractmethod
  def get_printer_name(self):
    pass
  
  @abstractmethod
  def print(self, string):
    pass
