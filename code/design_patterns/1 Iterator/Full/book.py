"""
Book class for Iterator Pattern Example

This class represents a simple book with a name.
It demonstrates the basic element that will be stored in a collection.
"""


class Book:
    """A simple book class that holds a book's name."""
    
    def __init__(self, name: str):
        """
        Initialize a new Book with the given name.
        
        Args:
            name (str): The name/title of the book
        """
        self._name = name
    
    def get_name(self) -> str:
        """
        Get the name of the book.
        
        Returns:
            str: The name of the book
        """
        return self._name
    
    def __str__(self) -> str:
        """String representation of the book."""
        return f"Book: {self._name}"
    
    def __repr__(self) -> str:
        """Developer-friendly representation of the book."""
        return f"Book('{self._name}')"
