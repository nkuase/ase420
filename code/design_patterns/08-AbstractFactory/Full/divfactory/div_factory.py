"""
Abstract Factory Pattern - Concrete Factory (Div Style)
This factory creates HTML components using HTML div tags.
"""

from factory.factory import Factory
from factory.link import Link
from factory.tray import Tray
from factory.page import Page
from divfactory.div_link import DivLink
from divfactory.div_tray import DivTray
from divfactory.div_page import DivPage


class DivFactory(Factory):
    """
    Concrete factory that creates HTML components using div-based formatting.
    Creates links, trays, and pages that use <div> HTML tags with CSS classes.
    """
    
    def create_link(self, caption: str, url: str) -> Link:
        """
        Create a div-style link.
        
        Args:
            caption (str): The text to display
            url (str): The URL to link to
            
        Returns:
            DivLink: A link formatted with div tags
        """
        return DivLink(caption, url)
    
    def create_tray(self, caption: str) -> Tray:
        """
        Create a div-style tray.
        
        Args:
            caption (str): The title for the tray
            
        Returns:
            DivTray: A tray formatted with div tags
        """
        return DivTray(caption)
    
    def create_page(self, title: str, author: str) -> Page:
        """
        Create a div-style page.
        
        Args:
            title (str): The title of the page
            author (str): The author of the page
            
        Returns:
            DivPage: A page with div-based formatting and CSS styling
        """
        return DivPage(title, author)
