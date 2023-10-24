# Replace Nested Conditional with Guard Clauses

is_dead = False
is_separated = False
is_retired= True

def dead_amount(): return 1
def separated_amount(): return 2
def retired_amount(): return 3
def normal_pay_mount(): return 4

# Before
## You have a group of nested conditionals and it’s hard to determine the normal flow of code execution.
def get_pay_amount1():
  if is_dead:
    result = dead_amount()
  else:
    if is_separated:
      result = separated_amount()
    else:
      if is_retired:
        result = retired_amount()
      else:
        result = normal_pay_mount()
  return result
      
# After
## Isolate all special checks and edge cases into separate clauses and place them before the main checks. 
# Ideally, you should have a “flat” list of conditionals, one after the other.
# Replace the array with an object that will have separate fields for each element.
def get_pay_amount2():
  if is_dead:
    return dead_amount()
  if is_separated:
    return separated_amount()
  if is_retired:
    return retired_amount()
  return normal_pay_mount()

if __name__ == "__main__":
  print("<Before>")
  print(get_pay_amount1())
  print("<After>")
  print(get_pay_amount2())
