import random
import time
from number_generator import NumberGenerator


class RandomNumberGenerator(NumberGenerator):
  
  def __init__(self, seed = None):
    super().__init__()
    self._random = random.Random(seed)
    self._number = 0
  
  def get_number(self):
    return self._number
  
  def execute(self, count):
    print("Starting random number generation...")
    
    for i in range(count):
      self._number = self._random.randint(0, 49)
      self.notify_observers()
    print("Random number generation completed.")


