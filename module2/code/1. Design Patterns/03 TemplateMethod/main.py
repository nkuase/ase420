from abstract_display import AbstractDisplay
from char_display import CharDisplay
from string_display import StringDisplay


def main():
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

if __name__ == "__main__":
    main()
