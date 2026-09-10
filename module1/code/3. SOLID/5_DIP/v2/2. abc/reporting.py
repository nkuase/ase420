from printers import IPrinter

# In the ABC approach, Reporting explicitly depends on the abstract contract IPrinter
class Reporting:
    def __init__(self, printer: IPrinter):
        self.printer = printer

    def print_receipt(self, receipt_text):
        self.printer.print_receipt(receipt_text)