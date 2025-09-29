"""
Simple Demo - Abstract Factory Pattern
======================================
"""

from list_factory import ListFactory
from div_factory import DivFactory


def create_content(factory):
    """Create the same content using any factory"""
    # Create some links
    blog1 = factory.create_link("Python Tutorial", "https://python.org")
    blog2 = factory.create_link("Design Patterns", "https://refactoring.guru")
    
    # Put links in a tray
    blog_tray = factory.create_tray("Learning Resources")
    blog_tray.add(blog1)
    blog_tray.add(blog2)
    
    # Create a page and add the tray
    page = factory.create_page("My Bookmarks", "Student")
    page.add(blog_tray)
    
    return page


def main():
    print("Abstract Factory Pattern Demo")
    print("=" * 30)
    
    # Demo with ListFactory
    print("\n1. Creating page with ListFactory...")
    list_factory = ListFactory()
    list_page = create_content(list_factory)
    list_page.printit()
    
    # Demo with DivFactory  
    print("\n2. Creating page with DivFactory...")
    div_factory = DivFactory()
    div_page = create_content(div_factory)
    div_page.printit()

if __name__ == "__main__":
    main()
