# Replace Magic Number with Symbolic Constant

# Before
## Your code uses a number that has a certain meaning to it.
def potential_energy1(mass, height):
  return mass * height * 9.81
      
# After
## Replace the array with an object that will have separate fields for each element.
GRAVITATIONAL_CONSTANT = 9.81
def potential_energy2(mass, height):
  return mass * height * GRAVITATIONAL_CONSTANT

if __name__ == "__main__":
  print("<Before>")
  print(potential_energy1(1, 2))
  print("<After>")
  print(potential_energy2(1, 2))
