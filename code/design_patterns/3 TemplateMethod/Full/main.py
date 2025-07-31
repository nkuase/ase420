"""
Main module for Template Method Pattern Example

This demonstrates the Template Method pattern where an abstract class
defines the skeleton of an algorithm (template method) and lets subclasses
override specific steps without changing the algorithm's structure.

Key concepts demonstrated:
1. Abstract Class (AbstractDisplay) - defines template method and abstract methods
2. Template Method (display) - defines algorithm skeleton
3. Concrete Classes (CharDisplay, StringDisplay) - implement abstract methods
4. Polymorphism - same method call produces different behaviors
"""

from abstract_display import AbstractDisplay
from char_display import CharDisplay
from string_display import StringDisplay


def main():
    """Demonstrate the Template Method pattern with different implementations."""
    
    print("=== Template Method Pattern Example ===\n")
    
    # Create instances of different concrete classes
    # Both inherit from AbstractDisplay but implement methods differently
    d1: AbstractDisplay = CharDisplay('H')
    d2: AbstractDisplay = StringDisplay("Hello, world.")
    
    print("1. CharDisplay with character 'H':")
    print(f"   Created: {d1}")
    print("   Output:")
    d1.display()  # Uses template method with CharDisplay's implementations
    
    print("\n2. StringDisplay with 'Hello, world.':")
    print(f"   Created: {d2}")
    print("   Output:")
    d2.display()  # Uses template method with StringDisplay's implementations
    
    print("\n" + "="*60)
    print("Pattern Analysis:")
    print("="*60)
    
    print("\n1. Template Method (display):")
    print("   - Defined in AbstractDisplay")
    print("   - Same algorithm structure for all subclasses:")
    print("     * Call open()")
    print("     * Call print() 5 times")
    print("     * Call close()")
    
    print("\n2. Abstract Methods (open, print, close):")
    print("   - Defined as abstract in AbstractDisplay")
    print("   - Each subclass provides different implementation")
    
    print("\n3. CharDisplay implementation:")
    print("   - open(): prints '<<'")
    print("   - print(): prints the character")
    print("   - close(): prints '>>'")
    
    print("\n4. StringDisplay implementation:")
    print("   - open(): prints top border '+---+'")
    print("   - print(): prints '|string|'")
    print("   - close(): prints bottom border '+---+'")
    
    # Demonstrate with more examples
    print("\n" + "="*60)
    print("Additional Examples:")
    print("="*60)
    
    examples = [
        CharDisplay('A'),
        CharDisplay('*'),
        StringDisplay("Python"),
        StringDisplay("Template Method Pattern"),
        CharDisplay('X')
    ]
    
    for i, display in enumerate(examples, 1):
        print(f"\n{i}. {display}:")
        display.display()
    
    # Demonstrate the benefits
    print("\n" + "="*60)
    print("Benefits of Template Method Pattern:")
    print("="*60)
    
    print("\n1. Code Reuse:")
    print("   - Common algorithm structure defined once")
    print("   - No duplication of the display logic")
    
    print("\n2. Consistency:")
    print("   - All subclasses follow the same algorithm")
    print("   - Guaranteed sequence: open → print × 5 → close")
    
    print("\n3. Flexibility:")
    print("   - Easy to add new display types")
    print("   - Each type can have unique formatting")
    
    print("\n4. Polymorphism:")
    print("   - Client code treats all displays uniformly")
    print("   - Runtime determines actual behavior")


if __name__ == "__main__":
    main()
