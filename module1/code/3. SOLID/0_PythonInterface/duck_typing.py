class Duck():
  def quack(self): print("Quack")
  
class Tiger():
  def quack(self): print("Wow")
    
def quack_checker(q): q.quack()
    
quack_checker(Duck())
quack_checker(Tiger())