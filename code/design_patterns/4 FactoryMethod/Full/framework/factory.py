"""
Factory abstract class for Factory Method Pattern

This abstract class defines the Factory Method pattern structure.
It contains the template method (create) and abstract factory methods
that concrete factories must implement.

In the Factory Method pattern:
- This is the abstract Factory (Creator) class
- Contains the factory method template
- Defines abstract methods that concrete factories implement
"""

from abc import ABC, abstractmethod
from .product import Product


class Factory(ABC):
    """
    Abstract factory class that defines the Factory Method pattern.
    
    This class implements the Template Method pattern within the Factory Method pattern:
    - create() is the template method that defines the creation process
    - createProduct() and registerProduct() are abstract methods that subclasses implement
    
    The factory method pattern lets subclasses decide which class to instantiate.
    """
    
    def create(self, owner: str) -> Product:
        """
        Template method that defines the product creation process.
        
        This method cannot be overridden (similar to Java's final method).
        It defines the algorithm for creating and registering products:
        1. Create the product using the factory method
        2. Register the product
        3. Return the product
        
        Args:
            owner (str): The owner information for the product
            
        Returns:
            Product: The created and registered product
        """
        # Step 1: Create the product (delegated to concrete factory)
        product = self.create_product(owner)
        
        # Step 2: Register the product (delegated to concrete factory)
        self.register_product(product)
        
        # Step 3: Return the created product
        return product
    
    @abstractmethod
    def create_product(self, owner: str) -> Product:
        """
        Abstract factory method for creating products.
        
        This is the core "Factory Method" that concrete factories must implement.
        Each concrete factory will create its specific type of product.
        
        Args:
            owner (str): The owner information for the product
            
        Returns:
            Product: The created product instance
        """
        pass
    
    @abstractmethod
    def register_product(self, product: Product) -> None:
        """
        Abstract method for registering created products.
        
        This method allows concrete factories to perform any necessary
        registration or logging of created products.
        
        Args:
            product (Product): The product to register
        """
        pass
    
    def __str__(self) -> str:
        """String representation of the factory."""
        return f"{self.__class__.__name__} factory"
    
    def __repr__(self) -> str:
        """Developer-friendly representation of the factory."""
        return f"{self.__class__.__name__}()"
