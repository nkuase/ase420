"""
Facade Pattern Demo
This example demonstrates the Facade pattern by providing a simple interface
to a complex subsystem for creating personalized welcome pages.

Key concepts demonstrated:
1. Simplified interface to a complex subsystem
2. Hiding implementation details from clients
3. Reducing dependencies between client and subsystem
4. Providing a unified entry point to related functionality
"""

from pagemaker.page_maker import PageMaker


def main():
    """
    Main function that demonstrates the Facade pattern.
    Uses the simplified PageMaker interface instead of dealing with
    the complex subsystem components directly.
    """
    print("=== Facade Pattern Demo ===\n")
    
    print("Creating welcome pages using the PageMaker facade...")
    print("The facade hides the complexity of:")
    print("- Database operations (reading user data)")
    print("- HTML generation (creating proper HTML structure)")
    print("- File operations (writing to files)")
    print("- Error handling")
    
    print("\n" + "="*50)
    print("Creating welcome pages:")
    print("="*50)
    
    # Simple facade calls - client doesn't need to know about
    # Database, HtmlWriter, or the complex process involved
    PageMaker.make_welcome_page("hyuki@example.com", "welcome_hyuki.html")
    PageMaker.make_welcome_page("youngjin@example.com", "welcome_youngjin.html")
    PageMaker.make_welcome_page("dojun@example.com", "welcome_dojun.html")
    PageMaker.make_welcome_page("unknown@example.com", "welcome_unknown.html")
    
    print("\n" + "="*50)
    print("Without Facade Pattern, clients would need to:")
    print("="*50)
    print("1. Understand Database class and properties file format")
    print("2. Know how to use HtmlWriter correctly")
    print("3. Handle file I/O operations")
    print("4. Manage the sequence of operations")
    print("5. Handle all possible exceptions")
    print("6. Coordinate between multiple subsystem components")
    
    print("\nWith Facade Pattern:")
    print("- Client only needs to call one simple method")
    print("- All complexity is hidden behind the facade")
    print("- Easy to use and understand")
    print("- Reduces coupling between client and subsystem")
    print("- Changes to subsystem don't affect client code")
    
    print("\nKey Points:")
    print("- Facade provides a unified interface to a set of interfaces")
    print("- It doesn't prevent clients from accessing subsystem classes directly")
    print("- Facade promotes weak coupling between subsystem and clients")
    print("- Useful when you want to provide a simple interface to a complex subsystem")


if __name__ == "__main__":
    main()
