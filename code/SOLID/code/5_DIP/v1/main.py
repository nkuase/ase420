from printers import LaserPrinter # code change

class Reporting():
    def print_receipt(self, receipt_text):
        # printer = CashRegisterPrinter()    # depends on a concrete class
        printer = LaserPrinter()
        printer.print_receipt(receipt_text)
        
p = Reporting()
p.print_receipt('Output')