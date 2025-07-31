"""
BookShelf class for Iterator Pattern Example

This class represents a collection of books that can be iterated over.
It demonstrates how to implement the Iterable interface/protocol in Python
and provides both custom iterator and Python's built-in iteration support.
"""

from typing import Iterator, List
from book import Book
from book_shelf_iterator import BookShelfIterator


class BookShelf:
    """A collection of books that supports iteration."""
    
    def __init__(self, max_size: int):
        """
        Initialize a BookShelf with a maximum capacity.
        
        Args:
            max_size (int): Maximum number of books the shelf can hold
        """
        self._books: List[Book] = [None] * max_size  # Fixed-size array like Java
        self._last = 0  # Index of the next available position
        self._max_size = max_size
    
    def get_book_at(self, index: int) -> Book:
        """
        Get the book at the specified index.
        
        Args:
            index (int): The index of the book to retrieve
            
        Returns:
            Book: The book at the specified index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if 0 <= index < self._last:
            return self._books[index]
        else:
            raise IndexError(f"Index {index} is out of bounds")
    
    def append_book(self, book: Book) -> None:
        """
        Add a book to the shelf.
        
        Args:
            book (Book): The book to add to the shelf
            
        Raises:
            ValueError: If the shelf is already full
        """
        if self._last >= self._max_size:
            raise ValueError("BookShelf is full, cannot add more books")
        
        self._books[self._last] = book
        self._last += 1
    
    def get_length(self) -> int:
        """
        Get the current number of books on the shelf.
        
        Returns:
            int: The number of books currently on the shelf
        """
        return self._last
    
    def __iter__(self) -> Iterator[Book]:
        """
        Return an iterator for the BookShelf.
        This enables Python's for-loop support.
        
        Returns:
            Iterator[Book]: An iterator over the books
        """
        return BookShelfIterator(self)
    
    def iterator(self) -> BookShelfIterator:
        """
        Return a custom iterator (similar to Java's iterator() method).
        This method is provided for educational purposes to show
        explicit iterator creation as in the Java example.
        
        Returns:
            BookShelfIterator: A custom iterator for this BookShelf
        """
        return BookShelfIterator(self)
    
    def __len__(self) -> int:
        """Return the number of books (Pythonic way)."""
        return self._last
    
    def __str__(self) -> str:
        """String representation of the BookShelf."""
        book_names = [book.get_name() for book in self._books[:self._last]]
        return f"BookShelf with {self._last} books: {book_names}"
