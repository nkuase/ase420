from datetime import date

# Before
## You use direct access to private fields inside a class.
class Ragen1(object):
  def __init__(self, low, high):
    self.low = low
    self.high = high
  def include(self, arg):
    return arg >= self.low and arg <= self.high
      
# After
## Create a getter and setter for the field, and use only them for accessing the field.
class Ragen2(object):
  def __init__(self, low, high):
    self._low = low
    self._high = high
  def get_low(self): return self._low
  def get_high(self): return self._high
  def include(self, arg):
    return arg >= self.get_low() and arg <= self.get_high()
  
if __name__ == "__main__":
  print("<Before>")
  print(Ragen1(10, 20).include(15))
  print("<After>")
  print(Ragen2(10, 20).include(15))
