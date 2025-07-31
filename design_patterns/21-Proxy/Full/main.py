"""
Proxy Pattern Demo
This example demonstrates the Proxy pattern by using a proxy to control
access to an expensive-to-create printer object.

Key concepts demonstrated:
1. Lazy initialization - real object created only when needed
2. Transparent interface - proxy implements same interface as real object
3. Access control - proxy can control when and how real object is accessed
4. Performance optimization - avoid expensive operations until necessary
"""

import time
from printer_proxy import PrinterProxy
from printer import Printer


def demonstrate_lazy_initialization():
    """
    Demonstrate how proxy delays creation of expensive objects.
    """
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


def compare_direct_vs_proxy():
    """
    Compare direct object creation with proxy-based lazy initialization.
    """
    print("\n=== Direct Creation vs Proxy Comparison ===")
    
    print("\n1. Direct Printer creation (immediate expensive operation):")
    start_time = time.time()
    direct_printer = Printer("DirectPrinter")
    direct_creation_time = time.time() - start_time
    print(f"   Direct printer created in {direct_creation_time:.3f} seconds")
    
    print("\n2. Proxy creation (fast, no real object yet):")
    start_time = time.time()
    proxy_printer = PrinterProxy("ProxyPrinter")
    proxy_creation_time = time.time() - start_time
    print(f"   Proxy created in {proxy_creation_time:.3f} seconds")
    print(f"   Speed improvement: {(direct_creation_time/proxy_creation_time):.1f}x faster")
    
    print("\n3. Using both printers...")
    print("   Direct printer:")
    direct_printer.print("Message from direct printer")
    
    print("\n   Proxy printer (triggers real object creation):")
    proxy_printer.print("Message from proxy printer")


def main():
    """
    Main function that demonstrates the Proxy pattern.
    """
    print("=== Proxy Pattern Demo ===\n")
    
    print("The Proxy Pattern provides a placeholder for expensive objects")
    print("and controls access to them through lazy initialization.\n")
    
    print("Scenario: Printer objects are expensive to create (simulated with delays)")
    print("Solution: Use a proxy that creates the real printer only when needed\n")
    
    # Original demo from Java version
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
    
    # Additional demonstrations
    print("\n" + "="*60)
    demonstrate_lazy_initialization()
    
    print("\n" + "="*60)
    compare_direct_vs_proxy()
    
    print(f"\n{'='*60}")
    print("Proxy Pattern Benefits Demonstrated:")
    print(f"{'='*60}")
    print("✅ Lazy Initialization: Expensive object created only when needed")
    print("✅ Performance: Fast proxy creation, delayed real object creation")
    print("✅ Transparency: Clients use proxy exactly like the real object")
    print("✅ Control: Proxy can add access control, caching, or logging")
    print("✅ Memory Efficiency: Real objects created only if actually used")
    
    print("\nProxy Pattern Use Cases:")
    print("- Virtual Proxy: Lazy initialization of expensive objects")
    print("- Protection Proxy: Access control and security")
    print("- Remote Proxy: Represent objects in different address spaces")
    print("- Cache Proxy: Add caching functionality")
    print("- Smart Reference: Additional functionality like reference counting")
    
    print("\nKey Points:")
    print("- Proxy and real object implement the same interface")
    print("- Proxy delegates to real object when necessary")
    print("- Transparent to clients - they don't know they're using a proxy")
    print("- Can be combined with other patterns (Singleton, Factory)")


if __name__ == "__main__":
    main()
