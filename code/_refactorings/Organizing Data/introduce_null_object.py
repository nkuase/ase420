# Introduce Null Object

class Order(object):
  def __init__(self, customer = None): 
    self.customer = customer
class Customer(object):
  def get_plan(self):
    return Plan()
class Plan(object):
  def __str__(self): return "Plan"
      
# Before
## Since some methods return null instead of real objects, you have many checks for null in your code.
def basic_plan(): return "basic plan"  
def f1(order):
  if (order.customer is None):
    plan = basic_plan()
  else:
    plan = order.customer.get_plan()
  return plan
      
# After
## Instead of null , return a null object that exhibits the default behavior.
class NullPlan(object): 
  def __str__(self): return "Basic plan"
class NullCustomer(Customer):
  def is_null(self): return True
  def get_plan(self): return NullPlan()

def f2(order):
  customer = order.customer if order.customer is not None else NullCustomer()
  # Use Null-object as if it's normal subclass.
  plan = customer.get_plan()
  return plan
  
if __name__ == "__main__":
  print("<Before>")
  print(f1(Order(Customer())))
  print(f1(Order()))
  print("<After>")
  print(f2(Order(Customer())))
  print(f2(Order()))