# Substitute Algorithm
# Before
## So you want to replace an existing algorithm with a new one?
def found_person1(people):
  for p in people:
    if p == "Don": return "Don"
    if p == "John": return "John"
    if p == "Kent": return "Kent"
    
# After
## Replace the body of the method that implements the algorithm with a new algorithm.
def found_person2(people):
  candidates = ["Don", "John", "Kent"]
  for p in people:
    if p in candidates: return p
    
if __name__ == "__main__":
  print(found_person1(["Kent"]))    
  print(found_person2(["John"]))