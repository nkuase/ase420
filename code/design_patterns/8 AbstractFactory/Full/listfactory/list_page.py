"""
Abstract Factory Pattern - Concrete Product (List Page)
Implementation of Page using HTML list format.
"""

from factory.page import Page


class ListPage(Page):
    """
    Concrete implementation of Page for list-based formatting.
    Creates HTML pages with content organized as unordered lists.
    """
    
    def __init__(self, title: str, author: str):
        """
        Initialize the list page.
        
        Args:
            title (str): The title of the page
            author (str): The author of the page
        """
        super().__init__(title, author)
    
    def make_html(self) -> str:
        """
        Generate complete HTML page with list-based formatting.
        
        Returns:
            str: Complete HTML page as string
        """
        html_parts = [
            "<!DOCTYPE html>\n",
            f"<html><head><title>{self.title}</title></head>\n",
            "<body>\n",
            f"<h1>{self.title}</h1>\n",
            "<ul>\n"
        ]
        
        for item in self.content:
            html_parts.append(item.make_html())
        
        html_parts.extend([
            "</ul>\n",
            f"<hr><address>{self.author}</address>\n",
            "</body></html>\n"
        ])
        
        return "".join(html_parts)
