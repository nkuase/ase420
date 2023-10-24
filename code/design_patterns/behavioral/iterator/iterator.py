# Interface
class Iterator(object):
  def next(self): pass
  def has_next(self): pass
  
class Iterable(object): 
  def iterator(self): pass

# Book Iterator
class BookshelfIterator(Iterator):
  def __init__(self, bookshelf):
    self.bookshelf = bookshelf
    self.index = -1 # we always ge the next one, so the first index is -1
  def next(self): 
    if self.has_next():
      self.index += 1
      return self.bookshelf.get(self.index)
  def has_next(self): 
    if self.index < self.bookshelf.length() - 1: return True
    return False
  def reset_index(self):
    self.index = -1

# Book object
class Book(object): 
  def __init__(self, name):
    self.name = name
  def __str__(self):
    return self.name

# Iterable Collection    
class Bookshelf(Iterable):
  def __init__(self):
    self._books = []
  def length(self): 
    return len(self._books)
  def add(self, book):
    self._books.append(book)
  def get(self, index):
    return self._books[index]
  def iterator(self):
    return BookshelfIterator(self)
    
# Driver
bookshelf = Bookshelf()
bookshelf.add(Book('book1'))
bookshelf.add(Book('book2'))
bookshelf.add(Book('book3'))
iterator = bookshelf.iterator()

# Iterate only two methods has_more and get_next
while iterator.has_next():
  res = iterator.next()
  print(res)