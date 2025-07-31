from abc import ABC, abstractmethod
from trouble import Trouble


class Support(ABC):
  
  def __init__(self, name):
    self.name = name
    self.next = None
  
  def set_next(self, next_support):
    self.next = next_support
    return next_support
  
  def support(self, trouble):
    if self.resolve(trouble):
      self.done(trouble)
    elif self.next is not None:
      self.next.support(trouble)
    else:
      self.fail(trouble)
  
  def __str__(self):
    return f"[{self.name}]"
  
  @abstractmethod
  def resolve(self, trouble):
    pass
  
  def done(self, trouble):
    print(f"{trouble} is resolved by {self}.")
  
  def fail(self, trouble):
    print(f"{trouble} cannot be resolved.")
