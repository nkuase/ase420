"""
Main module for Factory Method Pattern Example

This demonstrates the Factory Method pattern where an abstract factory
defines the creation process, and concrete factories implement the
specific creation logic for different types of products.

Key concepts demonstrated:
1. Abstract Factory - defines the creation template method
2. Concrete Factory - implements specific product creation
3. Abstract Product - defines the product interface
4. Concrete Product - implements specific product behavior
5. Client code - uses factory without knowing concrete types
"""

from framework.factory import Factory
from framework.product import Product
from idcard.id_card_factory import IDCardFactory


def main():
    """Demonstrate the Factory Method pattern with ID card creation."""
    
    print("=== Factory Method Pattern Example ===\n")
    
    # Create a concrete factory
    # Note: We're using the abstract Factory type, not the concrete type
    factory: Factory = IDCardFactory()
    
    print("1. Creating ID cards using the factory:")
    
    # Create products using the factory
    # The client code doesn't know about IDCard specifically
    card1: Product = factory.create("Youngjin Kim")
    card2: Product = factory.create("Heungmin Son") 
    card3: Product = factory.create("Kane")
    
    print("\n2. Using the created products:")
    
    # Use the products through their abstract interface
    card1.use()
    card2.use()
    card3.use()
    
    print("\n" + "="*60)
    print("Pattern Analysis:")
    print("="*60)
    
    print("\n1. Factory Method Pattern Structure:")
    print("   - Abstract Factory: Framework.Factory")
    print("   - Concrete Factory: IDCardFactory")
    print("   - Abstract Product: Framework.Product")
    print("   - Concrete Product: IDCard")
    
    print("\n2. Template Method within Factory Method:")
    print("   - create() method defines the creation process")
    print("   - createProduct() and registerProduct() are factory methods")
    print("   - Concrete factories implement these methods")
    
    print("\n3. Benefits demonstrated:")
    print("   - Client code works with abstract types")
    print("   - Easy to add new product types")
    print("   - Creation logic is encapsulated")
    print("   - Consistent creation process")
    
    # Demonstrate factory-specific functionality
    print("\n" + "="*60)
    print("Factory-Specific Features:")
    print("="*60)
    
    # Since we know this is an IDCardFactory, we can access specific features
    id_factory = factory  # We know it's an IDCardFactory
    
    if isinstance(id_factory, IDCardFactory):
        print(f"\nFactory information: {id_factory}")
        print(f"Total cards created: {id_factory.get_card_count()}")
        
        print("\nAll created cards:")
        for i, card in enumerate(id_factory.get_created_cards(), 1):
            print(f"  {i}. {card}")
        
        print("\nFinding specific cards:")
        try:
            found_card = id_factory.find_card_by_owner("Kane")
            print(f"  Found card for Kane: {found_card}")
            found_card.use()
        except ValueError as e:
            print(f"  Error: {e}")
    
    # Demonstrate extensibility
    print("\n" + "="*60)
    print("Extensibility Demonstration:")
    print("="*60)
    
    print("\n3. Adding more cards dynamically:")
    additional_names = ["Park Ji-sung", "Lee Kang-in", "Hwang Hee-chan"]
    
    for name in additional_names:
        card = factory.create(name)
        print(f"   Created and using card for {name}:")
        card.use()
    
    print(f"\n   Final factory status: {factory}")
    
    # Show pattern benefits
    print("\n" + "="*60)
    print("Key Benefits of Factory Method Pattern:")
    print("="*60)
    
    print("\n1. Encapsulation:")
    print("   - Object creation logic is encapsulated in factories")
    print("   - Client code doesn't need to know concrete classes")
    
    print("\n2. Flexibility:")
    print("   - Easy to introduce new product types")
    print("   - Can change creation logic without affecting clients")
    
    print("\n3. Consistency:")
    print("   - All products go through the same creation process")
    print("   - Template method ensures consistent behavior")
    
    print("\n4. Extensibility:")
    print("   - New factories can be added for new product types")
    print("   - Follows Open/Closed Principle")
    
    # Demonstrate polymorphism
    print("\n" + "="*60)
    print("Polymorphism in Action:")
    print("="*60)
    
    def create_and_use_product(factory: Factory, owner: str) -> None:
        """
        Function that works with any factory implementation.
        
        This demonstrates how client code can work with the abstract
        factory interface without knowing concrete implementations.
        """
        product = factory.create(owner)
        product.use()
        return product
    
    print("\nUsing polymorphic function:")
    create_and_use_product(factory, "Polymorphic User")


if __name__ == "__main__":
    main()
