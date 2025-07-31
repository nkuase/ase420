"""
Prototype Pattern - Manager Class
This class manages prototype objects and creates copies of them.
"""

from typing import Dict
from framework.product import Product


class Manager:
    """
    Manager class that stores prototype objects and creates copies on demand.
    Acts as a registry of prototypes that can be cloned.
    """
    
    def __init__(self):
        """Initialize the manager with an empty showcase of prototypes."""
        self.showcase: Dict[str, Product] = {}
    
    def register(self, name: str, prototype: Product):
        """
        Register a prototype with a given name.
        
        Args:
            name (str): The name to associate with the prototype
            prototype (Product): The prototype object to register
        """
        self.showcase[name] = prototype
    
    def create(self, prototype_name: str) -> Product:
        """
        Create a copy of the prototype with the given name.
        
        Args:
            prototype_name (str): The name of the prototype to copy
            
        Returns:
            Product: A copy of the requested prototype, or None if not found
        """
        prototype = self.showcase.get(prototype_name)
        if prototype is None:
            print(f"Prototype '{prototype_name}' not found")
            return None
        
        return prototype.create_copy()
    
    def list_prototypes(self):
        """List all registered prototype names."""
        print("Registered prototypes:")
        for name in self.showcase.keys():
            print(f"  - {name}")
