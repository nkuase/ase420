"""
Abstract Factory Pattern - Abstract Factory
This class defines the interface for creating families of related objects.
"""

from abc import ABC, abstractmethod
from factory.link import Link
from factory.tray import Tray
from factory.page import Page
import importlib


class Factory(ABC):
    """
    Abstract factory class that defines the interface for creating
    families of related HTML components.
    """
    
    @staticmethod
    def get_factory(classname: str) -> 'Factory':
        """
        Factory method to create a concrete factory instance.
        Uses dynamic import to load the specified factory class.
        
        Args:
            classname (str): Full module path to the factory class
                           (e.g., 'listfactory.list_factory.ListFactory')
        
        Returns:
            Factory: An instance of the requested factory
        """
        try:
            # Split the classname to get module and class name
            module_path, class_name = classname.rsplit('.', 1)
            
            # Import the module and get the class
            module = importlib.import_module(module_path)
            factory_class = getattr(module, class_name)
            
            # Create and return an instance
            return factory_class()
            
        except (ImportError, AttributeError) as e:
            print(f"Class '{classname}' was not found: {e}")
            return None
        except Exception as e:
            print(f"Error creating factory: {e}")
            return None
    
    @abstractmethod
    def create_link(self, caption: str, url: str) -> Link:
        """
        Create a link object.
        
        Args:
            caption (str): The text to display
            url (str): The URL to link to
            
        Returns:
            Link: A concrete link object
        """
        pass
    
    @abstractmethod
    def create_tray(self, caption: str) -> Tray:
        """
        Create a tray object.
        
        Args:
            caption (str): The title for the tray
            
        Returns:
            Tray: A concrete tray object
        """
        pass
    
    @abstractmethod
    def create_page(self, title: str, author: str) -> Page:
        """
        Create a page object.
        
        Args:
            title (str): The title of the page
            author (str): The author of the page
            
        Returns:
            Page: A concrete page object
        """
        pass
