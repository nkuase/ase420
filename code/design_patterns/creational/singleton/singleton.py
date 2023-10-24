class Singleton: 
  __instance = None
  # static method declared here 
  @staticmethod
  def getInstance():
    if Singleton.__instance == None: 
      Singleton.__instance = Singleton()
    return Singleton.__instance
  def __init__(self):
    self.x = 0
    self.y = 0
    
x = Singleton.getInstance()
y = Singleton.getInstance()
print(id(x) == id(y))
x.x = 10
print(y.x)