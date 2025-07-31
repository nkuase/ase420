# Consolidate Conditional Expression

price = 100
def send(): print("send")
def is_special_deal(): return True

# Before
## Identical code can be found in all branches of a conditional.
def f1():
  if is_special_deal():
    total = price * 0.95
    send()
  else:
    total = price * 0.98
    send()
      
# After
## Move the code outside of the conditional.
def f2():
  if is_special_deal():
    total = price * 0.95
  else:
    total = price * 0.98
  send()
  
if __name__ == "__main__":
  print("<Before>")
  f1()
  print("<After>")
  f2()
