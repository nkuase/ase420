# Replace Temp with Query
quantity = 100
itemPrice = 10

# Before
def replace_temp1():
  basePrice = quantity * itemPrice;
  if basePrice > 1000:
    return basePrice * 0.95;
  else:
    return basePrice * 0.98;

# After
## We make a query method basePrice() instead of a variable bestPrice.
def replace_temp2():
  def basePrice(): return quantity * itemPrice
  if basePrice() > 1000:
    return basePrice() * 0.95;
  else:
    return basePrice() * 0.98;  
    
if __name__ == "__main__":
  print(replace_temp1())    
  print(replace_temp2())