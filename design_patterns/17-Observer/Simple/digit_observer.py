import time
from observer import Observer
from number_generator import NumberGenerator


class DigitObserver(Observer):
  
  def __init__(self, name = "DigitObserver"):
    self._name = name
  
  def update(self, generator):
    current_number = generator.get_number()
    print(f"{self._name}: {current_number}")
    
  def get_name(self):
    return self._name
  


