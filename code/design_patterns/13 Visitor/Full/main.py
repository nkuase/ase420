"""
Visitor Pattern Demo
This example demonstrates the Visitor pattern by creating a file system
structure and using a visitor to display it.

Key concepts demonstrated:
1. Separation of data structure from operations performed on it
2. Adding new operations without modifying existing classes
3. Double dispatch mechanism
4. Recursive structure traversal
"""

from directory import Directory
from file import File
from list_visitor import ListVisitor


def main():
    """
    Main function that demonstrates the Visitor pattern.
    Creates a file system structure and applies a visitor to display it.
    """
    print("=== Visitor Pattern Demo ===\n")
    
    print("Making root entries...")
    # Create root directory structure
    rootdir = Directory("root")
    bindir = Directory("bin")
    tmpdir = Directory("tmp")
    usrdir = Directory("usr")
    
    # Build directory hierarchy
    rootdir.add(bindir).add(tmpdir).add(usrdir)
    
    # Add files to bin directory
    bindir.add(File("vi", 10000))
    bindir.add(File("latex", 20000))
    
    # Apply visitor to display the structure
    print("\nFile system structure:")
    rootdir.accept(ListVisitor())
    print()
    
    print("Making user entries...")
    # Create user directories
    youngjin = Directory("youngjin")
    gildong = Directory("gildong")
    dojun = Directory("dojun")
    
    # Add user directories to usr
    usrdir.add(youngjin).add(gildong).add(dojun)
    
    # Add files to user directories
    youngjin.add(File("diary.html", 100))
    youngjin.add(File("Composite.java", 200))
    gildong.add(File("memo.tex", 300))
    dojun.add(File("game.doc", 400))
    dojun.add(File("junk.mail", 500))
    
    # Display the complete structure
    print("\nComplete file system structure:")
    rootdir.accept(ListVisitor())
    
    print("\nKey Points:")
    print("- The Visitor pattern separates algorithms from object structure")
    print("- New operations can be added without modifying existing classes")
    print("- Visitor uses double dispatch to call the correct visit method")
    print("- Useful when you have a stable object structure but changing operations")
    print("- The file system structure doesn't need to know about display logic")


if __name__ == "__main__":
    main()
