from framework.factory import Factory
from framework.product import Product
from idcard.id_card_factory import IDCardFactory


def main():
  print("=== Factory Method Pattern Example ===\n")
  
  factory = IDCardFactory()
  
  print("1. Creating ID cards using the factory:")
  
  card1 = factory.create_product("Sam Cho") # create only without register
  card2 = factory.create("James Bond") 
  card3 = factory.create("Kane")
  
  print("\n2. Using the created products:")
  
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
  print("   - create_product() and register_product() are factory methods")
  print("   - Concrete factories implement these methods")
  
  print("\n3. Benefits demonstrated:")
  print("   - Client code works with abstract types")
  print("   - Easy to add new product types")
  print("   - Creation logic is encapsulated")
  print("   - Consistent creation process")
  
  print("\n" + "="*60)
  print("Factory-Specific Features:")
  print("="*60)
  
  if isinstance(factory, IDCardFactory):
    print(f"\nFactory information: factory")
    print(f"Total cards created: {factory.get_card_count()}")
    
    print("\nAll created cards:")
    for i, card in enumerate(factory.get_created_cards(), 1):
      print(f"  {i}. {card}")
    
    print("\nFinding specific cards:")
    try:
      found_card = factory.find_card_by_owner("Kane")
      print(f"  Found card for Kane: {found_card}")
      found_card.use()
    except ValueError as e:
      print(f"  Error: {e}")
  
  print("\n" + "="*60)
  print("Extensibility Demonstration:")
  print("="*60)
  
  print("\n3. Adding more cards dynamically:")
  additional_names = ["John Lennon", "Paul McCartney", "George Harrison"]
  
  for name in additional_names:
    card = factory.create(name)
    print(f"   Created and using card for {name}:")
    card.use()
  
  print(f"\n   Final factory status: {factory}")
  
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
  
  print("\n" + "="*60)
  print("Polymorphism in Action:")
  print("="*60)
  
  def create_and_use_product(factory, owner):
    product = factory.create(owner)
    product.use()
    return product
  
  print("\nUsing polymorphic function:")
  create_and_use_product(factory, "Polymorphic User")


if __name__ == "__main__":
  main()
