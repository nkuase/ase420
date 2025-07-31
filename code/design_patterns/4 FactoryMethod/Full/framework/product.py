"""
Product abstract class for Factory Method Pattern

This abstract class defines the interface that all concrete products must implement.
It represents the "Product" in the Factory Method pattern.

In the Factory Method pattern:
- This is the abstract Product class
- Concrete products inherit from this class
- The Factory creates instances of concrete products
"""

from abc import ABC, abstractmethod


class Product(ABC):
    """
    Abstract base class for all products created by factories.
    
    This class defines the common interface that all concrete products
    must implement. The Factory Method pattern uses this abstraction
    to work with products without knowing their concrete types.
    """
    
    @abstractmethod
    def use(self) -> None:
        """
        Abstract method that defines how the product should be used.
        
        Each concrete product must implement this method to define
        its specific usage behavior.
        """
        pass
    
    def __str__(self) -> str:
        """
        Default string representation of the product.
        
        Concrete products may override this method to provide
        more specific string representations.
        
        Returns:
            str: String representation of the product
        """
        return f"{self.__class__.__name__} instance"
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation of the product.
        
        Returns:
            str: Developer-friendly representation
        """
        return f"{self.__class__.__name__}()"
