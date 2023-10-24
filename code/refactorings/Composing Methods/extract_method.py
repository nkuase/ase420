def print_banner(): pass
def get_outstanding(): return "123"
name = "John"

# Before
def print_owing1():
  print_banner();

  # Print details.
  print("name: " + name)
  print("amount: " + get_outstanding())
  
# After
## Each print method should have a single responsibility, so we make print_details(). 
def print_details():
  print("name: " + name)
  print("amount: " + get_outstanding())

def print_owing2():
  print_banner()
  print_details()
  
if __name__ == "__main__":
  print("<Before>")
  print_owing1()
  print("<After>")
  print_owing2()
