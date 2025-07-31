# Encapsulate Field

# Before
## You have a public field.
class Person1(object):
  def __init__(self):
    self.name = None
      
# After
## Make the field private and create access methods for it.
class Person2(object):
  def __init__(self):
    self._name = None
  def get_name(self): return self._name
  def set_name(self, name): self._name = name

if __name__ == "__main__":
  print("<Before>")
  p = Person1(); p.name = "John"
  print(p.name)
  print("<After>")
  p = Person2(); p.set_name("John")
  print(p.get_name())
