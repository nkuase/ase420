# interface
class Subscriber(object):  
  def update(filename): pass  
class Publisher(object):  
  def subscribe(self, event_type, listner):
    pass
  def unsubscribe(self, event_type, listner):
    pass
  def notify(self, event_type, data):
    pass  

# Implementation
class EventManager(Publisher):
  def __init__(self):
    self._listeners = []
    self.state = None
  def subscribe(self, listner):
    self._listeners.append(listner)
  def unsubscribe(self, listner):
    self._listeners.remove(listner)
  def notify(self):
    for listner in self._listeners:
      listner.update(self)
    
class ListnerA(Subscriber):
  def update(self, event_manager): 
    print(f"Listner A is notified a new state {event_manager.state}")  

class ListnerB(Subscriber):
  def update(self, event_manager): 
    print(f"Listner B is notified a new state {event_manager.state}")       
    
l_a = ListnerA()    
l_b = ListnerB()

m = EventManager()
m.subscribe(l_a); m.subscribe(l_b)
m.state = 1
m.notify()

print('\n<<Removing A in the subscriber list>>')
m.unsubscribe(l_a)
m.state = 2
m.notify()