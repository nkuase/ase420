"""
Abstract Factory Pattern - Abstract Product (Tray)
This class represents an abstract container that can hold multiple items.
"""

from typing import List
from factory.item import Item


class Tray(Item):
    """
    Abstract tray class that can contain multiple items.
    Acts as a composite that can hold links and other trays.
    """
    
    def __init__(self, caption: str):
        """
        Initialize the tray with a caption.
        
        Args:
            caption (str): The title/caption for this tray
        """
        super().__init__(caption)
        self.tray: List[Item] = []
    
    def add(self, item: Item):
        """
        Add an item to this tray.
        
        Args:
            item (Item): The item to add (can be Link or another Tray)
        """
        self.tray.append(item)
