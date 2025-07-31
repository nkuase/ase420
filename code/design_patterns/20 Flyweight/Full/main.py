"""
Flyweight Pattern Demo
This example demonstrates the Flyweight pattern by creating ASCII art
representations of strings while sharing character font data efficiently.

Key concepts demonstrated:
1. Sharing intrinsic state (font data) among multiple contexts
2. Reducing memory usage when dealing with many similar objects
3. Separating intrinsic state (shared) from extrinsic state (context-specific)
4. Factory management of flyweight instances
"""

import sys
from big_string import BigString
from big_char_factory import BigCharFactory


def demonstrate_memory_efficiency():
    """
    Demonstrate how flyweights save memory by reusing shared instances.
    """
    print("=== Memory Efficiency Demonstration ===")
    
    factory = BigCharFactory.get_instance()
    
    # Create multiple strings with overlapping characters
    strings = ["123", "321", "111", "222", "333"]
    big_strings = []
    
    print("Creating multiple BigString objects...")
    for string in strings:
        print(f"\nCreating BigString for '{string}':")
        big_string = BigString(string)
        big_strings.append(big_string)
    
    print(f"\nFlyweight Pool Statistics:")
    print(f"- Total BigChar instances created: {factory.get_pool_size()}")
    print(f"- Cached characters: {factory.get_cached_characters()}")
    print(f"- Total character usages across all strings: {sum(len(s.get_string()) for s in big_strings)}")
    print(f"- Memory savings: {sum(len(s.get_string()) for s in big_strings) - factory.get_pool_size()} instances reused")
    
    return big_strings


def main():
    """
    Main function that demonstrates the Flyweight pattern.
    """
    print("=== Flyweight Pattern Demo ===\n")
    
    # Get input string
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
    else:
        print("No command line argument provided. Using default demo.")
        input_string = "1212123"
    
    print(f"Creating big ASCII art for: '{input_string}'")
    print("Supported characters: 0-9 and '-'")
    
    # Validate input
    valid_chars = set('0123456789-')
    if not all(c in valid_chars for c in input_string):
        print("Warning: Some characters are not supported and will show as '?'")
    
    print(f"\n{'='*60}")
    print("ASCII Art Output:")
    print(f"{'='*60}")
    
    # Create and display the big string
    big_string = BigString(input_string)
    big_string.print()
    
    print(f"\n{'='*60}")
    
    # Demonstrate memory efficiency with multiple strings
    print("\n")
    demonstrate_memory_efficiency()
    
    print(f"\n{'='*60}")
    print("Flyweight Pattern Benefits Demonstrated:")
    print(f"{'='*60}")
    print("✅ Memory Efficiency: Font data is shared among all instances of the same character")
    print("✅ Performance: No need to reload font data for duplicate characters")
    print("✅ Scalability: Memory usage grows with unique characters, not total characters")
    print("✅ Transparency: Clients use flyweights as if they were regular objects")
    
    print("\nKey Points:")
    print("- Intrinsic State: Font data (shared among all instances of same character)")
    print("- Extrinsic State: Position in string (passed as context when needed)")
    print("- Factory Pattern: Ensures flyweights are properly shared")
    print("- Memory Savings: Significant when many objects share common state")
    print("- Use Case: When you need many objects with shared characteristics")
    
    # Interactive demo
    print(f"\n{'='*60}")
    print("Interactive Demo:")
    print("Try running with different inputs to see flyweight reuse:")
    print("  python main.py 123")
    print("  python main.py 987654321")
    print("  python main.py 111-222-333")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
