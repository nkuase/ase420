from display import Display
from plain_display import PlainDisplay
from count_display import CountDisplay
from string_display_impl import StringDisplayImpl
from fancy_display_impl import FancyDisplayImpl

def main():
  print("=== Bridge Pattern Demo ===\n")
  
  print("1. Plain Display + StringDisplayImpl:")
  d1 = PlainDisplay(StringDisplayImpl("Hello, USA."))
  d1.display()
  
  print("\n2. Plain Display + FancyDisplayImpl:")
  d2 = PlainDisplay(FancyDisplayImpl("Hello, USA."))
  d2.display()
  
  print("\n3. CountDisplay + StringDisplayImpl:")
  d3 = CountDisplay(StringDisplayImpl("Hello, World."))
  d3.display()
  
  print("\n4. CountDisplay + FancyDisplayImpl:")
  d4 = CountDisplay(FancyDisplayImpl("Hello, World."))
  d4.display()
  
  print("\n5. Multiple display using CountDisplay:")
  d4.multi_display(5)
  
if __name__ == "__main__":
  main()
