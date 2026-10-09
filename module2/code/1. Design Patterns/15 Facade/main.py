from page_maker import PageMaker

# What facade does internally:
# 1. Database.get_properties() - get user data
# 2. HtmlWriter() - create HTML structure  
# 3. writer.title(), writer.paragraph() - add content
# 4. File operations - save to disk
# 5. Error handling - manage exceptions

def main():
  print("\n" + "="*50)
  print("Creating welcome pages:")
  print("="*50)
  
  PageMaker.make_welcome_page("a@example.com", "welcome_a.html")
  PageMaker.make_welcome_page("b@example.com", "welcome_b.html")
  
if __name__ == "__main__":
  main()
