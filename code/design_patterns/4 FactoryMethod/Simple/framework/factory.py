from abc import ABC, abstractmethod
from .product import Product


class Factory(ABC):
  
  def create(self, owner):
    product = self.create_product(owner)
    
    self.register_product(product)
    
    return product
  
  @abstractmethod
  def create_product(self, owner):
    pass
  
  @abstractmethod
  def register_product(self, product):
    pass
  
  def __str__(self):
    return f"{self.__class__.__name__} factory"
  
  def __repr__(self):
    return f"{self.__class__.__name__}()"
