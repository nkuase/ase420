import threading
from printable import Printable
from printer import Printer

class PrinterProxy(Printable):
  def __init__(self, name="No Name"):
    self.name = name
    self.real = None
  
  def set_printer_name(self, name):
    if self.real is not None:
      self.real.set_printer_name(name)
    self.name = name
  
  def get_printer_name(self):
    return self.name
  
  def print(self, string):
    self._realize()
    self.real.print(string)
  
  def _realize(self):
    if self.real is None:
      print(f"Creating real Printer instance for '{self.name}'...")
      self.real = Printer(self.name)
  
  def is_realized(self):
    return self.real is not None
  
  def __str__(self):
    status = "realized" if self.is_realized() else "not realized"
    return f"PrinterProxy(name='{self.name}', {status})"
