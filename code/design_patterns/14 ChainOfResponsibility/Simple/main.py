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
  
  print("Chain: Alice -> Bob -> Charlie -> Diana -> Elmo -> Fred")
  print("\nHandler capabilities:")
  print("- Alice: Never handles anything (passes everything)")
  print("- Bob: Handles troubles < 100")
  print("- Charlie: Handles only trouble 429")
  print("- Diana: Handles troubles < 200")
  print("- Elmo: Handles odd-numbered troubles")
  print("- Fred: Handles troubles < 300")
  
  print("\n" + "="*50)
  print("Processing troubles through the chain:")
  print("="*50)
  
  for i in range(0, 500, 33):
    print(f"\nSending trouble {i}:")
    alice.support(Trouble(i))
  
  print("\n" + "="*50)
  print("Analysis of results:")
  print("="*50)
  print("- Trouble 0: Handled by Bob (< 100)")
  print("- Trouble 33: Handled by Elmo (odd number)")
  print("- Trouble 66: Handled by Bob (< 100)")
  print("- Trouble 99: Handled by Elmo (odd number)")
  print("- Trouble 132: Handled by Diana (< 200)")
  print("- Trouble 165: Handled by Elmo (odd number)")
  print("- Trouble 198: Handled by Diana (< 200)")
  print("- Trouble 231: Handled by Elmo (odd number)")
  print("- Trouble 264: Handled by Fred (< 300)")
  print("- Trouble 297: Handled by Elmo (odd number)")
  print("- Trouble 330: Cannot be resolved (≥ 300 and even)")
  print("- Trouble 363: Handled by Elmo (odd number)")
  print("- Trouble 396: Cannot be resolved (≥ 300 and even)")
  print("- Trouble 429: Handled by Charlie (special case)")
  print("- Trouble 462: Cannot be resolved (≥ 300 and even)")
  print("- Trouble 495: Handled by Elmo (odd number)")

if __name__ == "__main__":
  main()
