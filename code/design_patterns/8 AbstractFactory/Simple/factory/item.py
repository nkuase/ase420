from abc import ABC, abstractmethod


class Item(ABC):
  
  def __init__(self, caption):
    self.caption = caption
  
  @abstractmethod
  def make_html(self):
    pass
