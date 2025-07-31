# Pull Up Constructor Body

# Before
## Your subclasses have constructors with code that’s mostly identical.
class Employee1(object):
  def __init__(self): pass
class Manager1(Employee1):
  def __init__(self, name, id, grade):
    self.name = name
    self.id = id
    self.grade = grade
  def __str__(self): return f"{self.name}:{self.id}:{self.grade}"
  
# After
## Each print method should have a single responsibility, so we make print_details(). 
class Employee2(object):
  def __init__(self, name, id):
    self.name = name
    self.id = id
class Manager2(Employee2):
  def __init__(self, name, id, grade):
    super().__init__(name, id)
    self.grade = grade
  def __str__(self): return f"{self.name}:{self.id}:{self.grade}"    
  
if __name__ == "__main__":
  print("<Before>")
  print(Manager1("J", 10, "A"))
  print("<After>")
  print(Manager2("J", 10, "A"))
