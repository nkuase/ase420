from abc import ABC, abstractmethod


class Visitor(ABC):
  
  @abstractmethod
  def visit_file(self, file):
    pass
  
  @abstractmethod
  def visit_directory(self, directory):
    pass
