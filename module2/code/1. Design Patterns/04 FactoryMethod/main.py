from product import Product
from id_card_factory import IDCardFactory
from super_card_factory import SuperCardFactory

def main():
  print("=== Factory Method Pattern Example ===\n")
  
  id_factory = IDCardFactory()
  super_factory = SuperCardFactory()
  
  print("1. Creating ID cards using the factory:")
  
  card1 = id_factory.create_product("James Bond") 
  card2 = super_factory.create_product("Kane")
  
  print("\n2. Using the created products:")
  
  card1.use()
  card2.use()

if __name__ == "__main__":
  main()
