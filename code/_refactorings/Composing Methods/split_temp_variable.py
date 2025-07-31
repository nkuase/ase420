# Split Temp Variable
height = 100
width = 10

# Before
def split_temp1():
  temp = 2 * (height + width);
  print(temp);
  temp = height * width;
  print(temp);

# After
## We make the variable names that show our intention
def split_temp2():
  perimeter = 2 * (height + width);
  print(perimeter);
  area = height * width;
  print(area); 
    
if __name__ == "__main__":
  split_temp1()    
  split_temp2()