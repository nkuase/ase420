from abc import ABC, abstractmethod

# Product interface
class Product(ABC):
    @abstractmethod
    def use(self): pass