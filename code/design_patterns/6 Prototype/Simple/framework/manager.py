from framework.product import Product

class Manager:
  def __init__(self):
    self.showcase = {}
  
  def register(self, name, prototype):
    self.showcase[name] = prototype
  
  def create(self, prototype_name):
    prototype = self.showcase.get(prototype_name)
    if prototype is None:
      print(f"Prototype '{prototype_name}' not found")
      return None
    
    return prototype.create_copy()
  
  def list_prototypes(self):
    print("Registered prototypes:")
    for name in self.showcase.keys():
      print(f"  - {name}")
