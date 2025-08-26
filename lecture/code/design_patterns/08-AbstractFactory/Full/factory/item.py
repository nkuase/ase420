"""
Abstract Factory Pattern - Abstract Product (Item)
This is the base class for all items that can be created by the factory.
"""

from abc import ABC, abstractmethod


class Item(ABC):
    """
    Abstract base class for all items in the HTML factory.
    Provides common functionality and interface for all items.
    """
    
    def __init__(self, caption: str):
        """
        Initialize the item with a caption.
        
        Args:
            caption (str): The caption/title for this item
        """
        self.caption = caption
    
    @abstractmethod
    def make_html(self) -> str:
        """
        Generate HTML representation of this item.
        This method must be implemented by concrete subclasses.
        
        Returns:
            str: HTML string representation of the item
        """
        pass
