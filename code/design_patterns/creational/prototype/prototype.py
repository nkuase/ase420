import copy

# Interfaces
class Prototype(object):
  def clone(): pass
  
class Rectangle(Prototype):
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def clone(self): 
    return copy.deepcopy(self)

class Circle(Prototype):
  def __init__(self, radius):
    self.radius = radius
  def clone(self): 
    return copy.deepcopy(self)

# Driver    
r0 = Rectangle(10, 20)
r = r0.clone(); r.width = 1000
print(f"Width({r0.width}):Height({r0.height})")
print(f"Width({r.width}):Height({r.height})")

r0 = Circle(10)
r = r0.clone(); r.radius = 100
print(f"Radius({r0.radius})")
print(f"Radius({r.radius})")