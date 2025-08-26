"""
Abstract Factory Pattern - Concrete Product (Div Link)
Implementation of Link using HTML div format.
"""

from factory.link import Link


class DivLink(Link):
    """
    Concrete implementation of Link for div-based formatting.
    Creates links as divs with CSS class for styling.
    """
    
    def __init__(self, caption: str, url: str):
        """
        Initialize the div link.
        
        Args:
            caption (str): The text to display
            url (str): The URL to link to
        """
        super().__init__(caption, url)
    
    def make_html(self) -> str:
        """
        Generate HTML representation as a div with LINK class.
        
        Returns:
            str: HTML string with <div> and <a> tags
        """
        return f'<div class="LINK"><a href="{self.url}">{self.caption}</a></div>\n'
