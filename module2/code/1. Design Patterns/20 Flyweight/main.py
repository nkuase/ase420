import sys
from big_string import BigString
from big_char_factory import BigCharFactory

def demonstrate_memory_efficiency():
  print("=== Memory Efficiency Demonstration ===")
  
  factory = BigCharFactory.get_instance()
  
  strings = ["123", "321", "111", "222", "333"]
  big_strings = []
  
  print("Creating multiple BigString objects...")
  for string in strings:
    print(f"\nCreating BigString for '{string}':")
    big_string = BigString(string)
    big_strings.append(big_string)
  
  print(f"\nFlyweight Pool Statistics:")
  print(f"- Total BigChar instances created: {factory.get_pool_size()}")
  print(f"- Cached characters: {factory.get_cached_characters()}")
  print(f"- Total character usages across all strings: {sum(len(s.get_string()) for s in big_strings)}")
  print(f"- Memory savings: {sum(len(s.get_string()) for s in big_strings) - factory.get_pool_size()} instances reused")
  
  return big_strings

def main():
  print("=== Flyweight Pattern Demo ===\n")
  
  if len(sys.argv) > 1:
    input_string = sys.argv[1]
  else:
    print("No command line argument provided. Using default demo.")
    input_string = "1212123"
  
  print(f"Creating big ASCII art for: '{input_string}'")
  print("Supported characters: 0-9 and '-'")
  
  valid_chars = set('0123456789-')
  if not all(c in valid_chars for c in input_string):
    print("Warning: Some characters are not supported and will show as '?'")
  
  print(f"\n{'='*60}")
  print("ASCII Art Output:")
  print(f"{'='*60}")
  
  big_string = BigString(input_string)
  big_string.print()
  
  print(f"\n{'='*60}")
  
  print("\n")
  demonstrate_memory_efficiency()
  
if __name__ == "__main__":
  main()
