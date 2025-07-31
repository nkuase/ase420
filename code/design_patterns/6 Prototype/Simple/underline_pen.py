from framework.product import Product

class UnderlinePen(Product):
  def __init__(self, ulchar):
    self.ulchar = ulchar
  
  def use(self, s):
    ulen = len(s)
    print(s)
    print(self.ulchar * ulen)
  
  def __str__(self):
    return f"UnderlinePen('{self.ulchar}')"
