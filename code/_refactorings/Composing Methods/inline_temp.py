# Inline Temp

class Order(object): 
  def basePrice(self): return 10000

# Before
def inline_temp1(order):
  basePrice = order.basePrice();
  return basePrice > 1000;
  
# After
## We don't need the temporary variable basePrice
def inline_temp2(order):
  return order.basePrice() > 1000

if __name__ == "__main__":  
  print(inline_temp1(Order()))  
  print(inline_temp2(Order()))
  