from abc import ABC, abstractmethod


class Product(ABC):
  
  @abstractmethod
  def use(self):
    pass
  
  def __str__(self):
    return f"{self.__class__.__name__} instance"
  
  def __repr__(self):
    return f"{self.__class__.__name__}()"
