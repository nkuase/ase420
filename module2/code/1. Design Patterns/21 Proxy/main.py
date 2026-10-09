import time
from printer_proxy import PrinterProxy
from printer import Printer

def demonstrate_lazy_initialization():
  print("=== Lazy Initialization Demonstration ===")
  
  print("\n1. Creating PrinterProxy (should be fast)...")
  start_time = time.time()
  proxy = PrinterProxy("LazyPrinter")
  creation_time = time.time() - start_time
  print(f"   Proxy created in {creation_time:.3f} seconds")
  print(f"   Proxy status: {proxy}")
  
  print("\n2. Using proxy methods that don't require real object...")
  print(f"   Current name: {proxy.get_printer_name()}")
  proxy.set_printer_name("UpdatedPrinter")
  print(f"   Updated name: {proxy.get_printer_name()}")
  print(f"   Proxy status: {proxy}")
  
  print("\n3. Now calling print() which requires real object...")
  start_time = time.time()
  proxy.print("Hello from proxy!")
  realization_time = time.time() - start_time
  print(f"   Real object created and used in {realization_time:.3f} seconds")
  print(f"   Proxy status: {proxy}")
  
  print("\n4. Subsequent calls should be fast (real object already exists)...")
  start_time = time.time()
  proxy.print("Second call is fast!")
  second_call_time = time.time() - start_time
  print(f"   Second call completed in {second_call_time:.3f} seconds")

def main():
  print("=== Proxy Pattern Demo ===\n")
  
  print("The Proxy Pattern provides a placeholder for expensive objects")
  print("and controls access to them through lazy initialization.\n")
  
  print("Scenario: Printer objects are expensive to create (simulated with delays)")
  print("Solution: Use a proxy that creates the real printer only when needed\n")
  
  print("=== Basic Proxy Usage ===")
  
  print("Creating printer proxy...")
  p = PrinterProxy("Alice")
  
  print(f"Current name: {p.get_printer_name()}")
  print("   ↑ This operation doesn't require the real printer")
  
  print("\nChanging name...")
  p.set_printer_name("Bob")
  print(f"Current name: {p.get_printer_name()}")
  print("   ↑ Name operations work without creating real printer")
  
  print(f"\nProxy status before printing: {p}")
  print("\nCalling print() method (this will create the real printer)...")
  p.print("Hello, world.")
  print(f"Proxy status after printing: {p}")
  
  print("\n" + "="*60)
  demonstrate_lazy_initialization()
  
if __name__ == "__main__":
  main()
