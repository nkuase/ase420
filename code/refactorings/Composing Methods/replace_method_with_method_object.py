# Replace Method with Method Object
quantity = 100
itemPrice = 10

# Before
class Order1(object):
  def get_price(self):
    primary_base_price = 32
    secondary_base_price = 44
    tertiary_base_price = 100
    # long computation
    return primary_base_price * secondary_base_price / tertiary_base_price
    
# After
## You have a long method in which the local variables are so intertwined that you can’t apply Extract Method.
class Order2(object):
  def get_price(self):
    return PriceCalculator().compute()

class PriceCalculator(object):
  def compute(self):
    primary_base_price = 32
    secondary_base_price = 44
    tertiary_base_price = 100
    # long computation
    return primary_base_price * secondary_base_price / tertiary_base_price
    
if __name__ == "__main__":
  print(Order1().get_price())    
  print(Order2().get_price())