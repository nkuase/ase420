from abc import ABC, abstractmethod

class AbstractIterator(ABC):
    @abstractmethod
    def next(self): pass
    @abstractmethod
    def has_next(self): pass