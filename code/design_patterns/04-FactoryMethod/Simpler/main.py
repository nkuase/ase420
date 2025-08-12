from id_card import IDCard


def main():
  print("=== Factory Method Pattern Example ===\n")
  
  print("1. Creating ID cards using the factory:")
  
  card1 = IDCard.create("Sam Cho") # create only without register
  card2 = IDCard.create("James Bond") 
  card3 = IDCard.create("Kane")
  
  print("\n2. Using the created products:")
  
  card1.use()
  card2.use()
  card3.use()
  
if __name__ == "__main__":
  main()
