from abc import ABC, abstractmethod
from product import Product

class Factory(object):
  
  @abstractmethod
  def part1(self): pass
  @abstractmethod
  def part2(self): pass
  
  def create_product(self, owner):
      pass
