# Replace Parameter with Explicit Methods

height = 0
width = 0

# Before
## You have multiple conditionals that lead to the same result or action.
def set_value1(name, value):
  global height, width
  if name == "height":
    height = value
    return
  if name == "width":
    width = value
    return
  raise Exception("ERROR!")
  
      
# After
## Extract the individual parts of the method into their own methods and call them instead of the original method.
def set_height(arg): 
  global height
  height = arg
def set_width(arg): 
  global weight
  width = arg
  
if __name__ == "__main__":
  print("<Before>")
  set_value1("height", 10); set_value1("width", 20)
  print(f"{height}/{width}")
  print("<After>")
  set_height(10); set_width(20)
  print(f"{height}/{width}")
