from framework.manager import Manager
from underline_pen import UnderlinePen
from message_box import MessageBox

def main():
  print("=== Prototype Pattern Demo ===\n")
  
  print("1. Creating manager and prototype objects...")
  manager = Manager()
  
  upen = UnderlinePen('-')
  mbox = MessageBox('*')
  sbox = MessageBox('/')
  
  print(f"   Created: {upen}")
  print(f"   Created: {mbox}")
  print(f"   Created: {sbox}")
  
  print("\n2. Registering prototypes...")
  manager.register("strong message", upen)
  manager.register("warning box", mbox)
  manager.register("slash box", sbox)
  
  manager.list_prototypes()
  
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
  
  print("\n4. Demonstrating independence of copies...")
  print("Original underline pen:")
  upen.use("Original")
  
  print("\nCopied underline pen:")
  p1.use("Copy")

if __name__ == "__main__":
  main()
