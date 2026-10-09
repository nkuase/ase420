class Book:
  def __init__(self, name: str):
    self._name = name
    
  def get_name(self):
    return self._name
    
  def __str__(self):
    return f"Book: {self._name}"
    