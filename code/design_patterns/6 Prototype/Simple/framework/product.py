import copy

class Product:
  def use(self, s):
    pass
  
  def create_copy(self):
    try:
      return copy.deepcopy(self)
    except Exception as e:
      print(f"Error creating copy: {e}")
      return None
