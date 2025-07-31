"""
Abstract Factory Pattern - Abstract Product (Page)
This class represents an abstract HTML page that can contain items.
"""

from typing import List
from factory.item import Item
from abc import ABC, abstractmethod


class Page(ABC):
    """
    Abstract page class that represents an HTML page.
    Can contain multiple items and generates complete HTML documents.
    """
    
    def __init__(self, title: str, author: str):
        """
        Initialize the page with title and author.
        
        Args:
            title (str): The title of the page
            author (str): The author of the page
        """
        self.title = title
        self.author = author
        self.content: List[Item] = []
    
    def add(self, item: Item):
        """
        Add an item to the page content.
        
        Args:
            item (Item): The item to add to the page
        """
        self.content.append(item)
    
    def output(self, filename: str):
        """
        Generate HTML and write to file.
        
        Args:
            filename (str): The name of the file to write
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.make_html())
            print(f"File '{filename}' has been created.")
        except IOError as e:
            print(f"Error writing file: {e}")
    
    @abstractmethod
    def make_html(self) -> str:
        """
        Generate HTML representation of the page.
        This method must be implemented by concrete subclasses.
        
        Returns:
            str: Complete HTML page as string
        """
        pass
