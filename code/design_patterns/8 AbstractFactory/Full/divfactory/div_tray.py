"""
Abstract Factory Pattern - Concrete Product (Div Tray)
Implementation of Tray using HTML div format.
"""

from factory.tray import Tray


class DivTray(Tray):
    """
    Concrete implementation of Tray for div-based formatting.
    Creates containers using divs with CSS class for styling.
    """
    
    def __init__(self, caption: str):
        """
        Initialize the div tray.
        
        Args:
            caption (str): The title for this tray
        """
        super().__init__(caption)
    
    def make_html(self) -> str:
        """
        Generate HTML representation as a div with TRAY class.
        
        Returns:
            str: HTML string with nested <div> tags
        """
        html_parts = [
            f"<p><b>{self.caption}</b></p>\n",
            '<div class="TRAY">'
        ]
        
        for item in self.tray:
            html_parts.append(item.make_html())
        
        html_parts.append("</div>\n")
        
        return "".join(html_parts)
