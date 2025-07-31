"""
BookShelfIterator class for Iterator Pattern Example

This class implements the iterator functionality for BookShelf.
It demonstrates how to create a custom iterator that can traverse
through a collection of books sequentially.
"""

from typing import Iterator
from book import Book


class BookShelfIterator:
    """Iterator for BookShelf that allows sequential access to books."""
    
    def __init__(self, book_shelf):
        """
        Initialize the iterator with a BookShelf.
        
        Args:
            book_shelf: The BookShelf instance to iterate over
        """
        self._book_shelf = book_shelf
        self._index = 0
    
    def __iter__(self) -> Iterator[Book]:
        """Return the iterator object itself."""
        return self
    
    def __next__(self) -> Book:
        """
        Get the next book in the sequence.
        
        Returns:
            Book: The next book in the shelf
            
        Raises:
            StopIteration: When there are no more books to iterate
        """
        if not self.has_next():
            raise StopIteration("No more books in the shelf")
        
        book = self._book_shelf.get_book_at(self._index)
        self._index += 1
        return book
    
    def has_next(self) -> bool:
        """
        Check if there are more books to iterate.
        
        Returns:
            bool: True if there are more books, False otherwise
        """
        return self._index < self._book_shelf.get_length()
