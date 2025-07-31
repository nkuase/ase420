from display import Display
from string_display import StringDisplay
from side_border import SideBorder
from full_border import FullBorder, CustomBorder


def basic_decorator_demo():
  print("=== Basic Decorator Demo ===")
  
  b1 = StringDisplay("Hello, world.")
  print("b1 (basic string):")
  b1.show()
  print()
  
  b2 = SideBorder(b1, '#')
  print("b2 (with side border):")
  b2.show()
  print()
  
  b3 = FullBorder(b2)
  print("b3 (full border around side border):")
  b3.show()
  print()


def complex_nesting_demo():
  print("=== Complex Nesting Demo ===")
  
  b4 = SideBorder(
    FullBorder(
      FullBorder(
        SideBorder(
          FullBorder(
            StringDisplay("Hello, world.")
          ),
          '*'
        )
      )
    ),
    '/'
  )
  
  print("b4 (complex nesting):")
  b4.show()
  print()

def main():
  
  print("=== Decorator Pattern Example ===\n")
  
  basic_decorator_demo()
  complex_nesting_demo()

  
if __name__ == "__main__":
  main()
