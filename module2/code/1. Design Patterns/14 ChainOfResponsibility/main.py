from trouble import Trouble
from no_support import NoSupport
from limit_support import LimitSupport
from odd_support import OddSupport
from special_support import SpecialSupport


def main():
  
  print("=== Chain of Responsibility Pattern Demo ===\n")
  
  print("Creating support handlers...")
  alice = NoSupport("Alice")
  bob = LimitSupport("Bob", 100)
  charlie = SpecialSupport("Charlie", 429)
  diana = LimitSupport("Diana", 200)
  elmo = OddSupport("Elmo")
  fred = LimitSupport("Fred", 300)
  
  print("Building the chain of responsibility...")
  alice.set_next(bob).set_next(charlie).set_next(diana).set_next(elmo).set_next(fred)
  
  print("\n" + "="*50)
  print("Processing troubles through the chain:")
  print("="*50)
  
  for i in range(0, 500, 50):
    print(f"\nSending trouble {i}:")
    alice.support(Trouble(i))
  
if __name__ == "__main__":
  main()
