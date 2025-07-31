"""
Abstract Factory Pattern - Concrete Product (List Link)
Implementation of Link using HTML list item format.
"""

from factory.link import Link


class ListLink(Link):
    """
    Concrete implementation of Link for list-based formatting.
    Creates links as list items with <li> tags.
    """
    
    def __init__(self, caption: str, url: str):
        """
        Initialize the list link.
        
        Args:
            caption (str): The text to display
            url (str): The URL to link to
        """
        super().__init__(caption, url)
    
    def make_html(self) -> str:
        """
        Generate HTML representation as a list item.
        
        Returns:
            str: HTML string with <li> and <a> tags
        """
        return f'  <li><a href="{self.url}">{self.caption}</a></li>\n'
