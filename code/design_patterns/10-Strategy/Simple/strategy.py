from abc import ABC, abstractmethod
from hand import Hand


class Strategy(ABC):
  
  @abstractmethod
  def next_hand(self):
    pass
  
  @abstractmethod
  def study(self, win):
    pass
