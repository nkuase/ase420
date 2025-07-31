# Consolidate Conditional Expression

seniority = 5
months_disabled = 10
is_part_time = True
# Before
## You have multiple conditionals that lead to the same result or action.
def disability_amount1():
  if seniority < 2: return 0
  if months_disabled > 12: return 0
  if is_part_time: return 0
  # compute diability amount
      
# After
## Decompose the complicated parts of the conditional into separate methods: the condition, then and else .
def is_not_eligible_for_disability():
  return seniority < 2 or months_disabled > 12 or is_part_time
def disability_amount2():
  if is_not_eligible_for_disability(): return 0
  # compute diability amount
  
if __name__ == "__main__":
  print("<Before>")
  print(disability_amount1())
  print("<After>")
  print(disability_amount2())
