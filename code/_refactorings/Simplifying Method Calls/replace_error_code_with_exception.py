# Replace Error Code with Exception

balance = 100
# Before
## You have multiple conditionals that lead to the same result or action.
def f1(amount):
  global balance
  if amount > balance: return -1 # ERROR!
  else: balance -= amount; return 0
      
# After
## Extract the individual parts of the method into their own methods and call them instead of the original method.
def f2(amount):
  global balance
  if amount > balance: raise Exception("Balance exception")
  else: balance -= amount
  
if __name__ == "__main__":
  print("<Before>")
  f1(10)
  res = f1(120)
  if (res == -1): print("Balance error")
  print("<After>")
  f2(10) 
  try:
    f2(120)
  except Exception as e: 
    print(e)
