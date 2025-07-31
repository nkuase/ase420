"""
Abstract Factory Pattern Demo
This example demonstrates the Abstract Factory pattern by creating
HTML pages using different factory implementations.

Key concepts demonstrated:
1. Abstract factory defines interface for creating families of objects
2. Concrete factories implement specific variations of the products
3. Client code works with abstract interfaces
4. Easy to switch between different product families
"""

import sys
from factory.factory import Factory


def usage():
    """Display usage information."""
    print("Usage: python main.py filename.html factory_type")
    print("Example 1: python main.py list.html list")
    print("Example 2: python main.py div.html div")


def main():
    """
    Main function that demonstrates the Abstract Factory pattern.
    Creates HTML pages using different factory implementations.
    """
    print("=== Abstract Factory Pattern Demo ===\n")
    
    # Parse command line arguments or use defaults for demo
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        factory_type = sys.argv[2]
    else:
        print("Demo with default parameters:")
        filename = "demo.html"
        factory_type = "list"
    
    # Determine factory class name based on type
    if factory_type == "list":
        classname = "listfactory.list_factory.ListFactory"
    elif factory_type == "div":
        classname = "divfactory.div_factory.DivFactory"
    else:
        print(f"Unknown factory type: {factory_type}")
        usage()
        return
    
    print(f"Creating HTML page using {factory_type} factory...")
    
    # Get the factory instance
    factory = Factory.get_factory(classname)
    if factory is None:
        print("Failed to create factory")
        return
    
    # Create blog section
    blog1 = factory.create_link("Blog 1", "https://example.com/blog1")
    blog2 = factory.create_link("Blog 2", "https://example.com/blog2")
    blog3 = factory.create_link("Blog 3", "https://example.com/blog3")
    
    blog_tray = factory.create_tray("Blog Site")
    blog_tray.add(blog1)
    blog_tray.add(blog2)
    blog_tray.add(blog3)
    
    # Create news section
    news1 = factory.create_link("News 1", "https://example.com/news1")
    news2 = factory.create_link("News 2", "https://example.com/news2")
    news3 = factory.create_tray("News 3")
    news3.add(factory.create_link("News 3 (US)", "https://example.com/news3us"))
    news3.add(factory.create_link("News 3 (Korea)", "https://example.com/news3kr"))
    
    news_tray = factory.create_tray("News Site")
    news_tray.add(news1)
    news_tray.add(news2)
    news_tray.add(news3)
    
    # Create the page
    page = factory.create_page("Blog and News", "Youngjin.com")
    page.add(blog_tray)
    page.add(news_tray)
    
    # Output the page
    page.output(filename)
    
    print(f"\nHTML page created successfully!")
    print(f"File: {filename}")
    print(f"Factory used: {classname}")
    
    print("\nKey Points:")
    print("- Same client code works with different factory implementations")
    print("- Each factory creates a consistent family of related objects")
    print("- Easy to add new product families by implementing new factories")
    print("- Abstract factory ensures products work together correctly")


if __name__ == "__main__":
    main()
