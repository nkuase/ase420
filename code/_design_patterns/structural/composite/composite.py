# Interface
class Graphic(object):
  def draw(self): pass

# Implementations  
class Leaf(Component):
  def __init__(self, x, y):
    self.x = x; self.y = y
  def draw(self):
    print(f"Dot@{self.x}:{self.y}")
    
class Composite(Component):
  def __init__(self):
    self._children = []
  def add(self, child):
    self._children.append(child)
  def draw(self):
    print(f"CompoundGraphic>> len({len(self._children)})")
    for i in self._children:
      i.draw()
    print(">>CompoundGraphic")

# Driver
# [[leaf, leaf], leaf, leaf]
cg0 = Composite()    
cg0.add(Leaf(10, 20))
cg0.add(Leaf(0,10))

cg = Composite()
cg.add(cg0)
cg.add(Leaf(30, 40))
cg.add(Leaf(10, 20))
cg.draw()
