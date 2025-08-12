from abc import ABC, abstractmethod

class Context(ABC):
  @abstractmethod
  def set_clock(self, hour):
    pass
  
  @abstractmethod
  def change_state(self, state):
    pass
  
  @abstractmethod
  def call_security_center(self, msg):
    pass
  
  @abstractmethod
  def record_log(self, msg):
    pass
