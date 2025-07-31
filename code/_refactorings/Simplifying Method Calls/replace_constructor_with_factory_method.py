# Replace Constructor with Factory Method

# Before
## You have a complex constructor that does something more than just setting parameter values in object fields.
class Employee1(object):
  def __init__(self, type):
    self.type = type
        
# After
## Create a factory method and use it to replace constructor calls.
class Employee2(object):
  def __init__(self, type):
    self.type = type  
  def create(type):
    e = Employee2(type)
    # Do some other work 
    return e
  
if __name__ == "__main__":
  print("<Before>")
  print(Employee1("a"))
  print("<After>")
  print(Employee2.create("a"))
