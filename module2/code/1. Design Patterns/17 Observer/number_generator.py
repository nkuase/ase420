from abc import ABC, abstractmethod
from observer import Observer


class NumberGenerator(ABC):
  
  def __init__(self):
    self._observers = []
  
  def add_observer(self, observer):
    if not isinstance(observer, Observer):
      raise TypeError("Observer must implement Observer interface")
    
    if observer not in self._observers:
      self._observers.append(observer)
  
  def delete_observer(self, observer):
    try:
      self._observers.remove(observer)
      return True
    except ValueError:
      return False
  
  def notify_observers(self):
    for observer in self._observers:
      observer.update(self)
  
  def get_observer_count(self):
    return len(self._observers)
  
  def clear_observers(self):
    self._observers.clear()
  
  @abstractmethod
  def get_number(self):
    pass
  
  @abstractmethod
  def execute(self):
    pass
  
