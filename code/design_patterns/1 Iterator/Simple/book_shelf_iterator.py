from book import Book

class BookShelfIterator:
  def __init__(self, book_shelf):
    self._book_shelf = book_shelf
    self._index = 0
  
  def next(self):
    if not self.has_next():
      raise StopIteration("No more books in the shelf")
      
    book = self._book_shelf.get_book_at(self._index)
    self._index += 1
    return book
  
  def has_next(self):
    return self._index < self._book_shelf.get_length()
