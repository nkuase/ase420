# Interface
class Graphic(object):
  def move(self, x, y): pass
  def draw(self): pass
  
class Dot(Graphic):
  def __init__(self, x, y):
    self.x = x; self.y = y
  def __str__(self):
    return f"Dot@{self.x}:{self.y}"
  def move(self, x, y):
    self.x = x; self.y = y
    print(f"Move dot to {x} {y}")
  def draw(self):
    print(f"Draw a dot at {self.x} {self.y}")
    
class Circle(Dot):
  def __init__(self, x, y, radius):
    self.radius = radius
    super().__init__(x, y)
  def __str__(self):
    return f"Circle@[{self.radius}]{self.x}:{self.y}"     
  def draw(self):
    print(f"Draw a circle at {self.x} {self.y} {self.radius}")    

class CompoundGraphic(Graphic):
  def __init__(self):
    self._children = []
  def __str__(self):
    result = f"CompoundGraphic>> len({len(self._children)})\n"
    for i in self._children:
      result += f"{i}\n"
    result += ">>CompoundGraphic"
    return result
  def move(self, x, y): pass
  def draw(self): pass
  def add(self, child):
    self._children.append(child)
  def remove(self, child):
    self._children.remove(child)

# Driver
    
cg0 = CompoundGraphic()    
cg0.add(Dot(10, 20))
cg0.add(Circle(0,0,10))

cg = CompoundGraphic()
cg.add(cg0)
cg.add(Dot(30, 40))
cg.add(Dot(10, 20))
print(cg)
