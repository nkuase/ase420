"""
Abstract Factory Pattern - Abstract Product (Link)
This class represents an abstract link item.
"""

from factory.item import Item


class Link(Item):
    """
    Abstract link class that extends Item.
    Represents a hyperlink with a caption and URL.
    """
    
    def __init__(self, caption: str, url: str):
        """
        Initialize the link with caption and URL.
        
        Args:
            caption (str): The text to display for the link
            url (str): The URL the link points to
        """
        super().__init__(caption)
        self.url = url
