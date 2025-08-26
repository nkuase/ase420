"""
Abstract Factory Pattern - Concrete Product (Div Page)
Implementation of Page using HTML div format with CSS styling.
"""

from factory.page import Page


class DivPage(Page):
    """
    Concrete implementation of Page for div-based formatting.
    Creates HTML pages with CSS styling for div elements.
    """
    
    def __init__(self, title: str, author: str):
        """
        Initialize the div page.
        
        Args:
            title (str): The title of the page
            author (str): The author of the page
        """
        super().__init__(title, author)
    
    def make_html(self) -> str:
        """
        Generate complete HTML page with div-based formatting and CSS.
        
        Returns:
            str: Complete HTML page as string with embedded CSS
        """
        html_parts = [
            "<!DOCTYPE html>\n",
            f"<html><head><title>{self.title}</title><style>\n",
            "div.TRAY { padding:0.5em; margin-left:5em; border:1px solid black; }\n",
            "div.LINK { padding:0.5em; background-color: lightgray; }\n",
            "</style></head><body>\n",
            f"<h1>{self.title}</h1>\n"
        ]
        
        for item in self.content:
            html_parts.append(item.make_html())
        
        html_parts.extend([
            f"<hr><address>{self.author}</address>\n",
            "</body></html>\n"
        ])
        
        return "".join(html_parts)
