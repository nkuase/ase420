class Memento:
  
  def __init__(self, money):
    self._money = money
    self._fruits = []
  
  def get_money(self):
    return self._money
  
  def _add_fruit(self, fruit):
    self._fruits.append(fruit)
  
  def _get_fruits(self):
    return self._fruits.copy()
  
  def add_fruit(self, fruit):
    self._add_fruit(fruit)
  
  def get_fruits(self):
    return self._get_fruits()
