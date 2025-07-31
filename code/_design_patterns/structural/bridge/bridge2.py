# Implementation <<Interface>>
class Remote(object):
  def __init__(self, device):
    self.device = device
  def volume_up(self): 
    self.device.set_volume(self.device.get_volume() + 1)
    print(f"Volume up to {self.device.get_volume()}")    
  def volume_down(self):
    self.device.set_volume(self.device.get_volume() + 1)
    print(f"Volume down to {self.device.get_volume()}")
    
class AdvancedRemote(Remote):
  def mute(self): 
    self.device.set_volume(0) # added feature
    print(f"Volume muted to {self.device.get_volume()}")

# Abstraction
class Device(object): 
  def set_volume(): pass
  def get_volume(): pass

class TV(Device):
  def __init__(self):
    self.volume = 0
  def set_volume(self, volume): self.volume = volume
  def get_volume(self): return self.volume
  
class Radio(Device): 
  def __init__(self):
    self.volume = 0
  def set_volume(self, volume): self.volume = volume
  def get_volume(self): return self.volume

# Driver  
tv = TV()    
remote = AdvancedRemote(tv)
remote.volume_up()

radio = Radio()
remote = AdvancedRemote(radio)
remote.mute()
