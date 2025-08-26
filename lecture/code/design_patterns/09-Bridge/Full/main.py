"""
Bridge Pattern Demo
This example demonstrates the Bridge pattern by separating the abstraction
(Display, CountDisplay) from the implementation (StringDisplayImpl).

Key concepts demonstrated:
1. Separation of abstraction and implementation
2. Both can vary independently
3. Implementation can be changed at runtime
4. Refined abstractions can add new functionality
"""

from display import Display
from count_display import CountDisplay
from string_display_impl import StringDisplayImpl


def main():
    """
    Demonstrate the Bridge pattern with different combinations
    of abstractions and implementations.
    """
    print("=== Bridge Pattern Demo ===\n")
    
    # Create different display objects with the same implementation
    print("1. Basic Display:")
    d1 = Display(StringDisplayImpl("Hello, USA."))
    d1.display()
    
    print("\n2. CountDisplay used as basic Display:")
    d2 = CountDisplay(StringDisplayImpl("Hello, World."))
    d2.display()
    
    print("\n3. CountDisplay with enhanced functionality:")
    d3 = CountDisplay(StringDisplayImpl("Hello, Universe."))
    d3.display()
    
    print("\n4. Multiple display using CountDisplay:")
    d3.multi_display(5)
    
    print("\nKey Points:")
    print("- The abstraction (Display/CountDisplay) is separated from implementation (StringDisplayImpl)")
    print("- We can extend abstractions (CountDisplay) without changing implementations")
    print("- We can create new implementations without changing abstractions")
    print("- This provides flexibility and maintainability")


if __name__ == "__main__":
    main()
