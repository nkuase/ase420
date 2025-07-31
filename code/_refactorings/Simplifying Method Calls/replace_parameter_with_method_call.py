# Replace Parameter with Method Call

# Before
## Calling a query method and passing its results as the parameters of another method, while that method could call the query directly.
def get_seasonal_discount():
  return 10.5
def discounted_price(base_price, season_discount, fees):
  return base_price * season_discount + fees
def get_fees(): return 200
def f1(quantity, itemPrice):
  base_price = quantity * itemPrice;
  season_discount = get_seasonal_discount();
  fees = get_fees();
  final_price = discounted_price(base_price, season_discount, fees)
  return final_price
        
# After
## Instead of passing the value through a parameter, try placing a query call inside the method body.
def discounted_price2(base_price):
  season_discount = get_seasonal_discount();
  fees = get_fees();
  return base_price * season_discount + fees 
def f2(quantity, itemPrice):
  base_price = quantity * itemPrice
  final_price = discounted_price2(base_price);
  return final_price
  
if __name__ == "__main__":
  print("<Before>")
  print(f1(100, 20))
  print("<After>")
  print(f2(100, 20))
