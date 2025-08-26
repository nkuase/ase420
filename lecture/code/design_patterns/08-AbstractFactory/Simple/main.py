import sys
from factory.factory import Factory


def usage():
  print("Usage: python main.py filename.html factory_type")
  print("Example 1: python main.py list.html list")
  print("Example 2: python main.py div.html div")


def main():
  print("=== Abstract Factory Pattern Demo ===\n")
  
  if len(sys.argv) == 3:
    filename = sys.argv[1]
    factory_type = sys.argv[2]
  else:
    print("Demo with default parameters:")
    filename = "demo.html"
    factory_type = "list"
  
  if factory_type == "list":
    classname = "listfactory.list_factory.ListFactory"
  elif factory_type == "div":
    classname = "divfactory.div_factory.DivFactory"
  else:
    print(f"Unknown factory type: {factory_type}")
    usage()
    return
  
  print(f"Creating HTML page using {factory_type} factory...")
  
  factory = Factory.get_factory(classname)
  if factory is None:
    print("Failed to create factory")
    return
  
  blog1 = factory.create_link("Blog 1", "https://example.com/blog1")
  blog2 = factory.create_link("Blog 2", "https://example.com/blog2")
  blog3 = factory.create_link("Blog 3", "https://example.com/blog3")
  
  blog_tray = factory.create_tray("Blog Site")
  blog_tray.add(blog1)
  blog_tray.add(blog2)
  blog_tray.add(blog3)
  
  news1 = factory.create_link("News 1", "https://example.com/news1")
  news2 = factory.create_link("News 2", "https://example.com/news2")
  news3 = factory.create_tray("News 3")
  news3.add(factory.create_link("News 3 (US)", "https://example.com/news3us"))
  news3.add(factory.create_link("News 3 (Cananda)", "https://example.com/news3ca"))
  
  news_tray = factory.create_tray("News Site")
  news_tray.add(news1)
  news_tray.add(news2)
  news_tray.add(news3)
  
  page = factory.create_page("Blog and News", "Youngjin.com")
  page.add(blog_tray)
  page.add(news_tray)
  
  page.output(filename)
  
  print(f"\nHTML page created successfully!")
  print(f"File: {filename}")
  print(f"Factory used: {classname}")

if __name__ == "__main__":
  main()
