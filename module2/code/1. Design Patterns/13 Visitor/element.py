from abc import ABC, abstractmethod


class Element(ABC):
  
  @abstractmethod
  def accept(self, visitor):
    pass
