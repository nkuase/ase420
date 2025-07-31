from abc import ABCMeta, abstractmethod

class IPrinter(metaclass=ABCMeta):
  @abstractmethod
  def print_receipt(self): 
      "interface methd"

class CashRegisterPrinter(IPrinter):
    def print_receipt(self, receipt_text):
        print(f"Print {receipt_text} to CashRegisterPrinter")
        
class LaserPrinter(IPrinter):
    def print_receipt(self, receipt_text):
        print(f"Print {receipt_text} to LaserPrinter")       