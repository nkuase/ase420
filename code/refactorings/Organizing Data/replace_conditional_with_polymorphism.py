# Replace Conditional with Polymorphism

# Before
## You have a conditional that performs various actions depending on object type or properties.

class Bird1(object):
  def __init__(self, type):
    self.type = type
    self.number_of_coconuts = 10
  def get_load_factor(self): return 10
  def get_base_speed(self): return 100
  def get_speed(self):
    if self.type == "EUROPEAN": return self.get_base_speed()
    elif self.type == "AFRICAN": 
      return self.get_base_speed() - self.get_load_factor() * self.number_of_coconuts
    elif self.type == "NORWEGIAN":
      return self.get_load_factor()*1.6
    raise Exception("The type is wrong")

      
# After
## Create subclasses matching the branches of the conditional.
class Bird2(object):
  def __init__(self):
    self.number_of_coconuts = 10
  def get_load_factor(self): return 10
  def get_base_speed(self): return 100    
class EuropeanBird(Bird2):  
  def get_speed(self):
    return self.get_base_speed()
class AfricanBird(Bird2):
  def get_speed(self):
    return self.get_base_speed() - self.get_load_factor() * self.number_of_coconuts
class NorwegianBird(Bird2):
  def get_speed(self):
    return self.get_load_factor()*1.6

if __name__ == "__main__":
  print("<Before>")
  print(Bird1("NORWEGIAN").get_speed())
  print("<After>")
  print(NorwegianBird().get_speed())
