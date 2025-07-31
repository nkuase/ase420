from abc import ABC, abstractmethod

class Node(ABC):
  @abstractmethod
  def parse(self, context):
    pass
  
  @abstractmethod
  def __str__(self):
    pass
