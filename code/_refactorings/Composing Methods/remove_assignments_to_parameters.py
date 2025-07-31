# Remove Assignments to Parameters
height = 100
width = 10

# Before
def discount1(inputval, quantity):
  if quantity > 50: inputval -= 2
  print(inputval)

# After
## We use local variables instead of parameters
def discount2(inputval, quantity):
  result = inputval
  if quantity > 50: result -= 2
  print(result)
    
if __name__ == "__main__":
  print(discount1(100, 10))
  print(discount2(100, 10))