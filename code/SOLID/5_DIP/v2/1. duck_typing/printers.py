# Duck typing
# Both CashRegisterPrinter and LaserPrinter have print_receipt method
class CashRegisterPrinter:
    def print_receipt(self, receipt_text):
        print(f"Print {receipt_text} to CashRegisterPrinter")
        
class LaserPrinter:
    def print_receipt(self, receipt_text):
        print(f"Print {receipt_text} to LaserPrinter")       