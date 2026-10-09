import sys
from director import Director
from text_builder import TextBuilder
from html_builder import HTMLBuilder


def usage():
  print("Usage: python main.py text       Create document in text format")
  print("Usage: python main.py html       Create document in HTML format")


def main():
  print("=== Builder Pattern Demo ===\n")
  
  if len(sys.argv) != 2:
    print("Demo with default text format:")
    format_type = "text"
  else:
    format_type = sys.argv[1]
  
  if format_type == "text":
    print("Creating text document...")
    text_builder = TextBuilder()
    director = Director(text_builder)
    director.construct()
    result = text_builder.get_text_result()
    print("\n--- Text Result ---")
    print(result)
    
  elif format_type == "html":
    print("Creating HTML document...")
    html_builder = HTMLBuilder()
    director = Director(html_builder)
    director.construct()
    filename = html_builder.get_html_result()
    print(f"\nHTML file '{filename}' has been created.")
    print("You can open it in a web browser to view the formatted document.")
    
  else:
    print(f"Unknown format: {format_type}")
    usage()
    return

if __name__ == "__main__":
  main()
