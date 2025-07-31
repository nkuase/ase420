# Preserve Whole Object

# Before
## You get several values from an object and then pass them as parameters to a method.
class TempRange(object):
  def get_low(self): return 10
  def get_high(self): return 20
class Plan1(object):
  def within_range(self, low, high): return f"{low}/{high}"

def f1(days_temp_range):
  low = days_temp_range.get_low()
  high = days_temp_range.get_high()
  plan_range = Plan1().within_range(low, high)
  return plan_range
        
# After
## Instead, try passing the whole object.
class Plan2(object):
  def within_range(self, temp_range): return f"{temp_range.get_low()}/{temp_range.get_high()}"
def f2(days_temp_range):
  plan_range = Plan2().within_range(days_temp_range)
  return plan_range
  
if __name__ == "__main__":
  print("<Before>")
  d = TempRange()
  print(f1(d))
  print("<After>")
  print(f2(d))
