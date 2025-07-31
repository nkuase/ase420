"""
IDCard class for Factory Method Pattern

This concrete class represents an ID card product.
It implements the Product interface defined in the framework.

This is a "Concrete Product" in the Factory Method pattern.
"""

from framework.product import Product


class IDCard(Product):
    """
    Concrete implementation of Product representing an ID card.
    
    This class demonstrates how concrete products implement the Product interface
    while providing their own specific functionality and behavior.
    """
    
    def __init__(self, owner: str):
        """
        Initialize an ID card for the specified owner.
        
        Args:
            owner (str): The name of the person who owns this ID card
        """
        print(f"{owner}의 카드를 만듭니다.")  # Korean: "Creating card for {owner}"
        self._owner = owner
    
    def use(self) -> None:
        """
        Implementation of the abstract use method from Product.
        
        Defines how this specific product (ID card) should be used.
        """
        print(f"{self}을 사용합니다.")  # Korean: "Using {self}"
    
    def get_owner(self) -> str:
        """
        Get the owner of this ID card.
        
        Returns:
            str: The name of the card owner
        """
        return self._owner
    
    def __str__(self) -> str:
        """
        String representation of the ID card.
        
        Returns:
            str: Formatted string showing the card and owner information
        """
        return f"[IDCard:{self._owner}]"
    
    def __repr__(self) -> str:
        """
        Developer-friendly representation of the ID card.
        
        Returns:
            str: Developer representation showing class and owner
        """
        return f"IDCard('{self._owner}')"
    
    def __eq__(self, other) -> bool:
        """
        Check equality with another IDCard.
        
        Args:
            other: Another object to compare with
            
        Returns:
            bool: True if both cards have the same owner, False otherwise
        """
        if not isinstance(other, IDCard):
            return False
        return self._owner == other._owner
    
    def __hash__(self) -> int:
        """
        Hash function for IDCard (useful for sets and dictionaries).
        
        Returns:
            int: Hash value based on the owner name
        """
        return hash(self._owner)
