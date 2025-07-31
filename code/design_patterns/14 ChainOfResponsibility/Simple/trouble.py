class Trouble:
  
  def __init__(self, number):
    self.number = number
  
  def get_number(self):
    return self.number
  
  def __str__(self):
    return f"[Trouble {self.number}]"
