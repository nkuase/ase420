# Decompose Conditional
from datetime import date

class Date(object):
  def __init__(self, month, day): 
    self.month = month
    self.day = day
  def before(self, date):
    return True # compute date logic
  def after(self, date):
    return True
    
winter_rate = 1
winter_service_charge = 5
summer_rate = 2
# Before
## You have a complex conditional (if-then / else or switch)
def f1(quantity):
  date = Date(8,2)
  if date.before(Date(7,1)) or date.after(Date(9,1)):
    charge = quantity * winter_rate + winter_service_charge;
  else:
    charge = quantity * summer_rate;
  return charge
      
# After
## Decompose the complicated parts of the conditional into separate methods: the condition, then and else .
def is_summer(date):
  return False # logic needed something like date > Date(7, 1) and date < Date(9, 1)
def summer_charge(quantity):
  return quantity * summer_rate;
def winter_charge(quantity):
  return quantity * winter_rate + winter_service_charge;
def f2(quantity):
  if is_summer(Date(8,2)): 
    charge = summer_charge(quantity)
  else:
    charge = winter_charge(quantity)
  return charge
  
if __name__ == "__main__":
  print("<Before>")
  print(f1(14))
  print("<After>")
  print(f2(14))
