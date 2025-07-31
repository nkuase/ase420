"""
Abstract Factory Pattern - Concrete Factory (List Style)
This factory creates HTML components using HTML list tags.
"""

from factory.factory import Factory
from factory.link import Link
from factory.tray import Tray
from factory.page import Page
from listfactory.list_link import ListLink
from listfactory.list_tray import ListTray
from listfactory.list_page import ListPage


class ListFactory(Factory):
    """
    Concrete factory that creates HTML components using list-based formatting.
    Creates links, trays, and pages that use <ul>, <li> HTML tags.
    """
    
    def create_link(self, caption: str, url: str) -> Link:
        """
        Create a list-style link.
        
        Args:
            caption (str): The text to display
            url (str): The URL to link to
            
        Returns:
            ListLink: A link formatted for list display
        """
        return ListLink(caption, url)
    
    def create_tray(self, caption: str) -> Tray:
        """
        Create a list-style tray.
        
        Args:
            caption (str): The title for the tray
            
        Returns:
            ListTray: A tray formatted as HTML list
        """
        return ListTray(caption)
    
    def create_page(self, title: str, author: str) -> Page:
        """
        Create a list-style page.
        
        Args:
            title (str): The title of the page
            author (str): The author of the page
            
        Returns:
            ListPage: A page with list-based formatting
        """
        return ListPage(title, author)
