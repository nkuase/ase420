"""
Main module for Adapter Pattern Example (Sample1 - Inheritance Version)

This demonstrates the Adapter pattern using inheritance (Class Adapter).
The PrintBanner class inherits from both Banner and implements Print interface,
allowing existing Banner functionality to be used through the Print interface.

Key concepts demonstrated:
1. Adaptee (Banner) - existing class with incompatible interface
2. Target (Print) - desired interface that client code expects
3. Adapter (PrintBanner) - bridges the gap using inheritance
4. Client (main) - uses the adapter through the target interface
"""

from print_interface import Print
from print_banner import PrintBanner
#from print_banner2 import PrintBanner

def main():
    """Demonstrate the Adapter pattern with inheritance approach."""
    
    print("=== Adapter Pattern Example (Sample1 - Inheritance) ===\n")
    
    # Create an adapter instance
    # Note: We're creating a PrintBanner but treating it as a Print interface
    p: Print = PrintBanner("Hello")
    
    print("Client code using Print interface:")
    print("Calling print_weak():")
    p.print_weak()  # This will be adapted to Banner's show_with_paren()
    
    print("\nCalling print_strong():")
    p.print_strong()  # This will be adapted to Banner's show_with_aster()
    
    print("\n" + "="*50)
    print("Pattern Analysis:")
    print("="*50)
    
    print("\n1. Adaptee (Banner):")
    print("   - Has methods: show_with_paren(), show_with_aster()")
    print("   - Existing class with its own interface")
    
    print("\n2. Target (Print interface):")
    print("   - Defines methods: print_weak(), print_strong()")
    print("   - Interface that client code expects")
    
    print("\n3. Adapter (PrintBanner):")
    print("   - Inherits from Banner")
    print("   - Implements Print interface")
    print("   - Translates print_weak() → show_with_paren()")
    print("   - Translates print_strong() → show_with_aster()")
    
    print("\n4. Client benefit:")
    print("   - Can use Banner functionality through familiar Print interface")
    print("   - No need to learn Banner's specific method names")
    print("   - Code is more maintainable and flexible")
    
    # Demonstrate that adapter has both interfaces
    print("\n" + "="*50)
    print("Adapter has access to Printer interface:")
    print("="*50)
    
    adapter = PrintBanner("Adapter Demo")
    print("\nUsing Print interface:")
    adapter.print_weak()
    adapter.print_strong()
    
    print("\nUsing Banner interface (It raises an error with delegation):")
    try:
        adapter.show_with_paren()
        adapter.show_with_aster()
    except AttributeError as e:
        print(e)


if __name__ == "__main__":
    main()
