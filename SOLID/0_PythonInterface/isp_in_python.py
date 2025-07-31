from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface (Product)"

    @abstractmethod
    def create_object():
        "An abstract interface method"
        
class Product(IProduct):
    def create_object(self):
        return "Object"
        
p = Product()
print(p.create_object())