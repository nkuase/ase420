import time
from observer import Observer
from number_generator import NumberGenerator


class GraphObserver(Observer):
  
  def __init__(self, name = "GraphObserver", symbol = "*"):
    self._name = name
    self._symbol = symbol
  
  def update(self, generator):
    current_number = generator.get_number()
    graph = self._symbol * current_number
    print(f"{self._name}: {graph}")

  


