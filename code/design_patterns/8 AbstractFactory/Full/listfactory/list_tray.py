"""
Abstract Factory Pattern - Concrete Product (List Tray)
Implementation of Tray using HTML list format.
"""

from factory.tray import Tray


class ListTray(Tray):
    """
    Concrete implementation of Tray for list-based formatting.
    Creates containers using nested HTML lists.
    """
    
    def __init__(self, caption: str):
        """
        Initialize the list tray.
        
        Args:
            caption (str): The title for this tray
        """
        super().__init__(caption)
    
    def make_html(self) -> str:
        """
        Generate HTML representation as a nested list.
        
        Returns:
            str: HTML string with nested <li> and <ul> tags
        """
        html_parts = ["<li>\n", self.caption, "\n<ul>\n"]
        
        for item in self.tray:
            html_parts.append(item.make_html())
        
        html_parts.extend(["</ul>\n", "</li>\n"])
        
        return "".join(html_parts)
