from display import Display
from count_display import CountDisplay
from string_display_impl import StringDisplayImpl
from fancy_display_impl import FancyDisplayImpl

def main():
  print("=== Bridge Pattern Demo ===\n")
  
  print("1. Basic Display:")
  d1 = Display(StringDisplayImpl("Hello, USA."))
  d1.display()
  
  print("\n2. CountDisplay used as basic Display:")
  d2 = CountDisplay(StringDisplayImpl("Hello, World."))
  d2.display()
  
  print("\n3. FancyDisplay with enhanced functionality:")
  d3 = CountDisplay(FancyDisplayImpl("Hello, Universe."))
  d3.display()
  
  print("\n4. Multiple display using CountDisplay:")
  d3.multi_display(5)
  
if __name__ == "__main__":
  main()
