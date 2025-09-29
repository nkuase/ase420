from number_generator import NumberGenerator
from random_number_generator import RandomNumberGenerator
from digit_observer import DigitObserver
from graph_observer import GraphObserver
from observer import Observer
import time

def basic_observer_demo():
  print("=== Basic Observer Demo ===")
  
  generator = RandomNumberGenerator()
  
  observer1 = DigitObserver()
  observer2 = GraphObserver()
  
  generator.add_observer(observer1)
  generator.add_observer(observer2)
  
  print(f"Registered {generator.get_observer_count()} observers")
  print("Starting number generation...\n")
  
  # 10 times
  generator.execute(10)
  
  print(f"\nDemo completed with {generator.get_observer_count()} observers")
  print()

def main():
  basic_observer_demo()
  
if __name__ == "__main__":
  main()
