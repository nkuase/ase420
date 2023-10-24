# https://www.python.org/download/releases/2.2/descrintro/#__new__
# It's unreasonably difficult to implement Singleton using Python
# So, this is just a reference, students don't have to understand how it works

class Singleton(object):
  # return a new instance of that class
  def __new__(cls, *args, **kwds):
    it = cls.__dict__.get("__it__")
    if it is not None:
        return it
    cls.__it__ = it = object.__new__(cls)
    it.init(*args, **kwds)
    return it
  def init(self, *args, **kwds): pass

class Hello(Singleton):
  def __init__(self, x, y):
    self.x = x; self.y = y

# Driver    
h1 = Hello(100, 200)
h2 = Hello(400, 500) # override the previous initalization

if (id(h1) == id(h2)):
  print("Same")
else:
  print("Different")