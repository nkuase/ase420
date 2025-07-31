# Interfaces

class Strategy(object):
  def execute(self): pass
  
# Implementation
class BicycleStrategy(Strategy): 
  def execute(self): 
    print(f"Use bicycle - Time (2 hours): Cost ($0)")

class BusStrategy(Strategy):  
  def execute(self): 
    print(f"Use Bus - Time (1 hours): Cost ($5)")

class TaxiStrategy(Strategy):  
  def execute(self): 
    print(f"Use Taxi - Time (0.1 hours): Cost ($20)")
      
# Client
class Context(object):  
  def set_strategy(self, strategy):
    self.strategy = strategy
  def make_decision(self, max_money, max_time):
    if max_money < 3: # No money
      self.set_strategy(BicycleStrategy())
    elif max_time < 0.5:
      self.set_strategy(TaxiStrategy())
    else:
      self.set_strategy(BusStrategy())
    self.strategy.execute()  
  
# Driver
c = Context() # have some money, and have some time
c.make_decision(10, 2)
c.make_decision(0, 5) # Don't have money)
c.make_decision(100, 0.2) # Don't have time)