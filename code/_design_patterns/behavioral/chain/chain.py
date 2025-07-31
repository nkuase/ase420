# Interface
class Handler(object):
  def set_next(self, handler): pass
  def handle(self, request): pass

# Implementations  
class BaseHandler(Handler):
  def __init__(self): self.next = None
  def set_next(self, handler):
    self.next = handler
  def handle(self, request):
    if self.next is not None:
      self.next.handle(request)
    else: # no next handler
      print(f"Base handler is processing {request}")
      
class HandlerA(BaseHandler):
  def set_next(self, handler):
    self.next = handler
  def handle(self, request):
    if self.can_handle(request):
      print("HandleA can handle it")
    else:
      print("Hand over to the next handler")
      self.next.handle(request)  
  def can_handle(self, request):
    if request.startswith("A"): return True
    else: return False
    
class HandlerB(BaseHandler):
  def set_next(self, handler):
    self.next = handler
  def handle(self, request):
    if self.can_handle(request):
      print(f"HandleB can handle {request}")
    else:
      print("Hand over to the next handler")
      self.next.handle(request)  
  def can_handle(self, request):
    if request.startswith("B"): return True
    else: return False  

# Driver

h = BaseHandler()    
h.handle("Process B")

h1 = HandlerA()    
h2 = HandlerB()

h.set_next(h1)
h1.set_next(h2)

h.handle("A - process C")
h.handle("B - process D")