from pagemaker.page_maker import PageMaker


def main():
  
  print("=== Facade Pattern Demo ===\n")
  
  print("Creating welcome pages using the PageMaker facade...")
  print("The facade hides the complexity of:")
  print("- Database operations (reading user data)")
  print("- HTML generation (creating proper HTML structure)")
  print("- File operations (writing to files)")
  print("- Error handling")
  
  print("\n" + "="*50)
  print("Creating welcome pages:")
  print("="*50)
  
  PageMaker.make_welcome_page("a@example.com", "welcome_a.html")
  PageMaker.make_welcome_page("b@example.com", "welcome_b.html")
  PageMaker.make_welcome_page("c@example.com", "welcome_c.html")
  PageMaker.make_welcome_page("d@example.com", "welcome_d.html")
  
if __name__ == "__main__":
  main()
