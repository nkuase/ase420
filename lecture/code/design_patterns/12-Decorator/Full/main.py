"""
Main module for Decorator Pattern Example

This demonstrates the Decorator pattern where additional responsibilities
are attached to objects dynamically. Decorators provide a flexible
alternative to subclassing for extending functionality.

Key concepts demonstrated:
1. Component (Display) - defines interface for objects that can have responsibilities added
2. Concrete Component (StringDisplay) - defines basic behavior that can be decorated
3. Decorator (Border) - maintains reference to component and defines decorating interface
4. Concrete Decorators (SideBorder, FullBorder) - add specific responsibilities

The display/border metaphor perfectly illustrates this pattern:
- Basic text display is the core component
- Various borders can be added as decorations
- Decorators can be stacked/nested for complex effects
"""

from display import Display
from string_display import StringDisplay
from side_border import SideBorder
from full_border import FullBorder, CustomBorder


def basic_decorator_demo():
    """Demonstrate basic decorator functionality (matching Java version)."""
    print("=== Basic Decorator Demo ===")
    
    # Create basic string display
    b1 = StringDisplay("Hello, world.")
    print("b1 (basic string):")
    b1.show()
    print()
    
    # Add side border
    b2 = SideBorder(b1, '#')
    print("b2 (with side border):")
    b2.show()
    print()
    
    # Add full border around side border
    b3 = FullBorder(b2)
    print("b3 (full border around side border):")
    b3.show()
    print()


def complex_nesting_demo():
    """Demonstrate complex nesting of decorators (matching Java version)."""
    print("=== Complex Nesting Demo ===")
    
    # Create the complex nested structure from the Java version
    b4 = SideBorder(
        FullBorder(
            FullBorder(
                SideBorder(
                    FullBorder(
                        StringDisplay("Hello, world.")
                    ),
                    '*'
                )
            )
        ),
        '/'
    )
    
    print("b4 (complex nesting):")
    b4.show()
    print()


def demonstrate_decorator_properties():
    """Demonstrate properties and introspection of decorated objects."""
    print("=== Decorator Properties ===")
    
    # Build a decorated display step by step
    base = StringDisplay("Python")
    side1 = SideBorder(base, '|')
    full1 = FullBorder(side1)
    side2 = SideBorder(full1, '*')
    full2 = FullBorder(side2)
    
    decorators = [
        ("Base", base),
        ("Side Border", side1),
        ("Full Border", full1),
        ("Another Side", side2),
        ("Final Full Border", full2)
    ]
    
    print("Decorator building process:")
    for name, display in decorators:
        print(f"\n{name}:")
        print(f"  Dimensions: {display.get_columns()}x{display.get_rows()}")
        print(f"  Content:")
        display.show()
    
    print()


def demonstrate_introspection():
    """Demonstrate introspection capabilities of decorators."""
    print("=== Decorator Introspection ===")
    
    # Create a complex decorated display
    display = FullBorder(
        SideBorder(
            FullBorder(
                StringDisplay("Core")
            ),
            '#'
        )
    )
    
    print("Analyzing decorated display:")
    print(f"Final dimensions: {display.get_columns()}x{display.get_rows()}")
    
    # Analyze the decoration structure
    if hasattr(display, 'get_decoration_depth'):
        print(f"Decoration depth: {display.get_decoration_depth()}")
    
    if hasattr(display, 'unwrap'):
        core = display.unwrap()
        print(f"Core component: {core}")
        print(f"Core dimensions: {core.get_columns()}x{core.get_rows()}")
    
    print(f"Representation: {repr(display)}")
    print()


def demonstrate_custom_decorators():
    """Demonstrate custom decorator implementations."""
    print("=== Custom Decorators ===")
    
    # Use CustomBorder with different characters
    base = StringDisplay("Custom")
    
    # ASCII border
    ascii_border = CustomBorder(base, '-', '|', '+')
    print("ASCII border:")
    ascii_border.show()
    print()
    
    # Unicode border
    unicode_border = CustomBorder(base, '═', '║', '╬')
    print("Unicode border:")
    unicode_border.show()
    print()
    
    # Star border
    star_border = CustomBorder(base, '*', '*', '*')
    print("Star border:")
    star_border.show()
    print()


def demonstrate_dynamic_decoration():
    """Demonstrate adding decorations dynamically."""
    print("=== Dynamic Decoration ===")
    
    base_text = "Dynamic"
    display = StringDisplay(base_text)
    
    print("Starting with base display:")
    display.show()
    print()
    
    # Dynamically add decorations based on user choices
    decorations = [
        ("side", lambda d: SideBorder(d, '|')),
        ("full", lambda d: FullBorder(d)),
        ("star", lambda d: SideBorder(d, '*')),
        ("double", lambda d: FullBorder(FullBorder(d)))
    ]
    
    print("Adding decorations dynamically:")
    for name, decorator_func in decorations:
        display = decorator_func(display)
        print(f"\nAfter adding {name} decoration:")
        display.show()
    
    print()


