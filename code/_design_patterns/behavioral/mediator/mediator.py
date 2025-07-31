# Interfaces
class Mediator(object):
  def notify(sender): pass
  
class Airplane(object):    
  def __init__(self, id): self.id = id
  def __str__(self): return self.id
  def operation(self, mediator): pass
  def receive(self, message): pass
  
# Implementations
class AirtrafficController(Mediator):  
  def __init__(self):
    self._airplanes = {}
  def __str__(self): return "AC1"
  def register(self, airplane):
    self._airplanes[airplane.id] = airplane
  def notify(self, sender):
    self.react_on(sender.id)
  def react_on(self, id):
    message = f"Mediator(AC1): responses to {self._airplanes[id]}"
    self._airplanes[id].receive(message)

class AirplaneA(Airplane):
  def operation(self, mediator):
    print(f"Airplane A notifies to the {mediator}")
    mediator.notify(self)
  def receive(self, message):
    print(message)
    
class AirplaneB(Airplane):
  def operation(self, mediator):
    print(f"Airplane B notifies to the {mediator}")
    mediator.notify(self)
  def receive(self, message):
    print(message)
        
class AirplaneC(Airplane):
  def operation(self, mediator):
    print(f"Airplane C notifies to the {mediator}")
    mediator.notify(self)        
  def receive(self, message):
    print(message)
     
# Driver    
m = AirtrafficController()    
a = AirplaneA('a')
m.register(a) 
b = AirplaneB('b')
m.register(b)   
c = AirplaneC('c')
m.register(c) 

# plane a notifies to the airtraffic control
a.operation(m)
# plane b notifies to the airtraffic control
b.operation(m)
# plane c notifies to the airtraffic control
c.operation(m)