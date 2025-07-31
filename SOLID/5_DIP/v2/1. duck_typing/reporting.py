class Reporting():
    def __init__(self, printer):
        self.printer = printer
    def print_receipt(self, receipt_text):
        self.printer.print_receipt(receipt_text)