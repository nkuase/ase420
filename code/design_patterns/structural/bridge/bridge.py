# Interfaces
class Device(object): # GoF calls it Implementation
  def set_volume(self): pass
  def get_volume(self): pass

class Remote(object): # GoF calls it Abstract
  def volume_up(self): pass
  def volume_down(self): pass

# Implementations
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
  
class AdvancedRemote(Remote):
  def __init__(self, device):
    self.device = device
  def volume_up(self): 
    self.device.set_volume(self.device.get_volume() + 1)
    print(f"Volume up to {self.device.get_volume()}")    
  def volume_down(self):
    self.device.set_volume(self.device.get_volume() + 1)
    print(f"Volume down to {self.device.get_volume()}")

# Driver  
tv = TV()    
remote = AdvancedRemote(tv)
remote.volume_up()

radio = Radio()
remote = AdvancedRemote(radio)
remote.volume_up()
