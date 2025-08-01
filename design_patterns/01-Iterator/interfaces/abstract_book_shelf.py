from abc import ABC, abstractmethod

class AbstractBookShelf(ABC):
    @abstractmethod
    def get_book_at(self, index): pass
    @abstractmethod
    def iterator(self): pass