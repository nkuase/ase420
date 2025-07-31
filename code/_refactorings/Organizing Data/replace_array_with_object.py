# Replace Array With Object
from datetime import date

# Before
## You have an array that contains various types of data.
def replace_array1():
  row = []
  row.append("Liverpool")
  row.append("15")
  return f"{row[0]}/{row[1]}"
      
# After
## Replace the array with an object that will have separate fields for each element.
def replace_array2():
  row = Performance()
  row.set_name("Liverpool")
  row.set_wins(15)
  return row

class Performance(object):
  def set_name(self, name): self.name = name
  def set_wins(self, wins): self.wins = wins
  def __str__(self): return f"{self.name}/{self.wins}"
  
if __name__ == "__main__":
  print("<Before>")
  print(replace_array1())
  print("<After>")
  print(replace_array2())
