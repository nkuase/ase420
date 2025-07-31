from book import Book
from book_shelf_iterator import BookShelfIterator

class BookShelf:
  def __init__(self, max_size: int):
    self._books: List[Book] = [None] * max_size  # Fixed-size array like Java
    self._last = 0  # Index of the next available position
    self._max_size = max_size
  
  def get_book_at(self, index):
    if 0 <= index < self._last:
      return self._books[index]
    else:
      raise IndexError(f"Index {index} is out of bounds")
  
  def append_book(self, book: Book):
    if self._last >= self._max_size:
      raise ValueError("BookShelf is full, cannot add more books")
      
    self._books[self._last] = book
    self._last += 1
  
  def iterator(self):
    return BookShelfIterator(self)
  
  def get_length(self):
    return self._last
  
  def __str__(self):
    book_names = [book.get_name() for book in self._books[:self._last]]
    return f"BookShelf with {self._last} books: {book_names}"
