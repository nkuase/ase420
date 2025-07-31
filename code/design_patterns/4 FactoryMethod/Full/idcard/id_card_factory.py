"""
IDCardFactory class for Factory Method Pattern

This concrete factory class implements the Factory interface
to create IDCard products specifically.

This is a "Concrete Factory" (or "Concrete Creator") in the Factory Method pattern.
"""

from typing import List
from framework.factory import Factory
from framework.product import Product
from .id_card import IDCard


class IDCardFactory(Factory):
    """
    Concrete factory implementation for creating ID cards.
    
    This class implements the abstract factory methods to create
    and register ID card products specifically.
    """
    
    def __init__(self):
        """Initialize the ID card factory."""
        self._created_cards: List[IDCard] = []  # Keep track of created cards
    
    def create_product(self, owner: str) -> Product:
        """
        Implementation of the abstract factory method.
        
        Creates a new IDCard instance with the specified owner.
        This is the core "Factory Method" that creates the specific product type.
        
        Args:
            owner (str): The name of the card owner
            
        Returns:
            Product: A new IDCard instance
        """
        return IDCard(owner)
    
    def register_product(self, product: Product) -> None:
        """
        Implementation of the abstract registration method.
        
        Registers the created product by logging and storing it.
        This demonstrates how factories can track or manage created products.
        
        Args:
            product (Product): The product to register (should be an IDCard)
        """
        print(f"{product}을 등록했습니다.")  # Korean: "Registered {product}"
        
        # Store the created card for tracking purposes
        if isinstance(product, IDCard):
            self._created_cards.append(product)
    
    def get_created_cards(self) -> List[IDCard]:
        """
        Get a list of all ID cards created by this factory.
        
        This method demonstrates how concrete factories can provide
        additional functionality beyond the basic factory interface.
        
        Returns:
            List[IDCard]: List of all created ID cards
        """
        return self._created_cards.copy()  # Return a copy to prevent external modification
    
    def get_card_count(self) -> int:
        """
        Get the total number of cards created by this factory.
        
        Returns:
            int: Number of cards created
        """
        return len(self._created_cards)
    
    def find_card_by_owner(self, owner: str) -> IDCard:
        """
        Find an ID card by owner name.
        
        Args:
            owner (str): The name of the card owner to find
            
        Returns:
            IDCard: The card for the specified owner
            
        Raises:
            ValueError: If no card found for the specified owner
        """
        for card in self._created_cards:
            if card.get_owner() == owner:
                return card
        raise ValueError(f"No card found for owner: {owner}")
    
    def __str__(self) -> str:
        """String representation of the factory."""
        return f"IDCardFactory (created {len(self._created_cards)} cards)"
    
    def __repr__(self) -> str:
        """Developer-friendly representation of the factory."""
        return f"IDCardFactory(created_cards={len(self._created_cards)})"