def demonstrate_decorator_benefits():
    """Demonstrate the benefits of the Decorator pattern."""
    print("=== Decorator Pattern Benefits ===")
    
    print("1. Flexible Extension:")
    print("   - Add responsibilities without modifying existing classes")
    print("   - Multiple decorators can be combined")
    
    print("\n2. Runtime Composition:")
    print("   - Decorations can be added/removed at runtime")
    print("   - Different combinations for different situations")
    
    print("\n3. Alternative to Inheritance:")
    print("   - Avoids class explosion from multiple combinations")
    print("   - More flexible than static inheritance")
    
    print("\n4. Transparency:")
    print("   - Decorated objects have the same interface as originals")
    print("   - Client code doesn't need to know about decorations")
    
    # Demonstrate transparency
    displays = [
        StringDisplay("Base"),
        SideBorder(StringDisplay("Decorated"), '#'),
        FullBorder(StringDisplay("Fully Decorated"))
    ]
    
    print("\n5. Uniform Interface Demonstration:")
    for i, display in enumerate(displays):
        print(f"   Display {i+1}: {display.get_columns()}x{display.get_rows()}")
    
    print()


def performance_comparison():
    """Compare different approaches to adding functionality."""
    print("=== Decorator vs Inheritance Comparison ===")
    
    print("Inheritance approach problems:")
    print("  - Need classes for every combination")
    print("  - StringDisplayWithSideBorder")
    print("  - StringDisplayWithFullBorder") 
    print("  - StringDisplayWithBothBorders")
    print("  - StringDisplayWithDoubleBorders")
    print("  - ... (exponential growth)")
    
    print("\nDecorator approach benefits:")
    print("  - One decorator class per feature")
    print("  - Unlimited combinations at runtime")
    print("  - Easy to add new decorators")
    print("  - No class explosion")
    
    # Show some combinations
    base = StringDisplay("Flexible")
    combinations = [
        SideBorder(base, '|'),
        FullBorder(base),
        SideBorder(FullBorder(base), '#'),
        FullBorder(SideBorder(base, '*')),
        SideBorder(FullBorder(SideBorder(base, '|')), '*')
    ]
    
    print(f"\n{len(combinations)} different combinations with just 2 decorator classes:")
    for i, combo in enumerate(combinations, 1):
        print(f"  Combination {i}: {combo.get_columns()}x{combo.get_rows()}")
    
    print()


def real_world_applications():
    """Show real-world applications of the Decorator pattern."""
    print("=== Real-World Applications ===")
    
    print("1. GUI Components:")
    print("   - ScrollPane(TextArea())")
    print("   - BorderLayout(Panel())")
    print("   - ResizableBorder(Window())")
    
    print("\n2. I/O Streams:")
    print("   - BufferedReader(FileReader())")
    print("   - GzipInputStream(FileInputStream())")
    print("   - DataInputStream(BufferedInputStream())")
    
    print("\n3. Web Frameworks:")
    print("   - Authentication(Authorization(Handler()))")
    print("   - Logging(Caching(RequestHandler()))")
    print("   - Compression(Response())")
    
    print("\n4. Text Processing:")
    print("   - Bold(Italic(Text()))")
    print("   - Encrypted(Compressed(Document()))")
    print("   - Highlighted(Formatted(Content()))")
    
    print()


def main():
    """Main function demonstrating the Decorator pattern."""
    
    print("=== Decorator Pattern Example ===\n")
    
    # Basic demonstration (matching Java version)
    basic_decorator_demo()
    
    # Complex nesting (matching Java version)
    complex_nesting_demo()
    
    # Demonstrate decorator properties
    demonstrate_decorator_properties()
    
    # Show introspection capabilities
    demonstrate_introspection()
    
    # Custom decorators
    demonstrate_custom_decorators()
    
    # Dynamic decoration
    demonstrate_dynamic_decoration()
    
    # Pattern benefits
    demonstrate_decorator_benefits()
    
    # Performance comparison
    performance_comparison()
    
    # Real-world applications
    real_world_applications()
    
    print("="*60)
    print("Pattern Analysis:")
    print("="*60)
    
    print("\n1. Decorator Pattern Structure:")
    print("   - Component: Defines interface for objects that can be decorated")
    print("   - ConcreteComponent: Basic implementation that can be decorated")
    print("   - Decorator: Base class that wraps a component")
    print("   - ConcreteDecorator: Adds specific responsibilities")
    
    print("\n2. Key Implementation Details:")
    print("   - Decorators implement same interface as components")
    print("   - Decorators forward requests to wrapped component")
    print("   - Additional behavior added before/after forwarding")
    print("   - Multiple decorators can be chained")
    
    print("\n3. Python-Specific Features:")
    print("   - Abstract Base Classes for interfaces")
    print("   - Method chaining for fluent interfaces")
    print("   - Introspection capabilities")
    print("   - String multiplication for repeated characters")
    
    print("\n4. Benefits Demonstrated:")
    print("   - Flexible alternative to inheritance")
    print("   - Runtime composition of behaviors")
    print("   - Transparent interface preservation")
    print("   - Unlimited combination possibilities")
    
    print("\n5. Design Considerations:")
    print("   - Can lead to many small objects")
    print("   - Object identity may be lost in decoration")
    print("   - Order of decoration can matter")
    print("   - Interface compatibility is crucial")


if __name__ == "__main__":
    main()
