class TreeType(object):
  def __init__(self, name, color, texture):
    self.name = name
    self.color = color
    self.texture = texture
  def draw(self, canvas, x, y):
    print(f"Draw on {canvas} at {x}:{y}")
    
class TreeFactoryFlyweight(object):
  def __init__(self):
    self.cache = {}    

  def find(self, name, color, texture):
    string = f"{name}/{color}/{texture}"
    if string in self.cache.keys(): 
      return self.cache[string] # return stored object
    else: None  

  def get_tree_type(self, name, color, texture):
    ## Search Cache
    res = self.find(name, color, texture)
    if res is None:
      key = f"{name}/{color}/{texture}"
      print("Cache object")
      res = TreeType(name, color, texture)
      self.cache[key] = res
    else:
      print("Use cached object")
    return res

# Driver
tree_factory = TreeFactoryFlyweight()
p = tree_factory.get_tree_type('a','red','shade')
p.draw('canvas', 10, 20)
p = tree_factory.get_tree_type('a','red','shade')
p.draw('canvas2', 100, 200)