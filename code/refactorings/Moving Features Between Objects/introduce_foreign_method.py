from datetime import date

# Utility class (in the 3rd party library)
class Date(object):
  def __init__(self, year = 0, month = 0, day = 0):
    self.year = year
    self.month = month
    self.day = day
  def get_today(self):
    today = date.today()
    return Date(today.year, today.month, today.day)
  def __str__(self): return f"{self.year}/{self.month}/{self.day}"

# Before
## A utility class doesn’t contain the method that you need and you can’t add the method to the class.
class Report1(object):
  def send_report(self):
    # we get today from Date() object
    today = Date().get_today()
    nextday = Date(today.year, today.month, today.day + 1) # <- This needs refactoring as I need to have the method to get the next day
    print(nextday)
  
# After
## Add the method to a client class and pass an object of the utility class to it as an argument.
class Report2(object):
  def send_report(self):
    today = Date().get_today()
    nextday = self.get_next_day(today)
    
  def get_next_day(self, today):
    # The Date object is given, and we use the method to make the next day
    nextday = Date(today.year, today.month, today.day + 1)
    print(nextday)
  
if __name__ == "__main__":
  print("<Before>")
  Report1().send_report()
  print("<After>")
  Report2().send_report()
