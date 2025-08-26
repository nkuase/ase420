from framework.product import Product

class MessageBox(Product):
  def __init__(self, decochar):
    self.decochar = decochar
  
  def use(self, s):
    decolen = 1 + len(s) + 1
    
    print(self.decochar * decolen)
    
    print(f"{self.decochar}{s}{self.decochar}")
    
    print(self.decochar * decolen)
  
  def __str__(self):
    return f"MessageBox('{self.decochar}')"
