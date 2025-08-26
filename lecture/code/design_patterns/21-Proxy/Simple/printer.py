import time
from printable import Printable

class Printer(Printable):
  def __init__(self, name="Unknown"):
    self.name = name
    self._heavy_job(f"Creating Printer instance ({name})")
  
  def set_printer_name(self, name):
    self.name = name
  
  def get_printer_name(self):
    return self.name
  
  def print(self, string):
    print(f"=== {self.name} ===")
    print(string)
  
  def _heavy_job(self, msg):
    print(msg, end='', flush=True)
    for i in range(5):
      time.sleep(0.1)
      print('.', end='', flush=True)
    print(' Completed!')
