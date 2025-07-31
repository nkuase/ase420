"""
Prototype Pattern Demo
This example demonstrates the Prototype pattern by creating and cloning
different types of text formatting objects.

Key concepts demonstrated:
1. Objects can be cloned without knowing their concrete classes
2. New instances are created by copying existing prototypes
3. Reduces the need for complex initialization code
4. Provides flexibility in object creation
"""

from framework.manager import Manager
from underline_pen import UnderlinePen
from message_box import MessageBox


def main():
    """
    Main function that demonstrates the Prototype pattern.
    Creates prototypes, registers them, and then creates copies.
    """
    print("=== Prototype Pattern Demo ===\n")
    
    # Preparation - create the manager and prototype objects
    print("1. Creating manager and prototype objects...")
    manager = Manager()
    
    upen = UnderlinePen('-')
    mbox = MessageBox('*')
    sbox = MessageBox('/')
    
    print(f"   Created: {upen}")
    print(f"   Created: {mbox}")
    print(f"   Created: {sbox}")
    
    # Registration - register prototypes with names
    print("\n2. Registering prototypes...")
    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)
    
    manager.list_prototypes()
    
    # Creation and usage - create copies and use them
    print("\n3. Creating copies and using them...\n")
    
    print("Creating copy of 'strong message':")
    p1 = manager.create("strong message")
    if p1:
        p1.use("Hello, world.")
    
    print("\nCreating copy of 'warning box':")
    p2 = manager.create("warning box")
    if p2:
        p2.use("Hello, world.")
    
    print("\nCreating copy of 'slash box':")
    p3 = manager.create("slash box")
    if p3:
        p3.use("Hello, world.")
    
    # Demonstrate that copies are independent
    print("\n4. Demonstrating independence of copies...")
    print("Original underline pen:")
    upen.use("Original")
    
    print("\nCopied underline pen:")
    p1.use("Copy")
    
    print("\nKey Points:")
    print("- Objects are created by cloning prototypes, not calling constructors")
    print("- The Manager doesn't need to know concrete classes")
    print("- Each copy is independent of the original")
    print("- Easy to add new product types without changing the Manager")
    print("- Useful when object creation is expensive or complex")


if __name__ == "__main__":
    main()
