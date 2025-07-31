"""
Prototype Pattern - Product Interface
This interface defines the contract for objects that can be cloned.
"""

from abc import ABC, abstractmethod
import copy


class Product(ABC):
    """
    Abstract interface for products that support cloning.
    All concrete products must implement this interface to work with the Manager.
    """
    
    @abstractmethod
    def use(self, s: str):
        """
        Use the product with the given string.
        This method defines how the product operates on data.
        
        Args:
            s (str): The string to operate on
        """
        pass
    
    def create_copy(self) -> 'Product':
        """
        Create a copy of this product.
        Uses Python's copy.deepcopy() to clone the object.
        
        Returns:
            Product: A deep copy of this product
        """
        try:
            return copy.deepcopy(self)
        except Exception as e:
            print(f"Error creating copy: {e}")
            return None
