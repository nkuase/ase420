"""
Builder Pattern Demo
This example demonstrates the Builder pattern by creating documents
in different formats using the same construction process.

Key concepts demonstrated:
1. Separation of construction process from representation
2. Same construction process can create different representations
3. Director controls the construction sequence
4. Builders handle format-specific details
"""

import sys
from director import Director
from text_builder import TextBuilder
from html_builder import HTMLBuilder


def usage():
    """Display usage information."""
    print("Usage: python main.py text       Create document in text format")
    print("Usage: python main.py html       Create document in HTML format")


def main():
    """
    Main function that demonstrates the Builder pattern.
    Creates documents in different formats based on command line argument.
    """
    print("=== Builder Pattern Demo ===\n")
    
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Demo with default text format:")
        format_type = "text"
    else:
        format_type = sys.argv[1]
    
    if format_type == "text":
        # Create text document
        print("Creating text document...")
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.get_text_result()
        print("\n--- Text Result ---")
        print(result)
        
    elif format_type == "html":
        # Create HTML document
        print("Creating HTML document...")
        html_builder = HTMLBuilder()
        director = Director(html_builder)
        director.construct()
        filename = html_builder.get_html_result()
        print(f"\nHTML file '{filename}' has been created.")
        print("You can open it in a web browser to view the formatted document.")
        
    else:
        print(f"Unknown format: {format_type}")
        usage()
        return
    
    print("\nKey Points:")
    print("- Same Director and construction process for both formats")
    print("- Different Builders create different representations")
    print("- Construction algorithm is separated from representation")
    print("- Easy to add new formats by creating new Builder implementations")


if __name__ == "__main__":
    main()
