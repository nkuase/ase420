from reporting import Reporting
from printers import LaserPrinter

p = LaserPrinter() # The dependency is inverted
r = Reporting(p) # No change in the Reporting 
r.print_receipt('Total: $45,00')