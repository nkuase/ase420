number_of_late_deliveries = 10

# Before
class PizzaDelivery1(object):
  def get_rating(self):
    return 2 if self.more_than_five_deliveries() else 1
  def more_than_five_deliveries(self):
    return number_of_late_deliveries > 5
  
# After
## We don't need more_than_five_deliveries() method that does only one simple responsibility
class PizzaDelivery2(object):
  def get_rating(self):
    return 2 if number_of_late_deliveries > 5 else 1
  
if __name__ == "__main__":
  print("<Before>")
  print(PizzaDelivery1().get_rating())
  print("<After>")
  print(PizzaDelivery2().get_rating())
