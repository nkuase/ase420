from print_interface import Print
from print_banner import PrintBanner
#from print_banner2 import PrintBanner

def main():
    print("=== Adapter Pattern Example (Sample1 - Inheritance) ===\n")

    p = PrintBanner("Hello")
        
    print("Client code using Print interface:")
    print("Calling print_weak():")
    p.print_weak()  # This will be adapted to Banner's show_with_paren()
    
    print("\nCalling print_strong():")
    p.print_strong()  # This will be adapted to Banner's show_with_aster()
    
    print("\n" + "="*50)
    print("Pattern Analysis:")
    print("="*50)
    
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
