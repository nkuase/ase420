from abc import ABC, abstractmethod

class State(ABC):
  @abstractmethod
  def do_clock(self, context, hour):
    pass
  
  @abstractmethod
  def do_use(self, context):
    pass
  
  @abstractmethod
  def do_alarm(self, context):
    pass
  
  @abstractmethod
  def do_phone(self, context):
    pass
